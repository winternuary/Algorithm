#include<stdio.h>
 
int main(){
    
    int a,b,c,d,result;
    scanf("%d %d %d %d",&a, &b, &c, &d);
    result = a;
    
    for(int i=2; i<=d; i++){
        result = result*b + c;
        
    }
    printf("%d",result);
    return 0;
    
}

