#include <stdio.h>

int main() {
    int h, m, t;
    scanf("%d %d\n %d", &h, &m, &t);

    m = m + t;

    if (m >= 60) {
        h = h + m / 60;
        m = m % 60;
    }

    if (h >= 24) {
        h = h % 24;
    }

    printf("%d %d", h, m);
    return 0;
}
