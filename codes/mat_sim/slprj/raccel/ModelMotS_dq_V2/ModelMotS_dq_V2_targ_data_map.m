  function targMap = targDataMap(),

  ;%***********************
  ;% Create Parameter Map *
  ;%***********************
      
    nTotData      = 0; %add to this count as we go
    nTotSects     = 1;
    sectIdxOffset = 0;
    
    ;%
    ;% Define dummy sections & preallocate arrays
    ;%
    dumSection.nData = -1;  
    dumSection.data  = [];
    
    dumData.logicalSrcIdx = -1;
    dumData.dtTransOffset = -1;
    
    ;%
    ;% Init/prealloc paramMap
    ;%
    paramMap.nSections           = nTotSects;
    paramMap.sectIdxOffset       = sectIdxOffset;
      paramMap.sections(nTotSects) = dumSection; %prealloc
    paramMap.nTotData            = -1;
    
    ;%
    ;% Auto data (rtP)
    ;%
      section.nData     = 39;
      section.data(39)  = dumData; %prealloc
      
	  ;% rtP.J
	  section.data(1).logicalSrcIdx = 0;
	  section.data(1).dtTransOffset = 0;
	
	  ;% rtP.Lfr
	  section.data(2).logicalSrcIdx = 1;
	  section.data(2).dtTransOffset = 1;
	
	  ;% rtP.Lfs
	  section.data(3).logicalSrcIdx = 2;
	  section.data(3).dtTransOffset = 2;
	
	  ;% rtP.Lmt
	  section.data(4).logicalSrcIdx = 3;
	  section.data(4).dtTransOffset = 3;
	
	  ;% rtP.Lr
	  section.data(5).logicalSrcIdx = 4;
	  section.data(5).dtTransOffset = 4;
	
	  ;% rtP.P1
	  section.data(6).logicalSrcIdx = 5;
	  section.data(6).dtTransOffset = 5;
	
	  ;% rtP.P2
	  section.data(7).logicalSrcIdx = 6;
	  section.data(7).dtTransOffset = 6;
	
	  ;% rtP.Prinit
	  section.data(8).logicalSrcIdx = 7;
	  section.data(8).dtTransOffset = 7;
	
	  ;% rtP.Psdnom
	  section.data(9).logicalSrcIdx = 8;
	  section.data(9).dtTransOffset = 9;
	
	  ;% rtP.Psinit
	  section.data(10).logicalSrcIdx = 9;
	  section.data(10).dtTransOffset = 10;
	
	  ;% rtP.Rr
	  section.data(11).logicalSrcIdx = 10;
	  section.data(11).dtTransOffset = 12;
	
	  ;% rtP.Rs
	  section.data(12).logicalSrcIdx = 11;
	  section.data(12).dtTransOffset = 13;
	
	  ;% rtP.Ts
	  section.data(13).logicalSrcIdx = 12;
	  section.data(13).dtTransOffset = 14;
	
	  ;% rtP.Ulim
	  section.data(14).logicalSrcIdx = 13;
	  section.data(14).dtTransOffset = 15;
	
	  ;% rtP.Uo
	  section.data(15).logicalSrcIdx = 14;
	  section.data(15).dtTransOffset = 16;
	
	  ;% rtP.np
	  section.data(16).logicalSrcIdx = 15;
	  section.data(16).dtTransOffset = 17;
	
	  ;% rtP.tauL
	  section.data(17).logicalSrcIdx = 16;
	  section.data(17).dtTransOffset = 18;
	
	  ;% rtP.thrinit
	  section.data(18).logicalSrcIdx = 17;
	  section.data(18).dtTransOffset = 19;
	
	  ;% rtP.wL
	  section.data(19).logicalSrcIdx = 18;
	  section.data(19).dtTransOffset = 20;
	
	  ;% rtP.wrinit
	  section.data(20).logicalSrcIdx = 19;
	  section.data(20).dtTransOffset = 21;
	
	  ;% rtP.ReferenceSpeedrads_rep_seq_y
	  section.data(21).logicalSrcIdx = 20;
	  section.data(21).dtTransOffset = 22;
	
	  ;% rtP.Loadvaluepu_rep_seq_y
	  section.data(22).logicalSrcIdx = 21;
	  section.data(22).dtTransOffset = 406417;
	
	  ;% rtP.Gain_Gain
	  section.data(23).logicalSrcIdx = 22;
	  section.data(23).dtTransOffset = 701817;
	
	  ;% rtP.Gain4_Gain
	  section.data(24).logicalSrcIdx = 23;
	  section.data(24).dtTransOffset = 701818;
	
	  ;% rtP.UnitDelay2_InitialCondition
	  section.data(25).logicalSrcIdx = 24;
	  section.data(25).dtTransOffset = 701819;
	
	  ;% rtP.Constant_Value
	  section.data(26).logicalSrcIdx = 25;
	  section.data(26).dtTransOffset = 701820;
	
	  ;% rtP.Constant4_Value
	  section.data(27).logicalSrcIdx = 26;
	  section.data(27).dtTransOffset = 701821;
	
	  ;% rtP.Constant5_Value
	  section.data(28).logicalSrcIdx = 27;
	  section.data(28).dtTransOffset = 701822;
	
	  ;% rtP.Constant_Value_dn2cyv14tz
	  section.data(29).logicalSrcIdx = 28;
	  section.data(29).dtTransOffset = 701823;
	
	  ;% rtP.LookUpTable1_bp01Data
	  section.data(30).logicalSrcIdx = 29;
	  section.data(30).dtTransOffset = 701824;
	
	  ;% rtP.Constant_Value_jaivf4zt3q
	  section.data(31).logicalSrcIdx = 30;
	  section.data(31).dtTransOffset = 1108219;
	
	  ;% rtP.LookUpTable1_bp01Data_jgw1iq0tw2
	  section.data(32).logicalSrcIdx = 31;
	  section.data(32).dtTransOffset = 1108220;
	
	  ;% rtP.PulseGenerator2_Amp
	  section.data(33).logicalSrcIdx = 32;
	  section.data(33).dtTransOffset = 1403620;
	
	  ;% rtP.PulseGenerator2_Duty
	  section.data(34).logicalSrcIdx = 33;
	  section.data(34).dtTransOffset = 1403621;
	
	  ;% rtP.PulseGenerator2_PhaseDelay
	  section.data(35).logicalSrcIdx = 34;
	  section.data(35).dtTransOffset = 1403622;
	
	  ;% rtP.Gain5_Gain
	  section.data(36).logicalSrcIdx = 35;
	  section.data(36).dtTransOffset = 1403623;
	
	  ;% rtP.Gain3_Gain
	  section.data(37).logicalSrcIdx = 36;
	  section.data(37).dtTransOffset = 1403624;
	
	  ;% rtP.Gain_Gain_cqbytxvbu0
	  section.data(38).logicalSrcIdx = 37;
	  section.data(38).dtTransOffset = 1403625;
	
	  ;% rtP.Gain_Gain_f4udjbnlx2
	  section.data(39).logicalSrcIdx = 38;
	  section.data(39).dtTransOffset = 1403626;
	
      nTotData = nTotData + section.nData;
      paramMap.sections(1) = section;
      clear section
      
    
      ;%
      ;% Non-auto Data (parameter)
      ;%
    

    ;%
    ;% Add final counts to struct.
    ;%
    paramMap.nTotData = nTotData;
    


  ;%**************************
  ;% Create Block Output Map *
  ;%**************************
      
    nTotData      = 0; %add to this count as we go
    nTotSects     = 2;
    sectIdxOffset = 0;
    
    ;%
    ;% Define dummy sections & preallocate arrays
    ;%
    dumSection.nData = -1;  
    dumSection.data  = [];
    
    dumData.logicalSrcIdx = -1;
    dumData.dtTransOffset = -1;
    
    ;%
    ;% Init/prealloc sigMap
    ;%
    sigMap.nSections           = nTotSects;
    sigMap.sectIdxOffset       = sectIdxOffset;
      sigMap.sections(nTotSects) = dumSection; %prealloc
    sigMap.nTotData            = -1;
    
    ;%
    ;% Auto data (rtB)
    ;%
      section.nData     = 59;
      section.data(59)  = dumData; %prealloc
      
	  ;% rtB.llcuyb21kn
	  section.data(1).logicalSrcIdx = 0;
	  section.data(1).dtTransOffset = 0;
	
	  ;% rtB.mlubadklks
	  section.data(2).logicalSrcIdx = 1;
	  section.data(2).dtTransOffset = 1;
	
	  ;% rtB.agjnm01x4l
	  section.data(3).logicalSrcIdx = 2;
	  section.data(3).dtTransOffset = 2;
	
	  ;% rtB.os0fclte0m
	  section.data(4).logicalSrcIdx = 3;
	  section.data(4).dtTransOffset = 3;
	
	  ;% rtB.g50obrftrn
	  section.data(5).logicalSrcIdx = 4;
	  section.data(5).dtTransOffset = 4;
	
	  ;% rtB.hzaypudxs2
	  section.data(6).logicalSrcIdx = 5;
	  section.data(6).dtTransOffset = 5;
	
	  ;% rtB.lbn1yidduk
	  section.data(7).logicalSrcIdx = 6;
	  section.data(7).dtTransOffset = 6;
	
	  ;% rtB.cst0qen3tf
	  section.data(8).logicalSrcIdx = 7;
	  section.data(8).dtTransOffset = 7;
	
	  ;% rtB.mgdokchm00
	  section.data(9).logicalSrcIdx = 8;
	  section.data(9).dtTransOffset = 9;
	
	  ;% rtB.ocuyjhtq5x
	  section.data(10).logicalSrcIdx = 9;
	  section.data(10).dtTransOffset = 11;
	
	  ;% rtB.jijx3h41qa
	  section.data(11).logicalSrcIdx = 10;
	  section.data(11).dtTransOffset = 13;
	
	  ;% rtB.fsuvnkcxxk
	  section.data(12).logicalSrcIdx = 11;
	  section.data(12).dtTransOffset = 15;
	
	  ;% rtB.kywwenqxru
	  section.data(13).logicalSrcIdx = 12;
	  section.data(13).dtTransOffset = 17;
	
	  ;% rtB.pzn3ntwo0f
	  section.data(14).logicalSrcIdx = 13;
	  section.data(14).dtTransOffset = 18;
	
	  ;% rtB.mugp5ilmof
	  section.data(15).logicalSrcIdx = 14;
	  section.data(15).dtTransOffset = 19;
	
	  ;% rtB.lfrpqznzmd
	  section.data(16).logicalSrcIdx = 15;
	  section.data(16).dtTransOffset = 21;
	
	  ;% rtB.czrf0nwdxd
	  section.data(17).logicalSrcIdx = 16;
	  section.data(17).dtTransOffset = 22;
	
	  ;% rtB.aa0ktk1lsw
	  section.data(18).logicalSrcIdx = 17;
	  section.data(18).dtTransOffset = 23;
	
	  ;% rtB.pt232evoj1
	  section.data(19).logicalSrcIdx = 18;
	  section.data(19).dtTransOffset = 24;
	
	  ;% rtB.lrkvz4jnvf
	  section.data(20).logicalSrcIdx = 19;
	  section.data(20).dtTransOffset = 26;
	
	  ;% rtB.fgi23zg44a
	  section.data(21).logicalSrcIdx = 20;
	  section.data(21).dtTransOffset = 28;
	
	  ;% rtB.ig1a00v4ao
	  section.data(22).logicalSrcIdx = 21;
	  section.data(22).dtTransOffset = 30;
	
	  ;% rtB.ngdf4g2c30
	  section.data(23).logicalSrcIdx = 22;
	  section.data(23).dtTransOffset = 31;
	
	  ;% rtB.dhnrbjjk55
	  section.data(24).logicalSrcIdx = 23;
	  section.data(24).dtTransOffset = 32;
	
	  ;% rtB.c40hosfmrc
	  section.data(25).logicalSrcIdx = 24;
	  section.data(25).dtTransOffset = 33;
	
	  ;% rtB.a01avw2uam
	  section.data(26).logicalSrcIdx = 25;
	  section.data(26).dtTransOffset = 34;
	
	  ;% rtB.its0a3zvwu
	  section.data(27).logicalSrcIdx = 26;
	  section.data(27).dtTransOffset = 36;
	
	  ;% rtB.ki404yqcws
	  section.data(28).logicalSrcIdx = 27;
	  section.data(28).dtTransOffset = 38;
	
	  ;% rtB.icrg1c0qbg
	  section.data(29).logicalSrcIdx = 28;
	  section.data(29).dtTransOffset = 40;
	
	  ;% rtB.n5nk0fcdxe
	  section.data(30).logicalSrcIdx = 29;
	  section.data(30).dtTransOffset = 42;
	
	  ;% rtB.jy42n5bwff
	  section.data(31).logicalSrcIdx = 30;
	  section.data(31).dtTransOffset = 43;
	
	  ;% rtB.onyyxbyf00
	  section.data(32).logicalSrcIdx = 31;
	  section.data(32).dtTransOffset = 44;
	
	  ;% rtB.h15hfh1vi3
	  section.data(33).logicalSrcIdx = 32;
	  section.data(33).dtTransOffset = 45;
	
	  ;% rtB.o4pvd4evkd
	  section.data(34).logicalSrcIdx = 33;
	  section.data(34).dtTransOffset = 47;
	
	  ;% rtB.do1g1252oq
	  section.data(35).logicalSrcIdx = 34;
	  section.data(35).dtTransOffset = 48;
	
	  ;% rtB.dxxqwldjss
	  section.data(36).logicalSrcIdx = 35;
	  section.data(36).dtTransOffset = 50;
	
	  ;% rtB.lrfbty4a0y
	  section.data(37).logicalSrcIdx = 36;
	  section.data(37).dtTransOffset = 52;
	
	  ;% rtB.ggbp0eubus
	  section.data(38).logicalSrcIdx = 37;
	  section.data(38).dtTransOffset = 54;
	
	  ;% rtB.ohojx4cexj
	  section.data(39).logicalSrcIdx = 38;
	  section.data(39).dtTransOffset = 55;
	
	  ;% rtB.awofsj5yej
	  section.data(40).logicalSrcIdx = 39;
	  section.data(40).dtTransOffset = 56;
	
	  ;% rtB.oussmmuoy4
	  section.data(41).logicalSrcIdx = 41;
	  section.data(41).dtTransOffset = 57;
	
	  ;% rtB.jp0zo1h5he
	  section.data(42).logicalSrcIdx = 42;
	  section.data(42).dtTransOffset = 59;
	
	  ;% rtB.of25molymw
	  section.data(43).logicalSrcIdx = 43;
	  section.data(43).dtTransOffset = 60;
	
	  ;% rtB.d005tmuemj
	  section.data(44).logicalSrcIdx = 44;
	  section.data(44).dtTransOffset = 61;
	
	  ;% rtB.hxnwe04xgr
	  section.data(45).logicalSrcIdx = 45;
	  section.data(45).dtTransOffset = 62;
	
	  ;% rtB.fzmloa30x1
	  section.data(46).logicalSrcIdx = 46;
	  section.data(46).dtTransOffset = 63;
	
	  ;% rtB.lpi4yujqet
	  section.data(47).logicalSrcIdx = 47;
	  section.data(47).dtTransOffset = 64;
	
	  ;% rtB.gapqmgw3j0
	  section.data(48).logicalSrcIdx = 48;
	  section.data(48).dtTransOffset = 65;
	
	  ;% rtB.d0fm2u13is
	  section.data(49).logicalSrcIdx = 49;
	  section.data(49).dtTransOffset = 66;
	
	  ;% rtB.iemxz0ldwq
	  section.data(50).logicalSrcIdx = 50;
	  section.data(50).dtTransOffset = 67;
	
	  ;% rtB.ij2le252ln
	  section.data(51).logicalSrcIdx = 51;
	  section.data(51).dtTransOffset = 69;
	
	  ;% rtB.aqq1i4urck
	  section.data(52).logicalSrcIdx = 52;
	  section.data(52).dtTransOffset = 71;
	
	  ;% rtB.dwwm1dvarc
	  section.data(53).logicalSrcIdx = 53;
	  section.data(53).dtTransOffset = 73;
	
	  ;% rtB.mpsvxrvii2
	  section.data(54).logicalSrcIdx = 54;
	  section.data(54).dtTransOffset = 74;
	
	  ;% rtB.gnoc4y3eil
	  section.data(55).logicalSrcIdx = 55;
	  section.data(55).dtTransOffset = 75;
	
	  ;% rtB.kqmoni0qee
	  section.data(56).logicalSrcIdx = 56;
	  section.data(56).dtTransOffset = 76;
	
	  ;% rtB.bc0tqww1op
	  section.data(57).logicalSrcIdx = 57;
	  section.data(57).dtTransOffset = 77;
	
	  ;% rtB.kxei2q2tej
	  section.data(58).logicalSrcIdx = 58;
	  section.data(58).dtTransOffset = 79;
	
	  ;% rtB.lfdym3aanm
	  section.data(59).logicalSrcIdx = 59;
	  section.data(59).dtTransOffset = 81;
	
      nTotData = nTotData + section.nData;
      sigMap.sections(1) = section;
      clear section
      
      section.nData     = 2;
      section.data(2)  = dumData; %prealloc
      
	  ;% rtB.k4xamhzsst
	  section.data(1).logicalSrcIdx = 60;
	  section.data(1).dtTransOffset = 0;
	
	  ;% rtB.oleotyrvsj
	  section.data(2).logicalSrcIdx = 61;
	  section.data(2).dtTransOffset = 1;
	
      nTotData = nTotData + section.nData;
      sigMap.sections(2) = section;
      clear section
      
    
      ;%
      ;% Non-auto Data (signal)
      ;%
    

    ;%
    ;% Add final counts to struct.
    ;%
    sigMap.nTotData = nTotData;
    


  ;%*******************
  ;% Create DWork Map *
  ;%*******************
      
    nTotData      = 0; %add to this count as we go
    nTotSects     = 6;
    sectIdxOffset = 2;
    
    ;%
    ;% Define dummy sections & preallocate arrays
    ;%
    dumSection.nData = -1;  
    dumSection.data  = [];
    
    dumData.logicalSrcIdx = -1;
    dumData.dtTransOffset = -1;
    
    ;%
    ;% Init/prealloc dworkMap
    ;%
    dworkMap.nSections           = nTotSects;
    dworkMap.sectIdxOffset       = sectIdxOffset;
      dworkMap.sections(nTotSects) = dumSection; %prealloc
    dworkMap.nTotData            = -1;
    
    ;%
    ;% Auto data (rtDW)
    ;%
      section.nData     = 2;
      section.data(2)  = dumData; %prealloc
      
	  ;% rtDW.piiyfoznre
	  section.data(1).logicalSrcIdx = 0;
	  section.data(1).dtTransOffset = 0;
	
	  ;% rtDW.icx4udn11x
	  section.data(2).logicalSrcIdx = 1;
	  section.data(2).dtTransOffset = 1;
	
      nTotData = nTotData + section.nData;
      dworkMap.sections(1) = section;
      clear section
      
      section.nData     = 1;
      section.data(1)  = dumData; %prealloc
      
	  ;% rtDW.abyvocg0q5
	  section.data(1).logicalSrcIdx = 2;
	  section.data(1).dtTransOffset = 0;
	
      nTotData = nTotData + section.nData;
      dworkMap.sections(2) = section;
      clear section
      
      section.nData     = 1;
      section.data(1)  = dumData; %prealloc
      
	  ;% rtDW.jevq1wybfe.LoggedData
	  section.data(1).logicalSrcIdx = 3;
	  section.data(1).dtTransOffset = 0;
	
      nTotData = nTotData + section.nData;
      dworkMap.sections(3) = section;
      clear section
      
      section.nData     = 2;
      section.data(2)  = dumData; %prealloc
      
	  ;% rtDW.ccffucponj
	  section.data(1).logicalSrcIdx = 4;
	  section.data(1).dtTransOffset = 0;
	
	  ;% rtDW.npl1j2qvtj
	  section.data(2).logicalSrcIdx = 5;
	  section.data(2).dtTransOffset = 1;
	
      nTotData = nTotData + section.nData;
      dworkMap.sections(4) = section;
      clear section
      
      section.nData     = 2;
      section.data(2)  = dumData; %prealloc
      
	  ;% rtDW.hdmj0f2xda
	  section.data(1).logicalSrcIdx = 6;
	  section.data(1).dtTransOffset = 0;
	
	  ;% rtDW.ncgacd0shm
	  section.data(2).logicalSrcIdx = 7;
	  section.data(2).dtTransOffset = 1;
	
      nTotData = nTotData + section.nData;
      dworkMap.sections(5) = section;
      clear section
      
      section.nData     = 2;
      section.data(2)  = dumData; %prealloc
      
	  ;% rtDW.cobnjav3td
	  section.data(1).logicalSrcIdx = 8;
	  section.data(1).dtTransOffset = 0;
	
	  ;% rtDW.cg43etw1s5
	  section.data(2).logicalSrcIdx = 9;
	  section.data(2).dtTransOffset = 1;
	
      nTotData = nTotData + section.nData;
      dworkMap.sections(6) = section;
      clear section
      
    
      ;%
      ;% Non-auto Data (dwork)
      ;%
    

    ;%
    ;% Add final counts to struct.
    ;%
    dworkMap.nTotData = nTotData;
    


  ;%
  ;% Add individual maps to base struct.
  ;%

  targMap.paramMap  = paramMap;    
  targMap.signalMap = sigMap;
  targMap.dworkMap  = dworkMap;
  
  ;%
  ;% Add checksums to base struct.
  ;%


  targMap.checksum0 = 1751391696;
  targMap.checksum1 = 1507898288;
  targMap.checksum2 = 8788277;
  targMap.checksum3 = 3058308105;

