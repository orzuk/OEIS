function [ counts ] = getPrimesPercent( mat )
%UNTITLED6 Summary of this function goes here
%   Detailed explanation goes here

lengths = size(mat,2)-sum(isnan(mat),2)-sum((mat<0),2);
mat(isnan(mat))=4;
mat(mat<0)=4;
load s4;
p = ismember(mat,s4);
percentages = sum(p,2)./lengths*100;
h = histogram(percentages,(0:1:100));
title('percentage of primes in series');
xlabel('percentage of primes');
counts = h.Values;
saveas(gcf,'primePercent.png');


end

