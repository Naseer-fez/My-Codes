#include <stdlib.h>

char *Day_of_the_year(int *date_arr, int format)
{

    int day = date_arr[1];
    int month = date_arr[2];
    int year = date_arr[3];
    if (day == 0 || month == 0)
    {

        return "No";
    }

    if (month < 3)
    {
        month += 12;
        year -= 1;
    }
    int varaible = (13 * (month + 1)) / 5;
    int yearofthecenturery = year % 100;
    int itgoftheyear = year / 100;

    int date = (day + varaible +
                yearofthecenturery +
                (yearofthecenturery / 4) +
                (itgoftheyear) / 4 - (2 * itgoftheyear)) %
               7;

    int postivemod = (date % 7 + 7) % 7;
    char *weekDays[] = {"Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"};
    return weekDays[postivemod];
}