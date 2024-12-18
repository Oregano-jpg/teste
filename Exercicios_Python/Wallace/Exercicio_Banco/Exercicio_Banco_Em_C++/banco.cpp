//Escreva um programa que apresente quatro opções:
//(a) consulta saldo,
//(b) saque,
//(c) depósito,
//(d) sair
//O saldo deve iniciar em R$ 0,00.
//A cada saque ou depósito o valor do saldo deve ser atualizado.
//Repetir o programa até que o usuário digite ‘d’ (sair).

#include<stdio.h>
#include<ctype.h>
void main ()
{
    char opcao;
    float saldo=0, valor;


    printf("Escolha uma opcao:\n a)saldo\n b)saque\n c)deposito\n d)sair\n");
    scanf(" %c", &opcao);
    opcao = tolower (opcao);
    while (opcao!='d')
    {

        if (opcao=='a')
        {
            printf("este eh o seu saldo = %.2f\n", saldo);
        }

        else if (opcao=='b')
        {
            printf("quanto deseja sacar?");
            scanf("%f", &valor);
            if (valor>saldo)
            {
                printf("voce nao possui saldo para sacar.\n");
            }
            else
            {
                saldo=saldo-valor;
            }

        }

        else if (opcao=='c')
        {
            printf("quanto deseja depositar?\n");
            scanf("%f", &valor);
            saldo=saldo+valor;
        }



        printf("Escolha uma opcao:\n a)saldo\n b)saque\n c)deposito\n d)sair\n");
        scanf(" %c", &opcao);
        opcao = tolower (opcao);

    }


}