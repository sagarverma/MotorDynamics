gt_speed = load('../../../results_sim/benchmark/GT_Speed.mat').speed;
gt_torque = load('../../../results_sim/benchmark/GT_Torque.mat').torque;
gt_time = load('../../../results_sim/benchmark/GT_Time.mat').time;

res_speed = load('../../../results_sim/benchmark/Res_Speed.mat').speed;
res_torque = load('../../../results_sim/benchmark/Res_Torque.mat').torque;


subplot(2,1,1); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Speed (rad/s) '); plot( gt_time , gt_speed ); plot(gt_time, res_speed);
subplot(2,1,2); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Torque (Nm) '); plot( gt_time , gt_torque ); plot(gt_time, res_torque);