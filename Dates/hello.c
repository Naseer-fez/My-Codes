#include <string.h>
#include <ctype.h>

#include <stdio.h>

#define date_size 4
int datevalidater(int *date_arr);
char *datearrangment(char *date, int *date_arr);
int values(char *date, int start, int end);
void less_values(char *real_date, int old_date_len);

char *datearrangment(char *date, int *date_arr)
{
    char *new_date = malloc(9);

    memset(new_date, '0', 8);

    size_t len = strlen(date);
    memcpy(new_date, date, len > 8 ? 8 : len);

    new_date[8] = 0;

    less_values(new_date, len); // Fixed: removed one *

    date_arr[1] = values(new_date, 0, 1);
    date_arr[2] = values(new_date, 2, 3);
    date_arr[3] = values(new_date, 4, 7);

    int input = datevalidater(date_arr);
    if (input == 1)
    {
        return new_date;
    }
    else
    {
        free(new_date);
        return "NO";
    }
}

int datevalidater(int *date_arr)
{

    int day = date_arr[1];
    int month = date_arr[2];
    int year = date_arr[3];
    if (month == 0)
    {
        return 1;
    }
    // if(month>12){

    //     return 0;
    // }
    int valid_date_range = 30 + (month + (month / 8)) % 2;

    if ((month == 2))
    {
        int isLeap = (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
        valid_date_range = isLeap ? 29 : 28;
    }
    if (day >= 0 && day <= valid_date_range)
    {

        return 1;
    }
}

int values(char *date, int start, int end)
{
    int length = end - start + 1;

    char number[length + 1];
    int index = 0;
    for (int i = 0; i < length; i++)
    {

        number[i] = date[i + start];
        index++;
    }
    number[index] = '\0';

    return atoi(number);
}

// The length of the string is wrong here
void less_values(char *real_date, int len)
{

    int max_len = 8;
    if (len <= 4)
    {
        char temp[len];
        strncpy(temp, real_date, len);

        for (int i = 0; i < max_len; i++)
        {
            if (i >= len)
            {

                real_date[i] = temp[i - len];
          
            }
            else
            {
                real_date[i] = '0';
            }
        }

        return;
    }

    if (len == 5)
    {
        for (int i = len; i < max_len; i++)
        {

            real_date[i] = '0';
        }
        
        return;
    }
    if (len == 6)
    {
        char dig4 = real_date[4];
        char dig5 = real_date[5];
        int number = ((dig4 - '0') * 10 + (dig5 - '0'));

        if (number > 12)
        {
            real_date[6] = '0';
            real_date[7] = dig5;
            real_date[4] = '0';
            real_date[5] = dig4;
            return;
        }
        if (number < 10)
        {

            real_date[5] = real_date[4];
            real_date[4] = '0';
            return;
        }
        real_date[6] = '0';
        real_date[7] = '0';
        return;
    }
    real_date[8] = '0';

    return;
}

