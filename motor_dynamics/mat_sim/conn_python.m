function [data] = runSim(speed, torque, speed_time, torque_time, simTime)

  model = 'ModelMotS_dq_V2bis_FVC';
  load_system(model);

  fprintf('data2str\n');

  set_param('ModelMotS_dq_V2bis_FVC/Reference Speed (rad//s)', 'rep_seq_t', speed_time, 'rep_seq_y', speed);
  set_param('ModelMotS_dq_V2bis_FVC/Load value p.u.', 'rep_seq_t', torque_time, 'rep_seq_y', torque);

  fprintf('model data load\n');

  simOut = sim('ModelMotS_dq_V2bis_FVC', 'SimulationMode', 'normal',...
         'StopTime', simTime, 'SaveOutput','on',...
         'OutputSaveName','Data_dq','SaveFormat', 'Dataset');
  Data_dq = simOut.get('Data_dq');
  voltage = Data_dq.Voltage.Data;
  current = Data_dq.Current.Data;
  torque = Data_dq.Torque.Data;
  speed = Data_dq.Speed.Data;
  statorPuls = Data_dq.StatorPuls.Data;
  time = Data_dq.Torque.Time;

  data = [voltage, current, torque, speed, statorPuls, time];

end
