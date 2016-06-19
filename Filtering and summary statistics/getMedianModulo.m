function [  ] = getMedianModulo( mat )
%getMedianModulo 
%finds modulo of first 10 primes for each number in sequence.
%computes median for each number and then for each seqience for on
%aforementioned median
primes10 = [2,3,5,7,11,13,17,19,23,29];
all = zeros(size(mat,1),size(mat,2),10);
for i=1:length(primes10)
   all(:,:,i)=mod(mat,primes10(i)); 
end
medianNUmber = median(all,3,'omitnan');
medianSequence = median(medianNUmber,2,'omitnan');
h = histogram(medianSequence,(0:1:max(medianSequence)+1));
title('histogram of modulo primes in series');

saveas(gcf,'moduloPrimes.png');


end

