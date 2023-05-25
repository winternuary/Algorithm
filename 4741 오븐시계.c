#include<stdio.h>
int main(){
	int h,m,c;
	int d;
	scanf("%d %d", &h, &m);
	scanf("%d", &c);
	m+=c;
	if(m>59){
		d = m / 60;
		m = m % 60;
		h += d;
	if(h>23)
	{
		h=h%24;
	}
	}
		printf("%d %d", h,m);
	}
