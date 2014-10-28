#include <stdio.h>
int main(int argc,char *argv[])
{
    unsigned short int result[29999]={0};
    int now=0, i, j, carry=0;
    int FIN,sum=0;

    printf("enter an integer : ");
    scanf("%d", &FIN);
    result[0]=1;
    for (i=0; i < FIN; i++)
    {
        for (j=0; j < now; j++)
        {
            result[j] *= 2;
            if (carry)
            {
                result[j]++;
                carry=0;
            }
            if (result[j] > 999)
            {
                result[j]-=1000;
                carry=1;
            }
        }
        result[now] *= 2;
        if (carry) result[now]++;
        if (result[now] > 999)
        {
            result[now]-=1000;
            result[now+1]++;
            now++;
        }
        carry=0;
    }

    printf("2 ^ %d = ", FIN);
    if (now)
    {
        printf("%d,", result[now]);
        for (i=now-1; i > 0; i--) printf("%03d,", result[i]);
        printf("%03d : ", result[0]);
    }
    else printf("%d : ", result[0]);

    carry = (now+1)*3;
    if (result[now] < 100) carry--;
    if (result[now] < 10) carry--;
    printf("%d digits\n", carry);
    for(i=0;i<29999;i++)
    {
        sum+=result[i]/1000;
        result[i]%=1000;
        sum+=result[i]/100;
        result[i]%=100;
        sum+=result[i]/10;
        result[i]%=10;
        sum+=result[i]/1;
    }
    printf("2 ^ %d = ", FIN);
    printf("2의 %d승의 각자릿수의 합은 %d입니다.\n", FIN, sum);
    return 0;
}
