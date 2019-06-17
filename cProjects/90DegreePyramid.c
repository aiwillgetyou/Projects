//
//  main.c
//  practice #3
//
//  Created by Keremsah Kaya on 15/05/2019.
//  Copyright © 2019 Keremsah Kaya. All rights reserved.
//

#include <stdio.h>

int comp(int n);

int main() {
    int n;
    printf("enter number\n");
    scanf("%d", &n);
    
    comp(n);
    return 0;
}


int comp(int n) {
    int i;
    int j;
    
    for (i = 0; i <= n; i++) {
        for (j = 1; j <= i; j++) {
            printf("%d ", j);
        }
        printf("\n");
    }
    
    for (i = 0; i < n; i++){
        for (j=1; j <= (n-i); j++)
        {
            printf ("%d ", j);
        }
        printf ("\n");
    }
    return 0;
}
