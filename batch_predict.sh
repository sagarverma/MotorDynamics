python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/shallow_fnn/shallow_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/shallow_fnn/shallow_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench1.pkl  \
--alpha=0.5

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/shallow_fnn/shallow_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/shallow_fnn/shallow_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench2.pkl  \
--alpha=0.5

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/shallow_fnn/shallow_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/shallow_fnn/shallow_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench3.pkl  \
--alpha=0.5


python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/shallow_fnn/shallow_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/shallow_fnn/shallow_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench4.pkl  \
--alpha=0.5

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/shallow_fnn/shallow_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/shallow_fnn/shallow_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench5.pkl  \
--alpha=0.5

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/shallow_fnn/shallow_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/shallow_fnn/shallow_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench6.pkl  \
--alpha=0.5

#############################################################################################

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/deep_fnn/deep_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/deep_fnn/deep_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench1.pkl  \
--alpha=0.5

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/deep_fnn/deep_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/deep_fnn/deep_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench2.pkl  \
--alpha=0.5

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/deep_fnn/deep_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/deep_fnn/deep_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench3.pkl  \
--alpha=0.5


python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/deep_fnn/deep_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/deep_fnn/deep_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench4.pkl  \
--alpha=0.5

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/deep_fnn/deep_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/deep_fnn/deep_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench5.pkl  \
--alpha=0.5

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/deep_fnn/deep_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/deep_fnn/deep_fnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench6.pkl  \
--alpha=0.5

#############################################################################################

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/shallow_rnn/shallow_rnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse_hiddenSize_32.pt  \
--torque_model_file=../../weights/Data_11052020/shallow_rnn/shallow_rnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse_hiddenSize_32.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench1.pkl  \
--alpha=0.6

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/shallow_rnn/shallow_rnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse_hiddenSize_32.pt  \
--torque_model_file=../../weights/Data_11052020/shallow_rnn/shallow_rnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse_hiddenSize_32.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench2.pkl \
--alpha=0.6

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/shallow_rnn/shallow_rnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse_hiddenSize_32.pt  \
--torque_model_file=../../weights/Data_11052020/shallow_rnn/shallow_rnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse_hiddenSize_32.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench3.pkl \
--alpha=0.6


python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/shallow_rnn/shallow_rnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse_hiddenSize_32.pt  \
--torque_model_file=../../weights/Data_11052020/shallow_rnn/shallow_rnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse_hiddenSize_32.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench4.pkl \
--alpha=0.6

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/shallow_rnn/shallow_rnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse_hiddenSize_32.pt  \
--torque_model_file=../../weights/Data_11052020/shallow_rnn/shallow_rnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse_hiddenSize_32.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench5.pkl \
--alpha=0.6

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/shallow_rnn/shallow_rnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse_hiddenSize_32.pt  \
--torque_model_file=../../weights/Data_11052020/shallow_rnn/shallow_rnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse_hiddenSize_32.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench6.pkl \
--alpha=0.6

#############################################################################################

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/deep_rnn/deep_rnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse_hiddenSize_32.pt  \
--torque_model_file=../../weights/Data_11052020/deep_rnn/deep_rnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse_hiddenSize_32.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench1.pkl \
--alpha=0.6

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/deep_rnn/deep_rnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse_hiddenSize_32.pt  \
--torque_model_file=../../weights/Data_11052020/deep_rnn/deep_rnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse_hiddenSize_32.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench2.pkl \
--alpha=0.6

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/deep_rnn/deep_rnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse_hiddenSize_32.pt  \
--torque_model_file=../../weights/Data_11052020/deep_rnn/deep_rnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse_hiddenSize_32.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench3.pkl \
--alpha=0.6


python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/deep_rnn/deep_rnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse_hiddenSize_32.pt  \
--torque_model_file=../../weights/Data_11052020/deep_rnn/deep_rnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse_hiddenSize_32.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench4.pkl \
--alpha=0.6

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/deep_rnn/deep_rnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse_hiddenSize_32.pt  \
--torque_model_file=../../weights/Data_11052020/deep_rnn/deep_rnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse_hiddenSize_32.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench5.pkl \
--alpha=0.6

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/deep_rnn/deep_rnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse_hiddenSize_32.pt  \
--torque_model_file=../../weights/Data_11052020/deep_rnn/deep_rnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse_hiddenSize_32.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench6.pkl \
--alpha=0.6

#############################################################################################

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/shallow_cnn/shallow_cnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/shallow_cnn/shallow_cnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench1.pkl  \
--alpha=0.7

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/shallow_cnn/shallow_cnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/shallow_cnn/shallow_cnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench2.pkl  \
--alpha=0.7

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/shallow_cnn/shallow_cnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/shallow_cnn/shallow_cnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench3.pkl  \
--alpha=0.7


python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/shallow_cnn/shallow_cnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/shallow_cnn/shallow_cnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench4.pkl  \
--alpha=0.7

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/shallow_cnn/shallow_cnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/shallow_cnn/shallow_cnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench5.pkl  \
--alpha=0.7

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/shallow_cnn/shallow_cnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/shallow_cnn/shallow_cnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench6.pkl  \
--alpha=0.7

#############################################################################################

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/deep_cnn/deep_cnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/deep_cnn/deep_cnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench1.pkl  \
--alpha=0.7

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/deep_cnn/deep_cnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/deep_cnn/deep_cnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench2.pkl  \
--alpha=0.7

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/deep_cnn/deep_cnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/deep_cnn/deep_cnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench3.pkl  \
--alpha=0.7


python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/deep_cnn/deep_cnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/deep_cnn/deep_cnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench4.pkl  \
--alpha=0.7

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/deep_cnn/deep_cnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/deep_cnn/deep_cnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench5.pkl  \
--alpha=0.7

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/deep_cnn/deep_cnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/deep_cnn/deep_cnn_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.1_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench6.pkl  \
--alpha=0.7

#############################################################################################

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/encdec_skip/encdec_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/encdec_skip/encdec_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench1.pkl  \
--alpha=0.7

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/encdec_skip/encdec_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/encdec_skip/encdec_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench2.pkl  \
--alpha=0.7

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/encdec_skip/encdec_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/encdec_skip/encdec_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench3.pkl  \
--alpha=0.7


python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/encdec_skip/encdec_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/encdec_skip/encdec_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench4.pkl  \
--alpha=0.7

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/encdec_skip/encdec_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/encdec_skip/encdec_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench5.pkl  \
--alpha=0.7

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/encdec_skip/encdec_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/encdec_skip/encdec_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench6.pkl  \
--alpha=0.7

#############################################################################################

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/encdec_rnn_skip/encdec_rnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/encdec_rnn_skip/encdec_rnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench1.pkl  \
--alpha=0.8

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/encdec_rnn_skip/encdec_rnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/encdec_rnn_skip/encdec_rnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench2.pkl \
--alpha=0.8

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/encdec_rnn_skip/encdec_rnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/encdec_rnn_skip/encdec_rnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench3.pkl \
--alpha=0.8


python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/encdec_rnn_skip/encdec_rnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/encdec_rnn_skip/encdec_rnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench4.pkl \
--alpha=0.8

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/encdec_rnn_skip/encdec_rnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/encdec_rnn_skip/encdec_rnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench5.pkl \
--alpha=0.8

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/encdec_rnn_skip/encdec_rnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/encdec_rnn_skip/encdec_rnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench6.pkl \
--alpha=0.8

#############################################################################################

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/encdec_birnn_skip/encdec_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/encdec_birnn_skip/encdec_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench1.pkl \
--alpha=0.85

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/encdec_birnn_skip/encdec_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/encdec_birnn_skip/encdec_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench2.pkl \
--alpha=0.85

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/encdec_birnn_skip/encdec_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/encdec_birnn_skip/encdec_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench3.pkl \
--alpha=0.85


python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/encdec_birnn_skip/encdec_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/encdec_birnn_skip/encdec_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench4.pkl \
--alpha=0.85

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/encdec_birnn_skip/encdec_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/encdec_birnn_skip/encdec_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench5.pkl \
--alpha=0.85

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/encdec_birnn_skip/encdec_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/encdec_birnn_skip/encdec_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench6.pkl \
--alpha=0.85

#############################################################################################

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/encdec_diag_birnn_skip/encdec_diag_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/encdec_diag_birnn_skip/encdec_diag_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench1.pkl \
--alpha=0.9

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/encdec_diag_birnn_skip/encdec_diag_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/encdec_diag_birnn_skip/encdec_diag_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench2.pkl \
--alpha=0.9

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/encdec_diag_birnn_skip/encdec_diag_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/encdec_diag_birnn_skip/encdec_diag_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench3.pkl \
--alpha=0.9


python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/encdec_diag_birnn_skip/encdec_diag_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/encdec_diag_birnn_skip/encdec_diag_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench4.pkl \
--alpha=0.9

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/encdec_diag_birnn_skip/encdec_diag_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/encdec_diag_birnn_skip/encdec_diag_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench5.pkl \
--alpha=0.9

python motornn/predict.py  \
--speed_model_file=../../weights/Data_11052020/encdec_diag_birnn_skip/encdec_diag_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt  \
--torque_model_file=../../weights/Data_11052020/encdec_diag_birnn_skip/encdec_diag_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_2048_epochs_1000_loss_mse.pt   \
--window=100  \
--save_dir=../../results/Data_11052020/  \
--benchmark_file=../../datasets/Data_11052020_exponential_dist_ramps/benchmarks/bench6.pkl \
--alpha=0.9

#############################################################################################
