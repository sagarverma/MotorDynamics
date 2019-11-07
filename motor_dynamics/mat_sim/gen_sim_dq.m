%load_system('ModelMotS_dq');

files = dir('../../../datasets/benchmark/sim_dynamic/Exp_acc_0.5_load_0_speed_50*.mat')
for file = files'
    
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

    model = 'ModelMotS_dq_V2bis_FVC';
    load_system(model);


    data = load(strcat('../../../datasets/benchmark/sim_dynamic/', file.name));

    t = strcat('[',num2str(data.t),']');
    speed = strcat('[',num2str(data.Speed),']');
    torque= strcat('[',num2str(data.Kvalv),']');

    fprintf('data2str\n');

    set_param('ModelMotS_dq_V2bis_FVC/Reference Speed (rad//s)','rep_seq_t',t,'rep_seq_y',speed);
    set_param('ModelMotS_dq_V2bis_FVC/Load value p.u.','rep_seq_t',t,'rep_seq_y',torque);

    fprintf('model data load\n');

    simOut = sim('ModelMotS_dq_V2bis_FVC', 'SimulationMode', 'normal',... 
           'StopTime', '24', 'SaveOutput','on',...
           'OutputSaveName','Data_dq','SaveFormat', 'Dataset');
    Data_dq = simOut.get('Data_dq');

    voltage = Data_dq.Voltage.Data;
    current = Data_dq.Current.Data;
    torque = Data_dq.Torque.Data;
    speed = Data_dq.Speed.Data;
    statorPuls = Data_dq.StatorPuls.Data;
    time = Data_dq.Torque.Time;
% 
    
%      save(strcat('../../../datasets/benchmark/sim_dynamic_output/', strrep(file.name, '.mat',''), '/Voltage.mat'), 'voltage');
%      save(strcat('../../../datasets/benchmark/sim_dynamic_output/', strrep(file.name, '.mat',''), '/Current.mat'), 'current');
%      save(strcat('../../../datasets/benchmark/sim_dynamic_output/', strrep(file.name, '.mat',''), '/Torque.mat'), 'torque');
%      save(strcat('../../../datasets/benchmark/sim_dynamic_output/', strrep(file.name, '.mat',''), '/Speed.mat'), 'speed');
%      save(strcat('../../../datasets/benchmark/sim_dynamic_output/', strrep(file.name, '.mat',''), '/StatorPuls.mat'), 'statorPuls');
%      save(strcat('../../../datasets/benchmark/sim_dynamic_output/', strrep(file.name, '.mat',''), '/Time.mat'), 'time');
% 
%      clear 
break
end
