/*------------------------------------------------------------------------------
#   Author	: Kim Hyunyoung
#   Date	: 2023.05.23
#   Module	: get string and file input
#   File	: ex2_78.c
------------------------------------------------------------------------------*/

/*------------------------------------------------------------------------------
	Header Files
------------------------------------------------------------------------------*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*----------------------------------------------------------------------------*/
int	main (void)
/*----------------------------------------------------------------------------*/
{   
    typedef struct sStruct 
    {
        char innerString[100];
        struct sStruct* nextP;
    } stringStruct;

    char tempBuffer [200] = "";
    int flag = 0;
    FILE* fp;

    stringStruct *head = NULL;
    stringStruct *tail = NULL;
    stringStruct *exNode = NULL;
    stringStruct *node = NULL;


    while (1)                                                                                               // input part
    {
        flag = 0;
        puts ("Please type string for (100 characters limit, not blank, type 'end' for end)");              // announcement for program start
        do
        {
            if (flag != 0)
            {
                puts ("Wrong input format. Please insert string (100 characters limit, not blank, type 'end' for end)");        // announcement for wrong format input
            }
            flag = 1;
            printf ("input : ");
            fgets (tempBuffer, 200, stdin);
        fflush(stdin);
        } while (strlen (tempBuffer) <= 1 || strlen (tempBuffer) > 100);

        node = (stringStruct*)malloc(sizeof(stringStruct));                                                 // makin linked list
        node->nextP = NULL;
        strcpy (node->innerString, tempBuffer);

        if (head == NULL)
        {
            head = node;
        } else
        {
            exNode->nextP = node;
        }

        if (strcmp (tempBuffer, "end\n") == 0 || strcmp (tempBuffer, "'end'\n") == 0)                                     // exit condition
        {
            tail = exNode;
            break;
        }
        exNode = node;
    }
    node = head;
    fp = fopen("ex2_78.dat", "w");

    while (node->nextP != NULL)                                                                                           // file input
    {
        if (node == tail) {
            node->innerString[strlen(node->innerString)-1] = '\0';
        }
        fputs(node->innerString, fp);
        node = node->nextP;
    }

    exNode = head;
    while (exNode->nextP != NULL) {                                                                                         // free()
        node = exNode->nextP;
        free(exNode);
        exNode = node;
    }
    free(exNode);

    while(getchar() != '\n');
    
    fclose(fp);

    printf("End of Program. Please check the datafile.\n");

    return 0;
}





// set list