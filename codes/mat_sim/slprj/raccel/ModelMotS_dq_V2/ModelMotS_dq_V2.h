#include "__cf_ModelMotS_dq_V2.h"
#ifndef RTW_HEADER_ModelMotS_dq_V2_h_
#define RTW_HEADER_ModelMotS_dq_V2_h_
#include <stddef.h>
#include <float.h>
#include <string.h>
#include "rtw_modelmap.h"
#ifndef ModelMotS_dq_V2_COMMON_INCLUDES_
#define ModelMotS_dq_V2_COMMON_INCLUDES_
#include <stdlib.h>
#include "rtwtypes.h"
#include "simtarget/slSimTgtSigstreamRTW.h"
#include "simtarget/slSimTgtSlioCoreRTW.h"
#include "simtarget/slSimTgtSlioClientsRTW.h"
#include "simtarget/slSimTgtSlioSdiRTW.h"
#include "sigstream_rtw.h"
#include "simstruc.h"
#include "fixedpoint.h"
#include "raccel.h"
#include "slsv_diagnostic_codegen_c_api.h"
#include "rt_logging.h"
#include "dt_info.h"
#include "ext_work.h"
#endif
#include "ModelMotS_dq_V2_types.h"
#include "multiword_types.h"
#include "rt_zcfcn.h"
#include "mwmathutil.h"
#include "rt_defines.h"
#include "rtGetInf.h"
#include "rt_nonfinite.h"
#define MODEL_NAME ModelMotS_dq_V2
#define NSAMPLE_TIMES (4) 
#define NINPUTS (0)       
#define NOUTPUTS (0)     
#define NBLOCKIO (62) 
#define NUM_ZC_EVENTS (1) 
#ifndef NCSTATES
#define NCSTATES (6)   
#elif NCSTATES != 6
#error Invalid specification of NCSTATES defined in compiler command
#endif
#ifndef rtmGetDataMapInfo
#define rtmGetDataMapInfo(rtm) (*rt_dataMapInfoPtr)
#endif
#ifndef rtmSetDataMapInfo
#define rtmSetDataMapInfo(rtm, val) (rt_dataMapInfoPtr = &val)
#endif
#ifndef IN_RACCEL_MAIN
#endif
typedef struct { real_T llcuyb21kn ; real_T mlubadklks ; real_T agjnm01x4l ;
real_T os0fclte0m ; real_T g50obrftrn ; real_T hzaypudxs2 ; real_T lbn1yidduk
; real_T cst0qen3tf [ 2 ] ; real_T mgdokchm00 [ 2 ] ; real_T ocuyjhtq5x [ 2 ]
; real_T jijx3h41qa [ 2 ] ; real_T fsuvnkcxxk [ 2 ] ; real_T kywwenqxru ;
real_T pzn3ntwo0f ; real_T mugp5ilmof [ 2 ] ; real_T lfrpqznzmd ; real_T
czrf0nwdxd ; real_T aa0ktk1lsw ; real_T pt232evoj1 [ 2 ] ; real_T lrkvz4jnvf
[ 2 ] ; real_T fgi23zg44a [ 2 ] ; real_T ig1a00v4ao ; real_T ngdf4g2c30 ;
real_T dhnrbjjk55 ; real_T c40hosfmrc ; real_T a01avw2uam [ 2 ] ; real_T
its0a3zvwu [ 2 ] ; real_T ki404yqcws [ 2 ] ; real_T icrg1c0qbg [ 2 ] ; real_T
n5nk0fcdxe ; real_T jy42n5bwff ; real_T onyyxbyf00 ; real_T h15hfh1vi3 [ 2 ]
; real_T o4pvd4evkd ; real_T do1g1252oq [ 2 ] ; real_T dxxqwldjss [ 2 ] ;
real_T lrfbty4a0y [ 2 ] ; real_T ggbp0eubus ; real_T ohojx4cexj ; real_T
awofsj5yej ; real_T oussmmuoy4 [ 2 ] ; real_T jp0zo1h5he ; real_T of25molymw
; real_T d005tmuemj ; real_T hxnwe04xgr ; real_T fzmloa30x1 ; real_T
lpi4yujqet ; real_T gapqmgw3j0 ; real_T d0fm2u13is ; real_T iemxz0ldwq [ 2 ]
; real_T ij2le252ln [ 2 ] ; real_T aqq1i4urck [ 2 ] ; real_T dwwm1dvarc ;
real_T mpsvxrvii2 ; real_T gnoc4y3eil ; real_T kqmoni0qee ; real_T bc0tqww1op
[ 2 ] ; real_T kxei2q2tej [ 2 ] ; real_T lfdym3aanm ; boolean_T k4xamhzsst ;
boolean_T oleotyrvsj ; } B ; typedef struct { real_T piiyfoznre ; real_T
icx4udn11x ; int64_T abyvocg0q5 ; struct { void * LoggedData [ 2 ] ; }
jevq1wybfe ; int32_T ccffucponj ; int32_T npl1j2qvtj ; int8_T hdmj0f2xda ;
int8_T ncgacd0shm ; boolean_T cobnjav3td ; boolean_T cg43etw1s5 ; } DW ;
typedef struct { real_T kucazwxe1p ; real_T ggygjq5ouq [ 2 ] ; real_T
hvulyscokz [ 2 ] ; real_T cr2w1d1tsl ; } X ; typedef struct { real_T
kucazwxe1p ; real_T ggygjq5ouq [ 2 ] ; real_T hvulyscokz [ 2 ] ; real_T
cr2w1d1tsl ; } XDot ; typedef struct { boolean_T kucazwxe1p ; boolean_T
ggygjq5ouq [ 2 ] ; boolean_T hvulyscokz [ 2 ] ; boolean_T cr2w1d1tsl ; } XDis
; typedef struct { real_T kucazwxe1p ; real_T ggygjq5ouq [ 2 ] ; real_T
hvulyscokz [ 2 ] ; real_T cr2w1d1tsl ; } CStateAbsTol ; typedef struct {
real_T oevrswkldz ; real_T neehjst0we ; real_T mm5kuwqdpx ; } ZCV ; typedef
struct { ZCSigState kl1isclcqj ; } PrevZCX ; typedef struct {
rtwCAPI_ModelMappingInfo mmi ; } DataMapInfo ; struct P_ { real_T J ; real_T
Lfr ; real_T Lfs ; real_T Lmt ; real_T Lr ; real_T P1 ; real_T P2 ; real_T
Prinit [ 2 ] ; real_T Psdnom ; real_T Psinit [ 2 ] ; real_T Rr ; real_T Rs ;
real_T Ts ; real_T Ulim ; real_T Uo ; real_T np ; real_T tauL ; real_T
thrinit ; real_T wL ; real_T wrinit ; real_T ReferenceSpeedrads_rep_seq_y [
406395 ] ; real_T Loadvaluepu_rep_seq_y [ 295400 ] ; real_T Gain_Gain ;
real_T Gain4_Gain ; real_T UnitDelay2_InitialCondition ; real_T
Constant_Value ; real_T Constant4_Value ; real_T Constant5_Value ; real_T
Constant_Value_dn2cyv14tz ; real_T LookUpTable1_bp01Data [ 406395 ] ; real_T
Constant_Value_jaivf4zt3q ; real_T LookUpTable1_bp01Data_jgw1iq0tw2 [ 295400
] ; real_T PulseGenerator2_Amp ; real_T PulseGenerator2_Duty ; real_T
PulseGenerator2_PhaseDelay ; real_T Gain5_Gain ; real_T Gain3_Gain ; real_T
Gain_Gain_cqbytxvbu0 ; real_T Gain_Gain_f4udjbnlx2 ; } ; extern const char *
RT_MEMORY_ALLOCATION_ERROR ; extern B rtB ; extern X rtX ; extern DW rtDW ;
extern PrevZCX rtPrevZCX ; extern P rtP ; extern const
rtwCAPI_ModelMappingStaticInfo * ModelMotS_dq_V2_GetCAPIStaticMap ( void ) ;
extern SimStruct * const rtS ; extern const int_T gblNumToFiles ; extern
const int_T gblNumFrFiles ; extern const int_T gblNumFrWksBlocks ; extern
rtInportTUtable * gblInportTUtables ; extern const char * gblInportFileName ;
extern const int_T gblNumRootInportBlks ; extern const int_T
gblNumModelInputs ; extern const int_T gblInportDataTypeIdx [ ] ; extern
const int_T gblInportDims [ ] ; extern const int_T gblInportComplex [ ] ;
extern const int_T gblInportInterpoFlag [ ] ; extern const int_T
gblInportContinuous [ ] ; extern const int_T gblParameterTuningTid ; extern
DataMapInfo * rt_dataMapInfoPtr ; extern rtwCAPI_ModelMappingInfo *
rt_modelMapInfoPtr ; void MdlOutputs ( int_T tid ) ; void
MdlOutputsParameterSampleTime ( int_T tid ) ; void MdlUpdate ( int_T tid ) ;
void MdlTerminate ( void ) ; void MdlInitializeSizes ( void ) ; void
MdlInitializeSampleTimes ( void ) ; SimStruct * raccel_register_model ( void
) ;
#endif
