#include <stdio.h>
int main()
{
	int n;  
	scanf("%d", &n);//Ãþ ¼ö ÀÔ·Â¹Þ±â 
	for(int i=1; i<=n; i++)
	{
		for(int k=n-i; k>0; k--)
		printf(" ");
		for(int j=1; j<=i*2-1; j=j+1)
		{
			printf("*");
		}
		printf("\n");
	}
	
	

	return 0;
}
