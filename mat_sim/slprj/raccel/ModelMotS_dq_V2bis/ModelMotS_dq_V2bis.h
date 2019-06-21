#include "__cf_ModelMotS_dq_V2bis.h"
#ifndef RTW_HEADER_ModelMotS_dq_V2bis_h_
#define RTW_HEADER_ModelMotS_dq_V2bis_h_
#include <stddef.h>
#include <float.h>
#include <string.h>
#include "rtw_modelmap.h"
#ifndef ModelMotS_dq_V2bis_COMMON_INCLUDES_
#define ModelMotS_dq_V2bis_COMMON_INCLUDES_
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
#include "ModelMotS_dq_V2bis_types.h"
#include "multiword_types.h"
#include "rt_zcfcn.h"
#include "mwmathutil.h"
#include "rt_defines.h"
#include "rtGetInf.h"
#include "rt_nonfinite.h"
#define MODEL_NAME ModelMotS_dq_V2bis
#define NSAMPLE_TIMES (5) 
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
typedef struct { real_T hykwlush2d ; real_T imb1ngw3np ; real_T huurwkokgq ;
real_T g0el003inj ; real_T lgdciemkfs ; real_T ievobaeq52 ; real_T hhj5dtpi3h
; real_T k2fa4oq2oz ; real_T ncmpb5etp2 ; real_T ebbpnwxezq ; real_T
m22z1j30gg [ 2 ] ; real_T iduowywrvk ; real_T nxuwj40k4p [ 2 ] ; real_T
gfhu5zazqc [ 2 ] ; real_T fef3w22snz ; real_T knilgucuxh ; real_T hnwzv3x0b1
[ 2 ] ; boolean_T dej0hbwdeh ; boolean_T aqhtrfrelr ; } B ; typedef struct {
real_T lkmfghp5xc ; real_T gct1bjyh0k ; int64_T jnxpeq0lu3 ; struct { void *
LoggedData [ 2 ] ; } kbibbih2er ; int32_T bqamzlhwct ; int32_T ahdljc2cgt ;
int8_T mcptvia4pt ; int8_T jyx4cdacyf ; boolean_T k1vowyvce2 ; boolean_T
oj5po2npmj ; } DW ; typedef struct { real_T miiiyhj1z3 ; real_T djxfhlz2mq [
2 ] ; real_T e2wmqpxlef [ 2 ] ; real_T milfjuwekh ; } X ; typedef struct {
real_T miiiyhj1z3 ; real_T djxfhlz2mq [ 2 ] ; real_T e2wmqpxlef [ 2 ] ;
real_T milfjuwekh ; } XDot ; typedef struct { boolean_T miiiyhj1z3 ;
boolean_T djxfhlz2mq [ 2 ] ; boolean_T e2wmqpxlef [ 2 ] ; boolean_T
milfjuwekh ; } XDis ; typedef struct { real_T miiiyhj1z3 ; real_T djxfhlz2mq
[ 2 ] ; real_T e2wmqpxlef [ 2 ] ; real_T milfjuwekh ; } CStateAbsTol ;
typedef struct { real_T aipe3pqgle ; real_T dqxws3qgfm ; real_T brqitilyar ;
} ZCV ; typedef struct { ZCSigState i53lpawwgq ; } PrevZCX ; typedef struct {
rtwCAPI_ModelMappingInfo mmi ; } DataMapInfo ; struct P_ { real_T J ; real_T
Lfr ; real_T Lfs ; real_T Lmt ; real_T Lr ; real_T P1 ; real_T P2 ; real_T
Prinit [ 2 ] ; real_T Psdnom ; real_T Psinit [ 2 ] ; real_T Rr ; real_T Rs ;
real_T Ts ; real_T Ulim ; real_T Uo ; real_T np ; real_T thrinit ; real_T wL
; real_T wrinit ; real_T ReferenceSpeedrads_rep_seq_y [ 1200000 ] ; real_T
Loadvaluepu_rep_seq_y [ 1200000 ] ; real_T Gain4_Gain ; real_T
UnitDelay2_InitialCondition ; real_T Constant_Value ; real_T Constant4_Value
; real_T Constant5_Value ; real_T Constant_Value_dn2cyv14tz ; real_T
LookUpTable1_bp01Data [ 1200000 ] ; real_T Constant_Value_jaivf4zt3q ; real_T
LookUpTable1_bp01Data_jgw1iq0tw2 [ 1200000 ] ; real_T PulseGenerator2_Amp ;
real_T PulseGenerator2_Duty ; real_T PulseGenerator2_PhaseDelay ; real_T
Gain5_Gain ; real_T Gain3_Gain ; real_T Gain_Gain ; real_T
Gain_Gain_f4udjbnlx2 ; } ; extern const char * RT_MEMORY_ALLOCATION_ERROR ;
extern B rtB ; extern X rtX ; extern DW rtDW ; extern PrevZCX rtPrevZCX ;
extern P rtP ; extern const rtwCAPI_ModelMappingStaticInfo *
ModelMotS_dq_V2bis_GetCAPIStaticMap ( void ) ; extern SimStruct * const rtS ;
extern const int_T gblNumToFiles ; extern const int_T gblNumFrFiles ; extern
const int_T gblNumFrWksBlocks ; extern rtInportTUtable * gblInportTUtables ;
extern const char * gblInportFileName ; extern const int_T
gblNumRootInportBlks ; extern const int_T gblNumModelInputs ; extern const
int_T gblInportDataTypeIdx [ ] ; extern const int_T gblInportDims [ ] ;
extern const int_T gblInportComplex [ ] ; extern const int_T
gblInportInterpoFlag [ ] ; extern const int_T gblInportContinuous [ ] ;
extern const int_T gblParameterTuningTid ; extern DataMapInfo *
rt_dataMapInfoPtr ; extern rtwCAPI_ModelMappingInfo * rt_modelMapInfoPtr ;
void MdlOutputs ( int_T tid ) ; void MdlOutputsParameterSampleTime ( int_T
tid ) ; void MdlUpdate ( int_T tid ) ; void MdlTerminate ( void ) ; void
MdlInitializeSizes ( void ) ; void MdlInitializeSampleTimes ( void ) ;
SimStruct * raccel_register_model ( void ) ;
#endif
