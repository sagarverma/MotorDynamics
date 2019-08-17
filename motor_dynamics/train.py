import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable

from motor_dynamics.utils.helpers import (get_file_names, initialize_metrics,
                                          get_mean_metrics, set_metrics, 
                                          denormalize_metrics, get_model,
                                          get_train_loaders, Log)
from motor_dynamics.utils.metrics import smape, r2, rmsle, rmse, mae

def train(opt):
    weight_file_path, log_file_path = get_file_names(opt)
    log = Log(log_file_path, 'w')

    model = get_model(opt)
    train_sim_loader, val_sim_loader = get_train_loaders(opt)

    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=opt.lr)

    best_smape = 1000000

    for epoch in range(opt.epochs):
        train_metrics = initialize_metrics()
        model.train()

        for inp, out in train_sim_loader:
            inp = Variable(inp).cuda()
            out = Variable(out).cuda()

            optimizer.zero_grad()
            preds = model(inp)
            loss = criterion(preds, out)
            loss.backward()
            optimizer.step()
            out = out.cpu().numpy()
            preds = preds.data.cpu().numpy()
            
            smape_err = smape(out, preds)
            r2_err = r2(out, preds)
            rmsle_err = rmsle(out, preds)
            rmse_err = rmse(out, preds)
            mae_err = mae(out, preds)

            train_metrics = set_metrics(train_metrics, loss, smape_err, r2_err,
                                        rmsle_err, rmse_err, mae_err)

        train_metrics = get_mean_metrics(train_metrics)
        train_metrics = denormalize_metrics(train_metrics, opt.out_quants)
        log.log_train_metrics(train_metrics, epoch)
        print (epoch, 'train', train_metrics)

        val_metrics = initialize_metrics()
        model.eval()

        for inp, out in val_sim_loader:
            inp = Variable(inp).cuda()
            out = Variable(out).cuda()

            preds = model(inp)
            loss = criterion(preds, out)
            out = out.cpu().numpy()
            preds = preds.data.cpu().numpy()
            
            smape_err = smape(out, preds)
            r2_err = r2(out, preds)
            rmsle_err = rmsle(out, preds)
            rmse_err = rmse(out, preds)
            mae_err = mae(out, preds)

            val_metrics = set_metrics(val_metrics, loss, smape_err, r2_err,
                                        rmsle_err, rmse_err, mae_err)

        val_metrics = get_mean_metrics(val_metrics)
        val_metrics = denormalize_metrics(val_metrics, opt.out_quants)
        log.log_validation_metrics(val_metrics, epoch)
        print (epoch, 'val', val_metrics)

        if val_metrics['smape'] < best_smape:
            torch.save(model, weight_file_path)
            best_smape = val_metrics['smape']

    log.close()
