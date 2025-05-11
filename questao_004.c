// Input/output function
#include <stdio.h>

// Main function
int main() {
    int num_1, num_2; // Declare two integer variables to hold the numbers
    int sum; // Declare an integer variable to hold the sum

    // Prompt the user for the first number
    printf("Digite o primeiro número: ");
    scanf("%d", &num_1); // Read the first number from the user
    // Prompt the user for the second number
    printf("Digite o segundo número: ");
    scanf("%d", &num_2); // Read the second number from the user
    // Calculate the sum of the two numbers
    sum = num_1 + num_2; // Add the two numbers and store the result in 'sum'
    // Print the result
    printf("A soma de %d e %d é %d.\n", num_1, num_2, sum); // Print the sum of the two numbers
   
    return 0; // Return 0 to indicate successful execution
}
// This program prompts the user for two numbers, calculates their sum, and prints the result.