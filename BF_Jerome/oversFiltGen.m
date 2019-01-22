function [P,M,W]=oversFiltGen(N,k,k2)
% oversFiltGen: Computes matrices M and W for oversampled transforms
% [P,M,W]=oversFiltGen(N,k,k2)
%
% oversFiltGen: 
% 
% Example : 
%
% See also OVERSTRANS1D
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


[Y,X]=meshgrid(1:N*k,1:N*k2);

%disp('Hamming window');
%ha=(hamming(k*N))';
%ha=ones(1,N*k);

disp('Classical sin window');
ha=(sin((1:N*k)*pi/(N*k+1)));

%ha=(normImg(atan([1:N*k]).*atan([N*k:-1:1]))+.05)/1.05;
HA=repmat(ha,[k2*N,1]);
M=1/sqrt(k*k2*N)*exp(-i*(X-N*k2/2-1/2).*(Y-N*k/2-1/2)*2*pi/(k2*N)).*HA;
%M=1/sqrt(k*k2*N)*exp(-i*(X-N*k2/2).*(Y-N*k/2)*2*pi/(k2*N)).*HA;
P=1;
testarret=1;
while testarret>1E-12
P=P+1;
%P=k;
Me=zeros(k2*N*P,N*(k+P-1));
for iT=1:P
    Me((iT-1)*k2*N+1:iT*k2*N,(iT-1)*N+1:(iT-1)*N+k*N)=M;
end
%imagesc(angle(Me))

U=[zeros(N,(P-1)*N) eye(N) zeros(N,(k-1)*N)]';
%Wt=linsolve(transpose(Me),U);
%Wt=pinv(transpose(Me))*U;
Wt=transpose(Me)\U;
W=transpose(Wt);
imagesc(angle(Wt))
testarret=abs(max(max(transpose(Me)*Wt-U)));
display(P);
end
