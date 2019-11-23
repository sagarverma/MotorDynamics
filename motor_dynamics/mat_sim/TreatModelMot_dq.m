%     Voltage: [1x1 timeseries]
%     Current: [1x1 timeseries]
%       Speed: [1x1 timeseries]
%      Torque: [1x1 timeseries]4
%
%
% data = load('../../datasets/CS2018_12_14/DataForSagar.mat');
Data = Data_dq;

RefSpeed = Data.RefSpeed.Data; RefLoad = Data.RefLoad.Data;
Voltage = Data.Voltage.Data; t = Data.Voltage.Time;
StatorPuls = Data.StatorPuls.Data; %t = Data.StatorPuls.Time;
Current = Data.Current.Data; %t = Data.Current.Time;
Speed   = Data.Speed.Data;   %t = Data.Speed.Time;
Torque  = Data.Torque.Data;  %t = Data.Torque.Time;

figure; set(gcf,'Name','dq')
subplot(4,4,1); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Ref Speed (rad/s) '); plot( t , RefSpeed );
subplot(4,4,2); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Voltage (V) '); plot( t , Voltage );
subplot(4,4,3); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Speed (rad/s) '); plot( t , Speed );
subplot(4,4,4); hold on; grid on; zoom on; xlabel(' t(s)'); ylabel(' Ref Speed and Speed'); plot(t, RefSpeed); plot(t, Speed);

subplot(4,4,5); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Ref Torque (Nm) '); plot( t , RefLoad);
subplot(4,4,6); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' StatorPuls (rad/s) '); plot( t , StatorPuls );
subplot(4,4,7); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Torque (Nm) '); plot( t , Torque );
subplot(4,4,8); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Ref Torque and Torque'); plot(t, RefLoad); plot(t, Torque);

subplot(4,4,9); hold on; grid on; zoom on; xlabel(' Ref Speed(rad/s) '); ylabel(' Ref Torque (Nm) '); plot(RefSpeed, RefLoad);
subplot(4,4,10); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Current (A) '); plot( t , Current );
subplot(4,4,11); hold on; grid on; zoom on; xlabel(' Speed(rad/s) '); ylabel(' Torque (Nm) '); plot(Speed, Torque);
subplot(4,4,12); hold on; grid on; zoom on; xlabel(' Speeds '); ylabel(' Torques '); plot(RefSpeed, RefLoad); plot(Speed, Torque);

%  hold on; grid on; zoom on; xlabel(' t(s)'); ylabel(' Ref Speed and Speed'); plot(t, RefSpeed); plot(t, Speed);
%  hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Ref Torque and Torque'); plot(t, RefLoad); plot(t, Torque);