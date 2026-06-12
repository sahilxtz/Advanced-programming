#include <stdio.h>
#include <stdlib.h>

void constantSpace()
{
    int a = 5, b = 10, c;
    c = a + b;
}

void linearSpace(int n)
{
    int *arr = (int *)malloc(n * sizeof(int));

    for (int i = 0; i < n; i++)
        arr[i] = i;

    free(arr);
}

void quadraticSpace(int n)
{
    int **mat = (int **)malloc(n * sizeof(int *));

    for (int i = 0; i < n; i++)
        mat[i] = (int *)malloc(n * sizeof(int));

    for (int i = 0; i < n; i++)
        free(mat[i]);

    free(mat);
}

int main()
{
    int n;

    printf("Enter input size: ");
    scanf("%d", &n);

    printf("\n--- Space Complexity Analysis ---\n");

    printf("\nO(1) Constant Space Used: %lu bytes",
           (unsigned long)(3 * sizeof(int)));

    printf("\nO(n) Linear Space Used: %lu bytes",
           (unsigned long)(n * sizeof(int)));

    printf("\nO(n^2) Quadratic Space Used: %lu bytes\n",
           (unsigned long)(n * n * sizeof(int)));

    constantSpace();
    linearSpace(n);
    quadraticSpace(n);

    return 0;
}