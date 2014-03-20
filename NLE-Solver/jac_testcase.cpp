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

int Rand(int Min, int Max)
{
    return (Min + (rand()%(Max - Min)));
}

int main(int argc,char *argv[])
{
    if(argc<2)
    {
        printf("Usage: jac_generate matrix_size [min_ans_range] [max_ans_range] [min_co-eff_range] [max_co-eff_range] [min_power_range] [max_power_range]\n Default values for last 6 options are: -10 10 0 10 0 5\n");
        return 0;
    }
    
    int n = atoi(argv[1]);
        
    srand(time(NULL));
    int* ans = new int[n];
    
    int ans_min=-10,ans_max=10,coeff_min=0,coeff_max=10,power_min=0,power_max=5;
    
    if(argc>2)
        ans_min = atoi(argv[2]);
        
    if(argc>3)
        ans_max = atoi(argv[3]);
        
    if(argc>4)
        coeff_min = atoi(argv[4]);
        
    if(argc>5)
        coeff_max = atoi(argv[5]); 

    if(argc>6)
        power_min = atoi(argv[6]);
        
    if(argc>7)
        power_max = atoi(argv[7]);
    
    for(int i=0;i<n;i++)
    {
        ans[i]= Rand( ans_min,  ans_max);
    }
    
    int *row = new int[n];
    int *row2 = new int[n];
    long sum;
    printf("%d\n",n);
    
    for(int i=0;i<n;i++)
    {
        sum=0;
        for(int j=0;j<n;j++)
        {
            row[j] = Rand( coeff_min,  coeff_max);
            row2[j] = Rand( power_min,  power_max);
            sum = sum+ (row[j] * (long)(pow(ans[j],row2[j])));
            printf("%d ",row[j]);
            printf("%d ",row2[j]);
        }
        printf("%ld\n",-sum);
        
    }
    
    printf("\nAnswers: ");
    for(int i=0;i<n;i++)
        printf("%d ",ans[i]);
        
    return 0;
    
}
    
    
