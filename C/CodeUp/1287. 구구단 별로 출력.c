#include <stdio.h>
int main() {
	int n;
	int r = 1;
	 
	scanf("%d", &n);
	
	for( int i=1; i<=9; i++){
		r = i * n;
		for(int j=1; j<=r; j++){
		printf("*", r);
	}
	printf("\n");
	}
}
