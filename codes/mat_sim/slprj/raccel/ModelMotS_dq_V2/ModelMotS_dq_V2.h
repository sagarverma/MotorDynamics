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
#define NBLOCKIO (20) 
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
typedef struct { real_T llcuyb21kn ; real_T agjnm01x4l ; real_T g50obrftrn ;
real_T lbn1yidduk ; real_T kywwenqxru ; real_T pzn3ntwo0f ; real_T lfrpqznzmd
; real_T czrf0nwdxd ; real_T aa0ktk1lsw ; real_T c40hosfmrc ; real_T
its0a3zvwu [ 2 ] ; real_T n5nk0fcdxe ; real_T dxxqwldjss [ 2 ] ; real_T
lrfbty4a0y [ 2 ] ; real_T ohojx4cexj ; real_T awofsj5yej ; real_T oussmmuoy4
[ 2 ] ; boolean_T k4xamhzsst ; boolean_T oleotyrvsj ; } B ; typedef struct {
real_T piiyfoznre ; real_T icx4udn11x ; int64_T abyvocg0q5 ; struct { void *
LoggedData [ 2 ] ; } jevq1wybfe ; int32_T ccffucponj ; int32_T npl1j2qvtj ;
int8_T hdmj0f2xda ; int8_T ncgacd0shm ; boolean_T cobnjav3td ; boolean_T
cg43etw1s5 ; } DW ; typedef struct { real_T kucazwxe1p ; real_T ggygjq5ouq [
2 ] ; real_T hvulyscokz [ 2 ] ; real_T cr2w1d1tsl ; } X ; typedef struct {
real_T kucazwxe1p ; real_T ggygjq5ouq [ 2 ] ; real_T hvulyscokz [ 2 ] ;
real_T cr2w1d1tsl ; } XDot ; typedef struct { boolean_T kucazwxe1p ;
boolean_T ggygjq5ouq [ 2 ] ; boolean_T hvulyscokz [ 2 ] ; boolean_T
cr2w1d1tsl ; } XDis ; typedef struct { real_T kucazwxe1p ; real_T ggygjq5ouq
[ 2 ] ; real_T hvulyscokz [ 2 ] ; real_T cr2w1d1tsl ; } CStateAbsTol ;
typedef struct { real_T oevrswkldz ; real_T neehjst0we ; real_T mm5kuwqdpx ;
} ZCV ; typedef struct { ZCSigState kl1isclcqj ; } PrevZCX ; typedef struct {
rtwCAPI_ModelMappingInfo mmi ; } DataMapInfo ; struct P_ { real_T J ; real_T
Lfr ; real_T Lfs ; real_T Lmt ; real_T Lr ; real_T P1 ; real_T P2 ; real_T
Prinit [ 2 ] ; real_T Psdnom ; real_T Psinit [ 2 ] ; real_T Rr ; real_T Rs ;
real_T Ts ; real_T Ulim ; real_T Uo ; real_T np ; real_T tauL ; real_T
thrinit ; real_T wL ; real_T wrinit ; real_T ReferenceSpeedrads_rep_seq_y [
12000 ] ; real_T Loadvaluepu_rep_seq_y [ 12000 ] ; real_T Gain_Gain ; real_T
Gain4_Gain ; real_T UnitDelay2_InitialCondition ; real_T Constant_Value ;
real_T Constant4_Value ; real_T Constant5_Value ; real_T
Constant_Value_dn2cyv14tz ; real_T LookUpTable1_bp01Data [ 12000 ] ; real_T
Constant_Value_jaivf4zt3q ; real_T LookUpTable1_bp01Data_jgw1iq0tw2 [ 12000 ]
; real_T PulseGenerator2_Amp ; real_T PulseGenerator2_Duty ; real_T
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
