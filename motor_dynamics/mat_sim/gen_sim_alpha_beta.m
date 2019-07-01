%load_system('ModelMotS_dq');

for i = 299:299
    
Data_Ts = 0.005;

Ts = 0.000250;
Tpwm = Ts;
Tfixe = 500e-6;

Rs = 1.5; Rr = 0.9;
Ls = 0.160; Lr = 0.160; Lm = 0.153; 
Lfs = 0.007; Lfr = 0.007; Lmt = 0.210; P1 = 0.7; P2 = 1.5;
np = 2;
Psdnom = 0.95; Uo = 15; Ulim = 415*sqrt(2/3);
Psinit = [ 0 ; 0 ]; Prinit = [ 0 ; 0 ];
Inom = 9.1; Prdnom = 1; SLP_Coeff = 100; Vnom = 400;
SFC_Coeff = 100;

J = 0.045;
wrinit = 2*pi*0;
thrinit = 0;
Jm = J;

tauL = 25;
wL = 2*pi*0;

wCurr = 0;
wSpeed_PI = 2*pi*2.5; xiSpeed_PI = 1;
wCurr_PI = 2*pi*50; xiCurr_PI = 1/2;
wSpeedEst = 2*pi*500;

wn = 2*pi*50;
Tn = 25;

model = 'ModelMotS_AlphaBeta_bis_FVC';
load_system(model);


data = load(strcat('../../datasets/synth_simulink/reference_data/Exp', int2str(i), '.mat'));

t = strcat('[',num2str(data.t),']');
speed = strcat('[',num2str(data.Speed),']');
torque= strcat('[',num2str(data.Kvalv),']');

fprintf('data2str\n');

set_param('ModelMotS_AlphaBeta_bis_FVC/Reference Speed (rad//s)2','rep_seq_t',t,'rep_seq_y',speed);
set_param('ModelMotS_AlphaBeta_bis_FVC/Load value p.u.2','rep_seq_t',t,'rep_seq_y',torque);

fprintf('model data load\n');

simOut = sim('ModelMotS_AlphaBeta_bis_FVC', 'SimulationMode', 'normal',... 
       'StopTime', '1200', 'SaveOutput','on',...
       'OutputSaveName','Data_ab','SaveFormat', 'Dataset');
Data_ab = simOut.get('Data_ab');

voltage = Data_ab.Voltage.Data;
current = Data_ab.Current.Data;
torque = Data_ab.Torque.Data;
speed = Data_ab.Speed.Data;
% statorPuls = Data_dq.StatorPuls.Data;
time = Data_ab.Torque.Time;

save(strcat('/home/sv/workspace/motor_control/datasets/synth_simulink/simulink_output/AlphaBeta_Exp', int2str(i), '/Voltage.mat'), 'voltage');
save(strcat('/home/sv/workspace/motor_control/datasets/synth_simulink/simulink_output/AlphaBeta_Exp', int2str(i), '/Current.mat'), 'current');
save(strcat('/home/sv/workspace/motor_control/datasets/synth_simulink/simulink_output/AlphaBeta_Exp', int2str(i), '/Torque.mat'), 'torque');
save(strcat('/home/sv/workspace/motor_control/datasets/synth_simulink/simulink_output/AlphaBeta_Exp', int2str(i), '/Speed.mat'), 'speed');
% save(strcat('/home/sv/workspace/motor_control/datasets/synth_simulink/simulink_output/AlphaBeta_Exp', int2str(i), '/StatorPuls.mat'), 'statorPuls');
save(strcat('/home/sv/workspace/motor_control/datasets/synth_simulink/simulink_output/AlphaBeta_Exp', int2str(i), '/Time.mat'), 'time');

clear 

end
