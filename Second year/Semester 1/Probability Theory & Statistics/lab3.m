pkg load statistics;



mu = input("mu = ");
sigma = input("sigma = ");

P1 = normcdf(0, mu, sigma);
P2 = 1 - P1;
P3 = normcdf(1, mu, sigma) - normcdf(-1, mu, sigma);
P4 = 1 - P3;

fprintf('P1 = %1.4f\n', P1)
fprintf('P2 = %1.4f\n', P2)
fprintf('P3 = %1.4f\n', P3)
fprintf('P4 = %1.4f\n', P4)
