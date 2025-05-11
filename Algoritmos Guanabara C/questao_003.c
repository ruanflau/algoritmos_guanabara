// Input/output function
#include <stdio.h>

// Main function
int main() {
    char name[100]; // Declare a character array to hold the name
    int wage; // Declare an integer variable to hold the wage

    // Prompt the user for their name and wage
    printf("Qual é o seu nome? ");
    scanf("%s", name); // Read the input string from the user
    printf("Qual é o seu salário? ");
    scanf("%d", &wage); // Read the input integer from the user

    // Print a message with the user's name and wage
    printf("Olá, %s! Seu salário é %d reais.\n", name, wage);

    return 0; // Return 0 to indicate successful completion
}
// This program prompts the user for their name and wage, then prints a message with the user's name and wage.