#include <stdio.h>

int main() {
    int list[] = {5, 3, 8, 1, 2, 7};
    int temp, index, i, j;
    
    for (i = 0; i < sizeof(list) / sizeof(int) - 1; i++) {
        index = i;
        for (j = i + 1; j < sizeof(list) / sizeof(int); j++) {
            if (list[index] > list[j]) {
                index = j;
            }
        }
        temp = list[index];
        list[index] = list[i];
        list[i] = temp;
    }
    
    for (i = 0; i < sizeof(list) / sizeof(int); i++) {
        printf("%d ", list[i]);
    }
    
    return 0;
}
//선택정렬 
