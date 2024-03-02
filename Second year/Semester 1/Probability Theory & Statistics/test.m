pkg load statistics;

steel = [4.6, 0.7, 4.2, 1.9, 4.8, 6.1, 4.7, 5.5, 5.4];
glass = [2.5, 1.3, 2.0, 1.8, 2.7, 3.2, 3.0, 3.5, 3.4];



%a. At the 1% significance level,
%do the population variances seem to differ?
fprintf('a) \n')
alpha=0.01

[h,p,ci,stats]=vartest2(steel,glass, 'alpha',alpha,'tail','left')

n1=length(steel)
n2=length(glass)
tt1=finv(alpha/2,n1-1,n2-1)
tt2=finv(1-(alpha/2),n1-1,n2-1)

if h == 0
    fprintf('R: Variances do not differ at %g significance level\n', alpha);
else
    fprintf('R: Variances differ at %g significance level\n', alpha);
end

fprintf('The test statistic = %1.2f \n',stats.fstat);
fprintf('RR=(-inf,%1.2f)U(%1.2f,inf) \n', tt1,tt2)

%b. Find a 99% confidence interval for the difference
%of the average heat losses
fprintf('b) \n')
alpha = 0.01;
critical_value = tinv(1-alpha/2, length(steel)-1);
[h,p,ci,stats] = ttest2(steel, glass, 'alpha',alpha,'tail','left')
t1=tinv(1-alpha,n1+n2-2)
RR=[t1,inf]

fprintf('The test statistic = %1.2f \n',stats.tstat);
fprintf('The RR =(%1.2f,%1.2f) \n', RR);

fprintf('R: 99%% Confidence interval for the difference of the average assembling time is [%.3f, %.3f]\n', ci(1), ci(2));

