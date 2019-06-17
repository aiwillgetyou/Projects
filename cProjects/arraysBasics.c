//
//  main.c
//  sizeOfArray-1
//
//  Created by Keremsah Kaya on 29/05/2019.
//  Copyright © 2019 Keremsah Kaya. All rights reserved.
//

#include <stdio.h>

// page 2

double mean(int array[], const int n);

//returning num of elements, sum and mean of an array.
void page2() {
    int arr[] = {1, 2, 3 ,4, 5, 6, 7};
    int num = sizeof(arr) / sizeof(int);
    
    printf("the num of elements are %d\n", num);
    
    double result = mean(arr, num);
    printf("the mean is %f\n", result);
    
}

double mean(int array[],int n) {
    
    double sum = 0;
    int i;
    
    for (i = 0; i< n; i++)
        sum += array[i];
    
    printf("the sum is %f\n", sum);
    
    return sum / n;
}

// return address of each value within array
void page3() {
    double arr[5] = {1, 2, 3, 4, 5};
    //int ptr1, ptr2;
    int i;
    
    
    for (i = 0; i < 5; ++i)
        printf("the %d-th element has address %p and value %f\n", i, &arr[i], arr[i]);
    
}
// return address of each value within array
void page4() {
    double *ptr = NULL;
    double arr[6] = {1, 2, 3, 4, 5, 6};
    ptr = &arr[0];
    int i;
    
    for (i = 0; i < 5; i++)
        printf("pointer %d address = %p and value = %f and arr address is %p\n", i, &ptr[i], arr[i],  &arr[i]);
    
}

//changing m to 10, changing a single value in an array

void page5() {
    
    int m = 7;
    int *ptr = &m;
    *ptr = 10;
    
    printf("value of m is %d address %p and *ptr %d\n", m, ptr, *ptr);
    
}

//calculate the sum of an array
void page6(){
    int arr[9] = {1, 2, 3, 4, 5, 6, 7, 8 ,9};
    int sum = 0;
    int *ptr= arr;
    int i;
    
    
    for(i = 0; i < 9; i++)
        sum += *(ptr+i);
    printf("%d\n", sum);
    
}

int getMax(int arr[], const int n);
int getMin(int arr[], const int n);


// Program to yield the highest and lowest value in an array and getting back its address.
void page7 () {
    int array2[5] = {3, 1, 2, 5 ,4};
    
    int maximum = 0;
    int minimum = 0;
    maximum = getMax(array2, 5);
    minimum = getMin(array2, 5);
    
    printf("max nr is %d\n", maximum);
    printf("min nr is %d\n", minimum);
}

int getMax(int arr[], const int n) {
    int max = -9;
    int i;
    int num = 0;
    
    for (i=0; i<n; i++) {
        num = arr[i];
        if (num > max) {
            max = num;
        }
    }
    
    return max;
}

int getMin(int arr[], const int n) {
    int min = 10;
    int i;
    int num = 0;
    
    for (i=0; i<n; i++) {
        num = arr[i];
        if (num < min) {
            min = num;
        }
    }
    
    return min;
}


int main()
{
    page2();
    return 0;
}

