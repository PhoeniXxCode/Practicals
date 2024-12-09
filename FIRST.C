#include <stdio.h>
#include <conio.h>

int main(void) {
   

    // Declare variables at the beginning
    int count = 10, i, continueValue, breakValue, choice;

    printf("Program to demonstrate nested control structure\n\n");

label:
    printf("Demo for goto: DONE!\n\n");
    printf("Menu\n");
    printf("1: Demo for \"continue\"\n");
    printf("2: Demo for \"break\"\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);
    printf("\n");

    switch (choice) {
    case 1:
        printf("This loop will print 1...10 except the skipped number\n\n");
        printf("Enter the number to skip: ");
        scanf("%d", &continueValue);

        for (i = 1; i <= count; i++) {
            if (i == continueValue)
                continue; // Skip the rest of the loop for this iteration.
            printf("%d ", i);
        }
        break;

    case 2:
        printf("This loop will print 1...10 until the stopping number\n\n");
        printf("Enter the number to stop: ");
        scanf("%d", &breakValue);

        for (i = 1; i <= count; i++) {
            if (i == breakValue)
                break; // Exit the loop when the condition is met.
            printf("%d ", i);
        }
        break;

    default:
        printf("Invalid choice");
        break;
    }

    printf("\n\n");
    getch(); // Wait for key press (only works in Turbo C).
    return 0;
}
