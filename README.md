# Quizly: The Mental Arithmetic Quiz Maker
#### Video Demo: https://youtu.be/DcaBSgTQGqg
#### Description:

Quizly is an short interactive program that lets you test your ability to solve mental arithmetic problems and improve your math skills through quizzes.

The main program starts by printing off the name of the application `Quizly` in a special font. The font is chosen arbitrarily in a list of five different fonts.

The user can then choose between three different options for a quiz:
1) `Additions only`
2) `A combination of additions and substractions`
3) `Multiplications only.`

The first option has numbers ranging from `0 to 100`, the second has numbers ranging from `-100 to 100` and the third option are simple multiplications with numbers lower than `50`.

The user then chooses how many questions they want in that quiz. This number ranges from `0 to infinity` (which means that he can be having as many questions that he wants).

Then, the quiz begins. Each question is basically one operation with 2 numbers that are small enough to make mathematical computations with. This operation can (and should) be solved using the user's head only, without the external aid of tools like pen and paper and calculators. This is the reason why the quiz has no particular limitations nor penalties, and lets the user think before answering with `no time limit`.

The program gives a direct feedback on the answer the user just typed for the current question, whether it is right or wrong and gives the answer away if wrong.

Each good answer is a `point` and a wrong answer gives no point. Those points add up and make up the `final score`. This score is calculated based on the total number of questions.

At the end of the quiz, the score gets printed on the screen in "number x out of number y" format and in percentage format, for example : `"4 out of 5! (80.0%)"`. It also prints a small message to congratulate the user and encourages them to take more quizzes. This is where the program ends. The user just has to rerun the program to take another quiz.

The only depandancy the program needs is the library `pyfiglet` that can be installed with the command `pip install pyfiglet`.
Then, the program can be lanched in the teminal with the following command : `python project.py`.

The project also has a test file that come with it. It helps testing some of the functions I created and used to make the main program work.
The first test is for `generate_numbers()` that generates numbers for a given option (1, 2 or 3).
The second test is for `check_answer()` that verifies the answer, prints `Correct` or `Incorrect`, and returns `True` or `False` depending on the truthfulness of the answer.
The final test is for `feedback()` that returns a message depending on the total number of points and the total number of questions.

In the same way the program can be ran, the test file also can by entering this command in the terminal : `pytest test_project.py`.

This was my Final Project for the online CS50P course hosted by Harvard University.

Thank you for reading!

