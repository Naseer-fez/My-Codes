#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int newvar = 0;
typedef struct student
{
    int roll;
    char name[50];
    float marks;
    char course[30];
    struct student *next;
} student;
student *createnode(int roll, char name[], float marks, char course[])
{
    student *newnode = (student *)malloc(sizeof(student));
    if (newnode == NULL)
    {
        printf("The linked list is empty\n");
        exit(1);
    }
    newnode->roll = roll;
    strcpy(newnode->name, name);
    newnode->marks = marks;
    strcpy(newnode->course, course);
    return newnode;
}
void insertatb(student **head, int roll, char name[], float marks, char course[])
{

    student *newnode = createnode(roll, name, marks, course);
    if (newnode == 0)
    {
        return;
    }
    newnode->next = *head;
    *head = newnode;
}
void insertatend(student **head, int roll, char name[], float marks, char course[])
{
    student *newnode = createnode(roll, name, marks, course);
    if (*head == NULL)
    {
        *head = newnode;
        return;
    }
    else
    {
        student *temp = *head;
        while (temp->next != NULL)
        {

            temp = temp->next;
        }
        temp->next = newnode;
    }
}
void insertatpos(student **head, int roll, char name[], float marks, char course[], int pos)
{
    student *newnode = createnode(roll, name, marks, course);
    if (*head == NULL)
    {
        *head = newnode;
        return;
    }
    else
    {
        student *temp = *head;
        int i = 0;
        while (temp != NULL && i < pos - 1)
        {
            temp = temp->next;
            i++;
        }
        newnode->next = temp->next;
        temp->next = newnode;
    }
}
void trave(student *head)
{
    if (head == NULL)
    {
        printf("The list is empty!!!!!!!!!!!");
        return;
    }
    int i = 1;
    student *temp = head;
    while (temp != NULL)
    {
        printf("Student %d \n", i);
        printf("Student name:%s\n", temp->name);
        printf("Student cource:%s\n", temp->course);
        printf("Student Roll no:%d\n", temp->roll);
        printf("Student marks:%f\n", temp->marks);
        printf("\n");
        temp = temp->next;
        i++;
    }
    printf("\nThat is it:");
}
void deleteatbeg(student **head)
{

    student *temp = *head;
    if (*head == NULL)
    {

        printf("NO input given ::");
        return;
    }
    else
    {

        *head = temp->next;
        free(temp);
        return;
    }
}
void deleteatend(student **head)
{
    student *temp = *head;
    if (*head == NULL)
    {
        printf("The Linked list is empty::");
        return;
    }
    if (temp->next == NULL)
    {
        free(temp);
        *head = NULL;
        return;
    }
    else
    {
        student *prev = NULL;
        while (temp->next != NULL)
        {
            prev = temp;
            temp = temp->next;
        }
        prev->next = NULL;
        free(temp);
    }
}
void deleteatpostion(student **head, int pos)
{
    student *temp = *head;
    if (*head == NULL)
    {
        printf("The List is empty ::");
        return;
    }
    if (pos == 0)
    {
        *head = temp->next;
        free(temp);
        return;
    }
    else
    {
        int i = 0;
        student *prev = NULL;

        while (temp->next != NULL && i < pos)
        {
            prev = temp;
            temp = temp->next;
            i++;
        }
        prev->next = temp->next;

        free(temp);
    }
}
void deleteAll(student **head)
{
    student *temp = *head;
    student *nextNode;

    printf("All students to be deleted\n");

    while (temp != NULL)
    {
        nextNode = temp->next;
        free(temp);
        temp = nextNode;
    }

    *head = NULL;
    printf("List is now empty.\n");
}
void data(student **head, int no)
{
    int i = 0;
    int roll;
    char name[100];
    float marks;
    char course[10];
    while (i < no)
    {
        printf("Input the %d student :\n", i + 1);
        printf("Input the %d student name  :", i + 1);
        scanf("%s", name);
        printf("Input the %d student roll number  :", i + 1);
        scanf("%d", &roll);
        printf("Input the %d students courss :", i + 1);
        scanf("%s", course);
        printf("Input the %d student marks  :", i + 1);
        scanf("%f", &marks);
        insertatb(head, roll, name, marks, course);
        i++;
        printf("\n");
    }
}
int sumstudents(student **head)
{
    int sum = 0;
    student *temp = *head;
    while (temp != NULL)
    {

        temp = temp->next;
        sum++;
    }

    return sum;
}
void input(student **head, int i)
{

    int roll;
    char name[100];
    float marks;
    char course[10];
    switch (i)
    {
    case 1:
    {
        printf("Input the  student :\n");
        printf("Input the  student name  :");
        scanf("%s", name);
        printf("Input the  student roll number  :");
        scanf("%d", &roll);
        printf("Input the  students courss :");
        scanf("%s", course);
        printf("Input the  student marks  :");
        scanf("%f", &marks);
        insertatb(head, roll, name, marks, course);
        trave(*head);
        break;
    }
    case 2:
    {
        printf("Input the  student :\n");
        printf("Input the  student name  :");
        scanf("%s", name);
        printf("Input the  student roll number  :");
        scanf("%d", &roll);
        printf("Input the  students courss :");
        scanf("%s", course);
        printf("Input the  student marks  :");
        scanf("%f", &marks);
        insertatend(head, roll, name, marks, course);
        trave(*head);
        break;
    }

    case 3:
    {
        int j;
        printf("Entre the postion of the student :");
        scanf("%d", &j);
        printf("\nInput the  student :\n");
        printf("Input the  student name  :");
        scanf("%s", name);
        printf("Input the  student roll number  :");
        scanf("%d", &roll);
        printf("Input the  students courss :");
        scanf("%s", course);
        printf("Input the  student marks  :");
        scanf("%f", &marks);
        insertatpos(head, roll, name, marks, course, j);
        trave(*head);
        break;
    }
    case 4:
    {
        int j;
        printf("Select the postion to delete :");
        scanf("%d", &j);
        deleteatpostion(head, j);
        break;
    }
    case 5:
    {
        int j;
        deleteAll(head);
        break;
    }
    case 6:
    {

        deleteatbeg(head);
        break;
    }
    case 7:
    {
        deleteatend(head);
        break;
    }
        // Count Total Students
    case 8:
    {
        int k = sumstudents(head);
        printf("The total no of students =%d", k);
        break;
    }
    case 9:
    {
        trave(*head);
        break;
    }
    case 0:
    {
        return;
        break;
    }
    default:
    {
        printf("failed :\n try again");
        // newoptions(*head) ;//i  need this
        break;
    }
    }
}
/*void newoptions(student **head)
{
    int i;
    printf("\n=====================================\n");
    printf("     📚 Student Record System Menu   \n");
    printf("=====================================\n");
    printf("1. Add Student at Beginning\n");
    printf("2. Add Student at End\n");
    printf("3. Add Student at Position\n");
    printf("4. Delete at Position\n");
    printf("5. Display All Students\n");
    printf("6. Delete from Beginning\n");
    printf("7. Delete from End\n");
    printf("8. Count Total Students\n");
    printf("9. Search Student by Roll Number\n");
    printf("10. Update Student Details\n");
    printf("11. Sort Students by Marks\n");

    printf("0. Exit\n");
    printf("=====================================\n");
    printf(" Enter your choice: ");
    scanf("%d", &i);
    input(head, i);

    scanf("%d", &i);
    input(head, i);
}*/
void options(student **head)
{
    int i;
    char c;
    printf("Any additional changes?\n");
    printf("if yes?\n");
    printf("select any key\n");
    printf("Else: press 'a'\n");

    scanf(" %c", &c);

    if (c == 'a')
    {
        return;
    }
    else
    {
        // if ((newvar  == 0))
        {
            printf("\n=====================================\n");
            printf("     📚 Student Record System Menu   \n");
            printf("=====================================\n");
            printf("1. Add Student at Beginning\n");
            printf("2. Add Student at End\n");
            printf("3. Add Student at Position\n");
            printf("4. Delete at Position\n");
            printf("5. Delete  All Students\n");
            printf("6. Delete from Beginning\n");
            printf("7. Delete from End\n");
            printf("8. Enter Sum)\n");
            printf("9. Display all students\n");
            // printf("9. Search Student by Roll Number\n");
            //  printf("10. Update Student Details\n");
            //  printf("11. Sort Students by Marks\n");
            //  printf("12. Count Total Students\n");
            //  printf("0. Exit\n");
            //  printf("=====================================\n");
            printf(" Enter your choice: ");
            scanf("%d", &i);
            if (i > 9 || i < 0)
            {
                printf("Select valid options :");
                options(head);
            }
            else
            {
                input(head, i);
                newvar = 1;
            }
        }
        /*else
        {
            int i;
            printf("     📚 Student Record System Menu   \n");
            printf("=====================================\n");
            printf("1. Add Student at Beginning\n");
            printf("2. Add Student at End\n");
            printf("3. Add Student at Position\n");

            scanf("%d", &i);
            input(head, i);
            newvar=0;
        }*/
    }
}

int main()
{
    student *head = NULL;
    int i;
    printf("Entre the  no of data for students =");
    scanf("%d", &i);
    data(&head, i);
    trave(head);
    // options(&head);
    while (1)
    {
        options(&head);
    }
}