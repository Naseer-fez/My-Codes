#include <stdio.h>
#include <string.h>
#include <stdlib.h>
char a[100]; // passing elemnt
char *totaltime[] = {
    " 1 = 12 AM - 01 AM ",
    " 2 = 01 AM - 02 AM ",
    " 3 = 02 AM - 03 AM ",
    " 4 = 03 AM - 04 AM ",
    " 5 = 04 AM - 05 AM ",
    " 6 = 05 AM - 06 AM ",
    " 7 = 06 AM - 07 AM ",
    " 8 = 07 AM - 08 AM ",
    " 9 = 08 AM - 09 AM ",
    "10 = 09 AM - 10 AM ",
    "11 = 10 AM - 11 AM ",
    "12 = 11 AM - 12 PM "};
char *printing[] = {
    "12 AM - 01 AM ",
    "01 AM - 02 AM ",
    "02 AM - 03 AM ",
    "03 AM - 04 AM ",
    "04 AM - 05 AM ",
    "05 AM - 06 AM ",
    "06 AM - 07 AM ",
    "07 AM - 08 AM ",
    "08 AM - 09 AM ",
    "09 AM - 10 AM ",
    "10 AM - 11 AM ",
    "11 AM - 12 PM "};
#define size 11
int check[size];
int sicheck[size];
int count = 0;
char realtask[size][100];
int countoftask;
int array[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};

int stilltry(int attempts);
int selection();
void option();
int asking();
void task(char task[]);
void print();
int delete(int attempts);
int change(int attempts);

int main(void)
{

    task(a);
    printf("\nThat is itttttt\n");
    print("The final task list is :\n");
    print();
    return 0;
}
int selection()
{
    int timepass = 3;
    int selection;
    printf("Choose selected time :\n");
    // time slots are ready
    int zero = 0;
    int n = size + 1;
    for (int i = 0; i < n; i++)
    {
        if (array[i] != 0)
        {
            printf("%s\n", totaltime[i]);
            zero++;
        }
    }
    if (zero == 0)
    {
        printf("All Slots are full ");
        return 0;
    }

    printf("\n"); // slection is donr here
    while (timepass != 0)
    {
        printf("Entre the time slot you want:");
        scanf("%d", &selection);
        selection = selection - 1;

        if (selection < 0 || selection >= 12 || array[selection] == 0)
        {
            printf("\nSelected option is invalid or the time slot already exists");
            printf("\n\nPlease enter a valid option\n");
            timepass--;
        }
        else
        {
            check[count] = selection;
            count++;
            array[selection] = 0;
            return selection;
        }
    }
    printf("\nYou have Exauhauted your attempts!!!\n");
    printf("Restart the program!!!!!!!!\n");
    return -1;
}
void option()
{
    int timepass = 3;
    int option;
    int go = 0;
    int tell;
    int new = -1;
    while (timepass != 0)
    { /// fro here

        printf("\n1:Adding the task\n");
        printf("2:Remove the task\n");
        printf("3:Change the time slot\n");
        printf("4:show all the slots");
        printf("::");
        scanf("%d", &option);
        switch (option)
        {
        case 1:
        { // adding task
            task(a);
            // tell=asking();
            go++;

            break;
        }

        case 2:
        {
            // removw task
            delete(2);
            go++;
            break;
        }
        case 3:
        {

            change(3);
            asking();
            go++;
            break;
        }

        case 4:
        {

            print();
            asking();
            go++;
            break;
        }

        default:
        {
            printf("Entre a  valid number ===");
            timepass--;
            new = stilltry(3);
            break;
        }
        }
        if (go != 0)
        {
            break;
        }
    }
    if (new != -1)
    {
        exit(1);
    }
}
int asking()
{
    int timepass = 3;
    char a;
    printf("\n\nDo you want anything else!!!!!");
    printf("\nY/N:");

    while (timepass != 0)
    {
        scanf(" %c", &a);
        if (a == 'Y' || a == 'y')
        {
            option();
        }
        else if (a == 'N' || a == 'n')
        {
            printf("\nThank you so much !");
            return 0;
        }
        else
        {
            printf("\nEntre a valid option::");
            // scanf(" %c", &a);
            timepass--;
        }
        //
    }
    return 1;
}
void task(char task[])
{
    int time;
    int take;
    printf("Entre the task= ");
    scanf("%s", task);
    printf("\n");
    time = selection();
    // we recived the time slot , now time to check it
    if (time != -1)
    {
        sicheck[countoftask] = time;
        // realtask[countoftask][100] = task;
        strcpy(realtask[countoftask], task);
        countoftask++;
    }
    print();

    take = asking();
    if (asking == 0)
    {

        printf("Thank you so much");
    }
}
void print()
{
    int number = 0;
    int n = 0;
    // int a = countoftask;
    for (int i = 0; i < countoftask; i++)
    {
        if (strlen(realtask[i]) > 0)
        {
            // printf("The task is %s and time slot is %s\n", realtask[i], printing[sicheck[i]]);
            printf("(%d) %s  →  %s\n", number + 1, realtask[i], printing[sicheck[i]]);
            n++;
            number++;
        }
    }
    if (n == 0)
    {
        printf("\n\nNO slots are inputed");
    }
}
int delete(int attempts)
{
    // maximum attempts
    if (attempts == 0)
    {

        printf("You have exahauseted your attempts");
        return 0;
    }

    printf("Select the time slot to change :");
    printf("\n");
    for (int i = 0; i < countoftask; i++)
    {
        if (strlen(realtask[i]) > 0)
        {
            // printf("The task is %s and time slot is %s\n", realtask[i], printing[sicheck[i]]);
            printf("(%d) %s  →  %s\n", sicheck[i] + 1, realtask[i], printing[sicheck[i]]);
        }
    }
    int selection;
    printf("::");
    scanf("%d", &selection);
    selection--; // 1,12,11

    if (selection < 0 || selection >= 12 || array[selection] == 1)
    {

        printf("Select a valid slot ::");
        delete(attempts - 1);
    }
    else
    {
        strcpy(realtask[selection], "");
        // array[selection] = 1;
        array[sicheck[selection]] = 1;
        countoftask--;
        printf("The task is removed !!!!!!!");
        asking();
    }
}
int stilltry(int attempts)
{
    char a;
    printf("You still wanna try??\n");
    printf("Y/N");

    int timepass = 3;
    while (timepass != 0)
    {
        scanf(" %c", &a);
        if (a == 'Y' || a == 'y')
        {
            return 1;
        }
        else if (a == 'N' || a == 'n')
        {
            printf("\nThank you so much !! \n have a great day");
            return 0;
        }
        else
        {
            printf("\nEntre a valid option::");
            // scanf(" %c", &a);
            timepass--;
        }
        //
    }
}
int change(int attempts)
{
    if (attempts == 0)
    {
        printf("Attemps are exahauted!!\n");

        return 0;
    }
    print();
    printf("Select the slot you want to change");
    int selectionn;
    printf("\n::");
    scanf("%d", &selectionn);
    selectionn--; // 1,12,11

    if (selectionn < 0 || selectionn >= 12 || array[selectionn] == 1)
    {

        printf("Select a valid slot so  ::\n");
        return change(attempts - 1);
        // option is selected
    }

    char task[100];
    printf("Entre the task= ");
    scanf("%s", task);
    printf("\n");
    strcpy(realtask[selectionn], task);
    array[selectionn] = 1;
    // printf("Entre the time slot");
    selection();
    print();
} // done 30-8-2025