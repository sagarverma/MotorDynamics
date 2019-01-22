function rslt=specOversInv(imSin,N,k,k2,W,P)
% oversInvTrans1D: Computes inverse oversampled transform using matrix W
% rslt=oversInvTrans1D(a,N,k,k2,W,P)
%
% oversInvTrans1D: 
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

% trnsf=imSin.';
% trnsf=trnsf(:);
% 
% trnsf2=[];
% Ml=k2*N;
% for iT=1:(length(trnsf)/(Ml)-P+1)
%     atemp=trnsf(1+(iT-1)*Ml:P*Ml+(iT-1)*Ml);
%     atemp2=fliplr(flipud(reshape(atemp,[Ml,P])));
%     y=zeros(N,1);
%     for jT=1:P
%         y=y+W(:,(jT-1)*Ml+1:Ml+(jT-1)*Ml)*atemp2(:,jT);
%     end
%     trnsf2=[trnsf2 y(end:-1:1)];
% end
% rslt1=conj(transpose(trnsf2(:)));
% 
% if P>k
% rslt=rslt1((P-k)*N+1:end);
% else
% rslt=rslt1(1:end-(k-P)*N);
% end

% trnsf=[];
% for iT=1:(length(aet)/N-k+1)
%     trnsf=[trnsf; transpose(M*aet((iT-1)*N+1:(iT-1)*N+k*N)')];
% end

%trnsf=zeros(1,length(trnsf));
%trnsf(27+48)=1;
%trnsf(46+48)=0;

%trnsf=imSin.';
trnsf=imSin(:);
trnsf2=[];
Mcurt=W;%transpose(W);
Ml=k2*N;
for iT=1:(length(trnsf)/(Ml)-P+1)
    atemp=trnsf(1+(iT-1)*Ml:P*Ml+(iT-1)*Ml);
    atemp2=fliplr(flipud(reshape(atemp,[Ml,P])));
    y=zeros(N,1);
    for jT=1:P
        y=y+Mcurt(:,(jT-1)*Ml+1:Ml+(jT-1)*Ml)*atemp2(:,jT);
    end
    trnsf2=[trnsf2 y(end:-1:1)];
end
%rslt1=real(trnsf2(:))';
rslt1=(trnsf2(:)).';
if P>k
rslt=rslt1((P-k)*N+1:end);
else
rslt=rslt1(1:end-(k-P)*N);
end
%plot(rslt)

