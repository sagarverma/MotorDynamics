python motornn/predict.py \
  --speed_model_file=../../weights/Data_23042020_noisy/deep_fnn/deep_fnn_act_relu_stride_1_window_50_inpQuants_noisy_voltage_d,noisy_voltage_q,noisy_current_d,noisy_current_q_outQuants_speed_lr_0.1_batchSize_10000_epochs_500_loss_mse.pt \
  --torque_model_file=../../weights/Data_23042020_noisy/deep_fnn/deep_fnn_act_relu_stride_1_window_50_inpQuants_noisy_voltage_d,noisy_voltage_q,noisy_current_d,noisy_current_q_outQuants_torque_lr_0.1_batchSize_10000_epochs_500_loss_mse.pt \
  --benchmark_file=../../datasets/Data_23042020_noisy/benchmark/0to50speed_0torque_0.1ramp.pkl \
  --window=50 \
  --save_dir=../../results/Data_23042020_noisy/ \
  --alpha=0.05 \
  --noise=True \
  --out_name=noisy_enc_dec_on_noisy_denoiser

python motornn/predict.py \
  --speed_model_file=../../weights/Data_23042020_noisy/deep_fnn/deep_fnn_act_relu_stride_1_window_50_inpQuants_noisy_voltage_d,noisy_voltage_q,noisy_current_d,noisy_current_q_outQuants_speed_lr_0.1_batchSize_10000_epochs_500_loss_mse.pt \
  --torque_model_file=../../weights/Data_23042020_noisy/deep_fnn/deep_fnn_act_relu_stride_1_window_50_inpQuants_noisy_voltage_d,noisy_voltage_q,noisy_current_d,noisy_current_q_outQuants_torque_lr_0.1_batchSize_10000_epochs_500_loss_mse.pt \
  --benchmark_file=../../datasets/Data_23042020_noisy/benchmark/0to50speed_0torque_0.1ramp.pkl \
  --window=50 \
  --save_dir=../../results/Data_23042020_noisy/ \
  --alpha=0.1 \
  --noise=False \
  --out_name=noisy_enc_dec_denoiser_on_noisy

python motornn/predict.py \
  --speed_model_file=../../weights/Data_23042020_noisy/deep_fnn/deep_fnn_act_relu_stride_1_window_50_inpQuants_noisy_voltage_d,noisy_voltage_q,noisy_current_d,noisy_current_q_outQuants_speed_lr_0.1_batchSize_10000_epochs_500_loss_mse.pt \
  --torque_model_file=../../weights/Data_23042020_noisy/deep_fnn/deep_fnn_act_relu_stride_1_window_50_inpQuants_noisy_voltage_d,noisy_voltage_q,noisy_current_d,noisy_current_q_outQuants_torque_lr_0.1_batchSize_10000_epochs_500_loss_mse.pt \
  --benchmark_file=../../datasets/Data_23042020_noisy/benchmark/0to50speed_0torque_0.1ramp.pkl \
  --window=50 \
  --save_dir=../../results/Data_23042020_noisy/ \
  --alpha=0.2 \
  --noise=False \
  --out_name=noisy_enc_dec_on_noisy

python motornn/predict.py \
  --speed_model_file=../../weights/Data_23042020/encdec_diag_birnn_skip/encdec_diag_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_10000_epochs_1000_loss_mse.pt \
  --torque_model_file=../../weights/Data_23042020/encdec_diag_birnn_skip/encdec_diag_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_10000_epochs_1000_loss_mse.pt \
  --benchmark_file=../../datasets/Data_23042020_noisy/benchmark/0to50speed_0torque_0.1ramp.pkl \
  --window=50 \
  --save_dir=../../results/Data_23042020_noisy/ \
  --alpha=0.2 \
  --noise=True \
  --out_name=enc_dec_on_noisy

python motornn/predict.py \
  --speed_model_file=../../weights/Data_23042020/encdec_diag_birnn_skip/encdec_diag_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_speed_lr_0.01_batchSize_10000_epochs_1000_loss_mse.pt \
  --torque_model_file=../../weights/Data_23042020/encdec_diag_birnn_skip/encdec_diag_birnn_skip_act_relu_stride_1_window_100_inpQuants_voltage_d,voltage_q,current_d,current_q_outQuants_torque_lr_0.01_batchSize_10000_epochs_1000_loss_mse.pt \
  --benchmark_file=../../datasets/Data_23042020_noisy/benchmark/0to50speed_0torque_0.1ramp.pkl \
  --window=50 \
  --save_dir=../../results/Data_23042020_noisy/ \
  --alpha=0.01 \
  --noise=False \
  --out_name=enc_dec_on_non_noisy
