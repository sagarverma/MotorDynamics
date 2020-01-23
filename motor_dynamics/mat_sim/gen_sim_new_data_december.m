%load_system('ModelMotS_dq');


Ts = 0.000250;
Rs = 1.5; Rr = 0.9;
Ls = 0.160; Lr = 0.160; Lm = 0.153; 
Lfs = 0.007; Lfr = 0.007; Lmt = 0.210; P1 = 0.7; P2 = 1.5;
np = 2;
Psdnom = 0.95; Uo = 15; Ulim = 415*sqrt(2/3);
Psinit = [ 0 ; 0 ]; Prinit = [ 0 ; 0 ];
J = 0.045;
wrinit = 2*pi*0;
thrinit = 0;
tauL = 25;
wL = 2*pi*0;

wn = 2*pi*50;
Tn = 25;


load_system('ModelMotS_dq');
data = load('../../../datasets/RefSynthData/Data8Feb2019.mat');

t = strcat('[',num2str(data.t'),']');
speed = strcat('[',num2str(data.Speed'),']');
torque= strcat('[',num2str(data.Kvalv'),']');

set_param('ModelMotS_dq/Reference Speed (rad//s)','rep_seq_t',t,'rep_seq_y',speed);
set_param('ModelMotS_dq/Load value p.u.','rep_seq_t',t,'rep_seq_y',torque);

% simOut = sim('ModelMotS_dq_V2', 'SimulationMode', 'rapid',... 
%         'StopTime', '1200', 'SaveOutput','on',...
%         'OutputSaveName','Data_dq','SaveFormat', 'Dataset');
% Data_dq = simOut.get('Data_dq');
% save('../../datasets/data_sim_ab_d2.mat', 'Data_dq');
    
