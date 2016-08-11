function [  ] = getMedianModulo(seqID)
%getMedianModulo 
%finds modulo of first 10 primes for each number in sequence.
%computes median for each number and then for each seqience for on
%aforementioned median
if nargin == 1
	cleaned_data=getSeq(seqID)
else
	load cleaned_data;
end
[x1,y1]=computeMedianModulo(cleaned_data);
r2 = randn(10000,123);
%hold on;

[x2,y2]=computeMedianModulo(r2);

r3 = min(cleaned_data(:)) + (max(cleaned_data(:))-min(cleaned_data(:)))*rand(10000,1);
[x3,y3]=computeMedianModulo(r3);

xLength = max(length(x1),length(x2));
xLength=max(xLength,length(x3));


dif12 =length(y1)-length(y2);
if dif12>0
    y2=[y2 zeros(dif12,1)];
elseif dif12<0
    y1=[y1 zeros(-dif12,1)];
end

dif23 = length(y3)-length(y2);
if dif23>0
    y2=[y2 zeros(dif,1)];
elseif dif23<0
    y3=[y3 zeros(-dif23,1)];
end

dif13 = length(y3)-length(y1);
if dif13>0
    y1=[y1 zeros(dif,1)];
elseif dif13<0
    y3=[y3 zeros(-dif13,1)];
end
%set(gca,'XTickLabel',{int2str((0:1:xLength-1))})
newX1 = (0:1:xLength-1)';

bar(newX1 ,[y1' y2' y3'])

title('histogram of modulo primes in series');
legend('database data','random data using normal distribution','random data using uniform distribution')
ylabel('percentage of total for each data set');
xlabel('median modulo');

saveas(gcf,'moduloPrimes.png');


end
function [x, y] =computeMedianModulo(mat)
primes10 = [2,3,5,7,11,13,17,19,23,29];
all = zeros(size(mat,1),size(mat,2),10);
for i=1:length(primes10)
   all(:,:,i)=mod(mat,primes10(i)); 
end
medianNumber = median(all,3,'omitnan');
medianSequence = median(medianNumber,2,'omitnan');
h = histogram(medianSequence,(0:1:max(medianSequence)+1));
normalizedHeight = h.Values/sum(h.Values);
x=(0:1:max(medianSequence));
y=normalizedHeight;
%bar((0:1:max(medianSequence)),normalizedHeight)
end

