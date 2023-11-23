# Loops, conditions and parsing

## Description
> This repository contains scripts that are created as part of the learning objectives of programming at ALX SE programme. The emphasis is on enforcing problem solving skills through programming and other technologies. The Bash files created are for a deeper understanding of loops, conditions, and parsing in scripting.

## Learning Objectives
- How to create SSH keys
- What is the advantage of using `#!/usr/bin/env bash` over `#!/bin/bash`
- How to use `while`, `until` and `for` loops
- How to use `if`, `else`, `elif` and `case` condition statements
- How to use the `cut` command
- What are files and other comparison operators, and how to use them

## Requirements
- Allowed editors: `vi`, `vim`, or `emacs`
- All files should end with a new line
- Operating system: `Ubuntu 20.04 LTS`
- The length of all files will be tested using `wc`
- All your Bash script files must be executable
- You are not allowed to use `awk`
- Your Bash script must pass `Shellcheck` (version `0.7.0`) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Scripts
0. **0-RSA_public_key.pub** - Create a RSA key pair.
    * Share your **public key** in your answer file `0-RSA_public_key.pub`
    * Fill the `SSH public key` field of your `intranet profile` with the public key you just generated
    * **Keep the private key to yourself in a secure location**, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects
    * If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase
<br>

1. **1-for_best_school** - Write a Bash script that displays `Best School` 10 times.
    * You must use the `for` loop (`while` and `until` are forbidden)
<br>

2. **2-while_best_school** - Write a Bash script that displays `Best School` 10 times.
    * You must use the `while` loop (`for` and `until` are forbidden)
<br>

3. **3-until_best_school** - Write a Bash script that displays `Best School` 10 times.
    * You must use the `until` loop (`for` and `while` are forbidden)
<br>

4. **4-if_9_say_hi** - Write a Bash script that displays `Best School` 10 times, but for the 9th iteration, displays `Best School` and then `Hi` on a new line.
    * You must use the `while` loop (`for` and `until` are forbidden)
    * You must use the `if` statement
<br>

5. **5-4_bad_luck_8_is_your_chance** - Write a Bash script that loops from 1 to 10 and:
    * displays `bad luck` for the 4th loop iteration
    * displays `good luck` for the 8th loop iteration
    * displays `Best School` for the other iterations
    * You must use the `while` loop (`for` and `until` are forbidden)
    * You must use the `if`, `elif` and `else` statements
<br>

6. **6-superstitious_numbers** - Write a Bash script that displays numbers from 1 to 20 and:
    * displays `4` and then `bad luck from China` for the 4th loop iteration
    * displays `9` and then `bad luck from Japan` for the 9th loop iteration
    * displays `17` and then `bad luck from Italy` for the 17th loop iteration
    * You must use the `while` loop (`for` and `until` are forbidden)
    * You must use the `case` statement
<br>

7. **7-clock** - Write a Bash script that displays the time for 12 hours and 59 minutes:
    * display hours from 0 to 12
    * display minutes from 1 to 59
    * You must use the `while` loop (`for` and `until` are forbidden)
<br>

8. **8-for_ls** - Write a Bash script that displays:
    * The content of the current directory
    * In a list format
    * Where only the part of the name after the first dash is displayed
    * You must use the `for` loop (`while` and `until` are forbidden)
    * Do not display hidden files
<br>

9. **9-to_file_or_not_to_file** - Write a Bash script that gives you information about the school file.
    * You must use `if` and, `else` (`case` is forbidden)
    * Your Bash script should check if the file exists and print:
        * if the file exists: `school file exists`
        * if the file does not exist: `school file does not exist`
    * If the file exists, print:
        * if the file is empty: `school file is empty`
        * if the file is not empty: `school file is not empty`
        * if the file is a regular file: `school is a regular file`
        * if the file is not a regular file: (nothing)
<br>

10. **10-fizzbuzz** - Write a Bash script that displays numbers from 1 to 100.
    * Displays `FizzBuzz` when the number is a multiple of 3 and 5
    * Displays `Fizz` when the number is multiple of 3
    * Displays `Buzz` when the number is a multiple of 5
    * Otherwise, displays the number
    * In a list format
<br>

11. **100-read_and_cut** - Write a Bash script that displays the content of the file `/etc/passwd`. Your script should only display:
    * username
    * user id
    * Home directory path for the user
    * You must use the `while` loop (`for` and `until` are forbidden)
<br>

12. **101-tell_the_story_of_passwd** - Write a Bash script that displays the content of the file `/etc/passwd`, using the `while` loop + IFS.
    * You must use the `while` loop (`for` and `until` are forbidden)
    * FORMAT: `The user USERNAME is part of the GROUP_ID gang, lives in HOME_DIRECTORY and rides COMMAND/SHELL. USER ID's place is protected by the passcode PASSWORD, more info about the user here: USER ID INFO`
<br>

13. **102-lets_parse_apache_logs** - Write a Bash script that displays the visitor IP along with the [HTTP status code](https://intranet.alxswe.com/rltoken/7de-UBmf8xgwH1iSwzX1MA) from the Apache log file.
    * Format: IP HTTP_COD
        * in a list format
    * You must use `awk`
    * You are not allowed to use `while`, `for`, `until` and `cut`
    * Download and commit the [apache-access.log](https://intranet-projects-files.s3.amazonaws.com/holbertonschool-sysadmin_devops/80/apache-access.log) file along with your answers files
<br>

14. **103-dig_the-data** - Using what you did in the previous exercise, write a Bash script that groups visitors by IP and HTTP status code, and displays this data.
    * The exact format must be:
        * OCCURENCE_NUMBER IP HTTP_CODE
        * In list format
    * Ordered from the greatest to the lowest number of occurrences
    * You must use `awk`
    * You are not allowed to use `while`, `for`, `until` and `cut`
<br>

---
## Author
* Siphamandla Matshiane, [![Twitter](http://i.imgur.com/wWzX9uB.png)](https://twitter.com/sbumatshiane916) 

## LICENSE
[ALX Software Engineering](https://www.alxafrica.com/software-engineering/)
