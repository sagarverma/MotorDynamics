function c = analDCTFB(y,L,K,dcttype)
%oversampled analysis filter bank using modulated filters
%   y : input signal of length N
%   L : filter length (filters based on hanning window)
%   K : number of subbands (default K = L)
%   dcttype : type of DCT (default 4)
%   c : K x (N-L+1) matrix of generated coefficients
%       each line corresponds to a given subband

if nargin <= 3
    dcttype = 4;
end

if nargin <=2
    K = L;
end
if K < L
    error('number of subbands must at least equal to filter length')
end

N = length(y);
if N < L
    error('data size must be larger than filter length');
end

y = y(:);
w = hanning(L);
size(w)

c = zeros(N-L+1,L);
for n = 1:N-L+1
    Y = y(n:n+L-1);
    c(n,:) = w.*Y;
end

c = dct(c',K,'Type',dcttype);

end

