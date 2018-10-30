import torch
from torch.nn.functional import softplus, sigmoid

class RBM():

    def __init__(self, num_visible_x, num_visible_y, num_hidden, k, learning_rate=1e-3, momentum_coefficient=0.5, weight_decay=1e-4, use_cuda=True):
        self.num_visible_x = num_visible_x
        self.num_visible_y = num_visible_y
        self.num_hidden = num_hidden
        self.k = k
        self.learning_rate = learning_rate
        self.momentum_coefficient = momentum_coefficient
        self.weight_decay = weight_decay
        self.use_cuda = use_cuda
        
        self.weights_x = torch.randn(num_visible_x, num_hidden) * 0.1
        self.weights_y = torch.randn(num_visible_y, num_hidden) * 0.1
        self.visible_bias_x = torch.ones(num_visible_x) * 0.5
        self.visible_bias_y = torch.ones(num_visible_y) * 0.5
        self.hidden_bias = torch.zeros(num_hidden)

        self.weights_momentum_x = torch.zeros(num_visible_x, num_hidden)
        self.weights_momentum_y = torch.zeros(num_visible_y, num_hidden)
        self.visible_bias_momentum_x = torch.zeros(num_visible_x)
        self.visible_bias_momentum_y = torch.zeros(num_visible_y)
        self.hidden_bias_momentum = torch.zeros(num_hidden)

        if self.use_cuda:
            self.weights_x = self.weights_x.cuda()
            self.weights_y = self.weights_y.cuda()
            self.visible_bias_x = self.visible_bias_x.cuda()
            self.visible_bias_y = self.visible_bias_y.cuda()
            self.hidden_bias = self.hidden_bias.cuda()

            self.weights_momentum_x = self.weights_momentum_x.cuda()
            self.weights_momentum_y = self.weights_momentum_y.cuda()
            self.visible_bias_momentum_x = self.visible_bias_momentum_x.cuda()
            self.visible_bias_momentum_y = self.visible_bias_momentum_y.cuda()
            self.hidden_bias_momentum = self.hidden_bias_momentum.cuda()

    def sample_hidden(self, visible_probabilities, labels):
        hidden_activations = torch.matmul(visible_probabilities, self.weights_x) + torch.matmul(labels, self.weights_y) + self.hidden_bias
        hidden_probabilities = self._sigmoid(hidden_activations)
        return hidden_probabilities

    def sample_visible_x(self, hidden_probabilities):
        visible_activations = torch.matmul(hidden_probabilities, self.weights_x.t()) + self.visible_bias_x
        visible_probabilities = self._sigmoid(visible_activations)
        return visible_probabilities
    
    def sample_visible_y(self, hidden_probabilities):
        visible_activations = torch.matmul(hidden_probabilities, self.weights_y.t()) + self.visible_bias_y
        visible_probabilities = self._sigmoid(visible_activations)
        return visible_probabilities

    def contrastive_divergence(self, input_data, labels):
        # Positive phase
        positive_hidden_probabilities = self.sample_hidden(input_data, labels)
        positive_hidden_activations = (positive_hidden_probabilities >= self._random_probabilities(self.num_hidden)).float()
        positive_x_associations = torch.matmul(input_data.t(), positive_hidden_activations)
        positive_y_associations = torch.matmul(labels.t(), positive_hidden_activations)
        
        # Negative phase
        hidden_activations = positive_hidden_activations

        for step in range(self.k):
            visible_x_probabilities = self.sample_visible_x(hidden_activations)
            visible_y_probabilities = self.sample_visible_y(hidden_activations)
            hidden_probabilities = self.sample_hidden(visible_x_probabilities, visible_y_probabilities)
            hidden_activations = (hidden_probabilities >= self._random_probabilities(self.num_hidden)).float()

        negative_visible_x_probabilities = visible_x_probabilities
        negative_visible_y_probabilities = visible_y_probabilities
        negative_hidden_probabilities = hidden_probabilities

        negative_x_associations = torch.matmul(negative_visible_x_probabilities.t(), negative_hidden_probabilities)
        negative_y_associations = torch.matmul(negative_visible_y_probabilities.t(), negative_hidden_probabilities)
        
        # Update parameters
        self.weights_momentum_x *= self.momentum_coefficient
        self.weights_momentum_x += (positive_x_associations - negative_x_associations)
        
        self.weights_momentum_y *= self.momentum_coefficient
        self.weights_momentum_y += (positive_y_associations - negative_y_associations)

        self.visible_bias_momentum_x *= self.momentum_coefficient
        self.visible_bias_momentum_x += torch.sum(input_data - negative_visible_x_probabilities, dim=0)
        
        self.visible_bias_momentum_y *= self.momentum_coefficient
        self.visible_bias_momentum_y += torch.sum(labels - negative_visible_y_probabilities, dim=0)

        self.hidden_bias_momentum *= self.momentum_coefficient
        self.hidden_bias_momentum += torch.sum(positive_hidden_probabilities - negative_hidden_probabilities, dim=0)

        batch_size = input_data.size(0)

        self.weights_x += self.weights_momentum_x * self.learning_rate / batch_size
        self.weights_y += self.weights_momentum_y * self.learning_rate / batch_size
        self.visible_bias_x += self.visible_bias_momentum_x * self.learning_rate / batch_size
        self.visible_bias_y += self.visible_bias_momentum_y * self.learning_rate / batch_size
        self.hidden_bias += self.hidden_bias_momentum * self.learning_rate / batch_size

        self.weights_x -= self.weights_x * self.weight_decay  # L2 weight decay
        self.weights_y -= self.weights_y * self.weight_decay

        # Compute reconstruction error
        error_x = torch.sum((input_data - negative_visible_x_probabilities)**2)
        error_y = torch.sum((labels - negative_visible_y_probabilities)**2)
        
        return error_x, error_y

    def _sigmoid(self, x):
        return 1 / (1 + torch.exp(-x))

    def _random_probabilities(self, num):
        random_probabilities = torch.rand(num)

        if self.use_cuda:
            random_probabilities = random_probabilities.cuda()

        return random_probabilities

    def predict(self, input_data):
        return sigmoid(self.visible_bias_y + torch.matmul(torch.matmul(input_data, self.weights_x), torch.t(self.weights_y)))

