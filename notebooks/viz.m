load('bench6.mat');
close all
subplot(2,2,1)
plot(time, denoised_diag_speed2)
hold on
plot(time, denoised_diag_speed1)
hold on
plot(time, diag_speed)
hold on
plot(time, ref_speed, '--')
hold on
plot(time, sim_speed, ':', 'linewidth', 2)
xlabel('Time (s)')
ylabel('Speed (Hz)')
legend('Enc-Dec(TV-MSE) + Denoiser(SMAPE) (Noisy Date)', 'Enc-Dec(SMAPE) + Denoiser(SMAPE) (Noisy Date)', 'Enc-Dec (Non-Noisy Data)', 'Ref', 'Sim')

subplot(2,2,2)
plot(time, sim_speed - denoised_diag_speed2)
hold on
plot(time, sim_speed - denoised_diag_speed1)
hold on
plot(time, sim_speed - diag_speed)
hold on
plot([0 time(end)],[-0.05 -0.05],'k--')
hold on 
plot([0 time(end)],[+0.05 +0.05],'k--')
xlabel('Time (s)')
ylabel('Speed (Hz)')
legend('Enc-Dec(TV-MSE) + Denoiser(SMAPE) (Noisy Date)', 'Enc-Dec(SMAPE) + Denoiser(SMAPE) (Noisy Date)', 'Enc-Dec (Non-Noisy Data)', 'Ref', 'Acceptance Range')


subplot(2,2,3)
plot(time, denoised_diag_torque2)
hold on
plot(time, denoised_diag_torque1)
hold on
plot(time, diag_torque)
hold on
plot(time, ref_torque, '--')
hold on
plot(time, sim_torque, ':', 'linewidth', 2)
xlabel('Time (s)')
ylabel('Torque (% Nominal)')
legend('Enc-Dec(TV-MSE) + Denoiser(SMAPE) (Noisy Date)', 'Enc-Dec(SMAPE) + Denoiser(SMAPE) (Noisy Date)', 'Enc-Dec (Non-Noisy Data)', 'Ref', 'Sim')

subplot(2,2,4)
plot(time, sim_torque - denoised_diag_torque2)
hold on
plot(time, sim_torque - denoised_diag_torque1)
hold on
plot(time, sim_torque - diag_torque)
xlabel('Time (s)')
ylabel('Torque (% Nominal)')
legend('Enc-Dec(TV-MSE) + Denoiser(SMAPE) (Noisy Date)', 'Enc-Dec(SMAPE) + Denoiser(SMAPE) (Noisy Date)', 'Enc-Dec (Non-Noisy Data)', 'Ref')


fprintf("\n\nSignal to noise ratio\n\n");
fprintf("Speed: Enc-Dec(TV-MSE) + Denoiser(SMAPE) (Noisy Date)=%.4f \n", snr(sim_speed, sim_speed -denoised_diag_speed2));
fprintf("Speed: Enc-Dec(SMAPE) + Denoiser(SMAPE) (Noisy Date)=%.4f \n", snr(sim_speed, sim_speed - denoised_diag_speed1));
fprintf("Torque: Enc-Dec(TV-MSE) + Denoiser(SMAPE) (Noisy Date)=%.4f \n", snr(sim_torque, sim_torque - denoised_diag_torque2));
fprintf("Torque: Enc-Dec(SMAPE) + Denoiser(SMAPE) (Noisy Date)=%.4f \n", snr(sim_torque, sim_torque - denoised_diag_torque1));

fprintf("\n\nMaximum absolute difference\n\n");
fprintf("Speed: Enc-Dec(TV-MSE) + Denoiser(SMAPE) (Noisy Date)=%.4f \n", max(abs(diag_speed - denoised_diag_speed2)));
fprintf("Speed: Enc-Dec(SMAPE) + Denoiser(SMAPE) (Noisy Date)=%.4f \n", max(abs(diag_speed - denoised_diag_speed1)));
fprintf("Torque: Enc-Dec(TV-MSE) + Denoiser(SMAPE) (Noisy Date)=%.4f \n", max(abs(diag_torque - denoised_diag_torque2)));
fprintf("Torque: Enc-Dec(SMAPE) + Denoiser(SMAPE) (Noisy Date)=%.4f \n", max(abs(diag_torque - denoised_diag_torque1)));

fprintf("\n\nMean absolute difference\n\n");
fprintf("Speed: Enc-Dec(TV-MSE) + Denoiser(SMAPE) (Noisy Date)=%.4f \n", mean(abs(diag_speed - denoised_diag_speed2)));
fprintf("Speed: Enc-Dec(SMAPE) + Denoiser(SMAPE) (Noisy Date)=%.4f \n", mean(abs(diag_speed - denoised_diag_speed1)));
fprintf("Torque: Enc-Dec(TV-MSE) + Denoiser(SMAPE) (Noisy Date)=%.4f \n", mean(abs(diag_torque - denoised_diag_torque2)));
fprintf("Torque: Enc-Dec(SMAPE) + Denoiser(SMAPE) (Noisy Date)=%.4f \n", mean(abs(diag_torque - denoised_diag_torque1)));


