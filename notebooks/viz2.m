clear; 
load('NoLM_SpeedVariations2.mat');
%load('../../../datasets/data/train_sim/30LM.mat');

 subplot(4,1,1)
hold on
 plot(time, cspeed)
 hold on
s = plot(time, dspeed )
s.Color = [s.Color 0.5]
xlabel('Time (s)')
ylabel('Speed (Hz)')
legend('Prediction', 'Raw')

 subplot(4,1,2)
 plot(time, dspeed - cspeed)
 xlabel('Time (s)')
 ylabel('Speed (Hz)')


 subplot(4,1,3)
hold on
 plot(time, ctorque)
 hold on
t = plot(time, dtorque)
t.Color = [t.Color 0.5]
xlabel('Time (s)')
ylabel('Torque (% Nominal)')
legend('Prediction', 'Raw')
%  
 subplot(4,1,4)
 plot(time, dtorque - ctorque)
 xlabel('Time (s)')
 ylabel('Torque (% Nominal)')



% fprintf("\n\nSignal to noise ratio\n\n");
% fprintf("Speed: Enc-Dec(TV-MSE) + Denoiser(SMAPE) (Noisy Date)=%.4f \n", snr(diag_speed, denoised_diag_speed2));
% fprintf("Speed: Enc-Dec(SMAPE) + Denoiser(SMAPE) (Noisy Date)=%.4f \n", snr(diag_speed, denoised_diag_speed1));
% fprintf("Torque: Enc-Dec(TV-MSE) + Denoiser(SMAPE) (Noisy Date)=%.4f \n", snr(diag_torque, denoised_diag_torque2));
% fprintf("Torque: Enc-Dec(SMAPE) + Denoiser(SMAPE) (Noisy Date)=%.4f \n", snr(diag_torque, denoised_diag_torque1));
% 
% fprintf("\n\nMaximum absolute difference\n\n");
% fprintf("Speed: Enc-Dec(TV-MSE) + Denoiser(SMAPE) (Noisy Date)=%.4f \n", max(abs(diag_speed - denoised_diag_speed2)));
% fprintf("Speed: Enc-Dec(SMAPE) + Denoiser(SMAPE) (Noisy Date)=%.4f \n", max(abs(diag_speed - denoised_diag_speed1)));
% fprintf("Torque: Enc-Dec(TV-MSE) + Denoiser(SMAPE) (Noisy Date)=%.4f \n", max(abs(diag_torque - denoised_diag_torque2)));
% fprintf("Torque: Enc-Dec(SMAPE) + Denoiser(SMAPE) (Noisy Date)=%.4f \n", max(abs(diag_torque - denoised_diag_torque1)));
% 
% fprintf("\n\nMean absolute difference\n\n");
% fprintf("Speed: Enc-Dec(TV-MSE) + Denoiser(SMAPE) (Noisy Date)=%.4f \n", mean(abs(diag_speed - denoised_diag_speed2)));
% fprintf("Speed: Enc-Dec(SMAPE) + Denoiser(SMAPE) (Noisy Date)=%.4f \n", mean(abs(diag_speed - denoised_diag_speed1)));
% fprintf("Torque: Enc-Dec(TV-MSE) + Denoiser(SMAPE) (Noisy Date)=%.4f \n", mean(abs(diag_torque - denoised_diag_torque2)));
% fprintf("Torque: Enc-Dec(SMAPE) + Denoiser(SMAPE) (Noisy Date)=%.4f \n", mean(abs(diag_torque - denoised_diag_torque1)));
