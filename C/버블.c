#include <stdio.h>
int main() {
	int list[]={5,3,8,1,2,7};
	int temp;
	
	for(int i=sizeof(list)/sizeof(int)-1; i>0; i--)
		for(int j=0; j<i; j++)
		{
			if(list[j]>list[j+1])
			{
				temp=list[j];
				list[j]=list[j+1];
				list[j+1]=temp;
			}
		}
    for (int i = 0; i < sizeof(list) / sizeof(int); i++) {
        printf("%d ", list[i]);
    }	
}
