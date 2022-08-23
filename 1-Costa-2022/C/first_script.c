#include <stdio.h>

void productoPotente(int vector[], int *resultado, int tam){
    *resultado = 1000;
}

void makeIntVector(int vector[], int tam){
    int num;
    for (int i=0; i<tam; i++){
        printf("Enter number in position: %d\n", i);
        scanf("%d", &num); 
        printf("\n");
        vector[i] = num;
    }
}

int main(){
    int resultado = 0;
    int tam;   
    printf("Enter lenght of the vector (integer) [0-100]: ");  
    scanf("%d", &tam);
    printf("You entered: %d\n", tam);
    while (tam < 0 || tam > 100){
        printf("Enter lenght of the vector (integer) [0-100]: ");  
        scanf("%d", &tam);
        printf("You entered: %d\n", tam);
    }
    
    int vector[tam];
    makeIntVector(vector[0], tam);
    printf("%d\n", vector[0]);
    printf("%d\n", vector[1]);

    productoPotente(vector, &resultado, tam);
    printf("Resultado %d\n", resultado);
    return 0;
    
}