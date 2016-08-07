function [lengths]=getLengths(seqID)
%getLengths
%gets lengths of each sequence
if nargin == 1
	cleaned_data=getSeq(seqID)
else
	load cleaned_data;
end
lengths = size(cleaned_data,2)-sum(isnan(cleaned_data),2);

h = histogram(lengths,(0:1:max(lengths)+1));
title('histogram of lengths in series');
counts = h.Values;
xlabel('length');
ylabel('amount of sequences');
saveas(gcf,'lengths.png');



