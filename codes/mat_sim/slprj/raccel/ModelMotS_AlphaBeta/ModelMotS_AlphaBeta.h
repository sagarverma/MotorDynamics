#include "__cf_ModelMotS_AlphaBeta.h"
#ifndef RTW_HEADER_ModelMotS_AlphaBeta_h_
#define RTW_HEADER_ModelMotS_AlphaBeta_h_
#include <stddef.h>
#include <float.h>
#include <string.h>
#include "rtw_modelmap.h"
#ifndef ModelMotS_AlphaBeta_COMMON_INCLUDES_
#define ModelMotS_AlphaBeta_COMMON_INCLUDES_
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
#include "ModelMotS_AlphaBeta_types.h"
#include "multiword_types.h"
#include "rt_zcfcn.h"
#include "mwmathutil.h"
#include "rt_defines.h"
#include "rtGetInf.h"
#include "rt_nonfinite.h"
#define MODEL_NAME ModelMotS_AlphaBeta
#define NSAMPLE_TIMES (4) 
#define NINPUTS (0)       
#define NOUTPUTS (0)     
#define NBLOCKIO (19) 
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
typedef struct { real_T gpbbxd3e1a ; real_T on2ofjgexa ; real_T g3axur342h ;
real_T hmytavveer ; real_T madwsvn1bo ; real_T mmagr3rvlr ; real_T ndhuby2l2s
; real_T f10pcxma3u ; real_T cgvtocnbhf ; real_T lmtcfzni2c [ 2 ] ; real_T
erkosogxty ; real_T otejpxdnyh ; real_T a2lne1ot00 [ 2 ] ; real_T a2aj3jru0z
[ 2 ] ; real_T h2sendcr2c ; real_T bnsafpf0ct ; boolean_T cjuexj30nh ;
boolean_T gj5i4vllld ; } B ; typedef struct { real_T bwejchtj5m ; real_T
ko425xjie0 ; real_T b5eaxoewzk ; real_T hoadgf1elz ; real_T gfcwkc4vko ;
int64_T ghpzi0bsm2 ; int32_T f2j1gzf1zg ; int32_T nzeprll3k2 ; int8_T
n1ldkmquay ; int8_T fcxjbwyybw ; boolean_T euhyjx5ttx ; boolean_T a4kg5nbqon
; } DW ; typedef struct { real_T etwdgvk3w3 ; real_T malc5kzyq4 [ 2 ] ;
real_T aekrnoednt [ 2 ] ; real_T lrwwpm2s4k ; } X ; typedef struct { real_T
etwdgvk3w3 ; real_T malc5kzyq4 [ 2 ] ; real_T aekrnoednt [ 2 ] ; real_T
lrwwpm2s4k ; } XDot ; typedef struct { boolean_T etwdgvk3w3 ; boolean_T
malc5kzyq4 [ 2 ] ; boolean_T aekrnoednt [ 2 ] ; boolean_T lrwwpm2s4k ; } XDis
; typedef struct { real_T etwdgvk3w3 ; real_T malc5kzyq4 [ 2 ] ; real_T
aekrnoednt [ 2 ] ; real_T lrwwpm2s4k ; } CStateAbsTol ; typedef struct {
real_T ekyny2ur1i ; real_T ashiibwaqp ; real_T ecb3emblhb ; } ZCV ; typedef
struct { ZCSigState mdpbkmi5bz ; } PrevZCX ; typedef struct {
rtwCAPI_ModelMappingInfo mmi ; } DataMapInfo ; struct P_ { real_T J ; real_T
Lfr ; real_T Lfs ; real_T Lmt ; real_T Lr ; real_T P1 ; real_T P2 ; real_T
Prinit [ 2 ] ; real_T Psdnom ; real_T Psinit [ 2 ] ; real_T Rr ; real_T Rs ;
real_T Ts ; real_T Ulim ; real_T Uo ; real_T np ; real_T tauL ; real_T
thrinit ; real_T wL ; real_T wrinit ; real_T Loadvaluepu_rep_seq_y [ 295400 ]
; real_T ReferenceSpeedrads_rep_seq_y [ 406395 ] ; real_T Gain_Gain ; real_T
Gain4_Gain ; real_T DiscreteTimeIntegrator_gainval ; real_T
DiscreteTimeIntegrator_IC ; real_T Gain1_Gain ; real_T
UnitDelay2_InitialCondition ; real_T Constant4_Value ; real_T Constant5_Value
; real_T Constant_Value ; real_T Constant_Value_jaivf4zt3q ; real_T
LookUpTable1_bp01Data [ 295400 ] ; real_T PulseGenerator1_Amp ; real_T
PulseGenerator1_Duty ; real_T PulseGenerator1_PhaseDelay ; real_T Gain5_Gain
; real_T Gain3_Gain ; real_T Gain_Gain_aopx5rkhzb ; real_T
Constant_Value_dn2cyv14tz ; real_T LookUpTable1_bp01Data_gh5vwq5i5u [ 406395
] ; } ; extern const char * RT_MEMORY_ALLOCATION_ERROR ; extern B rtB ;
extern X rtX ; extern DW rtDW ; extern PrevZCX rtPrevZCX ; extern P rtP ;
extern const rtwCAPI_ModelMappingStaticInfo *
ModelMotS_AlphaBeta_GetCAPIStaticMap ( void ) ; extern SimStruct * const rtS
; extern const int_T gblNumToFiles ; extern const int_T gblNumFrFiles ;
extern const int_T gblNumFrWksBlocks ; extern rtInportTUtable *
gblInportTUtables ; extern const char * gblInportFileName ; extern const
int_T gblNumRootInportBlks ; extern const int_T gblNumModelInputs ; extern
const int_T gblInportDataTypeIdx [ ] ; extern const int_T gblInportDims [ ] ;
extern const int_T gblInportComplex [ ] ; extern const int_T
gblInportInterpoFlag [ ] ; extern const int_T gblInportContinuous [ ] ;
extern const int_T gblParameterTuningTid ; extern DataMapInfo *
rt_dataMapInfoPtr ; extern rtwCAPI_ModelMappingInfo * rt_modelMapInfoPtr ;
void MdlOutputs ( int_T tid ) ; void MdlOutputsParameterSampleTime ( int_T
tid ) ; void MdlUpdate ( int_T tid ) ; void MdlTerminate ( void ) ; void
MdlInitializeSizes ( void ) ; void MdlInitializeSampleTimes ( void ) ;
SimStruct * raccel_register_model ( void ) ;
#endif
