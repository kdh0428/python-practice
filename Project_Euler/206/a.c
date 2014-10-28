#define U 10203040506070809
#define A  1000000000000000
#define B    10000000000000
#define C      100000000000
#define V        9090909090

#include <math.h>
#include <stdlib.h>

int main() {
  int a,b,c,i;
  long long u,m,mm;

  for(a=0;a<10;a++)
  for(b=0;b<10;b++)
  for(c=0;c<10;c++) {
    u=U+a*A+b*B+c*C;
    m=sqrt(u); m+=(m%2==0);
    for(;(mm=m*m)<u+V;m+=2){
      for(i=9;i>=3;i--)
        if(mm%10!=i) break;
        else mm/=100;
      if(i==2) printf("%i\n",10*m);
    }
  }
}
