//
//  main.c
//  Calculator
//
//  Created by Keremsah Kaya on 22/05/2019.
//  Copyright © 2019 Keremsah Kaya. All rights reserved.
//

#include <stdio.h>
#include <math.h>

float add_func(float, float);
float minus_func(float, float);
float mult_func(float, float);
float div_func(float, float);
float mod_func(float, float);
float exp_func(float, float);

int main(void) {
    FILE *ptr_file;
    ptr_file = fopen("cal_find.txt", "w");
    if(!ptr_file)
        printf("file create fail\n");
    
    float op1, op2, result;
    char op;
    int x;
    
    //if (!ptr_file) return 1;
    
    printf("-------------------------------------");
    fprintf(ptr_file, "-------------------------------------");
    printf("Calculator >> Operator: +, -, *, /, %%, ^");
    printf("=====================================\n");

    printf("operand >>");
    scanf("%f", &op1);
    getchar();
    
    
    //while (1) {
    for (x = 1; x <= 3; x++) {
        printf("operator >>");
        scanf("%c", &op);
        getchar();
    
        printf("operand >>");
        scanf("%f", &op2);
        getchar();
        
        switch(op) {
        
            case '+':
                result = add_func(op1, op2);
                break;
            case '-':
                result = minus_func(op1, op2);
                break;
            case '*':
                result = mult_func(op1, op2);
                break;
            case '/':
                result = div_func(op1, op2);
                break;
            case '%':
                result = mod_func(op1, op2);
                break;
            case '^':
                result = exp_func(op1, op2);
                break;
            default:
                result = -1;
                break;
            
        }
        printf("result >> %f\n", result);
        op1 = result;
    }

    fprintf(ptr_file, "calculator output");
    
    fclose(ptr_file);
    
    return 0;
}

float add_func(float op1, float op2) {
    return op1 + op2;
}

float minus_func(float op1, float op2) {
    return op1 - op2;
}

float mult_func(float op1, float op2) {
    return op1 * op2;
}

float div_func(float op1, float op2) {
    return op1 / op2;
}

float mod_func(float op1, float op2) {
    return (int) op1 % (int) op2;
}

float exp_func(float op1, float op2) {
    return pow(op1, op2);
}
