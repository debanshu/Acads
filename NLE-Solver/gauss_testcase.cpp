#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <ctime>
#include "omp.h"

double fRand(double fMin, double fMax)
{
    double f = (double)rand() / RAND_MAX;
    return fMin + f * (fMax - fMin);
}

int main(int argc,char *argv[])
{
    if(argc<2)
    {
        printf("Usage: generate matrix_size [min_ans_range] [max_ans_range] [min_co-eff_range] [max_co-eff_range]\n Default values for last 4 options are: 0 100 0 10\n");
        return 0;
    }
    
    int n = atoi(argv[1]);
        
    srand(time(NULL));
    double* ans = new double[n];
    
    double ans_min=0,ans_max=100,coeff_min=0,coeff_max=10;
    
    if(argc>2)
        ans_min = atof(argv[2]);
        
    if(argc>3)
        ans_max = atof(argv[3]);
        
    if(argc>4)
        coeff_min = atof(argv[4]);
        
    if(argc>5)
        coeff_max = atof(argv[5]);    
    
    for(int i=0;i<n;i++)
    {
        ans[i]= fRand( ans_min,  ans_max);
    }
    
    double *row = new double[n];
    double sum;
    printf("%d\n",n);
    
    for(int i=0;i<n;i++)
    {
        sum=0;
        for(int j=0;j<n;j++)
        {
            row[j] = fRand( coeff_min,  coeff_max);
            sum = sum+ (ans[j]*row[j]);
            printf("%lf ",row[j]);
        }
        printf("%lf\n",sum);
        
    }
    
    printf("\nAnswers: ");
    for(int i=0;i<n;i++)
        printf("%lf ",ans[i]);
        
    return 0;
    
}
    
    
