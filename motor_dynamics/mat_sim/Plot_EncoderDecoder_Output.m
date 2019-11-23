data = load('Exp_constant_speed_-10_ramp_load_20_acc_delta_0.1.mat');
% data = load('deconv_results.mat');

t = data.time;
Voltage1 = data.voltage_d; Voltage2 = data.voltage_q;
StatorPuls = data.statorPuls; Speed = data.speed;

Current1_true = data.current_d_true; Current1_pred = data.current_d_pred;
Current2_true = data.current_q_true; Current2_pred = data.current_q_pred;
Torque_true = data.torque_true; Torque_pred = data.torque_pred;

figure; set(gcf,'Name','encoder-decoder model')
subplot(321); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Voltage (V) '); plot( t , Voltage1); 
hold on
plot(t, Voltage2 );
hold off
legend('V1','V2');
subplot(323); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' StatorPuls (rad/s) '); plot( t , StatorPuls );
subplot(325); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Speed (rad/s) '); plot( t , Speed );

subplot(322); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Current1 (A) '); plot( t , Current1_true); 
hold on 
plot(t, Current1_pred );
hold off
legend('true','pred');
subplot(324); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Current2 (A) '); plot( t , Current2_true);
hold on 
plot(t, Current2_pred );
hold off
legend('true','pred');
subplot(326); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Torque (Nm) '); plot( t , Torque_true);
hold on 
plot(t, Torque_pred );
hold off
legend('true','pred');