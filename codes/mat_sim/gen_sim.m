%load_system('ModelMotS_dq');
fid = fopen('../../datasets/sample_speeds.txt');
txt = textscan(fid,'%s','delimiter','\n');
fclose(fid);

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

exp_no = 1;
for i = 1:5:length(txt{1,1})
    i
    load_system('ModelMotS_dq');
    set_param('ModelMotS_dq/Reference Speed (rad//s)','rep_seq_t',txt{1,1}{i,1},'rep_seq_y',txt{1,1}{i+1,1});
    set_param('ModelMotS_dq/Load value p.u.','rep_seq_t',txt{1,1}{i+2,1},'rep_seq_y',txt{1,1}{i+3,1});
    simOut = sim('ModelMotS_dq', 'SimulationMode', 'rapid',... 
            'StopTime', txt{1,1}{i+4,1}, 'SaveOutput','on',...
            'OutputSaveName','Data_dq','SaveFormat', 'Dataset');
    Data_dq = simOut.get('Data_dq');
    save(strcat('../../datasets/sample_experiments/exp', int2str(exp_no), '.mat'), 'Data_dq');
    exp_no = exp_no + 1;
end
    
