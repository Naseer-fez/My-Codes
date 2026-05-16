#include <stdio.h>
#include <string.h>
// #define quantity 2
#define quantity 20
#define totaltabels 10
int zap = 0;
int tableno[10];       // will take tabel data
int tabelspecific = 0; // will look for the tabel filing
int array[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int tableprice[totaltabels];
int leave = totaltabels;
// tabel is free or not
// first is tabel .second is order items
int tabelorder[10][quantity]; // will take the order and the wht iteams have been order
typedef struct items
{
    int id;
    char menu[50];
    float prices;
} items; // id , s menu,f prices
void swap(int *a, int *b)
{ // chatgpted it
    int t = *a;
    *a = *b;
    *b = t;
}
void sort(int n, int arr[], int arr2[])
{
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                swap(&arr[j], &arr[j + 1]);
                swap(&arr2[j], &arr2[j + 1]); // keep second array in sync
            }
        }
    }
}

int menutake(int tabel, items iteam[]);
int tabeldata(int tabel, items take[], int attempt);
void allitems(items all[], int tabel);
int takeorder(items all[], int tabel, int attempt);
int orderdetails(items task[], int order[], int orderquantity[], int tabel, int count);
int overallprice(items task[], int orderquantity[]);
void finalreport(items take[]);
int ask();

int main()
{ // tems take[quantity];
    // items take[quantity] = {{1, "pizza", 12.0}, {2, "BUrger", 13}};
    //  after menutake
    //  menutake(quantity,take);
    items take[quantity] = {
        {1, "Biryani", 150},
        {2, "Burger", 120},
        {3, "Pizza", 130},
        {4, "Pasta", 100},
        {5, "Noodles", 120},
        {6, "Sandwich", 75},
        {7, "Panner butter massla", 200},
        {8, "Fish", 100.0},
        {9, "Chicken fry ", 90.0},
        {10, "Sambar", 40.0},
        {11, "Rice", 20.0},
        {12, "Special dosa", 50.0},
        {13, "Dosa", 40.0},
        {14, "Idly", 30.0}, // sweet
        {15, "Bonda", 35.0},
        {16, "Rumali roti", 17},
        {17, "Roti", 12},
        {18, "Coke", 20.0},
        {19, "Coffee", 15.0},
        {20, "Tea", 12.0}

    };
    while (1)
    {
        int k = tabeldata(totaltabels, take, 3);
        if (k == 0)
        {
            break;
        }
    }
    printf("Do you need final reprt??");
    int z = ask();
    if (z == 1)
    {
        finalreport(take); // need to work
    }
    else
    {
        printf("\nDone");
    }
}

int menutake(int tabel, items iteam[]) // assume menu is all itemasn 20 items
{
    printf("Entre the menu iteam & Prices ::::\n");
    int k = 1;
    for (int i = 0; i < tabel; i++)
    {
        printf("Entre the iteam:\n->%d)", i + 1);
        // printf("%d)", i + 1);
        scanf("%s", iteam[i].menu);
        printf("Entre the price:$");
        scanf("%f", &iteam[i].prices);
        iteam[i].id = k;
        k++;
    }
    // return iteam;
}
int tabeldata(int tabel, items take[], int attempt) // working well
{
    int tablee;
    // int k=tabelspecific;
    if (attempt == 0)
    {

        printf("All attemps exhausted");
        return 0;
    }
    else if (leave != totaltabels)
    {
        printf("\n\nDo you want to add more tables??");
        int try = ask();

        if (try == 0)
        {
            // printf("Thank you so much");
            return 0;
        }
    }
    printf("\nEntre the tabel no:");
    scanf("%d", &tablee);
    // tabelspecific++;
    if (tablee > totaltabels || tablee <= 0)
    {
        if (array[tablee] != 0)
        {
            printf("Tabel already exists!!\n");
            return tabeldata(tabel, take, attempt - 1);
        }
        else
        {
            printf("invalid tabel no:::\n");
        }

        return tabeldata(tabel, take, attempt - 1);
    }
    for (int i = 0; i < totaltabels; i++)
    {
        if (tablee == tableno[i])
        {
            printf("The tabel already existsl!!"); // look fo this
            return tabeldata(tabel, take, attempt - 1);
        }
    }
    tableno[tabelspecific] = tablee;
    tabelspecific++;
    leave--;
    allitems(take, quantity);
    takeorder(take, tablee, 3);
}
void allitems(items all[], int tabel) // for printing the items
{
    printf("\n");
    int n = 1;
    printf("\nAll the menu items are::\n");
    for (int i = 0; i < tabel; i++, n++)
    {
        printf("%d)%s--->$%f            ", all[i].id, all[i].menu, all[i].prices);
        if ((i + 1) % 3 == 0)
        {
            printf("\n");
        }
    }
    printf("\n");
}
int takeorder(items all[], int tabel, int attempt)
{
    if (attempt == 0)
    {
        printf("Sorry you have exhausted your attempts");
        printf("\nTry again!!! ");
        return 0;
    }
    int count;
    printf("\nEntre the number of items u want:");

    scanf("%d", &count);

    if (count < 0 || count > quantity)
    {
        printf("\nInvalid entry !!!!\n");
        return takeorder(all, tabel, attempt - 1);
    }
    int orderiteam[count];
    int orderquantity[count];

    for (int i = 0; i < count; i++)
    {
        printf("\nEntre the item number-> ");
        scanf("%d", &orderiteam[i]);

        int chance = 3;
        while (chance != 0)
        { // int n=sizeof(orderiteam)/sizeof(orderiteam[0]);
            int z = 0;
            for (int j = 0; j < i; j++)
            {
                if (orderiteam[i] == orderiteam[j])
                {
                    printf("You have already entred the iteam!!!");

                    z = 1;
                    allitems(all, quantity);
                    break;
                }
            }

            if (orderiteam[i] <= 0 || orderiteam[i] > quantity || z != 0)
            {

                printf("\nIn valid input !!!!!\n");
                chance--;
                allitems(all, quantity);
                // continue;
                printf("Entre the item u wnat:: ");
                scanf("%d", &orderiteam[i]);
            }
            else
            {

                chance = 0;
                // break;
            }
        }

        printf("\nEntre the order quantity you want=");
        scanf("%d", &orderquantity[i]);
        // if(zap!=0){
    }
    allitems(all, quantity);
    sort(count, orderiteam, orderquantity);
    orderdetails(all, orderiteam, orderquantity, tabel, count);
    return 1;
}
int orderdetails(items task[], int order[], int orderquantity[], int tabel, int count)
{
    int k;
    // int tabelorder[10][quantity]
    // tabelorder[tabel - 1][order - 1] = 1;
    // 1,,,,,,tabel,,,,tabel,,,should inpput that
    /*tabelspecific, tableno[tabelspecific-1],
        tabel,tabelorder[tabel - 1][order - 1]*/
    for (int i = 0; i < count; i++)
    {
        tabelorder[tabel - 1][order[i] - 1] = orderquantity[i];
    }
    for (int i = 0; i < count; i++)
    {
        printf("%d->", tabelorder[tabel - 1][order[i] - 1]);
    } // if tableorder >0
    int number = 1;
    int sum = 0;

    printf("The orders of tabel no %d are:\n ", tabel);

    printf("No|Iteam|quantity|Total price\n");

    for (int i = 0; i < quantity; i++)
    {
        if (tabelorder[tabel - 1][i] > 0)
        {
            int final = tabelorder[tabel - 1][i] * task[i].prices;

            printf("%d) %s-> %d=$%d\n", number, task[i].menu, tabelorder[tabel - 1][i], final);

            number++;

            sum = sum + final;
        }
    }
    tableprice[tabel - 1] = sum;
    printf("\nThe final price is $%d", sum);
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
void finalreport(items take[])
{

    int table = totaltabels;
    for (int i = 0; i < 10; i++)
    {
        printf("\n");
        if (tableno[i] == 0)
        {
            continue;
        }
        printf("\nTabel no %d order is =\n", tableno[i]);
        printf("\n");
        int number = 1, sum = 0;
        for (int j = 0; j < quantity; j++)
        { // this is wher i need to work
            if (tabelorder[tableno[i] - 1][j] != 0)
            {
                int final = tabelorder[tableno[i] - 1][j] * take[j].prices;

                printf("%d) %s-> %d=$%d\n", number, take[j].menu, tabelorder[tableno[i] - 1][j], final);

                number++;

                // sum = sum + final;
            }
        }
        printf("\n");
        printf("Total for table %d = $%d", tableno[i], tableprice[tableno[i] - 1]);
        // float taxes = tableprice[tableno[i] - 1] + (tableprice[tableno[i] - 1] * 18) / 100;
        // printf("\n+taxes=$%f", taxes);
    }
} // 31-8-2025
