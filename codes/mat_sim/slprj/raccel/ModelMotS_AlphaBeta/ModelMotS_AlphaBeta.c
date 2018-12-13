#include "__cf_ModelMotS_AlphaBeta.h"
#include "rt_logging_mmi.h"
#include "ModelMotS_AlphaBeta_capi.h"
#include <math.h>
#include "ModelMotS_AlphaBeta.h"
#include "ModelMotS_AlphaBeta_private.h"
#include "ModelMotS_AlphaBeta_dt.h"
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
"slprj//raccel//ModelMotS_AlphaBeta//ModelMotS_AlphaBeta_Jpattern.mat" ;
const int_T gblNumRootInportBlks = 0 ; const int_T gblNumModelInputs = 0 ;
extern rtInportTUtable * gblInportTUtables ; extern const char *
gblInportFileName ; const int_T gblInportDataTypeIdx [ ] = { - 1 } ; const
int_T gblInportDims [ ] = { - 1 } ; const int_T gblInportComplex [ ] = { - 1
} ; const int_T gblInportInterpoFlag [ ] = { - 1 } ; const int_T
gblInportContinuous [ ] = { - 1 } ; int_T enableFcnCallFlag [ ] = { 1 , 1 , 1
, 1 } ;
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
rtX . etwdgvk3w3 = rtP . wrinit ; rtX . malc5kzyq4 [ 0 ] = rtP . Psinit [ 0 ]
; rtX . aekrnoednt [ 0 ] = rtP . Prinit [ 0 ] ; rtX . malc5kzyq4 [ 1 ] = rtP
. Psinit [ 1 ] ; rtX . aekrnoednt [ 1 ] = rtP . Prinit [ 1 ] ; rtX .
lrwwpm2s4k = rtP . thrinit ; rtDW . gfcwkc4vko = ssGetTaskTime ( rtS , 1 ) ;
rtDW . bwejchtj5m = rtP . DiscreteTimeIntegrator_IC ; rtDW . ko425xjie0 = rtP
. UnitDelay2_InitialCondition ; } void MdlEnable ( void ) { rtDW . f2j1gzf1zg
= 1 ; _ssSetSampleHit ( rtS , 2 , 1 ) ; _ssSetTaskTime ( rtS , 2 , ssGetT (
rtS ) ) ; _ssSetVarNextHitTime ( rtS , 0 , ssGetT ( rtS ) ) ; ; } void
MdlStart ( void ) { { void * * slioCatalogueAddr = rt_slioCatalogueAddr ( ) ;
void * r2 = ( NULL ) ; void * * pOSigstreamManagerAddr = ( NULL ) ; const int
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
numCycles ; real_T lx3glt2xmb ; real_T dxgnthws4f ; ZCEventType zcEvent ;
real_T plabggejsh ; real_T eenmuqiz0m_idx_0 ; real_T eenmuqiz0m_idx_1 ;
real_T nhbdqeqv12_idx_1 ; srClearBC ( rtDW . n1ldkmquay ) ; rtB . gpbbxd3e1a
= rtX . etwdgvk3w3 ; if ( ssIsSampleHit ( rtS , 2 , 0 ) ) { taskTimeV =
ssGetTaskTime ( rtS , 2 ) ; if ( ssGetTNextWasAdjusted ( rtS , 2 ) ) { rtDW .
b5eaxoewzk = _ssGetVarNextHitTime ( rtS , 0 ) ; } if ( rtDW . f2j1gzf1zg != 0
) { rtDW . f2j1gzf1zg = 0 ; if ( taskTimeV >= rtP .
PulseGenerator1_PhaseDelay ) { ratio = ( taskTimeV - rtP .
PulseGenerator1_PhaseDelay ) / rtP . Ts ; numCycles = ( uint32_T )
muDoubleScalarFloor ( ratio ) ; if ( muDoubleScalarAbs ( ( real_T ) (
numCycles + 1U ) - ratio ) < DBL_EPSILON * ratio ) { numCycles ++ ; } rtDW .
ghpzi0bsm2 = numCycles ; ratio = ( ( real_T ) numCycles * rtP . Ts + rtP .
PulseGenerator1_PhaseDelay ) + rtP . PulseGenerator1_Duty * rtP . Ts / 100.0
; if ( taskTimeV < ratio ) { rtDW . nzeprll3k2 = 1 ; rtDW . b5eaxoewzk =
ratio ; } else { rtDW . nzeprll3k2 = 0 ; rtDW . b5eaxoewzk = ( real_T ) (
numCycles + 1U ) * rtP . Ts + rtP . PulseGenerator1_PhaseDelay ; } } else {
rtDW . ghpzi0bsm2 = rtP . PulseGenerator1_PhaseDelay != 0.0 ? - 1 : 0 ; rtDW
. nzeprll3k2 = 0 ; rtDW . b5eaxoewzk = rtP . PulseGenerator1_PhaseDelay ; } }
else { if ( rtDW . b5eaxoewzk <= taskTimeV ) { if ( rtDW . nzeprll3k2 == 1 )
{ rtDW . nzeprll3k2 = 0 ; rtDW . b5eaxoewzk = ( real_T ) ( rtDW . ghpzi0bsm2
+ 1L ) * rtP . Ts + rtP . PulseGenerator1_PhaseDelay ; } else { rtDW .
ghpzi0bsm2 ++ ; rtDW . nzeprll3k2 = 1 ; rtDW . b5eaxoewzk = ( rtP .
PulseGenerator1_Duty * rtP . Ts * 0.01 + ( real_T ) rtDW . ghpzi0bsm2 * rtP .
Ts ) + rtP . PulseGenerator1_PhaseDelay ; } } } _ssSetVarNextHitTime ( rtS ,
0 , rtDW . b5eaxoewzk ) ; if ( rtDW . nzeprll3k2 == 1 ) { rtB . on2ofjgexa =
rtP . PulseGenerator1_Amp ; } else { rtB . on2ofjgexa = 0.0 ; } } if (
ssIsSampleHit ( rtS , 1 , 0 ) ) { lx3glt2xmb = rtB . on2ofjgexa ; }
eenmuqiz0m_idx_0 = rtP . Lfr * rtX . malc5kzyq4 [ 0 ] + rtP . Lfs * rtX .
aekrnoednt [ 0 ] ; eenmuqiz0m_idx_1 = rtP . Lfr * rtX . malc5kzyq4 [ 1 ] +
rtP . Lfs * rtX . aekrnoednt [ 1 ] ; taskTimeV = muDoubleScalarPower (
eenmuqiz0m_idx_0 , 2.0 ) + muDoubleScalarPower ( eenmuqiz0m_idx_1 , 2.0 ) ;
if ( taskTimeV < 0.0 ) { taskTimeV = - muDoubleScalarSqrt ( - taskTimeV ) ; }
else { taskTimeV = muDoubleScalarSqrt ( taskTimeV ) ; } rtB . hmytavveer =
1.0 / ( ( rtP . Lfr * rtP . Lfs / rtP . Lmt + rtP . Lfr ) + rtP . Lfs ) *
taskTimeV ; if ( ssIsSampleHit ( rtS , 1 , 0 ) ) { if ( ssIsMajorTimeStep (
rtS ) ) { rtDW . euhyjx5ttx = ( rtB . hmytavveer >= rtP . P1 ) ; } rtB .
cjuexj30nh = rtDW . euhyjx5ttx ; } if ( rtB . cjuexj30nh ) { ratio = ( rtP .
Lfr * rtP . Lfs / rtP . Lmt * ( rtP . P2 - 2.0 * rtP . P1 ) + ( rtP . Lfr +
rtP . Lfs ) * rtP . P2 ) - taskTimeV ; plabggejsh = ratio * ratio - ( ( rtP .
Lfr + rtP . Lfs ) * - 0.48999999999999994 - ( rtP . P2 - 2.0 * rtP . P1 ) *
taskTimeV ) * ( rtP . Lfr * rtP . Lfs / rtP . Lmt ) * rtP . Gain4_Gain ; if (
plabggejsh < 0.0 ) { plabggejsh = - muDoubleScalarSqrt ( muDoubleScalarAbs (
plabggejsh ) ) ; } else { plabggejsh = muDoubleScalarSqrt ( plabggejsh ) ; }
ratio = ( plabggejsh - ratio ) / rtB . g3axur342h ; eenmuqiz0m_idx_0 =
eenmuqiz0m_idx_0 / taskTimeV * ratio ; eenmuqiz0m_idx_1 = eenmuqiz0m_idx_1 /
taskTimeV * ratio ; } else { taskTimeV = 1.0 / ( ( rtP . Lfr * rtP . Lfs /
rtP . Lmt + rtP . Lfr ) + rtP . Lfs ) ; eenmuqiz0m_idx_0 *= taskTimeV ;
eenmuqiz0m_idx_1 *= taskTimeV ; } taskTimeV = muDoubleScalarPower (
eenmuqiz0m_idx_0 , 2.0 ) + muDoubleScalarPower ( eenmuqiz0m_idx_1 , 2.0 ) ;
if ( taskTimeV < 0.0 ) { rtB . madwsvn1bo = - muDoubleScalarSqrt ( -
taskTimeV ) ; } else { rtB . madwsvn1bo = muDoubleScalarSqrt ( taskTimeV ) ;
} if ( ssIsSampleHit ( rtS , 1 , 0 ) ) { if ( ssIsMajorTimeStep ( rtS ) ) {
rtDW . a4kg5nbqon = ( rtB . madwsvn1bo >= rtP . P1 ) ; } rtB . gj5i4vllld =
rtDW . a4kg5nbqon ; } if ( rtB . gj5i4vllld ) { taskTimeV = ( rtB .
madwsvn1bo * rtP . P2 - rtB . mmagr3rvlr ) / ( ( rtP . P2 - rtB . ndhuby2l2s
) + rtB . madwsvn1bo ) ; eenmuqiz0m_idx_0 = eenmuqiz0m_idx_0 / rtB .
madwsvn1bo * taskTimeV ; eenmuqiz0m_idx_1 = eenmuqiz0m_idx_1 / rtB .
madwsvn1bo * taskTimeV ; } taskTimeV = 1.0 / rtP . Lfr ; plabggejsh = ( rtX .
aekrnoednt [ 0 ] - eenmuqiz0m_idx_0 ) * taskTimeV ; nhbdqeqv12_idx_1 = ( rtX
. aekrnoednt [ 1 ] - eenmuqiz0m_idx_1 ) * taskTimeV ; rtB . f10pcxma3u = 3.0
* rtP . np / 2.0 * ( plabggejsh * rtX . aekrnoednt [ 1 ] - rtX . aekrnoednt [
0 ] * nhbdqeqv12_idx_1 ) ; if ( rtB . gpbbxd3e1a >= rtP . wL ) { taskTimeV =
look1_binlxpw ( muDoubleScalarRem ( ssGetT ( rtS ) - 0.0 , rtP .
Constant_Value_jaivf4zt3q ) , rtP . LookUpTable1_bp01Data , rtP .
Loadvaluepu_rep_seq_y , 295399U ) * rtP . tauL ; } else { taskTimeV =
look1_binlxpw ( muDoubleScalarRem ( ssGetT ( rtS ) - 0.0 , rtP .
Constant_Value_jaivf4zt3q ) , rtP . LookUpTable1_bp01Data , rtP .
Loadvaluepu_rep_seq_y , 295399U ) * rtP . tauL * rtP . Gain_Gain ; } rtB .
cgvtocnbhf = 1.0 / rtP . J * ( rtB . f10pcxma3u - taskTimeV ) ; taskTimeV =
1.0 / rtP . Lfs ; rtB . lmtcfzni2c [ 0 ] = ( rtX . malc5kzyq4 [ 0 ] -
eenmuqiz0m_idx_0 ) * taskTimeV ; rtB . lmtcfzni2c [ 1 ] = ( rtX . malc5kzyq4
[ 1 ] - eenmuqiz0m_idx_1 ) * taskTimeV ; rtB . erkosogxty = rtP . np * rtB .
gpbbxd3e1a ; rtB . otejpxdnyh = look1_binlxpw ( muDoubleScalarRem ( ssGetT (
rtS ) - 0.0 , rtP . Constant_Value_dn2cyv14tz ) , rtP .
LookUpTable1_bp01Data_gh5vwq5i5u , rtP . ReferenceSpeedrads_rep_seq_y ,
406394U ) ; if ( ssIsSampleHit ( rtS , 1 , 0 ) && ssIsMajorTimeStep ( rtS ) )
{ zcEvent = rt_ZCFcn ( RISING_ZERO_CROSSING , & rtPrevZCX . mdpbkmi5bz , (
lx3glt2xmb ) ) ; if ( zcEvent != NO_ZCEVENT ) { rtDW . hoadgf1elz =
ssGetTaskTime ( rtS , 1 ) - rtDW . gfcwkc4vko ; rtDW . gfcwkc4vko =
ssGetTaskTime ( rtS , 1 ) ; dxgnthws4f = muDoubleScalarSin ( rtDW .
bwejchtj5m ) ; lx3glt2xmb = rtP . Ts * rtP . Rr / rtP . Lr * ( rtP . Psdnom -
rtDW . ko425xjie0 ) + rtDW . ko425xjie0 ; ratio = rtB . otejpxdnyh *
lx3glt2xmb ; taskTimeV = muDoubleScalarPower ( rtP . Uo , 2.0 ) +
muDoubleScalarPower ( ratio , 2.0 ) ; if ( taskTimeV < 0.0 ) { taskTimeV = -
muDoubleScalarSqrt ( - taskTimeV ) ; } else { taskTimeV = muDoubleScalarSqrt
( taskTimeV ) ; } if ( taskTimeV <= rtP . Ulim ) { taskTimeV = rtP .
Constant4_Value ; } else { if ( taskTimeV <= rtP . Constant_Value ) {
taskTimeV = rtP . Constant5_Value ; } taskTimeV = rtP . Ulim / taskTimeV ; }
eenmuqiz0m_idx_0 = rtP . Uo * taskTimeV ; eenmuqiz0m_idx_1 = ratio *
taskTimeV ; taskTimeV = muDoubleScalarCos ( rtDW . bwejchtj5m ) ; rtB .
h2sendcr2c = rtP . Gain1_Gain * dxgnthws4f * eenmuqiz0m_idx_1 +
eenmuqiz0m_idx_0 * taskTimeV ; rtB . bnsafpf0ct = eenmuqiz0m_idx_1 *
taskTimeV + eenmuqiz0m_idx_0 * dxgnthws4f ; rtDW . bwejchtj5m += rtP .
DiscreteTimeIntegrator_gainval * rtDW . hoadgf1elz * rtB . otejpxdnyh ; rtDW
. ko425xjie0 = lx3glt2xmb ; rtDW . n1ldkmquay = 4 ; } } rtB . a2lne1ot00 [ 0
] = rtB . h2sendcr2c - rtP . Rs * rtB . lmtcfzni2c [ 0 ] ; rtB . a2lne1ot00 [
1 ] = rtB . bnsafpf0ct - rtP . Rs * rtB . lmtcfzni2c [ 1 ] ; rtB . a2aj3jru0z
[ 0 ] = rtP . Gain_Gain_aopx5rkhzb * rtX . aekrnoednt [ 1 ] * rtB .
erkosogxty - rtP . Rr * plabggejsh ; rtB . a2aj3jru0z [ 1 ] = rtB .
erkosogxty * rtX . aekrnoednt [ 0 ] - rtP . Rr * nhbdqeqv12_idx_1 ;
UNUSED_PARAMETER ( tid ) ; } void MdlOutputsTID3 ( int_T tid ) { rtB .
g3axur342h = rtP . Lfr * rtP . Lfs / rtP . Lmt * rtP . Gain5_Gain ; rtB .
mmagr3rvlr = rtP . P1 * rtP . P1 ; rtB . ndhuby2l2s = rtP . Gain3_Gain * rtP
. P1 ; UNUSED_PARAMETER ( tid ) ; } void MdlUpdate ( int_T tid ) {
UNUSED_PARAMETER ( tid ) ; } void MdlUpdateTID3 ( int_T tid ) {
UNUSED_PARAMETER ( tid ) ; } void MdlDerivatives ( void ) { XDot * _rtXdot ;
_rtXdot = ( ( XDot * ) ssGetdX ( rtS ) ) ; _rtXdot -> etwdgvk3w3 = rtB .
cgvtocnbhf ; _rtXdot -> malc5kzyq4 [ 0 ] = rtB . a2lne1ot00 [ 0 ] ; _rtXdot
-> aekrnoednt [ 0 ] = rtB . a2aj3jru0z [ 0 ] ; _rtXdot -> malc5kzyq4 [ 1 ] =
rtB . a2lne1ot00 [ 1 ] ; _rtXdot -> aekrnoednt [ 1 ] = rtB . a2aj3jru0z [ 1 ]
; _rtXdot -> lrwwpm2s4k = rtB . gpbbxd3e1a ; } void MdlProjection ( void ) {
} void MdlZeroCrossings ( void ) { ZCV * _rtZCSV ; _rtZCSV = ( ( ZCV * )
ssGetSolverZcSignalVector ( rtS ) ) ; _rtZCSV -> ekyny2ur1i = rtB .
hmytavveer - rtP . P1 ; _rtZCSV -> ashiibwaqp = rtB . madwsvn1bo - rtP . P1 ;
} void MdlTerminate ( void ) { if ( rt_slioCatalogue ( ) != ( NULL ) ) { void
* * slioCatalogueAddr = rt_slioCatalogueAddr ( ) ; rtwSaveDatasetsToMatFile (
rtwGetPointerFromUniquePtr ( rt_slioCatalogue ( ) ) ,
rt_GetMatSigstreamLoggingFileName ( ) ) ; rtwTerminateSlioCatalogue (
slioCatalogueAddr ) ; * slioCatalogueAddr = NULL ; } } void
MdlInitializeSizes ( void ) { ssSetNumContStates ( rtS , 6 ) ;
ssSetNumPeriodicContStates ( rtS , 0 ) ; ssSetNumY ( rtS , 0 ) ; ssSetNumU (
rtS , 0 ) ; ssSetDirectFeedThrough ( rtS , 0 ) ; ssSetNumSampleTimes ( rtS ,
3 ) ; ssSetNumBlocks ( rtS , 114 ) ; ssSetNumBlockIO ( rtS , 19 ) ;
ssSetNumBlockParams ( rtS , 1403629 ) ; } void MdlInitializeSampleTimes (
void ) { ssSetSampleTime ( rtS , 0 , 0.0 ) ; ssSetSampleTime ( rtS , 1 , 0.0
) ; ssSetSampleTime ( rtS , 2 , - 2.0 ) ; ssSetOffsetTime ( rtS , 0 , 0.0 ) ;
ssSetOffsetTime ( rtS , 1 , 1.0 ) ; ssSetOffsetTime ( rtS , 2 , 0.0 ) ; }
void raccel_set_checksum ( ) { ssSetChecksumVal ( rtS , 0 , 38497780U ) ;
ssSetChecksumVal ( rtS , 1 , 1605387947U ) ; ssSetChecksumVal ( rtS , 2 ,
1240629776U ) ; ssSetChecksumVal ( rtS , 3 , 3562513693U ) ; }
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
ModelMotS_AlphaBeta_InitializeDataMapInfo ( ) ; ssSetIsRapidAcceleratorActive
( rtS , true ) ; ssSetRootSS ( rtS , rtS ) ; ssSetVersion ( rtS ,
SIMSTRUCT_VERSION_LEVEL2 ) ; ssSetModelName ( rtS , "ModelMotS_AlphaBeta" ) ;
ssSetPath ( rtS , "ModelMotS_AlphaBeta" ) ; ssSetTStart ( rtS , 0.0 ) ;
ssSetTFinal ( rtS , 1200.0 ) ; { static RTWLogInfo rt_DataLoggingInfo ;
rt_DataLoggingInfo . loggingInterval = NULL ; ssSetRTWLogInfo ( rtS , &
rt_DataLoggingInfo ) ; } { { static int_T rt_LoggedStateWidths [ ] = { 1 , 2
, 2 , 1 , 1 , 1 } ; static int_T rt_LoggedStateNumDimensions [ ] = { 1 , 1 ,
1 , 1 , 1 , 1 } ; static int_T rt_LoggedStateDimensions [ ] = { 1 , 2 , 2 , 1
, 1 , 1 } ; static boolean_T rt_LoggedStateIsVarDims [ ] = { 0 , 0 , 0 , 0 ,
0 , 0 } ; static BuiltInDTypeId rt_LoggedStateDataTypeIds [ ] = { SS_DOUBLE ,
SS_DOUBLE , SS_DOUBLE , SS_DOUBLE , SS_DOUBLE , SS_DOUBLE } ; static int_T
rt_LoggedStateComplexSignals [ ] = { 0 , 0 , 0 , 0 , 0 , 0 } ; static
RTWPreprocessingFcnPtr rt_LoggingStatePreprocessingFcnPtrs [ ] = { ( NULL ) ,
( NULL ) , ( NULL ) , ( NULL ) , ( NULL ) , ( NULL ) } ; static const char_T
* rt_LoggedStateLabels [ ] = { "CSTATE" , "CSTATE" , "CSTATE" , "CSTATE" ,
"DSTATE" , "DSTATE" } ; static const char_T * rt_LoggedStateBlockNames [ ] =
{
 "ModelMotS_AlphaBeta/Induction Motor - Mechanical part\nRigid Coupling1/Integrator2"
,
"ModelMotS_AlphaBeta/Inudction Motor\nElectrical Part\nalpha,beta/Integrator"
,
"ModelMotS_AlphaBeta/Inudction Motor\nElectrical Part\nalpha,beta/Integrator1"
,
 "ModelMotS_AlphaBeta/Induction Motor - Mechanical part\nRigid Coupling1/Integrator1"
,
"ModelMotS_AlphaBeta/UF control _ abframe/UF control/Discrete-Time\nIntegrator"
, "ModelMotS_AlphaBeta/UF control _ abframe/UF control/Unit Delay2" } ;
static const char_T * rt_LoggedStateNames [ ] = { "" , "" , "" , "" , "" , ""
} ; static boolean_T rt_LoggedStateCrossMdlRef [ ] = { 0 , 0 , 0 , 0 , 0 , 0
} ; static RTWLogDataTypeConvert rt_RTWLogDataTypeConvert [ ] = { { 0 ,
SS_DOUBLE , SS_DOUBLE , 0 , 0 , 0 , 1.0 , 0 , 0.0 } , { 0 , SS_DOUBLE ,
SS_DOUBLE , 0 , 0 , 0 , 1.0 , 0 , 0.0 } , { 0 , SS_DOUBLE , SS_DOUBLE , 0 , 0
, 0 , 1.0 , 0 , 0.0 } , { 0 , SS_DOUBLE , SS_DOUBLE , 0 , 0 , 0 , 1.0 , 0 ,
0.0 } , { 0 , SS_DOUBLE , SS_DOUBLE , 0 , 0 , 0 , 1.0 , 0 , 0.0 } , { 0 ,
SS_DOUBLE , SS_DOUBLE , 0 , 0 , 0 , 1.0 , 0 , 0.0 } } ; static
RTWLogSignalInfo rt_LoggedStateSignalInfo = { 6 , rt_LoggedStateWidths ,
rt_LoggedStateNumDimensions , rt_LoggedStateDimensions ,
rt_LoggedStateIsVarDims , ( NULL ) , ( NULL ) , rt_LoggedStateDataTypeIds ,
rt_LoggedStateComplexSignals , ( NULL ) , rt_LoggingStatePreprocessingFcnPtrs
, { rt_LoggedStateLabels } , ( NULL ) , ( NULL ) , ( NULL ) , {
rt_LoggedStateBlockNames } , { rt_LoggedStateNames } ,
rt_LoggedStateCrossMdlRef , rt_RTWLogDataTypeConvert } ; static void *
rt_LoggedStateSignalPtrs [ 6 ] ; rtliSetLogXSignalPtrs ( ssGetRTWLogInfo (
rtS ) , ( LogSignalPtrsType ) rt_LoggedStateSignalPtrs ) ;
rtliSetLogXSignalInfo ( ssGetRTWLogInfo ( rtS ) , & rt_LoggedStateSignalInfo
) ; rt_LoggedStateSignalPtrs [ 0 ] = ( void * ) & rtX . etwdgvk3w3 ;
rt_LoggedStateSignalPtrs [ 1 ] = ( void * ) & rtX . malc5kzyq4 [ 0 ] ;
rt_LoggedStateSignalPtrs [ 2 ] = ( void * ) & rtX . aekrnoednt [ 0 ] ;
rt_LoggedStateSignalPtrs [ 3 ] = ( void * ) & rtX . lrwwpm2s4k ;
rt_LoggedStateSignalPtrs [ 4 ] = ( void * ) & rtDW . bwejchtj5m ;
rt_LoggedStateSignalPtrs [ 5 ] = ( void * ) & rtDW . ko425xjie0 ; }
rtliSetLogT ( ssGetRTWLogInfo ( rtS ) , "tout" ) ; rtliSetLogX (
ssGetRTWLogInfo ( rtS ) , "tmp_raccel_xout" ) ; rtliSetLogXFinal (
ssGetRTWLogInfo ( rtS ) , "xFinal" ) ; rtliSetLogVarNameModifier (
ssGetRTWLogInfo ( rtS ) , "none" ) ; rtliSetLogFormat ( ssGetRTWLogInfo ( rtS
) , 2 ) ; rtliSetLogMaxRows ( ssGetRTWLogInfo ( rtS ) , 1000 ) ;
rtliSetLogDecimation ( ssGetRTWLogInfo ( rtS ) , 1 ) ; rtliSetLogY (
ssGetRTWLogInfo ( rtS ) , "" ) ; rtliSetLogYSignalInfo ( ssGetRTWLogInfo (
rtS ) , ( NULL ) ) ; rtliSetLogYSignalPtrs ( ssGetRTWLogInfo ( rtS ) , ( NULL
) ) ; } { static struct _ssStatesInfo2 statesInfo2 ; ssSetStatesInfo2 ( rtS ,
& statesInfo2 ) ; } { static ssPeriodicStatesInfo periodicStatesInfo ;
ssSetPeriodicStatesInfo ( rtS , & periodicStatesInfo ) ; } { static
ssSolverInfo slvrInfo ; static boolean_T contStatesDisabled [ 6 ] ; static
real_T absTol [ 6 ] = { 1.0E-6 , 1.0E-6 , 1.0E-6 , 1.0E-6 , 1.0E-6 , 1.0E-6 }
; static uint8_T absTolControl [ 6 ] = { 0U , 0U , 0U , 0U , 0U , 0U } ;
static uint8_T zcAttributes [ 3 ] = { ( ZC_EVENT_ALL ) , ( ZC_EVENT_ALL ) , (
0xc0 | ZC_EVENT_ALL_UP ) } ; static ssNonContDerivSigInfo nonContDerivSigInfo
[ 4 ] = { { 1 * sizeof ( boolean_T ) , ( char * ) ( & rtB . gj5i4vllld ) , (
NULL ) } , { 1 * sizeof ( boolean_T ) , ( char * ) ( & rtB . cjuexj30nh ) , (
NULL ) } , { 1 * sizeof ( real_T ) , ( char * ) ( & rtB . bnsafpf0ct ) , (
NULL ) } , { 1 * sizeof ( real_T ) , ( char * ) ( & rtB . h2sendcr2c ) , (
NULL ) } } ; ssSetSolverRelTol ( rtS , 0.1 ) ; ssSetStepSize ( rtS , 0.0 ) ;
ssSetMinStepSize ( rtS , 0.01 ) ; ssSetMaxNumMinSteps ( rtS , - 1 ) ;
ssSetMinStepViolatedError ( rtS , 0 ) ; ssSetMaxStepSize ( rtS , 0.1 ) ;
ssSetSolverMaxOrder ( rtS , - 1 ) ; ssSetSolverRefineFactor ( rtS , 1 ) ;
ssSetOutputTimes ( rtS , ( NULL ) ) ; ssSetNumOutputTimes ( rtS , 0 ) ;
ssSetOutputTimesOnly ( rtS , 0 ) ; ssSetOutputTimesIndex ( rtS , 0 ) ;
ssSetZCCacheNeedsReset ( rtS , 1 ) ; ssSetDerivCacheNeedsReset ( rtS , 0 ) ;
ssSetNumNonContDerivSigInfos ( rtS , 4 ) ; ssSetNonContDerivSigInfos ( rtS ,
nonContDerivSigInfo ) ; ssSetSolverInfo ( rtS , & slvrInfo ) ;
ssSetSolverName ( rtS , "ode45" ) ; ssSetVariableStepSolver ( rtS , 1 ) ;
ssSetSolverConsistencyChecking ( rtS , 0 ) ; ssSetSolverAdaptiveZcDetection (
rtS , 0 ) ; ssSetSolverRobustResetMethod ( rtS , 0 ) ; ssSetAbsTolVector (
rtS , absTol ) ; ssSetAbsTolControlVector ( rtS , absTolControl ) ;
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
zc ) ; } { rtPrevZCX . mdpbkmi5bz = UNINITIALIZED_ZCSIG ; } ssSetChecksumVal
( rtS , 0 , 38497780U ) ; ssSetChecksumVal ( rtS , 1 , 1605387947U ) ;
ssSetChecksumVal ( rtS , 2 , 1240629776U ) ; ssSetChecksumVal ( rtS , 3 ,
3562513693U ) ; { static const sysRanDType rtAlwaysEnabled =
SUBSYS_RAN_BC_ENABLE ; static RTWExtModeInfo rt_ExtModeInfo ; static const
sysRanDType * systemRan [ 7 ] ; gblRTWExtModeInfo = & rt_ExtModeInfo ;
ssSetRTWExtModeInfo ( rtS , & rt_ExtModeInfo ) ;
rteiSetSubSystemActiveVectorAddresses ( & rt_ExtModeInfo , systemRan ) ;
systemRan [ 0 ] = & rtAlwaysEnabled ; systemRan [ 1 ] = & rtAlwaysEnabled ;
systemRan [ 2 ] = & rtAlwaysEnabled ; systemRan [ 3 ] = & rtAlwaysEnabled ;
systemRan [ 4 ] = & rtAlwaysEnabled ; systemRan [ 5 ] = ( sysRanDType * ) &
rtDW . n1ldkmquay ; systemRan [ 6 ] = ( sysRanDType * ) & rtDW . n1ldkmquay ;
rteiSetModelMappingInfoPtr ( ssGetRTWExtModeInfo ( rtS ) , &
ssGetModelMappingInfo ( rtS ) ) ; rteiSetChecksumsPtr ( ssGetRTWExtModeInfo (
rtS ) , ssGetChecksums ( rtS ) ) ; rteiSetTPtr ( ssGetRTWExtModeInfo ( rtS )
, ssGetTPtr ( rtS ) ) ; } return rtS ; }
#if defined(_MSC_VER)
#pragma optimize( "", on )
#endif
const int_T gblParameterTuningTid = 3 ; void MdlOutputsParameterSampleTime (
int_T tid ) { MdlOutputsTID3 ( tid ) ; }
