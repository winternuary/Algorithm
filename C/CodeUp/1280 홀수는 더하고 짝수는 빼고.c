#include <stdio.h>
int main() {
	int a, b,c=0;
	scanf("%d %d", &a, &b);
	
	for(int i=a; i<=b; i++){
		if(i%2==0){
			printf("-%d", i);
			c= c-i;
		}
		else{
			printf("+%d", i);
			c = c+i;
		}
	}
	printf("=%d", c);
}
