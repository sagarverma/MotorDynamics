python motornn/predict.py \
--speed_model_file=../../weights/Data_11052020/shallow_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt \
--torque_model_file=../../weights/Data_11052020/shallow_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--window=100 \
--save_dir=../../results/Data_11052020/ \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench1.pkl

python motornn/predict.py \
--speed_model_file=../../weights/Data_11052020/shallow_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt \
--torque_model_file=../../weights/Data_11052020/shallow_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--window=100 \
--save_dir=../../results/Data_11052020/ \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench2.pkl

python motornn/predict.py \
--speed_model_file=../../weights/Data_11052020/shallow_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt \
--torque_model_file=../../weights/Data_11052020/shallow_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--window=100 \
--save_dir=../../results/Data_11052020/ \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench3.pkl


python motornn/predict.py \
--speed_model_file=../../weights/Data_11052020/shallow_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt \
--torque_model_file=../../weights/Data_11052020/shallow_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--window=100 \
../../results/Data_11052020/ \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench4.pkl

python motornn/predict.py \
--speed_model_file=../../weights/Data_11052020/shallow_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt \
--torque_model_file=../../weights/Data_11052020/shallow_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--window=100 \
--save_dir=../../results/Data_11052020/ \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench5.pkl
