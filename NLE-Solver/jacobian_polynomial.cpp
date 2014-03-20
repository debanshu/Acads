#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include "omp.h"

using namespace std;

double h = 0.005; //global constant

struct funct{
    int n; //number of variables
    double* coeff; //coeff of variables
    int* pows;   //power of variables
    double constant; //constant of the function
};
 
typedef struct funct Fun;


/* SEQUENTIAL CODE */
double eval(Fun f,double* vals)
{
    double ans = 0;
    for(int i=0; i< f.n;i++)
        ans += f.coeff[i] * pow(vals[i],f.pows[i]);
    
    return (ans + f.constant);
}

double pDiff(Fun f, double* vals, int k)
{
    double* vals2 = new double[f.n];
    for(int i=0;i<f.n;i++)
        vals2[i] = vals[i];
        
    vals[k] += h;
    vals2[k] -= h;
    
    double ans = ( (eval(f,vals) - eval(f,vals2))/(2*h) );
    
    vals[k] -= h;
    vals2[k] += h;
    
    return ans;
}

double** jacobian_seq(Fun* f,double* vals)
{
    int n = f[0].n;
    double** jac = new double*[n];
    
    for(int i=0;i<n;i++)
    {
        jac[i] = new double[n];
        for(int j=0;j<n;j++)
        {
            jac[i][j] = pDiff(f[i],vals,j);
        }
    }
    
    return jac;
}

/* PARALLEL CODE */
double evalP(Fun f,double* vals)
{
    double ans = 0;
    int n = f.n;
    int i=0;
    #pragma omp parallel for reduction(+:ans)
    for(i=0; i< n;i++)
    {    ans += f.coeff[i] * pow(vals[i],f.pows[i]); }
    
    
    return (ans + f.constant);
}

double pDiffP(Fun f, double* vals, int k)
{
    double* vals2 = new double[f.n];
    
    #pragma omp parallel for
    for(int i=0;i<f.n;i++)
        vals2[i] = vals[i];
        
    vals[k] += h;
    vals2[k] -= h;
    
    double ans = ( (eval(f,vals) - eval(f,vals2))/(2*h) );
    
    vals[k] -= h;
    vals2[k] += h;
    
    return ans;
}

double** jacobian_par(Fun* f,double* vals)
{
    int n = f[0].n;
    double** jac = new double*[n];
    
    #pragma omp parallel for
    for(int i=0;i<n;i++)
        jac[i] = new double[n];
    
    #pragma omp parallel for collapse(2)
    for(int i=0;i<n;i++)
    {
        //jac[i] = new double[n];
        for(int j=0;j<n;j++)
        {
            jac[i][j] = pDiffP(f[i],vals,j);
        }
    }
    
    return jac;
}

int main()
{
    int n;
    scanf("%d",&n);
    
    Fun* f = new Fun[n];
    for(int i=0;i<n;i++)
    {
        f[i].n = n;
        f[i].coeff = new double[n];
        f[i].pows = new int[n];
        
        for(int j=0;j<n;j++)
        {
            scanf("%lf",&f[i].coeff[j]);
            scanf("%d",&f[i].pows[j]);
        }
        
        scanf("%lf",&f[i].constant);
    }
    
    double* vals= new double[n];
    for(int i=0;i<n;i++)
    {
        scanf("%lf",&vals[i]);
    }
    
    double t1 =  omp_get_wtime();    
    double** jac = jacobian_seq(f,vals);  
    double t2 = omp_get_wtime();
    double** jac2 = jacobian_par(f,vals);     
    double t3 = omp_get_wtime();
    
    printf("Sequential Time taken: %lfs",(t2-t1));
    
    /*
    printf("\nJacobian Sequential:\n");
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            printf("%lf ",jac[i][j]);
        }
        printf("\n");
    }
    */
    
    printf("\nParallel Time taken: %lfs\n",(t3-t2));
    
    /*
    printf("\nJacobian Parallel:\n");
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            printf("%lf ",jac2[i][j]);
        }
        printf("\n");
    }
    */
    
    return 0;
}
   
    
