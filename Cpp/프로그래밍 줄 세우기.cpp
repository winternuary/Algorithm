#include <stdio.h>

	void f(int *c, int *d)
	{
		int t;
		t=*c;
		*c=*d;
		*d=t;
	}	


int main(){
	int a,b,c;
	scanf("%d %d %d",&a,&b,&c);
	if(a>b)
		f(&a,&b);
	if(b>c)
		f(&b,&c);
	if(a>b)
		f(&a,&b);
	printf("%d %d %d",a,b,c);
	
	return 0;
}
