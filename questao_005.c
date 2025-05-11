// Input/output function
#include <stdio.h>

// Main function
int main() {
    int num_1, num_2; // Declare two integer variables to hold the numbers

    // Prompt the user for the first number
    printf("Digite o primeiro número: ");
    scanf("%d", &num_1); // Read the first number from the user

    // Prompt the user for the second number
    printf("Digite o segundo número: ");
    scanf("%d", &num_2); // Read the second number from the user

    // Calculate the average of the two numbers
    float average = (num_1 + num_2) / 2.0;

    // Print the result
    printf("A média de %d e %d é %.1f.\n", num_1, num_2, average);

    return 0; // Return 0 to indicate successful execution
}
