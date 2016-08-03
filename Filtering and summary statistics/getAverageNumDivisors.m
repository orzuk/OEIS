function [  ] = getAverageNumDivisors(  )
%getAverageNumDivisors
%finds percentage of primes. 
%s4 contains all numbers that are prime in cleaned_data.mat
%negative numbers are not considered prime
load cleaned_data;
mat2 = cleaned_data;
uniqueMat = unique(mat2);
uniqueMat(isnan(uniqueMat))=[];
uniqueMat(uniqueMat<0)=[];
%uniqueMat = int64(uniqueMat);
numDivisors = zeros(size(uniqueMat));
for i=1:length(uniqueMat)
    if uniqueMat(i)<=flintmax
        numDivisors(i)=length(factor(uniqueMat(i)));
    else
        n = sym(num2str(uniqueMat(i)));
        numDivisors(i)=length(factor(n));
    end
    
    
end
forAverage = mat2;
forAverage(forAverage<=0)=0;
forAverage(isnan(forAverage))=0;
[lia,locb]=ismember(forAverage,uniqueMat);
res = numDivisors(locb);
res(mat2<0)=nan;
res(isnan(mat2))=nan;
meanRes = mean(res,2,'omitnan');
histogram(meanRes,(0:1:max(meanRes)+1));

title('average number of divisors in series');
xlabel('average number of divisors');
saveas(gcf,'averageNumDivisors.png');

end

