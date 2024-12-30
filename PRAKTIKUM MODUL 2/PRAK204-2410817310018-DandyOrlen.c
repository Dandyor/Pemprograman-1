#include <stdio.h>
#include <math.h> 

int main() {
    float jarijari, tinggi;

    printf("Masukkan jari-jari: ");
    scanf("%f", &jarijari);

    printf("Masukkan tinggi: ");
    scanf("%f", &tinggi);

    float pi = 22.0 / 7.0; 
    float volume = pi * pow(jarijari, 2) * tinggi;
    float luas = 2 * pi * jarijari * (jarijari + tinggi);
    float keliling = 2 * pi * jarijari;

    printf("Volume = %.2f\n", volume);
    printf("Luas = %.2f\n", luas);
    printf("Keliling = %.2f\n", keliling);

    return 0;
}
