#include<stdio.h>

void insertion_sort(int list[], int first, int last, int gap) {
    int i, j, key;
    for (i = first + gap; i <= last; i = i + gap) {
        key = list[i];
        j = i - gap;
        while (j >= first && list[j] > key) {
            list[j + gap] = list[j];
            j = j - gap;
        }
        list[j + gap] = key;
    }
}

int main() {
    int list[] = {10, 8, 6, 20, 4, 3, 22, 1, 0, 15, 16};
    int temp, key, i, j, n, gap;
    n = sizeof(list) / sizeof(int);

    for (gap = n / 2; gap > 0; gap = gap / 2) {
        if ((gap % 2 == 0))
            gap++;
        for (i = 0; i < gap; i++)
            insertion_sort(list, i, n - 1, gap);
    }

    for (i = 0; i < sizeof(list) / sizeof(int); i++)
        printf("%d ", list[i]);
        
    return 0;
}
