function [ counts ] = getLengths( mat )
%getLengths
%gets lengths of each sequence

lengths = size(mat,2)-sum(isnan(mat),2);

h = histogram(lengths,(0:1:max(lengths)+1));
title('histogram of lengths in series');
counts = h.Values;

saveas(gcf,'lengths.png');


end
