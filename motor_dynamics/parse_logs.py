import os
import re

import torch 

models = os.listdir('../../logs/')

for model in models:
    if '.ipynb' not in model:
        logs = os.listdir('../../logs/' + model)

        current_d_best_model_smape = 201
        current_d_best_mae = 100000
        current_d_best_r2 = -100000
        current_d_best_rmse = 100000
        current_d_best_model = None
        current_d_best_model_params = None
        
        current_q_best_model_smape = 201
        current_q_best_mae = 100000
        current_q_best_r2 = -100000
        current_q_best_rmse = 100000
        current_q_best_model = None
        current_q_best_model_params = None
        
        torque_best_model_smape = 201
        torque_best_mae = 100000
        torque_best_r2 = -100000
        torque_best_rmse = 100000
        torque_best_model = None
        torque_best_model_params = None
        
        best_log = None
        
        for log in logs:
            if '.ipynb' not in log and '.ipynb' not in model:
                fin = open('../../logs/' + model + '/' + log, 'r')
                data = fin.read()
                fin.close()

                params = log.split('__')[1][:-4]
                params = params.replace('current_d', 'currentD')
                params = params.replace('current_q', 'currentQ')
                params = params.replace('voltage_d', 'voltageD')
                params = params.replace('voltage_q', 'voltageQ')
                params = params.split('_')


                param_pairs = {}
                for i in range(0,len(params),2):
                    param_pairs[params[i]] = params[i+1]

                smapes = re.findall('(smape=)(.*?)(\n)', data)
                maes = re.findall('(mae=)(.*?)(\n)', data)
                r2s = re.findall('(r2=)(.*?)(\n)', data)
                rmses = re.findall('(rmse=)(.*?)(\n)', data)
                

                min_val_smape = 201
                for i in range(0,len(smapes),2):
                    if float(smapes[i][1]) < min_val_smape:
                        min_val_smape = float(smapes[i][1])
                        min_val_mae = float(maes[i][1])
                        min_val_r2 = float(r2s[i][1])
                        min_val_rmses = float(rmses[i][1])

                if 'currentD' in param_pairs['outQuants'] and min_val_smape <= current_d_best_model_smape:
                    current_d_best_model_smape = min_val_smape
                    current_d_best_mae = min_val_mae
                    current_d_best_r2 = min_val_r2
                    current_d_best_rmse = min_val_rmses
                    current_d_best_model = model
                    current_d_best_model_params = param_pairs
                    best_log = log

                if 'currentQ' in param_pairs['outQuants'] and min_val_smape <= current_q_best_model_smape:
                    current_q_best_model_smape = min_val_smape
                    current_q_best_mae = min_val_mae
                    current_q_best_r2 = min_val_r2
                    current_q_best_rmse = min_val_rmses
                    current_q_best_model = model
                    current_q_best_model_params = param_pairs 
                    best_log = log
                    
                if 'torque' in param_pairs['outQuants'] and min_val_smape <= torque_best_model_smape:
                    torque_best_model_smape = min_val_smape
                    torque_best_mae = min_val_mae
                    torque_best_r2 = min_val_r2
                    torque_best_rmse = min_val_rmses
                    torque_best_model = model
                    torque_best_model_params = param_pairs
                    best_log = log
                    
        print (current_d_best_model)
        print (current_d_best_model_params)
        print ('smape', current_d_best_model_smape)
        print ('mae', current_d_best_mae)
        print ('r2', current_d_best_r2)
        print ('rmse', current_d_best_rmse)

        print (current_q_best_model)
        print (current_q_best_model_params)
        print ('smape', current_q_best_model_smape)
        print ('mae', current_q_best_mae)
        print ('r2', current_q_best_r2)
        print ('rmse', current_q_best_rmse)
        
        print (torque_best_model)
        print (torque_best_model_params)
        print ('smape', torque_best_model_smape)
        print ('mae', torque_best_mae)
        print ('r2', torque_best_r2)
        print ('rmse', torque_best_rmse)
        
        weight = torch.load('../../weights/' + model + '/' + best_log[:-3] + 'pt')
        print ('Parameters :', sum(p.numel() for p in weight.parameters()))
            
        print ('#################################')