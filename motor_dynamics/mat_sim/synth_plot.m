% fold_name = '0-100Hz.mat';
%  fold_name = '0-120TNm_0-100Hz.mat';
%  fold_name = '10LM.mat';
%  fold_name = '30LM.mat';
%  fold_name = '50LM.mat';
%  fold_name = '68LM.mat';
%  fold_name = 'Data8Feb2019.mat';
%  fold_name = 'DATACS2det.mat';
%  fold_name = 'DATACSdet.mat';
% fold_name = 'NoLM_SpeedVariations2.mat';
% fold_name = 'LM60_TorqueSteps.mat';
%  fold_name = 'NoLM_SpeedVariations.mat'
%  fold_name = 'LM45_TorqueSteps.mat';
 fold_name = 'LM20_TorqueSteps.mat';

voltage = load(strcat('../../../datasets/SimSynthData/', fold_name, '/Voltage.mat'));
current = load(strcat('../../../datasets/SimSynthData/', fold_name, '/Current.mat'));
statorPuls = load(strcat('../../../datasets/SimSynthData/', fold_name, '/StatorPuls.mat'));
speed = load(strcat('../../../datasets/SimSynthData/', fold_name, '/Speed.mat'));
torque = load(strcat('../../../datasets/SimSynthData/', fold_name, '/Torque.mat'));
time = load(strcat('../../../datasets/SimSynthData/', fold_name, '/Time.mat'));

figure; set(gcf,'Name','dq')
subplot(321); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Voltage (V) '); plot( time.time , voltage.voltage );
subplot(323); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' StatorPuls (rad/s) '); plot( time.time , statorPuls.statorPuls );
subplot(325); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Current (A) '); plot( time.time , current.current );
subplot(222); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Speed (rad/s) '); plot( time.time , speed.speed );
subplot(224); hold on; grid on; zoom on; xlabel(' t(s) '); ylabel(' Torque (Nm) '); plot( time.time , torque.torque );