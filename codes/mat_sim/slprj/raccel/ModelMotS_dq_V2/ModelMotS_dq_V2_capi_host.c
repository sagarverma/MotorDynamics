#include "ModelMotS_dq_V2_capi_host.h"
static ModelMotS_dq_V2_host_DataMapInfo_T root;
static int initialized = 0;
rtwCAPI_ModelMappingInfo *getRootMappingInfo()
{
    if (initialized == 0) {
        initialized = 1;
        ModelMotS_dq_V2_host_InitializeDataMapInfo(&(root), "ModelMotS_dq_V2");
    }
    return &root.mmi;
}

rtwCAPI_ModelMappingInfo *mexFunction() {return(getRootMappingInfo());}
