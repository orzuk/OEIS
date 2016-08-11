function [ percentages ] = getPercentageCubed( epsilon, seqID )
%getPercentageCubed
%epsilon - maximal distance from zero to be considered zero
%finds percentage of numbers that are cubed in each sequence
%negative numbers are not seen as squared numbers
if nargin == 2
	cleaned_data=getSeq(seqID)
else
	load cleaned_data;
end
mat = cleaned_data;
lengths = size(mat,2)-sum(isnan(mat),2)-sum((mat<0),2);
mat(isnan(mat))=3;
mat(mat<0)=3;
p=(mod(mat.^(1/3), 1))<epsilon;
percentages = sum(p,2)./lengths*100;
h = histogram(percentages,(0:1:100));
title('percentage of cubed in series');
xlabel('percentage of cubed');

saveas(gcf,'CubedPercent.png');


end
