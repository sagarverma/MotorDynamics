import torch
import torch.optim as optim

from motornn.utils.parser import get_parser_with_args
from motornn.utils.helpers import (get_file_names, get_dataloaders,
                                   get_model, get_loss_function, Log)
from motornn.utils.runner import Runner

parser = get_parser_with_args()
args = parser.parse_args()

weight_path, log_path = get_file_names(args)
print (weight_path, log_path)
logger = Log(log_path, 'w')

train_loader, val_loader = get_dataloaders(args)
model = get_model(args)
criterion = get_loss_function(args)
optimizer = optim.SGD(model.parameters(), lr=args.lr)

runner = Runner(args.gpu, model, optimizer, criterion,
                train_loader, val_loader)

best_smape = 1000

logger.write_model(model)

for epoch in range(args.epochs):
    runner.set_epoch_metrics()

    train_metrics = runner.train_model()
    val_metrics = runner.eval_model()

    print('TRAIN METRICS EPOCH ', epoch, train_metrics)
    print('EVAL METRICS EPOCH ', epoch, val_metrics)

    logger.log_train_metrics(train_metrics, epoch)
    logger.log_validation_metrics(val_metrics, epoch)

    if val_metrics['smape'] <= best_smape:
        torch.save(model, weight_path)
        best_smape = val_metrics['smape']

logger.close()
