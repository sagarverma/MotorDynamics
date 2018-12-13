%     Voltage: [1x1 timeseries]
%     Current: [1x1 timeseries]
%       Speed: [1x1 timeseries]
%      Torque: [1x1 timeseries]

%
%
Data = Data_ab;

Voltage = Data.Voltage.Data; t = Data.Voltage.Time;
Current = Data.Current.Data; %t = Data.Current.Time;
Speed   = Data.Speed.Data;   %t = Data.Speed.Time;
Torque  = Data.Torque.Data;  %t = Data.Torque.Time;

figure;  set(gcf,'Name','ab')
subplot(221); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Voltage (V) '); plot( t , Voltage );
subplot(223); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Current (A) '); plot( t , Current );
subplot(222); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Speed (rad/s) '); plot( t , Speed );
subplot(224); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Torque (Nm) '); plot( t , Torque );

