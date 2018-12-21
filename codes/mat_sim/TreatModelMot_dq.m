%     Voltage: [1x1 timeseries]
%     Current: [1x1 timeseries]
%       Speed: [1x1 timeseries]
%      Torque: [1x1 timeseries]

%
%
data = load('../../datasets/CS2018_12_14/DataForSagar.mat');
Data = data.Data_dq;

Voltage = Data.Voltage.Data; t = Data.Voltage.Time;
StatorPuls = Data.StatorPuls.Data; %t = Data.StatorPuls.Time;
Current = Data.Current.Data; %t = Data.Current.Time;
Speed   = Data.Speed.Data;   %t = Data.Speed.Time;
Torque  = Data.Torque.Data;  %t = Data.Torque.Time;

figure; set(gcf,'Name','dq')
subplot(321); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Voltage (V) '); plot( t , Voltage );
subplot(323); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' StatorPuls (rad/s) '); plot( t , StatorPuls );
subplot(325); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Current (A) '); plot( t , Current );
subplot(222); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Speed (rad/s) '); plot( t , Speed );
subplot(224); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Torque (Nm) '); plot( t , Torque );

