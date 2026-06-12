#include<stdio.h> 
#include<time.h> 
#include<stdlib.h> 
 
int linear(int a[],int n,int x) 
{ 
    int i; 
    for(i=0;i<n;i++) 
    { 
        if(a[i]==x) 
        { 
            printf("found"); 
            return 1; 
        } 
    } 
    return 0; 
} 
 
int selection_sort(int a[],int n) 
{ 
    int i,j,min; 
 
    for(i=0;i<n-1;i++) 
    { 
        min = i; 
        for(j=i+1;j<n;j++) 
        { 
            if(a[j]<a[min]) 
            { 
                min = j; 
            } 
        } 
        int temp = a[i]; 
        a[i] = a[min]; 
        a[min] = temp; 
 
    } 
    return 1; 
} 
 
// constant time complexity 
 
int getfirst(int a[]) 
{ 
    return a[0]; 
} 
 
int main() 
{ 
 
clock_t start,end; 
int n,i,m; 
double c_time; 
printf("Input\nEnter size of array : "); 
scanf("%d",&n); 
int a[n]; 
printf("here automatically stores values in array ."); 
for(i = 0;i<n;i++) 
{ 
} 
a[i]=n-i; 
int x; 
printf("\nEnter value of x to be search : "); 
scanf("%d",&x); 
/*linear search performed */ 
start = clock(); 
linear(a,n,x); 
end = clock(); 
c_time = ((double)(end-start))/CLOCKS_PER_SEC; 
printf("Output\nTime taken by linear search O(n): %lf\n",c_time); 
/* array gets sorted */ 
start = clock(); 
selection_sort(a,n); 
end = clock(); 
c_time = ((double)(end-start))/CLOCKS_PER_SEC; 
printf("Time taken by selection sort O(n^2): %lf\n",c_time); 
/* Array is now sorted, 1st element get returned */ 
start = clock(); 
m=getfirst(a); 
end = clock(); 
c_time = ((double)(end-start))/CLOCKS_PER_SEC; 
printf("Time taken by constant O(1) : %lf\n\n",c_time); 
return 0; 
}