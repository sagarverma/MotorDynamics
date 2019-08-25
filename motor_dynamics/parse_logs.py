import os
import re

models = os.listdir('../../logs/')

for model in models:
    if '.ipynb' not in model:
        logs = os.listdir('../../logs/' + model)

        current_d_best_model_smape = 201
        current_d_best_model = None
        current_d_best_model_params = None
        
        current_q_best_model_smape = 201
        current_q_best_model = None
        current_q_best_model_params = None
        
        torque_best_model_smape = 201
        torque_best_model = None
        torque_best_model_params = None
        
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

                min_val_smape = 201
                for i in range(0,len(smapes),2):
                    min_val_smape = min(float(smapes[i][1]), min_val_smape)

                if 'currentD' in param_pairs['outQuants'] and min_val_smape <= current_d_best_model_smape:
                    current_d_best_model_smape = min_val_smape
                    current_d_best_model = model
                    current_d_best_model_params = param_pairs

                if 'currentQ' in param_pairs['outQuants'] and min_val_smape <= current_q_best_model_smape:
                    current_q_best_model_smape = min_val_smape
                    current_q_best_model = model
                    current_q_best_model_params = param_pairs 
                    
                if 'torque' in param_pairs['outQuants'] and min_val_smape <= torque_best_model_smape:
                    torque_best_model_smape = min_val_smape
                    torque_best_model = model
                    torque_best_model_params = param_pairs
                    
        print (current_d_best_model)
        print (current_d_best_model_params)
        print (current_d_best_model_smape)

        print (current_q_best_model)
        print (current_q_best_model_params)
        print (current_q_best_model_smape)
        
        print (torque_best_model)
        print (torque_best_model_params)
        print (torque_best_model_smape)
        
        print ('#################################')