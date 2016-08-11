%plot different sequences using stem function

load('nondecreasingSeqData.mat')
load('nonincreasingSeqData.mat')

figure()
hold on
title('non decreasing sequence')
stem(nondecreasingMat(1,1:72))
hold off

figure()
hold on
title('non increasing sequence')
stem(nonincreasingMat(1,1:72))
hold off

figure()
hold on
title('other')
stem(cleaned_data(45,1:84))
hold off