#include <stdio.h>
int main() {
	int a,b;
	scanf("%d\n %d", &a, &b);
	
	int b1 = b%10;
	printf("%d\n", a*b1);
	
	int b2 = b%100;
	    b2 = b2/10;
	printf("%d\n", a*b2);
	
	int b3 = b/100;
	printf("%d\n", a*b3);
	
	printf("%d", a*b);
    return 0;
}
