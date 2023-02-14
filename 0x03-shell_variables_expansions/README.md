# Shell - Init Files, Variables and Expansions

### Description

This project is based on shell initialization files, variables and expansions. The scripts created are part of the learning curriculum developed at ALX SE Programme as part of the learning process.

### Requirements
* Language(s): `Bash`
* Operating System: `Ubuntu 20.04 LTS`
* Allowed Editors: `vi`, `vim`, or `emacs`
* All the files are executables.
* No use of `&&`, `||` or `;` is allowed.
* Not allowed to use `bc`, `sed` or `awk`

### Learning Objectives
* What happens when you type `$ ls -l *.txt`.
* What are the `/etc/profile` file and the `/etc/profile.d` directory.
* What is the `~/.bashrc` file.
* What is the difference between a local and a global variable.
* What is a reserved variable.
* How to create, update and delete shell variables.
* What are the roles of the following reserved variables: `HOME`, `PATH`, `PS1`
* What are special parameters.
* What is the special parameter `$?`?
* What is expansion and how to use them.
* What is the difference between single and double quotes and how to use them properly.
* How to do command substitution with `$()` and backticks.
* How to perform arithmetic operations with the shell.
* How to create an alias.
* How to list aliases.
* How to temporarily disable an alias.
* How to execute commands from a file in the current shell.

### Script Information

0. **0-alias** - Creates an alias. Name: `ls`, Value: `rm *`.<br>
1. **1-hello_you** - Prints `hello user`, where user is the current Linux user.<br>
2. **2-path** - Adds `/action` to the `PATH`. `/action` should be the last directory the shell looks into when looking for a program.<br>
3. **3-paths** - Counts the number of directories in the `PATH`.<br>
4. **4-global_variables** - Lists environment variables.<br>
5. **5-local_variables** - Lists all local variables and environment variables, and functions.<br>
6. **6-create_local_variable** - Creates a new local variable. Name: `BEST`, Value: `School`.<br>
7. **7-create_global_variable** - creates a new global variable. Name: `BEST`, Value: `School`.<br>
8. **8-true_knowledge** - Prints the result of the addition of 128 with the value stored in the environment variable `TRUEKNOWLEDGE`, followed by a new line.<br>
9. **9-divide_and_rule** - Prints the result of `POWER` divided by `DIVIDE`, followed by a new line. `POWER` and `DIVIDE` are environment variables.<br>
10. **10-love_exponent_breath** - Displays the result of `BREATH` to the power `LOVE`. `BREATH` and `LOVE` are environment variables. The script should display the result, followed by a new line.<br>
11. **11-binary_to_decimal** - Converts a number from base 2 to base 10. The number in base 2 is stored in the environment variable `BINARY`. The script should display the number in base 10, followed by a new line.<br>
12. **12-combinations** - Prints all possible combinations of two letters, except `oo`. Letters are lower cases, from `a` to `z`. One combination per line. The output should be alpha ordered, starting with `aa`. Do not print `oo`. Your script file should contain maximum 64 characters.<br>
13. **13-print_float** - Prints a number with two decimal places, followed by a new line. The number will be stored in the environment variable `NUM`.<br>
14. **100-decimal_to_hexadecimal** - Converts a number from base 10 to base 16. The number in base 10 is stored in the environment variable `DECIMAL`. The script should display the number in base 16, followed by a new line.<br>
15. **101-rot13** - Encodes and decodes text using the rot13 encryption. Assume ASCII.<br>
16. **102-odd** - Prints every other line from the input, starting with the first line.<br>
17. **103-water_and_stir** - Adds the two numbers stored in the environment variables `WATER` and `STIR` and prints the result. `WATER` is in base `water`. `STIR` is in base `stir`. The result should be in base `bestchol`.<br>

### Author(s)
* Siphamandla Matshiane

### LICENSE
* <a href="https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=0CAMQw7AJahcKEwjInaz955X9AhUAAAAAHQAAAAAQAw&url=https%3A%2F%2Fwww.holbertonschool.com%2F&psig=AOvVaw3ZYi51U1ZGM3r5xBJf4-26&ust=1676491570213568">ALX SE Programme</a>

