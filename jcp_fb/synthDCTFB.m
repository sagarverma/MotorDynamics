function yr = synthDCTFB(c,L,dcttype)
%   L : filter length (filters based on Hanning window)
%       by default equal to the number of rows of c
%   dcttype : type of DCT (default 4)
%   c : K x (N-L+1) matrix of generated coefficients
%       each line corresponds to a given subband
%   xr : reconstructed signal of length N

if nargin <= 2
    dcttype = 4;
end

if nargin == 1
    L = size(c,1);
end
if size(c,1) < L
    error('number of subbands should be at least equal to filter length')
end


w = hanning(L);

N = size(c,2)+L-1;
c = idct(c,'Type',dcttype);
c = c(1:L,:);

yr = zeros(N,1);
cf = fliplr(c);
for nn = N-L:-1:-L+1
    d = diag(cf,nn);
    if nn >= 0
        ww = w(1:length(d))';
    else
        ww = w(-nn+1:L)';
    end
    yr(N-L+1-nn) = ww*d/norm(ww)^2; 
end

end

