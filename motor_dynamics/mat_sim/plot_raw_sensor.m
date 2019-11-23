       data = load('../../../datasets/RawData/OFVC4kW_LM10Hz_paliers__0to120PercTnom_Data.mat');
%        data = load('../../datasets/RawData/OFVC4kW_LM50Hz_paliers_0to120PercTnom_Data.mat');
%        data = load('../../datasets/RawData/OFVC4kW_LM68Hz_paliers_0to120PercTnom_Data.mat');
%        data = load('../../datasets/RawData/OFVC4kW_NoLM_paliers_0to100Hz_Data.mat');
%   data = load('../../datasets/RawData/OFVC4kW_NoLM_SpeedVariations2_20190419_Data.mat');
%   data = load('../../datasets/RawData/OFVC4kW_LM60Hz_TorqueSteps_20190419_Data.mat');
%   data = load('../../datasets/RawData/OFVC4kW_NoLM_SpeedVariations_20190419_Data.mat');
%    data = load('../../datasets/RawData/OFVC4kW_LM45Hz_TorqueSteps_20190419_Data.mat');
%   data = load('../../datasets/RawData/OFVC4kW_LM20Hz_TorqueSteps_20190419_Data.mat');

vd = hampel(data.VdRef_V);
vq = hampel(data.VqRef_V);
vt = data.Time_VSpdTq;

id = hampel(data.IdMeas_A)

vd = hampel(data.VdRef_V);
vq = hampel(data.VqRef_V);
vt = data.Time_VSpdTq;

id = hampel(data.IdMeas_A);
iq = hampel(data.IqMeas_A);
it = data.Time_I;

spd = hampel(data.Speed_Hz) * 2 * pi;
trq = hampel(data.Torque_PercTnom) /100 * 25;

figure; set(gcf,'Name','alpha beta')
subplot(321); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Voltage (V) '); 
plot( vt , vd); plot(vt, vq);

subplot(325); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Current (A) '); 
plot( it , id); plot(it, iq);

subplot(222); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Speed (rad/s) '); plot(vt, spd);
subplot(224); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Torque (Nm) '); plot( vt, trq );

