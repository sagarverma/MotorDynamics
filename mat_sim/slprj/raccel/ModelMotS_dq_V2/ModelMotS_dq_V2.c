#include "__cf_ModelMotS_dq_V2.h"
#include "rt_logging_mmi.h"
#include "ModelMotS_dq_V2_capi.h"
#include <math.h>
#include "ModelMotS_dq_V2.h"
#include "ModelMotS_dq_V2_private.h"
#include "ModelMotS_dq_V2_dt.h"
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
"slprj//raccel//ModelMotS_dq_V2//ModelMotS_dq_V2_Jpattern.mat" ; const int_T
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
rtX . kucazwxe1p = rtP . wrinit ; rtX . ggygjq5ouq [ 0 ] = rtP . Psinit [ 0 ]
; rtX . hvulyscokz [ 0 ] = rtP . Prinit [ 0 ] ; rtX . ggygjq5ouq [ 1 ] = rtP
. Psinit [ 1 ] ; rtX . hvulyscokz [ 1 ] = rtP . Prinit [ 1 ] ; rtX .
cr2w1d1tsl = rtP . thrinit ; rtDW . piiyfoznre = rtP .
UnitDelay2_InitialCondition ; } void MdlEnable ( void ) { rtDW . ccffucponj =
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
real_T fsuvnkcxxk_idx_0 ; real_T fsuvnkcxxk_idx_1 ; real_T fgi23zg44a_idx_1 ;
srClearBC ( rtDW . hdmj0f2xda ) ; rtB . llcuyb21kn = look1_binlxpw (
muDoubleScalarRem ( ssGetT ( rtS ) - 0.0 , rtP . Constant_Value_dn2cyv14tz )
, rtP . LookUpTable1_bp01Data , rtP . ReferenceSpeedrads_rep_seq_y , 11999U )
; rtB . agjnm01x4l = look1_binlxpw ( muDoubleScalarRem ( ssGetT ( rtS ) - 0.0
, rtP . Constant_Value_jaivf4zt3q ) , rtP . LookUpTable1_bp01Data_jgw1iq0tw2
, rtP . Loadvaluepu_rep_seq_y , 11999U ) ; rtB . g50obrftrn = rtX .
kucazwxe1p ; if ( ssIsSampleHit ( rtS , 2 , 0 ) ) { taskTimeV = ssGetTaskTime
( rtS , 2 ) ; if ( ssGetTNextWasAdjusted ( rtS , 2 ) ) { rtDW . icx4udn11x =
_ssGetVarNextHitTime ( rtS , 0 ) ; } if ( rtDW . ccffucponj != 0 ) { rtDW .
ccffucponj = 0 ; if ( taskTimeV >= rtP . PulseGenerator2_PhaseDelay ) { ratio
= ( taskTimeV - rtP . PulseGenerator2_PhaseDelay ) / rtP . Ts ; numCycles = (
uint32_T ) muDoubleScalarFloor ( ratio ) ; if ( muDoubleScalarAbs ( ( real_T
) ( numCycles + 1U ) - ratio ) < DBL_EPSILON * ratio ) { numCycles ++ ; }
rtDW . abyvocg0q5 = numCycles ; ratio = ( ( real_T ) numCycles * rtP . Ts +
rtP . PulseGenerator2_PhaseDelay ) + rtP . PulseGenerator2_Duty * rtP . Ts /
100.0 ; if ( taskTimeV < ratio ) { rtDW . npl1j2qvtj = 1 ; rtDW . icx4udn11x
= ratio ; } else { rtDW . npl1j2qvtj = 0 ; rtDW . icx4udn11x = ( real_T ) (
numCycles + 1U ) * rtP . Ts + rtP . PulseGenerator2_PhaseDelay ; } } else {
rtDW . abyvocg0q5 = rtP . PulseGenerator2_PhaseDelay != 0.0 ? - 1 : 0 ; rtDW
. npl1j2qvtj = 0 ; rtDW . icx4udn11x = rtP . PulseGenerator2_PhaseDelay ; } }
else { if ( rtDW . icx4udn11x <= taskTimeV ) { if ( rtDW . npl1j2qvtj == 1 )
{ rtDW . npl1j2qvtj = 0 ; rtDW . icx4udn11x = ( real_T ) ( rtDW . abyvocg0q5
+ 1L ) * rtP . Ts + rtP . PulseGenerator2_PhaseDelay ; } else { rtDW .
abyvocg0q5 ++ ; rtDW . npl1j2qvtj = 1 ; rtDW . icx4udn11x = ( rtP .
PulseGenerator2_Duty * rtP . Ts * 0.01 + ( real_T ) rtDW . abyvocg0q5 * rtP .
Ts ) + rtP . PulseGenerator2_PhaseDelay ; } } } _ssSetVarNextHitTime ( rtS ,
0 , rtDW . icx4udn11x ) ; if ( rtDW . npl1j2qvtj == 1 ) { rtB . lbn1yidduk =
rtP . PulseGenerator2_Amp ; } else { rtB . lbn1yidduk = 0.0 ; } } if (
ssIsSampleHit ( rtS , 1 , 0 ) ) { cvt0djk3nv = rtB . lbn1yidduk ; }
fsuvnkcxxk_idx_0 = rtP . Lfr * rtX . ggygjq5ouq [ 0 ] + rtP . Lfs * rtX .
hvulyscokz [ 0 ] ; fsuvnkcxxk_idx_1 = rtP . Lfr * rtX . ggygjq5ouq [ 1 ] +
rtP . Lfs * rtX . hvulyscokz [ 1 ] ; taskTimeV = muDoubleScalarPower (
fsuvnkcxxk_idx_0 , 2.0 ) + muDoubleScalarPower ( fsuvnkcxxk_idx_1 , 2.0 ) ;
if ( taskTimeV < 0.0 ) { taskTimeV = - muDoubleScalarSqrt ( - taskTimeV ) ; }
else { taskTimeV = muDoubleScalarSqrt ( taskTimeV ) ; } rtB . pzn3ntwo0f =
1.0 / ( ( rtP . Lfr * rtP . Lfs / rtP . Lmt + rtP . Lfr ) + rtP . Lfs ) *
taskTimeV ; if ( ssIsSampleHit ( rtS , 1 , 0 ) ) { if ( ssIsMajorTimeStep (
rtS ) ) { rtDW . cobnjav3td = ( rtB . pzn3ntwo0f >= rtP . P1 ) ; } rtB .
k4xamhzsst = rtDW . cobnjav3td ; } if ( rtB . k4xamhzsst ) { ratio = ( rtP .
Lfr * rtP . Lfs / rtP . Lmt * ( rtP . P2 - 2.0 * rtP . P1 ) + ( rtP . Lfr +
rtP . Lfs ) * rtP . P2 ) - taskTimeV ; iaas34rry1 = ratio * ratio - ( ( rtP .
Lfr + rtP . Lfs ) * - 0.48999999999999994 - ( rtP . P2 - 2.0 * rtP . P1 ) *
taskTimeV ) * ( rtP . Lfr * rtP . Lfs / rtP . Lmt ) * rtP . Gain4_Gain ; if (
iaas34rry1 < 0.0 ) { iaas34rry1 = - muDoubleScalarSqrt ( muDoubleScalarAbs (
iaas34rry1 ) ) ; } else { iaas34rry1 = muDoubleScalarSqrt ( iaas34rry1 ) ; }
ratio = ( iaas34rry1 - ratio ) / rtB . kywwenqxru ; fsuvnkcxxk_idx_0 =
fsuvnkcxxk_idx_0 / taskTimeV * ratio ; fsuvnkcxxk_idx_1 = fsuvnkcxxk_idx_1 /
taskTimeV * ratio ; } else { taskTimeV = 1.0 / ( ( rtP . Lfr * rtP . Lfs /
rtP . Lmt + rtP . Lfr ) + rtP . Lfs ) ; fsuvnkcxxk_idx_0 *= taskTimeV ;
fsuvnkcxxk_idx_1 *= taskTimeV ; } taskTimeV = muDoubleScalarPower (
fsuvnkcxxk_idx_0 , 2.0 ) + muDoubleScalarPower ( fsuvnkcxxk_idx_1 , 2.0 ) ;
if ( taskTimeV < 0.0 ) { rtB . lfrpqznzmd = - muDoubleScalarSqrt ( -
taskTimeV ) ; } else { rtB . lfrpqznzmd = muDoubleScalarSqrt ( taskTimeV ) ;
} if ( ssIsSampleHit ( rtS , 1 , 0 ) ) { if ( ssIsMajorTimeStep ( rtS ) ) {
rtDW . cg43etw1s5 = ( rtB . lfrpqznzmd >= rtP . P1 ) ; } rtB . oleotyrvsj =
rtDW . cg43etw1s5 ; } if ( rtB . oleotyrvsj ) { taskTimeV = ( rtB .
lfrpqznzmd * rtP . P2 - rtB . czrf0nwdxd ) / ( ( rtP . P2 - rtB . aa0ktk1lsw
) + rtB . lfrpqznzmd ) ; fsuvnkcxxk_idx_0 = fsuvnkcxxk_idx_0 / rtB .
lfrpqznzmd * taskTimeV ; fsuvnkcxxk_idx_1 = fsuvnkcxxk_idx_1 / rtB .
lfrpqznzmd * taskTimeV ; } taskTimeV = 1.0 / rtP . Lfr ; iaas34rry1 = ( rtX .
hvulyscokz [ 0 ] - fsuvnkcxxk_idx_0 ) * taskTimeV ; fgi23zg44a_idx_1 = ( rtX
. hvulyscokz [ 1 ] - fsuvnkcxxk_idx_1 ) * taskTimeV ; rtB . c40hosfmrc = 3.0
* rtP . np / 2.0 * ( iaas34rry1 * rtX . hvulyscokz [ 1 ] - rtX . hvulyscokz [
0 ] * fgi23zg44a_idx_1 ) ; taskTimeV = 1.0 / rtP . Lfs ; rtB . its0a3zvwu [ 0
] = ( rtX . ggygjq5ouq [ 0 ] - fsuvnkcxxk_idx_0 ) * taskTimeV ; rtB .
its0a3zvwu [ 1 ] = ( rtX . ggygjq5ouq [ 1 ] - fsuvnkcxxk_idx_1 ) * taskTimeV
; rtB . n5nk0fcdxe = rtP . np * rtB . g50obrftrn ; if ( ssIsSampleHit ( rtS ,
1 , 0 ) && ssIsMajorTimeStep ( rtS ) ) { zcEvent = rt_ZCFcn (
RISING_ZERO_CROSSING , & rtPrevZCX . kl1isclcqj , ( cvt0djk3nv ) ) ; if (
zcEvent != NO_ZCEVENT ) { rtB . awofsj5yej = rtB . llcuyb21kn ; cvt0djk3nv =
rtP . Ts * rtP . Rr / rtP . Lr * ( rtP . Psdnom - rtDW . piiyfoznre ) + rtDW
. piiyfoznre ; ratio = rtB . awofsj5yej * cvt0djk3nv ; taskTimeV =
muDoubleScalarPower ( rtP . Uo , 2.0 ) + muDoubleScalarPower ( ratio , 2.0 )
; if ( taskTimeV < 0.0 ) { taskTimeV = - muDoubleScalarSqrt ( - taskTimeV ) ;
} else { taskTimeV = muDoubleScalarSqrt ( taskTimeV ) ; } if ( taskTimeV <=
rtP . Ulim ) { taskTimeV = rtP . Constant4_Value ; } else { if ( taskTimeV <=
rtP . Constant_Value ) { taskTimeV = rtP . Constant5_Value ; } taskTimeV =
rtP . Ulim / taskTimeV ; } rtB . oussmmuoy4 [ 0 ] = rtP . Uo * taskTimeV ;
rtB . oussmmuoy4 [ 1 ] = ratio * taskTimeV ; rtDW . piiyfoznre = cvt0djk3nv ;
rtDW . hdmj0f2xda = 4 ; } } cvt0djk3nv = rtB . n5nk0fcdxe - rtB . awofsj5yej
; rtB . dxxqwldjss [ 0 ] = ( rtB . oussmmuoy4 [ 0 ] - rtP .
Gain_Gain_f4udjbnlx2 * rtX . ggygjq5ouq [ 1 ] * rtB . awofsj5yej ) - rtP . Rs
* rtB . its0a3zvwu [ 0 ] ; rtB . dxxqwldjss [ 1 ] = ( rtB . oussmmuoy4 [ 1 ]
- rtB . awofsj5yej * rtX . ggygjq5ouq [ 0 ] ) - rtP . Rs * rtB . its0a3zvwu [
1 ] ; rtB . lrfbty4a0y [ 0 ] = rtP . Gain_Gain_cqbytxvbu0 * rtX . hvulyscokz
[ 1 ] * cvt0djk3nv - rtP . Rr * iaas34rry1 ; rtB . lrfbty4a0y [ 1 ] =
cvt0djk3nv * rtX . hvulyscokz [ 0 ] - rtP . Rr * fgi23zg44a_idx_1 ; if ( rtB
. g50obrftrn >= rtP . wL ) { taskTimeV = rtP . tauL * rtB . agjnm01x4l ; }
else { taskTimeV = rtP . tauL * rtB . agjnm01x4l * rtP . Gain_Gain ; } rtB .
ohojx4cexj = 1.0 / rtP . J * ( rtB . c40hosfmrc - taskTimeV ) ;
UNUSED_PARAMETER ( tid ) ; } void MdlOutputsTID3 ( int_T tid ) { rtB .
kywwenqxru = rtP . Lfr * rtP . Lfs / rtP . Lmt * rtP . Gain5_Gain ; rtB .
czrf0nwdxd = rtP . P1 * rtP . P1 ; rtB . aa0ktk1lsw = rtP . Gain3_Gain * rtP
. P1 ; UNUSED_PARAMETER ( tid ) ; } void MdlUpdate ( int_T tid ) {
UNUSED_PARAMETER ( tid ) ; } void MdlUpdateTID3 ( int_T tid ) {
UNUSED_PARAMETER ( tid ) ; } void MdlDerivatives ( void ) { XDot * _rtXdot ;
_rtXdot = ( ( XDot * ) ssGetdX ( rtS ) ) ; _rtXdot -> kucazwxe1p = rtB .
ohojx4cexj ; _rtXdot -> ggygjq5ouq [ 0 ] = rtB . dxxqwldjss [ 0 ] ; _rtXdot
-> hvulyscokz [ 0 ] = rtB . lrfbty4a0y [ 0 ] ; _rtXdot -> ggygjq5ouq [ 1 ] =
rtB . dxxqwldjss [ 1 ] ; _rtXdot -> hvulyscokz [ 1 ] = rtB . lrfbty4a0y [ 1 ]
; _rtXdot -> cr2w1d1tsl = rtB . g50obrftrn ; } void MdlProjection ( void ) {
} void MdlZeroCrossings ( void ) { ZCV * _rtZCSV ; _rtZCSV = ( ( ZCV * )
ssGetSolverZcSignalVector ( rtS ) ) ; _rtZCSV -> oevrswkldz = rtB .
pzn3ntwo0f - rtP . P1 ; _rtZCSV -> neehjst0we = rtB . lfrpqznzmd - rtP . P1 ;
} void MdlTerminate ( void ) { if ( rt_slioCatalogue ( ) != ( NULL ) ) { void
* * slioCatalogueAddr = rt_slioCatalogueAddr ( ) ; rtwSaveDatasetsToMatFile (
rtwGetPointerFromUniquePtr ( rt_slioCatalogue ( ) ) ,
rt_GetMatSigstreamLoggingFileName ( ) ) ; rtwTerminateSlioCatalogue (
slioCatalogueAddr ) ; * slioCatalogueAddr = NULL ; } } void
MdlInitializeSizes ( void ) { ssSetNumContStates ( rtS , 6 ) ;
ssSetNumPeriodicContStates ( rtS , 0 ) ; ssSetNumY ( rtS , 0 ) ; ssSetNumU (
rtS , 0 ) ; ssSetDirectFeedThrough ( rtS , 0 ) ; ssSetNumSampleTimes ( rtS ,
3 ) ; ssSetNumBlocks ( rtS , 111 ) ; ssSetNumBlockIO ( rtS , 20 ) ;
ssSetNumBlockParams ( rtS , 48037 ) ; } void MdlInitializeSampleTimes ( void
) { ssSetSampleTime ( rtS , 0 , 0.0 ) ; ssSetSampleTime ( rtS , 1 , 0.0 ) ;
ssSetSampleTime ( rtS , 2 , - 2.0 ) ; ssSetOffsetTime ( rtS , 0 , 0.0 ) ;
ssSetOffsetTime ( rtS , 1 , 1.0 ) ; ssSetOffsetTime ( rtS , 2 , 0.0 ) ; }
void raccel_set_checksum ( ) { ssSetChecksumVal ( rtS , 0 , 3900505454U ) ;
ssSetChecksumVal ( rtS , 1 , 3953980274U ) ; ssSetChecksumVal ( rtS , 2 ,
2949447938U ) ; ssSetChecksumVal ( rtS , 3 , 2506987305U ) ; }
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
ModelMotS_dq_V2_InitializeDataMapInfo ( ) ; ssSetIsRapidAcceleratorActive (
rtS , true ) ; ssSetRootSS ( rtS , rtS ) ; ssSetVersion ( rtS ,
SIMSTRUCT_VERSION_LEVEL2 ) ; ssSetModelName ( rtS , "ModelMotS_dq_V2" ) ;
ssSetPath ( rtS , "ModelMotS_dq_V2" ) ; ssSetTStart ( rtS , 0.0 ) ;
ssSetTFinal ( rtS , 12.0 ) ; { static RTWLogInfo rt_DataLoggingInfo ;
rt_DataLoggingInfo . loggingInterval = NULL ; ssSetRTWLogInfo ( rtS , &
rt_DataLoggingInfo ) ; } { { static int_T rt_LoggedStateWidths [ ] = { 1 , 2
, 2 , 1 , 1 } ; static int_T rt_LoggedStateNumDimensions [ ] = { 1 , 1 , 1 ,
1 , 1 } ; static int_T rt_LoggedStateDimensions [ ] = { 1 , 2 , 2 , 1 , 1 } ;
static boolean_T rt_LoggedStateIsVarDims [ ] = { 0 , 0 , 0 , 0 , 0 } ; static
BuiltInDTypeId rt_LoggedStateDataTypeIds [ ] = { SS_DOUBLE , SS_DOUBLE ,
SS_DOUBLE , SS_DOUBLE , SS_DOUBLE } ; static int_T
rt_LoggedStateComplexSignals [ ] = { 0 , 0 , 0 , 0 , 0 } ; static
RTWPreprocessingFcnPtr rt_LoggingStatePreprocessingFcnPtrs [ ] = { ( NULL ) ,
( NULL ) , ( NULL ) , ( NULL ) , ( NULL ) } ; static const char_T *
rt_LoggedStateLabels [ ] = { "CSTATE" , "CSTATE" , "CSTATE" , "CSTATE" ,
"DSTATE" } ; static const char_T * rt_LoggedStateBlockNames [ ] = {
"ModelMotS_dq_V2/Induction Motor - Mechanical part\nRigid Coupling2/Integrator2"
, "ModelMotS_dq_V2/Induction Motor \nElectrical Part\nd,q/Integrator" ,
"ModelMotS_dq_V2/Induction Motor \nElectrical Part\nd,q/Integrator1" ,
"ModelMotS_dq_V2/Induction Motor - Mechanical part\nRigid Coupling2/Integrator1"
, "ModelMotS_dq_V2/UF control _ dqframe/UF control/Unit Delay2" } ; static
const char_T * rt_LoggedStateNames [ ] = { "" , "" , "" , "" , "" } ; static
boolean_T rt_LoggedStateCrossMdlRef [ ] = { 0 , 0 , 0 , 0 , 0 } ; static
RTWLogDataTypeConvert rt_RTWLogDataTypeConvert [ ] = { { 0 , SS_DOUBLE ,
SS_DOUBLE , 0 , 0 , 0 , 1.0 , 0 , 0.0 } , { 0 , SS_DOUBLE , SS_DOUBLE , 0 , 0
, 0 , 1.0 , 0 , 0.0 } , { 0 , SS_DOUBLE , SS_DOUBLE , 0 , 0 , 0 , 1.0 , 0 ,
0.0 } , { 0 , SS_DOUBLE , SS_DOUBLE , 0 , 0 , 0 , 1.0 , 0 , 0.0 } , { 0 ,
SS_DOUBLE , SS_DOUBLE , 0 , 0 , 0 , 1.0 , 0 , 0.0 } } ; static
RTWLogSignalInfo rt_LoggedStateSignalInfo = { 5 , rt_LoggedStateWidths ,
rt_LoggedStateNumDimensions , rt_LoggedStateDimensions ,
rt_LoggedStateIsVarDims , ( NULL ) , ( NULL ) , rt_LoggedStateDataTypeIds ,
rt_LoggedStateComplexSignals , ( NULL ) , rt_LoggingStatePreprocessingFcnPtrs
, { rt_LoggedStateLabels } , ( NULL ) , ( NULL ) , ( NULL ) , {
rt_LoggedStateBlockNames } , { rt_LoggedStateNames } ,
rt_LoggedStateCrossMdlRef , rt_RTWLogDataTypeConvert } ; static void *
rt_LoggedStateSignalPtrs [ 5 ] ; rtliSetLogXSignalPtrs ( ssGetRTWLogInfo (
rtS ) , ( LogSignalPtrsType ) rt_LoggedStateSignalPtrs ) ;
rtliSetLogXSignalInfo ( ssGetRTWLogInfo ( rtS ) , & rt_LoggedStateSignalInfo
) ; rt_LoggedStateSignalPtrs [ 0 ] = ( void * ) & rtX . kucazwxe1p ;
rt_LoggedStateSignalPtrs [ 1 ] = ( void * ) & rtX . ggygjq5ouq [ 0 ] ;
rt_LoggedStateSignalPtrs [ 2 ] = ( void * ) & rtX . hvulyscokz [ 0 ] ;
rt_LoggedStateSignalPtrs [ 3 ] = ( void * ) & rtX . cr2w1d1tsl ;
rt_LoggedStateSignalPtrs [ 4 ] = ( void * ) & rtDW . piiyfoznre ; }
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
real_T absTol [ 6 ] = { 1.0000000000000001E-7 , 1.0000000000000001E-7 ,
1.0000000000000001E-7 , 1.0000000000000001E-7 , 1.0000000000000001E-7 ,
1.0000000000000001E-7 } ; static uint8_T absTolControl [ 6 ] = { 0U , 0U , 0U
, 0U , 0U , 0U } ; static uint8_T zcAttributes [ 3 ] = { ( ZC_EVENT_ALL ) , (
ZC_EVENT_ALL ) , ( 0xc0 | ZC_EVENT_ALL_UP ) } ; static ssNonContDerivSigInfo
nonContDerivSigInfo [ 4 ] = { { 1 * sizeof ( boolean_T ) , ( char * ) ( & rtB
. oleotyrvsj ) , ( NULL ) } , { 1 * sizeof ( boolean_T ) , ( char * ) ( & rtB
. k4xamhzsst ) , ( NULL ) } , { 2 * sizeof ( real_T ) , ( char * ) ( & rtB .
oussmmuoy4 [ 0 ] ) , ( NULL ) } , { 1 * sizeof ( real_T ) , ( char * ) ( &
rtB . awofsj5yej ) , ( NULL ) } } ; ssSetSolverRelTol ( rtS , 0.0001 ) ;
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
zc ) ; } { rtPrevZCX . kl1isclcqj = UNINITIALIZED_ZCSIG ; } ssSetChecksumVal
( rtS , 0 , 3900505454U ) ; ssSetChecksumVal ( rtS , 1 , 3953980274U ) ;
ssSetChecksumVal ( rtS , 2 , 2949447938U ) ; ssSetChecksumVal ( rtS , 3 ,
2506987305U ) ; { static const sysRanDType rtAlwaysEnabled =
SUBSYS_RAN_BC_ENABLE ; static RTWExtModeInfo rt_ExtModeInfo ; static const
sysRanDType * systemRan [ 7 ] ; gblRTWExtModeInfo = & rt_ExtModeInfo ;
ssSetRTWExtModeInfo ( rtS , & rt_ExtModeInfo ) ;
rteiSetSubSystemActiveVectorAddresses ( & rt_ExtModeInfo , systemRan ) ;
systemRan [ 0 ] = & rtAlwaysEnabled ; systemRan [ 1 ] = & rtAlwaysEnabled ;
systemRan [ 2 ] = & rtAlwaysEnabled ; systemRan [ 3 ] = & rtAlwaysEnabled ;
systemRan [ 4 ] = & rtAlwaysEnabled ; systemRan [ 5 ] = ( sysRanDType * ) &
rtDW . hdmj0f2xda ; systemRan [ 6 ] = ( sysRanDType * ) & rtDW . hdmj0f2xda ;
rteiSetModelMappingInfoPtr ( ssGetRTWExtModeInfo ( rtS ) , &
ssGetModelMappingInfo ( rtS ) ) ; rteiSetChecksumsPtr ( ssGetRTWExtModeInfo (
rtS ) , ssGetChecksums ( rtS ) ) ; rteiSetTPtr ( ssGetRTWExtModeInfo ( rtS )
, ssGetTPtr ( rtS ) ) ; } return rtS ; }
#if defined(_MSC_VER)
#pragma optimize( "", on )
#endif
const int_T gblParameterTuningTid = 3 ; void MdlOutputsParameterSampleTime (
int_T tid ) { MdlOutputsTID3 ( tid ) ; }
