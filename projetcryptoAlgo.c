#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char * crypter();
char * decrypter();

struct Chaines
{
    char * message;
    char * messageDecrypte;
    char * messageCrypte;
    char * clef;
};


int main(void){

    struct Chaines C;
    char * message;
    char * clef = "FMUQLTRIHOJGDPWBEZSCXKYNVA";
    char * messageEncode;
    char * messageCrypte;
    int tailleChaine, choix;


    puts("Ecrivez le message : ");
    fgets( message, 200, stdin);
    C.message = malloc(sizeof(char) * strlen(message));
    C.messageCrypte = malloc(sizeof(char) * strlen(message));
    C.messageDecrypte = malloc(sizeof(char) * strlen(message));
    C.message = strcpy(C.message, message);
    C.clef = malloc(sizeof(char) * strlen(clef));
    C.clef = strcpy(C.clef, clef);

    
    puts("Voulez vous crypter ou decrypter le message :\nCrypter : 1\nDecripter : 2");
    scanf(" %d", &choix);
    if(choix == 1 )
    {
        crypter(C);
        printf("\nVotre message crypte : %s\n", C.messageCrypte);

    }else
    {
        C.message = strcpy(C.messageCrypte, message);
        decrypter(C);
        printf("Votre message decrypte : %s\n", C.messageDecrypte);

    }
}

char * crypter(struct Chaines C)
{
    for(int i=0;i<strlen(C.message)-1;i++)
    {
        C.messageCrypte[i]=C.message[i]^C.clef[i];
    }
    
    return(C.messageCrypte);
}

char * decrypter(struct Chaines C)
{
    for(int i = 0; i<strlen(C.message)-1; i++)
    {
        C.messageDecrypte[i]=C.messageCrypte[i]^C.clef[i];
    }
    return(C.messageDecrypte);
}