#include <stdio.h>
int main(){
 char alpha[6] = { 'H', 'E', 'L', 'L', 'O', '!'} ;
  char c;
  int i;
  printf("찾고 싶은 문자 : ");
 //여기에 작성
	scanf("%c", &c);
	
	for(int i=0; i<6; i++){
		if(alpha[i]==c){
			printf("%d번째\n", i);
		}
	}
	
	return 0;
}
