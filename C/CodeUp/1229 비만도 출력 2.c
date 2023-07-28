#include <stdio.h>
int main() {
	double h, w;
	scanf("%lf %lf", &h, &w);
	
	double ratio, result;
	if(h<150){
		ratio = h - 100;
	}
	else if(h<160){
		ratio = (h - 150)/2 + 50;
	} 
	else{
		ratio = (h - 100)*0.9;
	}
	
		result = (w - ratio)*100 / ratio;
		
	if(result<=10){
		printf("정상");
	}
	else if(result<=20){
		printf("과체중");
	}
	else{
		printf("비만");
	}
	return 0; 
}
