function [ counts ] = getLengths( mat )
%UNTITLED6 Summary of this function goes here
%   Detailed explanation goes here

lengths = size(mat,2)-sum(isnan(mat),2);

h = histogram(lengths,(0:1:max(lengths)+1));
title('histogram of lengths in series');
counts = h.Values;

saveas(gcf,'lengths.png');


end