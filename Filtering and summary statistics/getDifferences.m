
%getDifferences
%finds the median of differences between adjacent members in a sequence for each sequence
load cleaned_data
diffs = diff(cleaned_data,1,2);
m=median(diffs,2,'omitnan');
m(m>intmax)= intmax;
m(m<0)= [];
m(m==0)=0.000000001;

h1=histogram(m,(min(m)-1:1000:max(m)+1));

hold on;

m=median(diffs,2,'omitnan');
m(m<intmin)= intmin;
m(m>=0)= [];
m=-m;
h2=histogram(m,(min(m)-1:1000:max(m)+1));

%%c = unique(h.Values);
%set(gca, 'YScale', 'log')
%mlog = log2(h.Values);
%mlog(isinf(mlog))=0;
%clear h
%[n, xout] = hist(m,(min(m)-1:1000:max(m)+1));
%bar(xout, n, 'barwidth', 1, 'basevalue', 1);
set(gca,'YScale','log')
set(gca,'XScale','log')

%bar((min(m)+1000:1000:max(m)+1),mlog);
title('histogram of median difference  series');
ylabel('log(histogram height')
xlabel('log (median value)')
legend('positive median values','negative median values');
saveas(gcf,'difference.png');


