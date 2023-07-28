#include <stdio.h>
int main() {
	double start, end;
	scanf("%lf %lf", &start, &end);
	double i;
	for(i=start; i<=end; i+=0.01){
		printf("%.2lf ", i);
	}

	return 0; 
}
