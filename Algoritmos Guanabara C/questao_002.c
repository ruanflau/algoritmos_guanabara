// Input/output function
#include <stdio.h>

// Main function
int main() {
    char str[100]; // Declare a character array to hold the string

    printf("Qual é o seu nome? "); // Prompt the user for their name
    scanf("%s", str); // Read the input string from the user

    // Print a greeting message with the user's name
    printf("Olá, %s! É um prazer conhecê-lo!\n", str);

    return 0; // Return 0 to indicate successful completion
}
// This program prompts the user for their name and prints a greeting message with the user's name.