The objective of this project is to build a simple number guessing game that challenges the user to identify a randomly selected number within a specified range. The game begins by allowing the user to define a range by entering a lower and an upper bound (for example, from A to B). Once the range is set, the system randomly selects an integer that falls within this user-defined interval. The user's task is then to guess the chosen number using as few attempts as possible. The game provides feedback after each guess, helping the user refine their next guess based on whether their previous attempt was too high or too low.

How the Game Works
To understand how the number guessing game functions, let’s walk through two practical scenarios. These examples demonstrate how narrowing down the range intelligently—similar to a binary search—can help guess the number efficiently.

Example 1: Guessing in a Range from 1 to 100
Suppose the user defines the range from 1 to 100, and the system randomly selects 42 as the target number. The guessing process might look like this:

Guess 1: 50 → Too high
Guess 2: 25 → Too low
Guess 3: 37 → Too low
Guess 4: 43 → Too high
Guess 5: 40 → Too low
Guess 6: 41 → Too low
Guess 7: 42 → Correct!
Total Guesses: 7

Example 2: Guessing in a Range from 1 to 50
Now consider a smaller range, from 1 to 50, with the same target number 42. Here's how the guesses might proceed:

Guess 1: 25 → Too low
Guess 2: 37 → Too low
Guess 3: 43 → Too high
Guess 4: 40 → Too low
Guess 5: 41 → Too low
Guess 6: 42 → Correct!
Total Guesses: 6