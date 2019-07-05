import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable

from motor_dynamics.utils.helpers import (get_file_names, initialize_metrics,
                                          get_mean_metrics, set_metrics,
                                          get_model_from_weight, get_train_loaders, Log)
from motor_dynamics.utils.metrics import smape

def finetune(opt):
    weight_file_path, log_file_path = get_file_names(opt)
    log = Log(log_file_path, 'w')

    model = get_model_from_weight(opt)
    train_raw_loader, val_sim_loader = get_finetune_loaders(opt)

    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=opt.lr)

    for epoch in range(opt.epochs):
        train_metrics = initialize_metrics()
        model.train()

        for inp, out in train_raw_loader:
            inp = Variable(inp).cuda()
            out = Variable(out).cuda()

            optimizer.zero_grad()
            preds = model(inp)
            loss = criterion(preds, out)
            loss.backward()
            optimizer.step()

            smape_err = smape(out.cpu().numpy(), preds.data.cpu().numpy())
            train_metrics = set_metrics(train_metrics, loss, smape_err)

        train_metrics = get_mean_metrics(train_metrics)
        log.log_train_metrics(train_metrics, epoch)

        test_metrics = initialize_metrics()
        model.eval()

        for inp, out in test_loader:
            inp = Variable(inp).cuda()
            out = Variable(out).cuda()

            preds = model(inp)
            loss = criterion(preds, out)
            test_losses.append(loss.item())

            smape_err = smape(out.cpu().numpy(), preds.data.cpu().numpy())
            test_metrics = set_metrics(test_metrics, loss, smape_err)

        test_metrics = get_mean_metrics(test_metrics)
        log.log_train_metrics(test_metrics, epoch)

        torch.save(model, weight_path)

    log.close()
