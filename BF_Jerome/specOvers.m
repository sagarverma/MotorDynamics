function trnsf=specOvers(a,N,k,k2,M,P)
% oversTrans1D: Computes oversampled transform using matrix M
% rslt=oversTrans1D(a,N,k,k2,W,M,P)
%
% oversTrans1D: 
% 
% Example : 
%
% See also OVERSFILTGEN
%
% Input:        
% Output:       
% Uses:         
% Used in:      
% Comments:     
% Notes:
% Created:      2005/10/12
% Modified:     
%
%   Author: Laurent C. Duval, laurent.duval@ifp.fr
%           Jérôme Gauthier, jerome.gauthier@ifp.fr
%   Institution: IFP, Technology Department
%   (c) All right reserved


aet=zeros(1,length(a)+2*(max(k,P)-1)*N);
aet((max(k,P)-1)*N+1:end-(max(k,P)-1)*N)=a;

trnsf=[];
for iT=1:(length(aet)/N-k+1)
    trnsf=[trnsf (M*aet((iT-1)*N+1:(iT-1)*N+k*N)')];
end


