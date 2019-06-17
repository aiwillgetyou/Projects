//
//  main.c
//  practice #2-2
//
//  Created by Keremsah Kaya on 15/05/2019.
//  Copyright © 2019 Keremsah Kaya. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void comp(int r, int x);

int main(void) {
    int r;
    r = rand() % 101;
    int x;
    
    int count;
    count = 0;
    printf("guess the number between 1 and 100\n");
    
    while (count < 6) {
    
        scanf("%d", &x);
        comp(r, x);
        
        count++;
    
    }
    return 0;
}

void comp(int r, int x) {
    
    if (x < r) {
        printf("higher than %d\n", x);
    }
    else if (x > r) {
        printf("smaller than %d\n", x);
    } else if (x == r) {
        printf("Yes, right");
    }
}
