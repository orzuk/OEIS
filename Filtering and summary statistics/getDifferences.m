function [  ] = getDifferences( mat )
%UNTITLED6 Summary of this function goes here
%   Detailed explanation goes here

diffs = diff(mat,1,2);
m=median(diffs,2,'omitnan');
m(m>intmax)= intmax;
m(m<intmin)= intmin;

histogram(m,(min(m):100:max(m)+1));


title('histogram of median difference  series');
saveas(gcf,'difference.png');


end

