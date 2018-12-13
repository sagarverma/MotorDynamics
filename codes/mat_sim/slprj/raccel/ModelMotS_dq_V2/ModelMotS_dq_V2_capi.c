#include "__cf_ModelMotS_dq_V2.h"
#include "rtw_capi.h"
#ifdef HOST_CAPI_BUILD
#include "ModelMotS_dq_V2_capi_host.h"
#define sizeof(s) ((size_t)(0xFFFF))
#undef rt_offsetof
#define rt_offsetof(s,el) ((uint16_T)(0xFFFF))
#define TARGET_CONST
#define TARGET_STRING(s) (s)    
#ifndef SS_INT64
#define SS_INT64  15
#endif
#ifndef SS_UINT64
#define SS_UINT64  16
#endif
#else
#include "builtin_typeid_types.h"
#include "ModelMotS_dq_V2.h"
#include "ModelMotS_dq_V2_capi.h"
#include "ModelMotS_dq_V2_private.h"
#ifdef LIGHT_WEIGHT_CAPI
#define TARGET_CONST                  
#define TARGET_STRING(s)               (NULL)                    
#else
#define TARGET_CONST                   const
#define TARGET_STRING(s)               (s)
#endif
#endif
static const rtwCAPI_Signals rtBlockSignals [ ] = { { 0 , 6 , TARGET_STRING (
"ModelMotS_dq_V2/UF control _ dqframe" ) , TARGET_STRING ( "" ) , 0 , 0 , 0 ,
0 , 0 } , { 1 , 6 , TARGET_STRING ( "ModelMotS_dq_V2/UF control _ dqframe" )
, TARGET_STRING ( "" ) , 1 , 0 , 1 , 0 , 0 } , { 2 , 0 , TARGET_STRING (
"ModelMotS_dq_V2/Pulse Generator2" ) , TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 ,
1 } , { 3 , 1 , TARGET_STRING ( "ModelMotS_dq_V2/Constant Load System2/Gain"
) , TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 4 , 0 , TARGET_STRING (
"ModelMotS_dq_V2/Constant Load System2/Product" ) , TARGET_STRING ( "" ) , 0
, 0 , 1 , 0 , 2 } , { 5 , 0 , TARGET_STRING (
"ModelMotS_dq_V2/Constant Load System2/Switch" ) , TARGET_STRING ( "" ) , 0 ,
0 , 1 , 0 , 2 } , { 6 , 0 , TARGET_STRING (
"ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Gain14" ) ,
TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 , 2 } , { 7 , 0 , TARGET_STRING (
"ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Gain2" ) ,
TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 , 2 } , { 8 , 0 , TARGET_STRING (
"ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Gain4" ) ,
TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 9 , 0 , TARGET_STRING (
"ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Integrator" ) ,
TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 , 2 } , { 10 , 0 , TARGET_STRING (
"ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Integrator1" ) ,
TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 , 2 } , { 11 , 0 , TARGET_STRING (
"ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Product" ) ,
TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 , 2 } , { 12 , 0 , TARGET_STRING (
"ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Product1" ) ,
TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 , 2 } , { 13 , 0 , TARGET_STRING (
"ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Sum" ) , TARGET_STRING
( "" ) , 0 , 0 , 0 , 0 , 2 } , { 14 , 0 , TARGET_STRING (
"ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Sum1" ) , TARGET_STRING
( "" ) , 0 , 0 , 0 , 0 , 2 } , { 15 , 0 , TARGET_STRING (
"ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Sum3" ) , TARGET_STRING
( "" ) , 0 , 0 , 1 , 0 , 2 } , { 16 , 0 , TARGET_STRING (
"ModelMotS_dq_V2/Induction Motor - Mechanical part Rigid Coupling2/Gain" ) ,
TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 17 , 0 , TARGET_STRING (
"ModelMotS_dq_V2/Induction Motor - Mechanical part Rigid Coupling2/Integrator2"
) , TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 18 , 0 , TARGET_STRING (
"ModelMotS_dq_V2/Induction Motor - Mechanical part Rigid Coupling2/Sum2" ) ,
TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 19 , 0 , TARGET_STRING (
"ModelMotS_dq_V2/Load value p.u./Output" ) , TARGET_STRING ( "" ) , 0 , 0 , 1
, 0 , 2 } , { 20 , 0 , TARGET_STRING ( "ModelMotS_dq_V2/Load value p.u./Sum"
) , TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 21 , 0 , TARGET_STRING (
"ModelMotS_dq_V2/Reference Speed (rad//s)/Output" ) , TARGET_STRING ( "" ) ,
0 , 0 , 1 , 0 , 2 } , { 22 , 6 , TARGET_STRING (
"ModelMotS_dq_V2/UF control _ dqframe/wref" ) , TARGET_STRING ( "" ) , 0 , 0
, 1 , 0 , 0 } , { 23 , 0 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Electromagnetic torque/Gain"
) , TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 24 , 0 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Electromagnetic torque/Product"
) , TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 25 , 0 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Electromagnetic torque/Product1"
) , TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 26 , 0 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Electromagnetic torque/Sum2"
) , TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 27 , 0 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/Gain"
) , TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 , 2 } , { 28 , 0 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/Gain1"
) , TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 , 2 } , { 29 , 0 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/Gain2"
) , TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 , 2 } , { 30 , 0 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/Gain3"
) , TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 , 2 } , { 31 , 0 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/Sum3"
) , TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 , 2 } , { 32 , 0 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/Sum4"
) , TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 , 2 } , { 33 , 0 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/Sum5"
) , TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 , 2 } , { 34 , 0 , TARGET_STRING (
"ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/jPr/Gain" ) ,
TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 35 , 0 , TARGET_STRING (
"ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/jPs/Gain" ) ,
TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 36 , 0 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/f/Fcn"
) , TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 37 , 0 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/f/Gain3"
) , TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 3 } , { 38 , 0 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/f/Math Function3"
) , TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 3 } , { 39 , 2 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/f/Product1"
) , TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 40 , 2 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/f/Product2"
) , TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 , 2 } , { 41 , 2 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/f/Product3"
) , TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 , 2 } , { 42 , 2 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/f/Product4"
) , TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 43 , 0 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/f/Relational Operator1"
) , TARGET_STRING ( "" ) , 0 , 1 , 1 , 0 , 4 } , { 44 , 2 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/f/Sum8"
) , TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 45 , 2 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/f/Sum9"
) , TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 46 , 0 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/f/Switch"
) , TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 , 2 } , { 47 , 0 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/g_1/Gain2"
) , TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 48 , 4 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/g_1/Gain3"
) , TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 49 , 4 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/g_1/Gain4"
) , TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 50 , 0 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/g_1/Gain5"
) , TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 3 } , { 51 , 3 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/g_1/Gain6"
) , TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 , 2 } , { 52 , 4 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/g_1/Product"
) , TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 53 , 4 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/g_1/Product1"
) , TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 54 , 4 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/g_1/Product2"
) , TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 , 2 } , { 55 , 4 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/g_1/Product3"
) , TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 , 2 } , { 56 , 0 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/g_1/Relational Operator1"
) , TARGET_STRING ( "" ) , 0 , 1 , 1 , 0 , 4 } , { 57 , 4 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/g_1/Sum4"
) , TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 58 , 4 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/g_1/Sum5"
) , TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 59 , 4 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/g_1/Sum6"
) , TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 60 , 4 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/g_1/Sum7"
) , TARGET_STRING ( "" ) , 0 , 0 , 1 , 0 , 2 } , { 61 , 0 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/g_1/Switch"
) , TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 , 2 } , { 62 , 6 , TARGET_STRING (
"ModelMotS_dq_V2/UF control _ dqframe/UF control/Limitation/Product1" ) ,
TARGET_STRING ( "" ) , 0 , 0 , 0 , 0 , 0 } , { 0 , 0 , ( NULL ) , ( NULL ) ,
0 , 0 , 0 , 0 , 0 } } ; static const rtwCAPI_BlockParameters
rtBlockParameters [ ] = { { 63 , TARGET_STRING (
"ModelMotS_dq_V2/Load value p.u." ) , TARGET_STRING ( "rep_seq_y" ) , 0 , 2 ,
0 } , { 64 , TARGET_STRING ( "ModelMotS_dq_V2/Reference Speed (rad//s)" ) ,
TARGET_STRING ( "rep_seq_y" ) , 0 , 3 , 0 } , { 65 , TARGET_STRING (
"ModelMotS_dq_V2/Pulse Generator2" ) , TARGET_STRING ( "Amplitude" ) , 0 , 1
, 0 } , { 66 , TARGET_STRING ( "ModelMotS_dq_V2/Pulse Generator2" ) ,
TARGET_STRING ( "PulseWidth" ) , 0 , 1 , 0 } , { 67 , TARGET_STRING (
"ModelMotS_dq_V2/Pulse Generator2" ) , TARGET_STRING ( "PhaseDelay" ) , 0 , 1
, 0 } , { 68 , TARGET_STRING ( "ModelMotS_dq_V2/Constant Load System2/Gain" )
, TARGET_STRING ( "Gain" ) , 0 , 1 , 0 } , { 69 , TARGET_STRING (
"ModelMotS_dq_V2/Load value p.u./Constant" ) , TARGET_STRING ( "Value" ) , 0
, 1 , 0 } , { 70 , TARGET_STRING (
"ModelMotS_dq_V2/Load value p.u./Look-Up Table1" ) , TARGET_STRING (
"BreakpointsForDimension1" ) , 0 , 2 , 0 } , { 71 , TARGET_STRING (
"ModelMotS_dq_V2/Reference Speed (rad//s)/Constant" ) , TARGET_STRING (
"Value" ) , 0 , 1 , 0 } , { 72 , TARGET_STRING (
"ModelMotS_dq_V2/Reference Speed (rad//s)/Look-Up Table1" ) , TARGET_STRING (
"BreakpointsForDimension1" ) , 0 , 3 , 0 } , { 73 , TARGET_STRING (
"ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/jPr/Gain" ) ,
TARGET_STRING ( "Gain" ) , 0 , 1 , 0 } , { 74 , TARGET_STRING (
"ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/jPs/Gain" ) ,
TARGET_STRING ( "Gain" ) , 0 , 1 , 0 } , { 75 , TARGET_STRING (
"ModelMotS_dq_V2/UF control _ dqframe/UF control/Unit Delay2" ) ,
TARGET_STRING ( "InitialCondition" ) , 0 , 1 , 0 } , { 76 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/f/Gain3"
) , TARGET_STRING ( "Gain" ) , 0 , 1 , 0 } , { 77 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/g_1/Gain4"
) , TARGET_STRING ( "Gain" ) , 0 , 1 , 0 } , { 78 , TARGET_STRING (
 "ModelMotS_dq_V2/Induction Motor  Electrical Part d,q/Non Linear Magnetic Coupling/g_1/Gain5"
) , TARGET_STRING ( "Gain" ) , 0 , 1 , 0 } , { 79 , TARGET_STRING (
"ModelMotS_dq_V2/UF control _ dqframe/UF control/Limitation/Constant4" ) ,
TARGET_STRING ( "Value" ) , 0 , 1 , 0 } , { 80 , TARGET_STRING (
"ModelMotS_dq_V2/UF control _ dqframe/UF control/Limitation/Constant5" ) ,
TARGET_STRING ( "Value" ) , 0 , 1 , 0 } , { 81 , TARGET_STRING (
 "ModelMotS_dq_V2/UF control _ dqframe/UF control/Limitation/Compare To Zero/Constant"
) , TARGET_STRING ( "Value" ) , 0 , 1 , 0 } , { 0 , ( NULL ) , ( NULL ) , 0 ,
0 , 0 } } ; static const rtwCAPI_ModelParameters rtModelParameters [ ] = { {
82 , TARGET_STRING ( "J" ) , 0 , 1 , 0 } , { 83 , TARGET_STRING ( "Lfr" ) , 0
, 1 , 0 } , { 84 , TARGET_STRING ( "Lfs" ) , 0 , 1 , 0 } , { 85 ,
TARGET_STRING ( "Lmt" ) , 0 , 1 , 0 } , { 86 , TARGET_STRING ( "Lr" ) , 0 , 1
, 0 } , { 87 , TARGET_STRING ( "P1" ) , 0 , 1 , 0 } , { 88 , TARGET_STRING (
"P2" ) , 0 , 1 , 0 } , { 89 , TARGET_STRING ( "Prinit" ) , 0 , 0 , 0 } , { 90
, TARGET_STRING ( "Psdnom" ) , 0 , 1 , 0 } , { 91 , TARGET_STRING ( "Psinit"
) , 0 , 0 , 0 } , { 92 , TARGET_STRING ( "Rr" ) , 0 , 1 , 0 } , { 93 ,
TARGET_STRING ( "Rs" ) , 0 , 1 , 0 } , { 94 , TARGET_STRING ( "Ts" ) , 0 , 1
, 0 } , { 95 , TARGET_STRING ( "Ulim" ) , 0 , 1 , 0 } , { 96 , TARGET_STRING
( "Uo" ) , 0 , 1 , 0 } , { 97 , TARGET_STRING ( "np" ) , 0 , 1 , 0 } , { 98 ,
TARGET_STRING ( "tauL" ) , 0 , 1 , 0 } , { 99 , TARGET_STRING ( "thrinit" ) ,
0 , 1 , 0 } , { 100 , TARGET_STRING ( "wL" ) , 0 , 1 , 0 } , { 101 ,
TARGET_STRING ( "wrinit" ) , 0 , 1 , 0 } , { 0 , ( NULL ) , 0 , 0 , 0 } } ;
#ifndef HOST_CAPI_BUILD
static void * rtDataAddrMap [ ] = { & rtB . oussmmuoy4 [ 0 ] , & rtB .
awofsj5yej , & rtB . lbn1yidduk , & rtB . lfdym3aanm , & rtB . os0fclte0m , &
rtB . hzaypudxs2 , & rtB . ki404yqcws [ 0 ] , & rtB . icrg1c0qbg [ 0 ] , &
rtB . n5nk0fcdxe , & rtB . cst0qen3tf [ 0 ] , & rtB . ocuyjhtq5x [ 0 ] , &
rtB . h15hfh1vi3 [ 0 ] , & rtB . do1g1252oq [ 0 ] , & rtB . dxxqwldjss [ 0 ]
, & rtB . lrfbty4a0y [ 0 ] , & rtB . jy42n5bwff , & rtB . ohojx4cexj , & rtB
. g50obrftrn , & rtB . ggbp0eubus , & rtB . agjnm01x4l , & rtB . mlubadklks ,
& rtB . llcuyb21kn , & rtB . awofsj5yej , & rtB . c40hosfmrc , & rtB .
ig1a00v4ao , & rtB . ngdf4g2c30 , & rtB . dhnrbjjk55 , & rtB . mgdokchm00 [ 0
] , & rtB . jijx3h41qa [ 0 ] , & rtB . its0a3zvwu [ 0 ] , & rtB . fgi23zg44a
[ 0 ] , & rtB . fsuvnkcxxk [ 0 ] , & rtB . a01avw2uam [ 0 ] , & rtB .
lrkvz4jnvf [ 0 ] , & rtB . onyyxbyf00 , & rtB . o4pvd4evkd , & rtB .
lfrpqznzmd , & rtB . aa0ktk1lsw , & rtB . czrf0nwdxd , & rtB . kqmoni0qee , &
rtB . kxei2q2tej [ 0 ] , & rtB . bc0tqww1op [ 0 ] , & rtB . mpsvxrvii2 , &
rtB . oleotyrvsj , & rtB . gnoc4y3eil , & rtB . dwwm1dvarc , & rtB .
pt232evoj1 [ 0 ] , & rtB . pzn3ntwo0f , & rtB . jp0zo1h5he , & rtB .
hxnwe04xgr , & rtB . kywwenqxru , & rtB . aqq1i4urck [ 0 ] , & rtB .
d005tmuemj , & rtB . d0fm2u13is , & rtB . ij2le252ln [ 0 ] , & rtB .
iemxz0ldwq [ 0 ] , & rtB . k4xamhzsst , & rtB . fzmloa30x1 , & rtB .
of25molymw , & rtB . lpi4yujqet , & rtB . gapqmgw3j0 , & rtB . mugp5ilmof [ 0
] , & rtB . oussmmuoy4 [ 0 ] , & rtP . Loadvaluepu_rep_seq_y [ 0 ] , & rtP .
ReferenceSpeedrads_rep_seq_y [ 0 ] , & rtP . PulseGenerator2_Amp , & rtP .
PulseGenerator2_Duty , & rtP . PulseGenerator2_PhaseDelay , & rtP . Gain_Gain
, & rtP . Constant_Value_jaivf4zt3q , & rtP .
LookUpTable1_bp01Data_jgw1iq0tw2 [ 0 ] , & rtP . Constant_Value_dn2cyv14tz ,
& rtP . LookUpTable1_bp01Data [ 0 ] , & rtP . Gain_Gain_cqbytxvbu0 , & rtP .
Gain_Gain_f4udjbnlx2 , & rtP . UnitDelay2_InitialCondition , & rtP .
Gain3_Gain , & rtP . Gain4_Gain , & rtP . Gain5_Gain , & rtP .
Constant4_Value , & rtP . Constant5_Value , & rtP . Constant_Value , & rtP .
J , & rtP . Lfr , & rtP . Lfs , & rtP . Lmt , & rtP . Lr , & rtP . P1 , & rtP
. P2 , & rtP . Prinit [ 0 ] , & rtP . Psdnom , & rtP . Psinit [ 0 ] , & rtP .
Rr , & rtP . Rs , & rtP . Ts , & rtP . Ulim , & rtP . Uo , & rtP . np , & rtP
. tauL , & rtP . thrinit , & rtP . wL , & rtP . wrinit , } ; static int32_T *
rtVarDimsAddrMap [ ] = { ( NULL ) } ;
#endif
static TARGET_CONST rtwCAPI_DataTypeMap rtDataTypeMap [ ] = { { "double" ,
"real_T" , 0 , 0 , sizeof ( real_T ) , SS_DOUBLE , 0 , 0 } , {
"unsigned char" , "boolean_T" , 0 , 0 , sizeof ( boolean_T ) , SS_BOOLEAN , 0
, 0 } } ;
#ifdef HOST_CAPI_BUILD
#undef sizeof
#endif
static TARGET_CONST rtwCAPI_ElementMap rtElementMap [ ] = { { ( NULL ) , 0 ,
0 , 0 , 0 } , } ; static const rtwCAPI_DimensionMap rtDimensionMap [ ] = { {
rtwCAPI_VECTOR , 0 , 2 , 0 } , { rtwCAPI_SCALAR , 2 , 2 , 0 } , {
rtwCAPI_VECTOR , 4 , 2 , 0 } , { rtwCAPI_VECTOR , 6 , 2 , 0 } } ; static
const uint_T rtDimensionArray [ ] = { 2 , 1 , 1 , 1 , 1 , 295400 , 1 , 406395
} ; static const real_T rtcapiStoredFloats [ ] = { - 2.0 , 0.0 , 1.0 } ;
static const rtwCAPI_FixPtMap rtFixPtMap [ ] = { { ( NULL ) , ( NULL ) ,
rtwCAPI_FIX_RESERVED , 0 , 0 , 0 } , } ; static const rtwCAPI_SampleTimeMap
rtSampleTimeMap [ ] = { { ( NULL ) , ( NULL ) , - 1 , 0 } , { ( const void *
) & rtcapiStoredFloats [ 0 ] , ( const void * ) & rtcapiStoredFloats [ 1 ] ,
2 , 0 } , { ( const void * ) & rtcapiStoredFloats [ 1 ] , ( const void * ) &
rtcapiStoredFloats [ 1 ] , 0 , 0 } , { ( NULL ) , ( NULL ) , 3 , 0 } , { (
const void * ) & rtcapiStoredFloats [ 1 ] , ( const void * ) &
rtcapiStoredFloats [ 2 ] , 1 , 0 } } ; static rtwCAPI_ModelMappingStaticInfo
mmiStatic = { { rtBlockSignals , 63 , ( NULL ) , 0 , ( NULL ) , 0 } , {
rtBlockParameters , 19 , rtModelParameters , 20 } , { ( NULL ) , 0 } , {
rtDataTypeMap , rtDimensionMap , rtFixPtMap , rtElementMap , rtSampleTimeMap
, rtDimensionArray } , "float" , { 1751391696U , 1507898288U , 8788277U ,
3058308105U } , ( NULL ) , 0 , 0 } ; const rtwCAPI_ModelMappingStaticInfo *
ModelMotS_dq_V2_GetCAPIStaticMap ( void ) { return & mmiStatic ; }
#ifndef HOST_CAPI_BUILD
void ModelMotS_dq_V2_InitializeDataMapInfo ( void ) { rtwCAPI_SetVersion ( (
* rt_dataMapInfoPtr ) . mmi , 1 ) ; rtwCAPI_SetStaticMap ( ( *
rt_dataMapInfoPtr ) . mmi , & mmiStatic ) ; rtwCAPI_SetLoggingStaticMap ( ( *
rt_dataMapInfoPtr ) . mmi , ( NULL ) ) ; rtwCAPI_SetDataAddressMap ( ( *
rt_dataMapInfoPtr ) . mmi , rtDataAddrMap ) ; rtwCAPI_SetVarDimsAddressMap (
( * rt_dataMapInfoPtr ) . mmi , rtVarDimsAddrMap ) ;
rtwCAPI_SetInstanceLoggingInfo ( ( * rt_dataMapInfoPtr ) . mmi , ( NULL ) ) ;
rtwCAPI_SetChildMMIArray ( ( * rt_dataMapInfoPtr ) . mmi , ( NULL ) ) ;
rtwCAPI_SetChildMMIArrayLen ( ( * rt_dataMapInfoPtr ) . mmi , 0 ) ; }
#else
#ifdef __cplusplus
extern "C" {
#endif
void ModelMotS_dq_V2_host_InitializeDataMapInfo (
ModelMotS_dq_V2_host_DataMapInfo_T * dataMap , const char * path ) {
rtwCAPI_SetVersion ( dataMap -> mmi , 1 ) ; rtwCAPI_SetStaticMap ( dataMap ->
mmi , & mmiStatic ) ; rtwCAPI_SetDataAddressMap ( dataMap -> mmi , NULL ) ;
rtwCAPI_SetVarDimsAddressMap ( dataMap -> mmi , NULL ) ; rtwCAPI_SetPath (
dataMap -> mmi , path ) ; rtwCAPI_SetFullPath ( dataMap -> mmi , NULL ) ;
rtwCAPI_SetChildMMIArray ( dataMap -> mmi , ( NULL ) ) ;
rtwCAPI_SetChildMMIArrayLen ( dataMap -> mmi , 0 ) ; }
#ifdef __cplusplus
}
#endif
#endif
