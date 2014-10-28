#include <stdio.h>
double sum(int num){
    return num<=50 ? (1.0/num++)+sum(num) : 0.0;
}
int main(int argc,char *argv[]){
    printf("%d",(int)sum(1));
    return 0;

}
