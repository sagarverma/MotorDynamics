import torch


class ClassRBM():

    def __init__(self, num_visible, num_target, num_hidden, k, learning_rate=1e-3, momentum_coefficient=0.5, weight_decay=1e-4, use_cuda=True):
        self.num_visible = num_visible
        self.num_hidden = num_hidden
        self.num_target = num_target

        self.k = k
        self.learning_rate = learning_rate
        self.momentum_coefficient = momentum_coefficient
        self.weight_decay = weight_decay
        self.use_cuda = use_cuda

        self.weightsVH = torch.randn(num_visible, num_hidden) * 0.01
        self.weightsTH = torch.randn(num_target, num_hidden) * 0.01

        self.visible_bias = torch.randn(num_visible) * 0.01
        self.target_bias = torch.randn(num_target) * 0.01
        self.hidden_bias = torch.randn(num_hidden) * 0.01

        self.weightsVH_gradient = torch.zeros(num_visible, num_hidden)
        self.weightsTH_gradient = torch.zeros(num_target, num_hidden)
        self.visible_gradient = torch.zeros(num_visible)
        self.target_gradient = torch.zeros(num_target)
        self.hidden_gradient = torch.zeros(num_hidden)


        if self.use_cuda:
            self.weightsVH = self.weightsVH.cuda()
            self.weightsTH = self.weightsTH.cuda()

            self.visible_bias = self.visible_bias.cuda()
            self.target_bias = self.target_bias.cuda()
            self.hidden_bias = self.hidden_bias.cuda()

            self.weightsVH_gradient = self.weightsVH_gradient.cuda()
            self.weightsTH_gradient = self.weightsTH_gradient.cuda()
            self.visible_gradient = self.visible_gradient.cuda()
            self.target_gradient = self.target_gradient.cuda()
            self.hidden_gradient = self.hidden_gradient.cuda()


    def sample_hidden(self, visible_probabilities, target_probabilities):
        hidden_activations = torch.matmul(visible_probabilities, self.weightsVH) + torch.matmul(target_probabilities, self.weightsTH) + self.hidden_bias
        hidden_probabilities = self._sigmoid(hidden_activations)
        return hidden_probabilities

    def sample_visible(self, hidden_probabilities):
        visible_activations = torch.matmul(hidden_probabilities, self.weightsVH.t()) + self.visible_bias
        visible_probabilities = self._sigmoid(visible_activations)
        return visible_probabilities

    def sample_target(self, hidden_probabilities):
        target_activations = torch.matmul(hidden_probabilities, self.weightsTH.t()) + self.target_bias
        target_probabilities = self._sigmoid(target_activations)
        return target_probabilities

    def contrastive_divergence(self, input_data, target):
        # Positive phase
        positive_hidden_probabilities = self.sample_hidden(input_data, target)
        positive_visible_associations = torch.matmul(input_data.t(), positive_hidden_probabilities)
        positive_target_associations = torch.matmul(target.t(), positive_hidden_probabilities)

        # Negative phase

        for step in range(self.k):
            visible_probabilities = self.sample_visible(positive_hidden_probabilities)
            target_probabilities = self.sample_target(positive_hidden_probabilities)
            hidden_probabilities = self.sample_hidden(visible_probabilities, target_probabilities)

        negative_visible_probabilities = visible_probabilities
        negative_target_probabilities = target_probabilities
        negative_hidden_probabilities = hidden_probabilities

        negative_visible_associations = torch.matmul(negative_visible_probabilities.t(), negative_hidden_probabilities)
        negative_target_associations = torch.matmul(negative_target_probabilities.t(), negative_hidden_probabilities)

        # Update parameters
        self.weightsVH_gradient *= 1 - self.momentum_coefficient
        self.weightsVH_gradient += self.momentum_coefficient * (positive_visible_associations - negative_visible_associations)

        self.weightsTH_gradient *= 1 - self.momentum_coefficient
        self.weightsTH_gradient += self.momentum_coefficient * (positive_target_associations - negative_target_associations)

        self.visible_gradient *= 1 - self.momentum_coefficient
        self.visible_gradient += self.momentum_coefficient * torch.sum(input_data - negative_visible_probabilities, dim=0)

        self.target_gradient *= 1 - self.momentum_coefficient
        self.target_gradient += self.momentum_coefficient * torch.sum(target - negative_target_probabilities, dim=0)

        self.hidden_gradient *= 1 - self.momentum_coefficient
        self.hidden_gradient += self.momentum_coefficient * torch.sum(positive_hidden_probabilities - negative_hidden_probabilities, dim=0)

        batch_size = input_data.size(0)

        self.weightsVH += self.weightsVH_gradient * self.learning_rate / batch_size
        self.weightsTH += self.weightsTH_gradient * self.learning_rate / batch_size
        self.visible_bias += self.visible_gradient * self.learning_rate / batch_size
        self.target_bias += self.target_gradient * self.learning_rate / batch_size
        self.hidden_bias += self.hidden_gradient * self.learning_rate / batch_size

        self.weightsVH -= self.weightsVH * self.weight_decay  # L2 weight decay
        self.weightsTH -= self.weightsTH * self.weight_decay

        # Compute reconstruction error
        visible_error = torch.sum((input_data - negative_visible_probabilities)**2)
        target_error = torch.sum((target - negative_target_probabilities)**2)

        return visible_error, target_error

    def _sigmoid(self, x):
        return 1 / (1 + torch.exp(-x))

    def _random_probabilities(self, num):
        random_probabilities = torch.rand(num)

        if self.use_cuda:
            random_probabilities = random_probabilities.cuda()

        return random_probabilities

    def predict(self, input):
        target = torch.zeros(input.size()[0],self.num_target).cuda()
        for step in range(self.k):
            hidden_probabilities = self.sample_hidden(input, target)
            target = self.sample_target(hidden_probabilities)

        return target