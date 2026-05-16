#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define Totalgrids 15

int winnercheck;
int matrix[Totalgrids];

void display();
int grids();
int choices(int choice);
int takingvalue(int attempts);
int counter();
int ask();
int sucess();
int minesweeper(int choice);
int main()
{
    srand(time(0));
    display();
    counter();
    int count=0;
   
/*  for (int i = 0; i < Totalgrids; i++)
  {
    if(matrix[i]==2)printf("%d->",i+1);
  }*/
  
  

    while (1)
    {

        int k = grids();

        if (!k)
        {
            printf("\nTHE ENDDDDDDDDDDD!!!!!!\n");
            break;
        }
    }
    printf("THANK YOU");
}
void display()
{
    printf("\n");
    for (int i = 0; i < Totalgrids; i++)
    {
        printf("  O  ");
        if ((i + 1) % 10 == 0)
        {
            printf("\n");
        }
    }
    printf("\n");
}
int choices(int choice)
{
    if (choice < 0)
    {
        printf("Sorry DO you wanna Try again\n");
        int reask = ask();
        if (reask == 0)
        {
            // printf("THank you\n");
            return 0;
        }
        else
        {
            for (int i = 0; i < Totalgrids; i++)
            {
                matrix[i] = 0;
            }
            counter();
            // display();
            return 1;
        }
    }
}
int grids()
{

    int choice = takingvalue(3);
    if (choice == -9)
    {

        // printf("You have been mine sweeped");

        return 0;
    }
    else if(choice==-69){
     //   printf("\nYOU HAVE BEEN MINEDDDDDDDDDD!!!!!!!!\n");
      //  minesweeper(choice);
        return 0;
    }

    int toknow = choices(choice);
    if (toknow == 1)
    {
        //  display();
    }
    else if (toknow == -1)
    {
        return 0;
    }
    int sending = minesweeper(choice);
    if (sending == -1)
    {
        printf("\nGAME OVERRRRRRRR\n");
        choices(3);
        return 0;
    }
    else
    {
        int ithink = Totalgrids - ((Totalgrids) / 5);
        sucess();
        winnercheck++;
        if (winnercheck == ithink)
        {
            printf("\nYOU ARE THE WINNERRRRRRRRRR!!!!!!!!!!!!!");
            return 0;
        }
       // grids();
    }
}
int takingvalue(int attempts)
{
    int choice;
    int i = 1;
    do
    {
        printf("\nEntre the number you want to swipe(1-%d)->", Totalgrids);
        scanf("%d", &choice);
        if (choice < 1 || choice > Totalgrids)
        {
            printf("Invalid choice !!\n");
            attempts--;
        }
        else if (matrix[choice - 1] == 1)
        {
            printf("The selection is already done!!\nTRy again\n");
            attempts--;
        }
        else if (matrix[choice - 1] == 0)
        {
            matrix[choice - 1] = 1;
            break;
        }
        else if (matrix[choice - 1] == 2)
        {
              minesweeper(choice - 1);
            return -69;
        }

    } while (attempts != 0);
    if (attempts == 0)
    {
        printf("YOU have exhausted your attempts\n");
        return -9;
    }
    else
    {
        // sucess();
        return choice - 1;
    }
}
int counter()
{ // int k=24;
   int k = (Totalgrids) / 5;
int count=0;
    for (int i = 0; i < k; i++)
    {
        int randomNumber = rand() % Totalgrids;
        
        if (matrix[randomNumber] != 2)
        {
            matrix[randomNumber] = 2;
            count++;
        }
        else
        {
            i--;
        }
    }
    printf("\nTHeir are %d Mines\n",count);
    printf("Be Careful\n");
}
int ask()
{
    int timepass = 3;
    char a;
    //
    printf("\nY/N:");

    while (timepass != 0)
    {
        scanf(" %c", &a);
        if (a == 'Y' || a == 'y')
        {
            timepass = 0;

            return 1;
            break;
        }
        else if (a == 'N' || a == 'n')
        {
            printf("\nThank you so much !\n");

            timepass = 0;
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
    return 0;
}
int minesweeper(int choice)
{

    if (matrix[choice] == 2)
    {
        printf("YOU HAVE BEEN MINE SWEEPEDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD!!!!!!\n");
        for (int i = 0; i < Totalgrids; i++)
        {
            if (matrix[i] == 2)
                printf("  *  ");
            else if (matrix[i] == 1)
                printf("  X  ");
            else
                printf("  O  ");

            if ((i + 1) % 10 == 0)
                printf("\n");
        }

        return -1;
    }
    else
    {
        return 1;
    }
}
int sucess()
{
    int k = 0;
    // printf("THis is printing her e\n");

    for (int i = 0; i < Totalgrids; i++)
    {

        if (matrix[i] == 1)
        {
            printf("  X  ");
        }
        else if (!matrix[i])
        {
            printf("  O  ");
        }
        else if (matrix[i] == 2)
            printf("  O  ");

        if ((i + 1) % 10 == 0)
            printf("\n");
    }

} // 6-9-2025