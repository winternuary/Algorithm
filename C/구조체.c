#include <stdio.h>
int main(){

	struct STUDENT{
		int no;
		int inf;
		int mat;
		int sum;
		double avg;
	};
	int n;
	scanf("%d", &n);
	struct STUDENT s[101];
	int i; 
	for(i=0; i<n; i++){
		scanf("%d %d %d", &(s[i].no), &(s[i].inf), &(s[i].mat));
		s[i].sum= s[i].inf + s[i].mat;
		s[i].avg= s[i].sum/2.0;
	}
	
	for(i=1; i<n; i++){
		printf("%d %d %.1f", s[i].no, s[i].sum, s[i].avg);
	}
}

