#include<stdio.h>
int main(){
    
    int n,a=1;
    scanf("%d", &n);
    
    for(int i=n; i>=1; i--){
		a*=i;
	}
	printf("%d",a);
    return 0;
}
