#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include "omp.h"

using namespace std;

void printMatrix(double **a,int n)
{
    for(int j=0;j<n;j++)
    {   
        for(int i=0;i<(n+1);i++)
            printf("%lf ",a[j][i]);
        printf("\n");
    }
}

double* gauss_elim_seq(double** a,int n)
{
    double pvt; 
    int temp;
    
    //elimination
    for(int j=0;j<(n-1);j++)
    {
        //pivoting
        pvt = abs(a[j][j]);
        temp = j;
        
        //find pivot row
        for(int i = j+1;i<n;i++)
        {
            if( abs(a[i][j]) > pvt)
            {
                pvt = abs(a[i][j]);
                temp = i;
            }
        }
        double* tmp;
        //switch pivot rows
        if( j!= temp)
            {
                tmp = a[j];
                a[j] = a[temp];
                a[temp] = tmp;
            }
            
        for(int i=j+1; i<n; i++)
        {
            //store multiplier
            a[i][j] = a[i][j]/a[j][j];
            
            for(int k = j+1; k<(n+1); k++)
                a[i][k] = a[i][k] - a[i][j]*a[j][k];
                
        }
        
    }
    
    //back-substitution
    double *x=new double[n];
    //x[n-1] = a[n-1][n]/a[n-1][n-1];
    
    for(int j=(n-1);j>-1;j--)
    {
        x[j] = a[j][n];
        for(int k= (n-1); k>j; k--)
            x[j] = x[j] - x[k]*a[j][k];
        x[j] = x[j]/a[j][j];
        
    }
    
    return x;
    
}


double* gauss_elim_par(double** a,int n)
{
    double pvt; 
    int temp;
    
    //elimination
    for(int j=0;j<(n-1);j++)
    {
        //pivoting
        pvt = abs(a[j][j]);
        temp = j;
        
        //find pivot row
        for(int i = j+1;i<n;i++)
        {
            if( abs(a[i][j]) > pvt)
            {
                pvt = abs(a[i][j]);
                temp = i;
            }
        }
        double* tmp;
        //switch pivot rows
        if( j!= temp)
            {
                tmp = a[j];
                a[j] = a[temp];
                a[temp] = tmp;
            }
        
        #pragma omp parallel for
        for(int i=j+1; i<n; i++)
        {   
            //store multiplier
            a[i][j] = a[i][j]/a[j][j];
        }
        
        #pragma omp parallel for collapse(2)        
        for(int i=j+1; i<n; i++)
        {    
            for(int k = j+1; k<(n+1); k++)
                a[i][k] = a[i][k] - a[i][j]*a[j][k];
                
        }
        
    }
    
    //back-substitution
    double *x=new double[n];
    //x[n-1] = a[n-1][n]/a[n-1][n-1];
    
    for(int j=(n-1);j>-1;j--)
    {
        x[j] = a[j][n];
        for(int k= (n-1); k>j; k--)
            x[j] = x[j] - x[k]*a[j][k];
        x[j] = x[j]/a[j][j];
        
    }
    
    return x;
    
}

int main()
{
    int n;
    scanf("%d",&n);
    double** a = new double*[n];
    double** b = new double*[n];
    bool f= true;
    
    for(int i=0;i<n;i++)
    {
        a[i]= new double[n+1];
        b[i]= new double[n+1];
        for(int j=0; j <n+1; j++)
            { scanf("%lf",&a[i][j]); b[i][j] = a[i][j]; }
            
    }
    
    //timing sequential code
    double t1 =  omp_get_wtime();    
    double *ans = gauss_elim_seq(a,n);    
    double t2 = omp_get_wtime();
    double *ans2 = gauss_elim_par(b,n);    
    double t3 = omp_get_wtime();
    
    printf("Sequential Time taken: %lfs",(t2-t1));
    
    /*for(int i=0;i<n;i++)
        printf("%lf ",ans[i]); */
        
    printf("\nParallel Time taken: %lfs\n",(t3-t2));
    
    /* for(int i=0;i<n;i++)
        printf("%lf ",ans2[i]);*/
        
    /*
    for(int i=0;i<n;i++)
    {
        if( ans[i]!=ans2[i])
            {   f=false; printf("%lf %lf\n",ans[i],ans2[i]); break; }
    }
    
    
    if(f)
        printf("\nAnswers Match!");
    else
        {
        printf("Answers DON'T Match! Printing both solved matrices for errors:\nSequential Matrix: \n");
        //printMatrix(a,n);
        printf("\nParallel Matrix: \n");
        //printMatrix(b,n);
        }
        */
        
        
    return 0;
    
}
    