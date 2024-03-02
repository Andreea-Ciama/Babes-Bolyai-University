pkg load statistics;

x=[7, 7, 4, 5, 9, 9 ...
   4, 12, 8, 1, 8, 7 ...
   3, 13, 2, 1, 17, 7 ...
   12, 5, 6, 2, 1, 13 ...
   14, 10, 2, 4, 9, 11 ...
   3, 5, 12, 6, 10, 7]

n=length(x);
sigma = 5;
a=0.01;
miu=9;
[h, p, ci, test]= ztest(x,9,5,'alpha',0.05,'tail','left')

tt=norminv(a)
RR=[-inf, tt]
if h==1
    fprintf('The hipothesis is rejected \n');
else fprintf('The hipothesis is not rejected \n');
endif

fprintf('The p value = %1.2f \n',p);
fprintf('The test statistic = %1.2f \n',test);
fprintf('The RR =(%1.2f,%1.2f) \n', RR);

[h, p, ci, test]=ttest(x, miu, 'alpha', a, 'tail','right');

RR=[tinv(1-a,n-1),inf]
if h==1
    fprintf('The hipothesis is rejected \n');
else fprintf('The hipothesis is not rejected \n');
endif

fprintf('The p value = %1.2f \n',p);
fprintf('The test statistic = %1.2f \n',test.tstat);
fprintf('The RR =(%1.2f,%1.2f) \n', RR);





a=0.05;
x1=[22.4,21.7,24.5,23.4,21.6,23.3,22.4 ,21.6,24.8,20.0]
x2=[17.7,14.8,19.6,19.6,12.1,14.8,15.4,12.6,14.0,12.2]

[h, p, ci, test]=vartest2(x1,x2,'alpha', a, 'tail','both')
n1=length(x1)
n2=length(x2)
tt1=finv(a/2,n1-1,n2-1)
tt2=finv(1-(a/2),n1-1,n2-1)
if h==1
    fprintf('The hipothesis is rejected \n');
else fprintf('The hipothesis is not rejected \n');
endif

fprintf('The p value = %1.2f \n',p);
fprintf('The test statistic = %1.2f \n',test.fstat);

fprintf('RR=(-inf,%1.2f)U(%1.2f,inf)', tt1,tt2)


[h, p, ci, test]=ttest2(x, x2, 'alpha', a, 'tail','right');


t1=tinv(1-a,n1+n2-2)
RR=[t1,inf]
if h==1
    fprintf('The hipothesis is rejected \n');
else fprintf('The hipothesis is not rejected \n');
endif

fprintf('The p value = %1.2f \n',p);
fprintf('The test statistic = %1.2f \n',test.tstat);
fprintf('The RR =(%1.2f,%1.2f) \n', RR);



