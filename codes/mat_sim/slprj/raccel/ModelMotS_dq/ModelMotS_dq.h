#include "__cf_ModelMotS_dq.h"
#ifndef RTW_HEADER_ModelMotS_dq_h_
#define RTW_HEADER_ModelMotS_dq_h_
#include <stddef.h>
#include <float.h>
#include <string.h>
#include "rtw_modelmap.h"
#ifndef ModelMotS_dq_COMMON_INCLUDES_
#define ModelMotS_dq_COMMON_INCLUDES_
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
#include "ModelMotS_dq_types.h"
#include "multiword_types.h"
#include "rt_zcfcn.h"
#include "mwmathutil.h"
#include "rt_defines.h"
#include "rtGetInf.h"
#include "rt_nonfinite.h"
#define MODEL_NAME ModelMotS_dq
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
typedef struct { real_T jpjuugikxn ; real_T nhqekpgwd4 ; real_T hpkni4150v ;
real_T efr02sxb5p ; real_T j3axnrlwog ; real_T ejcqi1uyvj ; real_T fti1ov2wx1
; real_T hti1q415mf ; real_T gnbeldsapz [ 2 ] ; real_T blwx3ic5mc ; real_T
dhpwcmsv2i ; real_T ohdbrztky4 [ 2 ] ; real_T bpsnzsfty3 [ 2 ] ; real_T
fc2lccxhbh ; real_T niveaq0uyq ; real_T gsrx3j1z5n [ 2 ] ; boolean_T
knnwpmthcv ; boolean_T ln3t0mutle ; } B ; typedef struct { real_T hcnzorryht
; real_T lnlinophuy ; int64_T k5zytz2ycl ; int32_T ln0cfsnmll ; int32_T
cjoc0ogxrg ; int8_T aetlgmgzmu ; int8_T kkmzxxbuo0 ; boolean_T nt3wnc5mjd ;
boolean_T inkxzlg3qp ; } DW ; typedef struct { real_T ij3r2xyt4x ; real_T
cfcfwtiyhh [ 2 ] ; real_T bvebikoxww [ 2 ] ; real_T dr2wn3m2tz ; } X ;
typedef struct { real_T ij3r2xyt4x ; real_T cfcfwtiyhh [ 2 ] ; real_T
bvebikoxww [ 2 ] ; real_T dr2wn3m2tz ; } XDot ; typedef struct { boolean_T
ij3r2xyt4x ; boolean_T cfcfwtiyhh [ 2 ] ; boolean_T bvebikoxww [ 2 ] ;
boolean_T dr2wn3m2tz ; } XDis ; typedef struct { real_T ij3r2xyt4x ; real_T
cfcfwtiyhh [ 2 ] ; real_T bvebikoxww [ 2 ] ; real_T dr2wn3m2tz ; }
CStateAbsTol ; typedef struct { real_T cyxbe0cwjw ; real_T oslyw3c0pz ;
real_T nvqn3wv401 ; } ZCV ; typedef struct { ZCSigState jgcq4ftyys ; }
PrevZCX ; typedef struct { rtwCAPI_ModelMappingInfo mmi ; } DataMapInfo ;
struct P_ { real_T J ; real_T Lfr ; real_T Lfs ; real_T Lmt ; real_T Lr ;
real_T P1 ; real_T P2 ; real_T Prinit [ 2 ] ; real_T Psdnom ; real_T Psinit [
2 ] ; real_T Rr ; real_T Rs ; real_T Ts ; real_T Ulim ; real_T Uo ; real_T np
; real_T tauL ; real_T thrinit ; real_T wL ; real_T wrinit ; real_T
Loadvaluepu_rep_seq_y [ 3 ] ; real_T ReferenceSpeedrads_rep_seq_y [ 53 ] ;
real_T Gain_Gain ; real_T Gain4_Gain ; real_T UnitDelay2_InitialCondition ;
real_T Constant_Value ; real_T Constant4_Value ; real_T Constant5_Value ;
real_T Constant_Value_jaivf4zt3q ; real_T LookUpTable1_bp01Data [ 3 ] ;
real_T PulseGenerator2_Amp ; real_T PulseGenerator2_Duty ; real_T
PulseGenerator2_PhaseDelay ; real_T Gain5_Gain ; real_T Gain3_Gain ; real_T
Constant_Value_dn2cyv14tz ; real_T LookUpTable1_bp01Data_gh5vwq5i5u [ 53 ] ;
real_T Gain_Gain_cqbytxvbu0 ; real_T Gain_Gain_f4udjbnlx2 ; } ; extern const
char * RT_MEMORY_ALLOCATION_ERROR ; extern B rtB ; extern X rtX ; extern DW
rtDW ; extern PrevZCX rtPrevZCX ; extern P rtP ; extern const
rtwCAPI_ModelMappingStaticInfo * ModelMotS_dq_GetCAPIStaticMap ( void ) ;
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
