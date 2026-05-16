#include <stdio.h>
#include <string.h>
#define Totalbeds 100
int bedcount[Totalbeds];
char patientsnames[Totalbeds][100];
int incpatientname = 0;
int lastadmitted;
int lastdischarged;
char recentdischarege[100];

int basicdata(int attempts);
int optionsselction(int basicdata_option);
int admitpatient(int attempts);
int checkingbed(int attempts);
int discharepatient(int attempts);
int bedstatus2d(int need);
int allstats();
int statsswitch(int attempts);
int asking(int attempts);
int basicdataafterstata(int attempts);
int ask(); // fav**

int main()

{
    printf("WELCOME TO THE HOSPITAL MANAGMENT\n\n\n");

    while (1)
    {
        if (!basicdata(3))
            break;
    }
    printf("Do you need final reprt??");
    int z = ask();
    if (z == 1)
    {
        bedstatus2d(3); // need to work
    }
    else
    {
        printf("\nDone");
    }
}

int basicdata(int attempts)
{
    int k = 0;
    int basicdata_option;
    if (attempts == 0)
    {
        printf("You have exhaused your attemps !!");
        return 0;
    }
    else if (attempts == 1)
    {
        printf("Last attempt !\nEntre carefully\n");
    }

    printf("Hospital Bed Managment System\n");
    printf("1.Admit patient\n");
    printf("2.Discharge PAatient\n");
    printf("3.Show Bed Status\n");
    printf("4.Show Statics\n");
    printf("5.Exit\n");

    printf("Entre Your Option:");
    scanf("%d", &basicdata_option);
    if (basicdata_option < 0 || basicdata_option > 5)
    {
        printf("\nInvalid entry\n please give the correct option !!\n");
        attempts--;
        return basicdata(attempts);
    }
    else if (basicdata_option > 0 && basicdata_option < 5)
    {
        optionsselction(basicdata_option);
        if (basicdata_option == 5)
        {
            printf("\nExiting ");
            return 0;
        }
        k = asking(3);
    }

    if (k == 1)
    {
        printf("\n");
        basicdata(3);
    }
    else
    {
        return 0;
    }
}
int optionsselction(int basicdata_option)
{

    switch (basicdata_option)
    {

    case 1:
    {
        admitpatient(3);
    }
    break;
    case 2:
    {
        discharepatient(3);
    }
    break;
    case 3:
    {
        bedstatus2d(3);
    }
    break;
    case 4:
    {
        allstats();
    }
    break;
    case 5:
    {
        return 0;
    }
    break;
    }
}
int admitpatient(int attempts)
{
    char patient[100];
    int bedno;

    printf("Entre the Patient name :");
    scanf("%s", patient);
    printf("\n");
    int check;

    check = checkingbed(3);
    if (check == -1)
        printf("We are sorry !!\n Looks like we have no bed\n ");
    else
    {
        strcpy(patientsnames[check], patient);
        incpatientname++;
        printf("\nThe bed has been added succufulyy!!!");
    }
}
int checkingbed(int attempts)
{
    int bedno;
    if (attempts == 0)
    {
        printf("\nYou have exhaused your attemps !!\n");
        return -1;
    }
    else if (attempts == 1)
    {
        printf("\nThe bed number alredy exists :::");
        printf("\nLast attempt !\nEntre carefully\n");
    }
    else if (attempts == 2)
    {
        printf("Invalid");
    }
    if (incpatientname == Totalbeds - 1)
    {
        printf("The ward is full");
        return 0;
    }
    printf("\nEntre the bed number :");
    scanf("%d", &bedno);

    // here
    if (bedno > Totalbeds || bedno <= 0)
    {
        printf("Bed number too high(100)");
        attempts--;
        checkingbed(attempts);
    }

    else if (bedcount[bedno - 1] == 0)
    {
        bedcount[bedno - 1] = 1;
        lastadmitted = bedno;

        return bedno - 1;
    }
    else
    {
        return checkingbed(attempts--);
    }
}
int discharepatient(int attempts)
{
    int bedno;
    if (attempts == 0)
    {
        printf("\nYou have exhaused your attemps !!\n");
        return 0;
    }
    else if (attempts == 1)
    {
        printf("Last attempt !\nEntre carefully\n");
    }

    int z = bedstatus2d(2);
    if (z == 0)
    {
        printf("\nNo beds right now\n");
        return 0;
    }
    printf("\nEntre The Bed no :");
    scanf("%d", &bedno);
    int k = 1;
    if (bedno <= 0 || bedno > Totalbeds)
    {
        printf("Invalid bed number! (1-%d)\n", Totalbeds);
        return discharepatient(attempts - 1);
    }
    if (bedcount[bedno - 1] == 0)
    {
        printf("Sorry noone is on this bed\n");
        printf("Please try again\n");
        return discharepatient(attempts - 1);
    }
    printf("\nThe bed has been freed successfully!\n");
    bedcount[bedno - 1] = 0;
    incpatientname--;

    strcpy(recentdischarege, patientsnames[bedno - 1]);
    patientsnames[bedno - 1][0] = '\0'; // clear name

    lastdischarged = bedno;

    return 1;
}
int bedstatus2d(int need)
{
    if (need == 3)
    {
        printf("\nThe bed staus is :\n");
        printf("\nX=occupied\nO=Empty\n");
        for (int i = 0; i < Totalbeds; i++)
        {
            if (bedcount[i] == 1)
                printf(" X ");
            else
                printf(" O ");
            if ((i + 1) % 10 == 0 && i != 0)
                printf("\n");
        }
        printf("Occupied=%d\nAvalibale=%d\n", incpatientname, (Totalbeds - incpatientname));
    }
    else
    {
        printf("\n");
        int k = 0;
        for (int i = 0; i < Totalbeds; i++)
        {
            if (bedcount[i] == 1)
            // this is wht not working
            {
                printf("%2d)Bed  %d\n->%s", k + 1, i + 1, patientsnames[i]);
                k++;
            }
        }
        return k;
    }
}
int allstats()
{

    printf("\nThe stats of the Ward are ::\n");
    printf("1.Total Bed in the hosipals\n");
    printf("2.Available beds\n ");
    printf("3.Ocupany pct\n");
    printf("4.patient details\n");
    printf("5.lastAdmitted\n");
    printf("6.lastDischarged\n");

    printf("7.GO BACKKKKKK\n");
    int k = statsswitch(3);
    if (k == 0)
        printf("bOOM");
}
int statsswitch(int attempts)
{
    int selection;
    if (attempts == 0)
    {
        printf("\nYou have exhaused your attemps !!\n");
        return 0;
    }
    else if (attempts == 1)
    {

        printf("\nLast attempt !\nEntre carefully\n");
    }
    else if (attempts == 2)
    {
        printf("\n Second Last attempt !\nEntre carefully\n");
    }

    printf("Entre the stat you want to see:");
    scanf("%d", &selection);
    if (selection < 0 || selection > 7)
    {
        printf("\nInvalid option");
        attempts--;
        return statsswitch(attempts);
    }
    int occupied = 0;
    int avalibale = 0;

    for (int i = 0; i < Totalbeds; i++)
    {
        if (bedcount[i] == 1)
        {
            occupied++;
        }
    }
    switch (selection)
    {
    case 1:
    { // Total Bed in the hosipals
        printf("The Total beds in hospital are %d\n", Totalbeds);
    }
    break;
    case 2:
    { // Available beds
        bedstatus2d(1);

        printf("\nThe Avalibale beds in hospital are %d", Totalbeds - occupied);
    }
    break;
    case 3:
    {
        // Ocupany pct
        float ocp = ((float)occupied / Totalbeds) * 100.0;
        printf("The occupied pct is %f", ocp);
    }
    break;
    case 4:
    {
        int k = 1;
        printf("All patients detail are :\n");
        bedstatus2d(1);
    }
    break;

    case 5:
    {
        if (lastadmitted > 0)
            printf("The last admitted person is %s at bed %d\n", patientsnames[lastadmitted - 1], lastadmitted);
        else
            printf("No patients admitted yet.\n");
    }
    break;
    case 6:
    {
        // lastdischgared
        printf("The last discharged person is %s and bed no is %d", recentdischarege, lastdischarged);
    }
    break;
    case 7:
    {
        printf("Going back to the previous menu");
        basicdataafterstata(3);
    }
    break;
    }
}
int basicdataafterstata(int attempts)
{
    int basicdata_option;
    if (attempts == 0)
    {
        printf("You have exhaused your attemps !!");
        return 0;
    }
    else if (attempts == 1)
    {
        printf("Last attempt !\nEntre carefully\n");
    }

    printf("\nHospital Bed Managment System\n");
    printf("1.Admit patient\n");
    printf("2.Discharge PAatient\n");
    printf("3.Show Bed Status\n");
    // printf("4.Show Statics\n");
    printf("4.Exit\n");

    printf("Entre Your Option:");
    scanf("%d", &basicdata_option);
    if (basicdata_option == 4)
    {
        printf("\nExiting");
        return 0;
    }
    if (basicdata_option < 0 || basicdata_option > 4)
    {
        printf("\nInvalid entry\n please give the correct option !!\n");
        attempts--;
        return basicdata(attempts);
    }
    else if (basicdata_option == 4)
    {
        optionsselction(5);
    }
    else
    {
        optionsselction(basicdata_option);
    }
}
int asking(int attempts)
{
    char c;
    char a;
    if (attempts == 0)
    {
        printf("You have exhausted your limits \n");
        return 0;
    }
    else if (attempts == 1)
    {

        printf("/nLast chanece /nSo be carefullll\n");
    }
    else if (attempts == 2)
    {
        printf("\n Invalid entry\n");
    }
    else if (attempts == 3)
    {
        printf("\nDo you need anything else(y/n)?\n");
    }
    printf("::");
    scanf(" %c", &c);
    if (c == 'y' || c == 'Y')
    {
        return 1;
    }
    else if (c == 'n' || c == 'N')
    {
        printf("\nare you sure !!\n");
        printf("Confirm (y/n)\n");
        printf("::");
        scanf(" %c", &a);
        if (a == 'y' || a == 'Y')
        {
            return 0;
        }
        else if (a == 'n' || a == 'N')
        {
            return 1;
        }
    }

    else
    {
        attempts--;
        asking(attempts);
    }
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
} // 4-09
