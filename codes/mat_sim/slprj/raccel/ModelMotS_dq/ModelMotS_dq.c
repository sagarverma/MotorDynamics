#include "__cf_ModelMotS_dq.h"
#include "rt_logging_mmi.h"
#include "ModelMotS_dq_capi.h"
#include <math.h>
#include "ModelMotS_dq.h"
#include "ModelMotS_dq_private.h"
#include "ModelMotS_dq_dt.h"
extern void * CreateDiagnosticAsVoidPtr_wrapper ( const char * id , int nargs
, ... ) ; RTWExtModeInfo * gblRTWExtModeInfo = NULL ; extern boolean_T
gblExtModeStartPktReceived ; void raccelForceExtModeShutdown ( ) { if ( !
gblExtModeStartPktReceived ) { boolean_T stopRequested = false ;
rtExtModeWaitForStartPkt ( gblRTWExtModeInfo , 3 , & stopRequested ) ; }
rtExtModeShutdown ( 3 ) ; }
#include "slsv_diagnostic_codegen_c_api.h"
const int_T gblNumToFiles = 0 ; const int_T gblNumFrFiles = 0 ; const int_T
gblNumFrWksBlocks = 0 ;
#ifdef RSIM_WITH_SOLVER_MULTITASKING
boolean_T gbl_raccel_isMultitasking = 1 ;
#else
boolean_T gbl_raccel_isMultitasking = 0 ;
#endif
boolean_T gbl_raccel_tid01eq = 0 ; int_T gbl_raccel_NumST = 4 ; const char_T
* gbl_raccel_Version = "9.0 (R2018b) 24-May-2018" ; void
raccel_setup_MMIStateLog ( SimStruct * S ) {
#ifdef UseMMIDataLogging
rt_FillStateSigInfoFromMMI ( ssGetRTWLogInfo ( S ) , & ssGetErrorStatus ( S )
) ;
#else
UNUSED_PARAMETER ( S ) ;
#endif
} static DataMapInfo rt_dataMapInfo ; DataMapInfo * rt_dataMapInfoPtr = &
rt_dataMapInfo ; rtwCAPI_ModelMappingInfo * rt_modelMapInfoPtr = & (
rt_dataMapInfo . mmi ) ; const char * gblSlvrJacPatternFileName =
"slprj//raccel//ModelMotS_dq//ModelMotS_dq_Jpattern.mat" ; const int_T
gblNumRootInportBlks = 0 ; const int_T gblNumModelInputs = 0 ; extern
rtInportTUtable * gblInportTUtables ; extern const char * gblInportFileName ;
const int_T gblInportDataTypeIdx [ ] = { - 1 } ; const int_T gblInportDims [
] = { - 1 } ; const int_T gblInportComplex [ ] = { - 1 } ; const int_T
gblInportInterpoFlag [ ] = { - 1 } ; const int_T gblInportContinuous [ ] = {
- 1 } ; int_T enableFcnCallFlag [ ] = { 1 , 1 , 1 , 1 } ;
#include "simstruc.h"
#include "fixedpoint.h"
B rtB ; X rtX ; DW rtDW ; PrevZCX rtPrevZCX ; static SimStruct model_S ;
SimStruct * const rtS = & model_S ; real_T look1_binlxpw ( real_T u0 , const
real_T bp0 [ ] , const real_T table [ ] , uint32_T maxIndex ) { real_T frac ;
uint32_T iRght ; uint32_T iLeft ; uint32_T bpIdx ; if ( u0 <= bp0 [ 0U ] ) {
iLeft = 0U ; frac = ( u0 - bp0 [ 0U ] ) / ( bp0 [ 1U ] - bp0 [ 0U ] ) ; }
else if ( u0 < bp0 [ maxIndex ] ) { bpIdx = maxIndex >> 1U ; iLeft = 0U ;
iRght = maxIndex ; while ( iRght - iLeft > 1U ) { if ( u0 < bp0 [ bpIdx ] ) {
iRght = bpIdx ; } else { iLeft = bpIdx ; } bpIdx = ( iRght + iLeft ) >> 1U ;
} frac = ( u0 - bp0 [ iLeft ] ) / ( bp0 [ iLeft + 1U ] - bp0 [ iLeft ] ) ; }
else { iLeft = maxIndex - 1U ; frac = ( u0 - bp0 [ maxIndex - 1U ] ) / ( bp0
[ maxIndex ] - bp0 [ maxIndex - 1U ] ) ; } return ( table [ iLeft + 1U ] -
table [ iLeft ] ) * frac + table [ iLeft ] ; } void MdlInitialize ( void ) {
rtX . ij3r2xyt4x = rtP . wrinit ; rtX . cfcfwtiyhh [ 0 ] = rtP . Psinit [ 0 ]
; rtX . bvebikoxww [ 0 ] = rtP . Prinit [ 0 ] ; rtX . cfcfwtiyhh [ 1 ] = rtP
. Psinit [ 1 ] ; rtX . bvebikoxww [ 1 ] = rtP . Prinit [ 1 ] ; rtX .
dr2wn3m2tz = rtP . thrinit ; rtDW . hcnzorryht = rtP .
UnitDelay2_InitialCondition ; } void MdlEnable ( void ) { rtDW . ln0cfsnmll =
1 ; _ssSetSampleHit ( rtS , 2 , 1 ) ; _ssSetTaskTime ( rtS , 2 , ssGetT ( rtS
) ) ; _ssSetVarNextHitTime ( rtS , 0 , ssGetT ( rtS ) ) ; ; } void MdlStart (
void ) { { void * * slioCatalogueAddr = rt_slioCatalogueAddr ( ) ; void * r2
= ( NULL ) ; void * * pOSigstreamManagerAddr = ( NULL ) ; const int
maxErrorBufferSize = 16384 ; char errMsgCreatingOSigstreamManager [ 16384 ] ;
bool errorCreatingOSigstreamManager = false ; const char *
errorAddingR2SharedResource = ( NULL ) ; * slioCatalogueAddr =
rtwGetNewSlioCatalogue ( rt_GetMatSigLogSelectorFileName ( ) ) ;
errorAddingR2SharedResource = rtwAddR2SharedResource (
rtwGetPointerFromUniquePtr ( rt_slioCatalogue ( ) ) , 1 ) ; if (
errorAddingR2SharedResource != ( NULL ) ) { rtwTerminateSlioCatalogue (
slioCatalogueAddr ) ; * slioCatalogueAddr = ( NULL ) ; ssSetErrorStatus ( rtS
, errorAddingR2SharedResource ) ; return ; } r2 = rtwGetR2SharedResource (
rtwGetPointerFromUniquePtr ( rt_slioCatalogue ( ) ) ) ;
pOSigstreamManagerAddr = rt_GetOSigstreamManagerAddr ( ) ;
errorCreatingOSigstreamManager = rtwOSigstreamManagerCreateInstance (
rt_GetMatSigLogSelectorFileName ( ) , r2 , pOSigstreamManagerAddr ,
errMsgCreatingOSigstreamManager , maxErrorBufferSize ) ; if (
errorCreatingOSigstreamManager ) { * pOSigstreamManagerAddr = ( NULL ) ;
ssSetErrorStatus ( rtS , errMsgCreatingOSigstreamManager ) ; return ; } } {
bool externalInputIsInDatasetFormat = false ; void * pISigstreamManager =
rt_GetISigstreamManager ( ) ; rtwISigstreamManagerGetInputIsInDatasetFormat (
pISigstreamManager , & externalInputIsInDatasetFormat ) ; if (
externalInputIsInDatasetFormat ) { } } MdlInitialize ( ) ; MdlEnable ( ) ; }
void MdlOutputs ( int_T tid ) { real_T taskTimeV ; real_T ratio ; uint32_T
numCycles ; real_T cvt0djk3nv ; ZCEventType zcEvent ; real_T iaas34rry1 ;
real_T a3va4l0q3t_idx_0 ; real_T a3va4l0q3t_idx_1 ; real_T awwnlmpfsr_idx_1 ;
srClearBC ( rtDW . aetlgmgzmu ) ; rtB . jpjuugikxn = rtX . ij3r2xyt4x ; if (
ssIsSampleHit ( rtS , 2 , 0 ) ) { taskTimeV = ssGetTaskTime ( rtS , 2 ) ; if
( ssGetTNextWasAdjusted ( rtS , 2 ) ) { rtDW . lnlinophuy =
_ssGetVarNextHitTime ( rtS , 0 ) ; } if ( rtDW . ln0cfsnmll != 0 ) { rtDW .
ln0cfsnmll = 0 ; if ( taskTimeV >= rtP . PulseGenerator2_PhaseDelay ) { ratio
= ( taskTimeV - rtP . PulseGenerator2_PhaseDelay ) / rtP . Ts ; numCycles = (
uint32_T ) muDoubleScalarFloor ( ratio ) ; if ( muDoubleScalarAbs ( ( real_T
) ( numCycles + 1U ) - ratio ) < DBL_EPSILON * ratio ) { numCycles ++ ; }
rtDW . k5zytz2ycl = numCycles ; ratio = ( ( real_T ) numCycles * rtP . Ts +
rtP . PulseGenerator2_PhaseDelay ) + rtP . PulseGenerator2_Duty * rtP . Ts /
100.0 ; if ( taskTimeV < ratio ) { rtDW . cjoc0ogxrg = 1 ; rtDW . lnlinophuy
= ratio ; } else { rtDW . cjoc0ogxrg = 0 ; rtDW . lnlinophuy = ( real_T ) (
numCycles + 1U ) * rtP . Ts + rtP . PulseGenerator2_PhaseDelay ; } } else {
rtDW . k5zytz2ycl = rtP . PulseGenerator2_PhaseDelay != 0.0 ? - 1 : 0 ; rtDW
. cjoc0ogxrg = 0 ; rtDW . lnlinophuy = rtP . PulseGenerator2_PhaseDelay ; } }
else { if ( rtDW . lnlinophuy <= taskTimeV ) { if ( rtDW . cjoc0ogxrg == 1 )
{ rtDW . cjoc0ogxrg = 0 ; rtDW . lnlinophuy = ( real_T ) ( rtDW . k5zytz2ycl
+ 1L ) * rtP . Ts + rtP . PulseGenerator2_PhaseDelay ; } else { rtDW .
k5zytz2ycl ++ ; rtDW . cjoc0ogxrg = 1 ; rtDW . lnlinophuy = ( rtP .
PulseGenerator2_Duty * rtP . Ts * 0.01 + ( real_T ) rtDW . k5zytz2ycl * rtP .
Ts ) + rtP . PulseGenerator2_PhaseDelay ; } } } _ssSetVarNextHitTime ( rtS ,
0 , rtDW . lnlinophuy ) ; if ( rtDW . cjoc0ogxrg == 1 ) { rtB . nhqekpgwd4 =
rtP . PulseGenerator2_Amp ; } else { rtB . nhqekpgwd4 = 0.0 ; } } if (
ssIsSampleHit ( rtS , 1 , 0 ) ) { cvt0djk3nv = rtB . nhqekpgwd4 ; }
a3va4l0q3t_idx_0 = rtP . Lfr * rtX . cfcfwtiyhh [ 0 ] + rtP . Lfs * rtX .
bvebikoxww [ 0 ] ; a3va4l0q3t_idx_1 = rtP . Lfr * rtX . cfcfwtiyhh [ 1 ] +
rtP . Lfs * rtX . bvebikoxww [ 1 ] ; taskTimeV = muDoubleScalarPower (
a3va4l0q3t_idx_0 , 2.0 ) + muDoubleScalarPower ( a3va4l0q3t_idx_1 , 2.0 ) ;
if ( taskTimeV < 0.0 ) { taskTimeV = - muDoubleScalarSqrt ( - taskTimeV ) ; }
else { taskTimeV = muDoubleScalarSqrt ( taskTimeV ) ; } rtB . efr02sxb5p =
1.0 / ( ( rtP . Lfr * rtP . Lfs / rtP . Lmt + rtP . Lfr ) + rtP . Lfs ) *
taskTimeV ; if ( ssIsSampleHit ( rtS , 1 , 0 ) ) { if ( ssIsMajorTimeStep (
rtS ) ) { rtDW . nt3wnc5mjd = ( rtB . efr02sxb5p >= rtP . P1 ) ; } rtB .
knnwpmthcv = rtDW . nt3wnc5mjd ; } if ( rtB . knnwpmthcv ) { ratio = ( rtP .
Lfr * rtP . Lfs / rtP . Lmt * ( rtP . P2 - 2.0 * rtP . P1 ) + ( rtP . Lfr +
rtP . Lfs ) * rtP . P2 ) - taskTimeV ; iaas34rry1 = ratio * ratio - ( ( rtP .
Lfr + rtP . Lfs ) * - 0.48999999999999994 - ( rtP . P2 - 2.0 * rtP . P1 ) *
taskTimeV ) * ( rtP . Lfr * rtP . Lfs / rtP . Lmt ) * rtP . Gain4_Gain ; if (
iaas34rry1 < 0.0 ) { iaas34rry1 = - muDoubleScalarSqrt ( muDoubleScalarAbs (
iaas34rry1 ) ) ; } else { iaas34rry1 = muDoubleScalarSqrt ( iaas34rry1 ) ; }
ratio = ( iaas34rry1 - ratio ) / rtB . hpkni4150v ; a3va4l0q3t_idx_0 =
a3va4l0q3t_idx_0 / taskTimeV * ratio ; a3va4l0q3t_idx_1 = a3va4l0q3t_idx_1 /
taskTimeV * ratio ; } else { taskTimeV = 1.0 / ( ( rtP . Lfr * rtP . Lfs /
rtP . Lmt + rtP . Lfr ) + rtP . Lfs ) ; a3va4l0q3t_idx_0 *= taskTimeV ;
a3va4l0q3t_idx_1 *= taskTimeV ; } taskTimeV = muDoubleScalarPower (
a3va4l0q3t_idx_0 , 2.0 ) + muDoubleScalarPower ( a3va4l0q3t_idx_1 , 2.0 ) ;
if ( taskTimeV < 0.0 ) { rtB . j3axnrlwog = - muDoubleScalarSqrt ( -
taskTimeV ) ; } else { rtB . j3axnrlwog = muDoubleScalarSqrt ( taskTimeV ) ;
} if ( ssIsSampleHit ( rtS , 1 , 0 ) ) { if ( ssIsMajorTimeStep ( rtS ) ) {
rtDW . inkxzlg3qp = ( rtB . j3axnrlwog >= rtP . P1 ) ; } rtB . ln3t0mutle =
rtDW . inkxzlg3qp ; } if ( rtB . ln3t0mutle ) { taskTimeV = ( rtB .
j3axnrlwog * rtP . P2 - rtB . ejcqi1uyvj ) / ( ( rtP . P2 - rtB . fti1ov2wx1
) + rtB . j3axnrlwog ) ; a3va4l0q3t_idx_0 = a3va4l0q3t_idx_0 / rtB .
j3axnrlwog * taskTimeV ; a3va4l0q3t_idx_1 = a3va4l0q3t_idx_1 / rtB .
j3axnrlwog * taskTimeV ; } taskTimeV = 1.0 / rtP . Lfr ; iaas34rry1 = ( rtX .
bvebikoxww [ 0 ] - a3va4l0q3t_idx_0 ) * taskTimeV ; awwnlmpfsr_idx_1 = ( rtX
. bvebikoxww [ 1 ] - a3va4l0q3t_idx_1 ) * taskTimeV ; rtB . hti1q415mf = 3.0
* rtP . np / 2.0 * ( iaas34rry1 * rtX . bvebikoxww [ 1 ] - rtX . bvebikoxww [
0 ] * awwnlmpfsr_idx_1 ) ; taskTimeV = 1.0 / rtP . Lfs ; rtB . gnbeldsapz [ 0
] = ( rtX . cfcfwtiyhh [ 0 ] - a3va4l0q3t_idx_0 ) * taskTimeV ; rtB .
gnbeldsapz [ 1 ] = ( rtX . cfcfwtiyhh [ 1 ] - a3va4l0q3t_idx_1 ) * taskTimeV
; rtB . blwx3ic5mc = rtP . np * rtB . jpjuugikxn ; rtB . dhpwcmsv2i =
look1_binlxpw ( muDoubleScalarRem ( ssGetT ( rtS ) - 0.0 , rtP .
Constant_Value_dn2cyv14tz ) , rtP . LookUpTable1_bp01Data_gh5vwq5i5u , rtP .
ReferenceSpeedrads_rep_seq_y , 52U ) ; if ( ssIsSampleHit ( rtS , 1 , 0 ) &&
ssIsMajorTimeStep ( rtS ) ) { zcEvent = rt_ZCFcn ( RISING_ZERO_CROSSING , &
rtPrevZCX . jgcq4ftyys , ( cvt0djk3nv ) ) ; if ( zcEvent != NO_ZCEVENT ) {
rtB . niveaq0uyq = rtB . dhpwcmsv2i ; cvt0djk3nv = rtP . Ts * rtP . Rr / rtP
. Lr * ( rtP . Psdnom - rtDW . hcnzorryht ) + rtDW . hcnzorryht ; ratio = rtB
. niveaq0uyq * cvt0djk3nv ; taskTimeV = muDoubleScalarPower ( rtP . Uo , 2.0
) + muDoubleScalarPower ( ratio , 2.0 ) ; if ( taskTimeV < 0.0 ) { taskTimeV
= - muDoubleScalarSqrt ( - taskTimeV ) ; } else { taskTimeV =
muDoubleScalarSqrt ( taskTimeV ) ; } if ( taskTimeV <= rtP . Ulim ) {
taskTimeV = rtP . Constant4_Value ; } else { if ( taskTimeV <= rtP .
Constant_Value ) { taskTimeV = rtP . Constant5_Value ; } taskTimeV = rtP .
Ulim / taskTimeV ; } rtB . gsrx3j1z5n [ 0 ] = rtP . Uo * taskTimeV ; rtB .
gsrx3j1z5n [ 1 ] = ratio * taskTimeV ; rtDW . hcnzorryht = cvt0djk3nv ; rtDW
. aetlgmgzmu = 4 ; } } cvt0djk3nv = rtB . blwx3ic5mc - rtB . niveaq0uyq ; rtB
. ohdbrztky4 [ 0 ] = ( rtB . gsrx3j1z5n [ 0 ] - rtP . Gain_Gain_f4udjbnlx2 *
rtX . cfcfwtiyhh [ 1 ] * rtB . niveaq0uyq ) - rtP . Rs * rtB . gnbeldsapz [ 0
] ; rtB . ohdbrztky4 [ 1 ] = ( rtB . gsrx3j1z5n [ 1 ] - rtB . niveaq0uyq *
rtX . cfcfwtiyhh [ 0 ] ) - rtP . Rs * rtB . gnbeldsapz [ 1 ] ; rtB .
bpsnzsfty3 [ 0 ] = rtP . Gain_Gain_cqbytxvbu0 * rtX . bvebikoxww [ 1 ] *
cvt0djk3nv - rtP . Rr * iaas34rry1 ; rtB . bpsnzsfty3 [ 1 ] = cvt0djk3nv *
rtX . bvebikoxww [ 0 ] - rtP . Rr * awwnlmpfsr_idx_1 ; if ( rtB . jpjuugikxn
>= rtP . wL ) { taskTimeV = look1_binlxpw ( muDoubleScalarRem ( ssGetT ( rtS
) - 0.0 , rtP . Constant_Value_jaivf4zt3q ) , rtP . LookUpTable1_bp01Data ,
rtP . Loadvaluepu_rep_seq_y , 2U ) * rtP . tauL ; } else { taskTimeV =
look1_binlxpw ( muDoubleScalarRem ( ssGetT ( rtS ) - 0.0 , rtP .
Constant_Value_jaivf4zt3q ) , rtP . LookUpTable1_bp01Data , rtP .
Loadvaluepu_rep_seq_y , 2U ) * rtP . tauL * rtP . Gain_Gain ; } rtB .
fc2lccxhbh = 1.0 / rtP . J * ( rtB . hti1q415mf - taskTimeV ) ;
UNUSED_PARAMETER ( tid ) ; } void MdlOutputsTID3 ( int_T tid ) { rtB .
hpkni4150v = rtP . Lfr * rtP . Lfs / rtP . Lmt * rtP . Gain5_Gain ; rtB .
ejcqi1uyvj = rtP . P1 * rtP . P1 ; rtB . fti1ov2wx1 = rtP . Gain3_Gain * rtP
. P1 ; UNUSED_PARAMETER ( tid ) ; } void MdlUpdate ( int_T tid ) {
UNUSED_PARAMETER ( tid ) ; } void MdlUpdateTID3 ( int_T tid ) {
UNUSED_PARAMETER ( tid ) ; } void MdlDerivatives ( void ) { XDot * _rtXdot ;
_rtXdot = ( ( XDot * ) ssGetdX ( rtS ) ) ; _rtXdot -> ij3r2xyt4x = rtB .
fc2lccxhbh ; _rtXdot -> cfcfwtiyhh [ 0 ] = rtB . ohdbrztky4 [ 0 ] ; _rtXdot
-> bvebikoxww [ 0 ] = rtB . bpsnzsfty3 [ 0 ] ; _rtXdot -> cfcfwtiyhh [ 1 ] =
rtB . ohdbrztky4 [ 1 ] ; _rtXdot -> bvebikoxww [ 1 ] = rtB . bpsnzsfty3 [ 1 ]
; _rtXdot -> dr2wn3m2tz = rtB . jpjuugikxn ; } void MdlProjection ( void ) {
} void MdlZeroCrossings ( void ) { ZCV * _rtZCSV ; _rtZCSV = ( ( ZCV * )
ssGetSolverZcSignalVector ( rtS ) ) ; _rtZCSV -> cyxbe0cwjw = rtB .
efr02sxb5p - rtP . P1 ; _rtZCSV -> oslyw3c0pz = rtB . j3axnrlwog - rtP . P1 ;
} void MdlTerminate ( void ) { if ( rt_slioCatalogue ( ) != ( NULL ) ) { void
* * slioCatalogueAddr = rt_slioCatalogueAddr ( ) ; rtwSaveDatasetsToMatFile (
rtwGetPointerFromUniquePtr ( rt_slioCatalogue ( ) ) ,
rt_GetMatSigstreamLoggingFileName ( ) ) ; rtwTerminateSlioCatalogue (
slioCatalogueAddr ) ; * slioCatalogueAddr = NULL ; } } void
MdlInitializeSizes ( void ) { ssSetNumContStates ( rtS , 6 ) ;
ssSetNumPeriodicContStates ( rtS , 0 ) ; ssSetNumY ( rtS , 0 ) ; ssSetNumU (
rtS , 0 ) ; ssSetDirectFeedThrough ( rtS , 0 ) ; ssSetNumSampleTimes ( rtS ,
3 ) ; ssSetNumBlocks ( rtS , 108 ) ; ssSetNumBlockIO ( rtS , 19 ) ;
ssSetNumBlockParams ( rtS , 149 ) ; } void MdlInitializeSampleTimes ( void )
{ ssSetSampleTime ( rtS , 0 , 0.0 ) ; ssSetSampleTime ( rtS , 1 , 0.0 ) ;
ssSetSampleTime ( rtS , 2 , - 2.0 ) ; ssSetOffsetTime ( rtS , 0 , 0.0 ) ;
ssSetOffsetTime ( rtS , 1 , 1.0 ) ; ssSetOffsetTime ( rtS , 2 , 0.0 ) ; }
void raccel_set_checksum ( ) { ssSetChecksumVal ( rtS , 0 , 1568829732U ) ;
ssSetChecksumVal ( rtS , 1 , 1397010639U ) ; ssSetChecksumVal ( rtS , 2 ,
3449803728U ) ; ssSetChecksumVal ( rtS , 3 , 1935705335U ) ; }
#if defined(_MSC_VER)
#pragma optimize( "", off )
#endif
SimStruct * raccel_register_model ( void ) { static struct _ssMdlInfo mdlInfo
; ( void ) memset ( ( char * ) rtS , 0 , sizeof ( SimStruct ) ) ; ( void )
memset ( ( char * ) & mdlInfo , 0 , sizeof ( struct _ssMdlInfo ) ) ;
ssSetMdlInfoPtr ( rtS , & mdlInfo ) ; { static time_T mdlPeriod [
NSAMPLE_TIMES ] ; static time_T mdlOffset [ NSAMPLE_TIMES ] ; static time_T
mdlTaskTimes [ NSAMPLE_TIMES ] ; static int_T mdlTsMap [ NSAMPLE_TIMES ] ;
static int_T mdlSampleHits [ NSAMPLE_TIMES ] ; static boolean_T
mdlTNextWasAdjustedPtr [ NSAMPLE_TIMES ] ; static int_T mdlPerTaskSampleHits
[ NSAMPLE_TIMES * NSAMPLE_TIMES ] ; static time_T mdlTimeOfNextSampleHit [
NSAMPLE_TIMES ] ; { int_T i ; for ( i = 0 ; i < NSAMPLE_TIMES ; i ++ ) {
mdlPeriod [ i ] = 0.0 ; mdlOffset [ i ] = 0.0 ; mdlTaskTimes [ i ] = 0.0 ;
mdlTsMap [ i ] = i ; mdlSampleHits [ i ] = 1 ; } } ssSetSampleTimePtr ( rtS ,
& mdlPeriod [ 0 ] ) ; ssSetOffsetTimePtr ( rtS , & mdlOffset [ 0 ] ) ;
ssSetSampleTimeTaskIDPtr ( rtS , & mdlTsMap [ 0 ] ) ; ssSetTPtr ( rtS , &
mdlTaskTimes [ 0 ] ) ; ssSetSampleHitPtr ( rtS , & mdlSampleHits [ 0 ] ) ;
ssSetTNextWasAdjustedPtr ( rtS , & mdlTNextWasAdjustedPtr [ 0 ] ) ;
ssSetPerTaskSampleHitsPtr ( rtS , & mdlPerTaskSampleHits [ 0 ] ) ;
ssSetTimeOfNextSampleHitPtr ( rtS , & mdlTimeOfNextSampleHit [ 0 ] ) ; }
ssSetSolverMode ( rtS , SOLVER_MODE_SINGLETASKING ) ; { ssSetBlockIO ( rtS ,
( ( void * ) & rtB ) ) ; ( void ) memset ( ( ( void * ) & rtB ) , 0 , sizeof
( B ) ) ; } { real_T * x = ( real_T * ) & rtX ; ssSetContStates ( rtS , x ) ;
( void ) memset ( ( void * ) x , 0 , sizeof ( X ) ) ; } { void * dwork = (
void * ) & rtDW ; ssSetRootDWork ( rtS , dwork ) ; ( void ) memset ( dwork ,
0 , sizeof ( DW ) ) ; } { static DataTypeTransInfo dtInfo ; ( void ) memset (
( char_T * ) & dtInfo , 0 , sizeof ( dtInfo ) ) ; ssSetModelMappingInfo ( rtS
, & dtInfo ) ; dtInfo . numDataTypes = 17 ; dtInfo . dataTypeSizes = &
rtDataTypeSizes [ 0 ] ; dtInfo . dataTypeNames = & rtDataTypeNames [ 0 ] ;
dtInfo . BTransTable = & rtBTransTable ; dtInfo . PTransTable = &
rtPTransTable ; dtInfo . dataTypeInfoTable = rtDataTypeInfoTable ; }
ModelMotS_dq_InitializeDataMapInfo ( ) ; ssSetIsRapidAcceleratorActive ( rtS
, true ) ; ssSetRootSS ( rtS , rtS ) ; ssSetVersion ( rtS ,
SIMSTRUCT_VERSION_LEVEL2 ) ; ssSetModelName ( rtS , "ModelMotS_dq" ) ;
ssSetPath ( rtS , "ModelMotS_dq" ) ; ssSetTStart ( rtS , 0.0 ) ; ssSetTFinal
( rtS , 221.5 ) ; { static RTWLogInfo rt_DataLoggingInfo ; rt_DataLoggingInfo
. loggingInterval = NULL ; ssSetRTWLogInfo ( rtS , & rt_DataLoggingInfo ) ; }
{ rtliSetLogXSignalInfo ( ssGetRTWLogInfo ( rtS ) , ( NULL ) ) ;
rtliSetLogXSignalPtrs ( ssGetRTWLogInfo ( rtS ) , ( NULL ) ) ; rtliSetLogT (
ssGetRTWLogInfo ( rtS ) , "tout" ) ; rtliSetLogX ( ssGetRTWLogInfo ( rtS ) ,
"" ) ; rtliSetLogXFinal ( ssGetRTWLogInfo ( rtS ) , "" ) ;
rtliSetLogVarNameModifier ( ssGetRTWLogInfo ( rtS ) , "none" ) ;
rtliSetLogFormat ( ssGetRTWLogInfo ( rtS ) , 4 ) ; rtliSetLogMaxRows (
ssGetRTWLogInfo ( rtS ) , 1000 ) ; rtliSetLogDecimation ( ssGetRTWLogInfo (
rtS ) , 1 ) ; rtliSetLogY ( ssGetRTWLogInfo ( rtS ) , "" ) ;
rtliSetLogYSignalInfo ( ssGetRTWLogInfo ( rtS ) , ( NULL ) ) ;
rtliSetLogYSignalPtrs ( ssGetRTWLogInfo ( rtS ) , ( NULL ) ) ; } { static
struct _ssStatesInfo2 statesInfo2 ; ssSetStatesInfo2 ( rtS , & statesInfo2 )
; } { static ssPeriodicStatesInfo periodicStatesInfo ;
ssSetPeriodicStatesInfo ( rtS , & periodicStatesInfo ) ; } { static
ssSolverInfo slvrInfo ; static boolean_T contStatesDisabled [ 6 ] ; static
real_T absTol [ 6 ] = { 1.0000000000000001E-7 , 1.0000000000000001E-7 ,
1.0000000000000001E-7 , 1.0000000000000001E-7 , 1.0000000000000001E-7 ,
1.0000000000000001E-7 } ; static uint8_T absTolControl [ 6 ] = { 0U , 0U , 0U
, 0U , 0U , 0U } ; static uint8_T zcAttributes [ 3 ] = { ( ZC_EVENT_ALL ) , (
ZC_EVENT_ALL ) , ( 0xc0 | ZC_EVENT_ALL_UP ) } ; static ssNonContDerivSigInfo
nonContDerivSigInfo [ 4 ] = { { 1 * sizeof ( boolean_T ) , ( char * ) ( & rtB
. ln3t0mutle ) , ( NULL ) } , { 1 * sizeof ( boolean_T ) , ( char * ) ( & rtB
. knnwpmthcv ) , ( NULL ) } , { 2 * sizeof ( real_T ) , ( char * ) ( & rtB .
gsrx3j1z5n [ 0 ] ) , ( NULL ) } , { 1 * sizeof ( real_T ) , ( char * ) ( &
rtB . niveaq0uyq ) , ( NULL ) } } ; ssSetSolverRelTol ( rtS , 0.0001 ) ;
ssSetStepSize ( rtS , 0.0 ) ; ssSetMinStepSize ( rtS , 0.0 ) ;
ssSetMaxNumMinSteps ( rtS , - 1 ) ; ssSetMinStepViolatedError ( rtS , 0 ) ;
ssSetMaxStepSize ( rtS , 0.0001 ) ; ssSetSolverMaxOrder ( rtS , - 1 ) ;
ssSetSolverRefineFactor ( rtS , 1 ) ; ssSetOutputTimes ( rtS , ( NULL ) ) ;
ssSetNumOutputTimes ( rtS , 0 ) ; ssSetOutputTimesOnly ( rtS , 0 ) ;
ssSetOutputTimesIndex ( rtS , 0 ) ; ssSetZCCacheNeedsReset ( rtS , 1 ) ;
ssSetDerivCacheNeedsReset ( rtS , 0 ) ; ssSetNumNonContDerivSigInfos ( rtS ,
4 ) ; ssSetNonContDerivSigInfos ( rtS , nonContDerivSigInfo ) ;
ssSetSolverInfo ( rtS , & slvrInfo ) ; ssSetSolverName ( rtS , "ode45" ) ;
ssSetVariableStepSolver ( rtS , 1 ) ; ssSetSolverConsistencyChecking ( rtS ,
0 ) ; ssSetSolverAdaptiveZcDetection ( rtS , 0 ) ;
ssSetSolverRobustResetMethod ( rtS , 0 ) ; ssSetAbsTolVector ( rtS , absTol )
; ssSetAbsTolControlVector ( rtS , absTolControl ) ;
ssSetSolverAbsTol_Obsolete ( rtS , absTol ) ;
ssSetSolverAbsTolControl_Obsolete ( rtS , absTolControl ) ;
ssSetSolverStateProjection ( rtS , 0 ) ; ssSetSolverMassMatrixType ( rtS , (
ssMatrixType ) 0 ) ; ssSetSolverMassMatrixNzMax ( rtS , 0 ) ;
ssSetModelOutputs ( rtS , MdlOutputs ) ; ssSetModelLogData ( rtS ,
rt_UpdateTXYLogVars ) ; ssSetModelLogDataIfInInterval ( rtS ,
rt_UpdateTXXFYLogVars ) ; ssSetModelUpdate ( rtS , MdlUpdate ) ;
ssSetModelDerivatives ( rtS , MdlDerivatives ) ; ssSetSolverZcSignalAttrib (
rtS , zcAttributes ) ; ssSetSolverNumZcSignals ( rtS , 3 ) ;
ssSetModelZeroCrossings ( rtS , MdlZeroCrossings ) ;
ssSetSolverConsecutiveZCsStepRelTol ( rtS , 2.8421709430404007E-13 ) ;
ssSetSolverMaxConsecutiveZCs ( rtS , 1000 ) ; ssSetSolverConsecutiveZCsError
( rtS , 2 ) ; ssSetSolverMaskedZcDiagnostic ( rtS , 1 ) ;
ssSetSolverIgnoredZcDiagnostic ( rtS , 1 ) ; ssSetSolverMaxConsecutiveMinStep
( rtS , 1 ) ; ssSetSolverShapePreserveControl ( rtS , 2 ) ; ssSetTNextTid (
rtS , INT_MIN ) ; ssSetTNext ( rtS , rtMinusInf ) ; ssSetSolverNeedsReset (
rtS ) ; ssSetNumNonsampledZCs ( rtS , 2 ) ; ssSetContStateDisabled ( rtS ,
contStatesDisabled ) ; ssSetSolverMaxConsecutiveMinStep ( rtS , 1 ) ; } {
ZCSigState * zc = ( ZCSigState * ) & rtPrevZCX ; ssSetPrevZCSigState ( rtS ,
zc ) ; } { rtPrevZCX . jgcq4ftyys = UNINITIALIZED_ZCSIG ; } ssSetChecksumVal
( rtS , 0 , 1568829732U ) ; ssSetChecksumVal ( rtS , 1 , 1397010639U ) ;
ssSetChecksumVal ( rtS , 2 , 3449803728U ) ; ssSetChecksumVal ( rtS , 3 ,
1935705335U ) ; { static const sysRanDType rtAlwaysEnabled =
SUBSYS_RAN_BC_ENABLE ; static RTWExtModeInfo rt_ExtModeInfo ; static const
sysRanDType * systemRan [ 7 ] ; gblRTWExtModeInfo = & rt_ExtModeInfo ;
ssSetRTWExtModeInfo ( rtS , & rt_ExtModeInfo ) ;
rteiSetSubSystemActiveVectorAddresses ( & rt_ExtModeInfo , systemRan ) ;
systemRan [ 0 ] = & rtAlwaysEnabled ; systemRan [ 1 ] = & rtAlwaysEnabled ;
systemRan [ 2 ] = & rtAlwaysEnabled ; systemRan [ 3 ] = & rtAlwaysEnabled ;
systemRan [ 4 ] = & rtAlwaysEnabled ; systemRan [ 5 ] = ( sysRanDType * ) &
rtDW . aetlgmgzmu ; systemRan [ 6 ] = ( sysRanDType * ) & rtDW . aetlgmgzmu ;
rteiSetModelMappingInfoPtr ( ssGetRTWExtModeInfo ( rtS ) , &
ssGetModelMappingInfo ( rtS ) ) ; rteiSetChecksumsPtr ( ssGetRTWExtModeInfo (
rtS ) , ssGetChecksums ( rtS ) ) ; rteiSetTPtr ( ssGetRTWExtModeInfo ( rtS )
, ssGetTPtr ( rtS ) ) ; } return rtS ; }
#if defined(_MSC_VER)
#pragma optimize( "", on )
#endif
const int_T gblParameterTuningTid = 3 ; void MdlOutputsParameterSampleTime (
int_T tid ) { MdlOutputsTID3 ( tid ) ; }
