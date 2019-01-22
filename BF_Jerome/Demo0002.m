close all;clear all
% %% Add paths
% addpath('C:\Users\duvall\Documents\MATLAB\work\GAUTHIER-Jerome-COLT-Filter-Fanks-Toolbox\Source\20190000_Filter-banks-1D-Dioniseis');
% %addpath('C:\Users\duvall\Documents\MATLAB\work\GAUTHIER-Jerome-COLT-Filter-Fanks-Toolbox\Source\FB_Inversion\FB_Inversion');
% addpath('C:\Users\duvall\Documents\MATLAB\work\STFT_Inverse\FB_Inversion');

%% Analysis filter bank parameters
N=16; % Channels
k=4; k2=8/4; % Filter fold/Oversampling
length_Filter = N*k;

%% Signal parameters
length_Signal = 512;
data = zeros(length_Signal,1);
data(50:80,1) = sin((50:80)*pi/4).*(hamming(31))';
data = data + 0.05*randn(size(data));
figure(1);

%% Synthesis filter bank parameters
[P,M,W]=oversFiltGen(N,k,k2);
% W2 = W; % No optimization so foar
% W2 = FB_Inv(N,k,k2);

%%
dataAnalysis = specOvers(data,N,k,k2,M,P);

%% Plot data, modulus, real and imaginary spectrograms
figure(1); 
subplot(2,2,1);
plot(data);grid on;axis tight;xlabel('Data')
subplot(2,2,3);
imagesc(abs(dataAnalysis));grid on;axis tight;xlabel('Spectrogram (modulus)')
subplot(2,2,2);
imagesc(real(dataAnalysis));grid on;axis tight;xlabel('Spectrogram (real)')
subplot(2,2,4);
imagesc(imag(dataAnalysis));grid on;axis tight;xlabel('Spectrogram (imaginary)')

%% DO YOUR PROCESSING HERE
%% JCP PROCESSING

dataAnalysisSynthesis1raw = specOversInv(dataAnalysis,N,k,k2,W,P);
% dataAnalysisSynthesis2raw = specOversInv(dataAnalysis,N,k,k2,W2,P);

length_Final = min (length(dataAnalysisSynthesis1raw),length_Signal);

dataAnalysisSynthesis1 = real(dataAnalysisSynthesis1raw(1:length_Final))';
% dataAnalysisSynthesis2 = real(dataAnalysisSynthesis2raw(1:length_Final))';

% figure(1); 
% subplot(2,2,1);
% plot([data,dataAnalysisSynthesis1]);grid on;axis tight;xlabel('Data: original and recovered FB1')
% subplot(2,2,3);
% plot([data,dataAnalysisSynthesis2]);grid on;axis tight;xlabel('Data: original and recovered FB2')
% subplot(2,2,2);
% plot([data-dataAnalysisSynthesis1]);grid on;axis tight;xlabel('Error: original and recovered FB1')
% subplot(2,2,4);
% plot([data-dataAnalysisSynthesis2]);grid on;axis tight;xlabel('Error: original and recovered FB2')

figure(2); 
subplot(1,2,1);
plot([data,dataAnalysisSynthesis1]);grid on;axis tight;xlabel('Data: original and recovered FB1')
subplot(1,2,2);
plot([data-dataAnalysisSynthesis1]);grid on;axis tight;xlabel('Error: original minus recovered FB1')

