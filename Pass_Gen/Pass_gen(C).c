#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int character;
int count = 0;
char avalibale[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                   "abcdefghijklmnopqrstuvwxyz"
                   "0123456789"
                   "!@#$^&*()_+-=[]{}|;:',.<>?/`~";

int ask();
int optionselection(int range, int attempt);
int request();
void passwordgen(int character);
int randomnessofcharacter(int number);
int randomnessofindex(int number, int check[]);
int main()
{
    count = 0;
    srand(time(0));
    printf("nWELCOME\n");
    while (1)
    {
        int z = request();
        if (z)
            break;
    }
}
int request()
{

    printf("Entre NO of Character You want:-->");
    scanf(" %d", &character);

    passwordgen(character);
    return 1;
}
void passwordgen(int character)
{
    int check[character];
    for (int i = 0; i < character; i++)
        check[i] = -1;
    char genrator[character + 1];
    int length = sizeof(avalibale) - 1;
    while (count < character)
    {
        int forallchars = randomnessofcharacter(length);

        int forallindex = randomnessofindex(character, check);

        genrator[forallindex] = avalibale[forallchars];
        check[count] = forallindex;
        count++;
    }
    genrator[character] = '\0';
    printf("%s", genrator);
}
int randomnessofcharacter(int number)
{

    int send = rand() % (number);

    return send;
}
int randomnessofindex(int number, int check[])
{
    int s = 0;
    int send = rand() % (number);

     int unique;
    do {
        send = rand() % number;
        unique = 1;
        for (int i = 0; i < number; i++) {
            if (send == check[i]) {
                unique = 0;
                break;
            }
        }
    } while (!unique);

    return send;
}
