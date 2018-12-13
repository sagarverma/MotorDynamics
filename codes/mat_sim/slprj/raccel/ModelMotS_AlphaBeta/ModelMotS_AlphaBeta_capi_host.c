#include "ModelMotS_AlphaBeta_capi_host.h"
static ModelMotS_AlphaBeta_host_DataMapInfo_T root;
static int initialized = 0;
rtwCAPI_ModelMappingInfo *getRootMappingInfo()
{
    if (initialized == 0) {
        initialized = 1;
        ModelMotS_AlphaBeta_host_InitializeDataMapInfo(&(root), "ModelMotS_AlphaBeta");
    }
    return &root.mmi;
}

rtwCAPI_ModelMappingInfo *mexFunction() {return(getRootMappingInfo());}
