include<stdio.h>
int main(
	int list[]={5,3,8,1,2,7};
	int temp, key, i, j;
	
	for(i=1; i<sizeof(list)/sizeof(int); i++){
		key=list[i];
		for(j=i-1; j>=0 && lsit[j]>key; j--){
			list[s    j+i]>=list[j];
		}
	}
	
	for(i=0;i<sizeof(list)/sizeof(int);i++)
	printf("%d", list[i]);)
	//인서트 정렬 
