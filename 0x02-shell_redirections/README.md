# Shell I/O, Redirections, and Filters

### Description
The project contains shell scripts that are based on shell redirections, I/O, and filters. The scriptd are developed as part of the learning curriculum at ALX SE programme.

### Requirements
* Language(s): `Bash`
* Operating System: `Ubuntu 20.04 LTS`
* Allowed Editors: `vi`, `vim`, or `emacs`
* All files must be executables.

### Learning Objectives

* What do the commands `head`, `tail`, `find`, `wc`, `sort`, `uniq`, `grep`, `tr` do.
* How to redirect standard output to a file.
* How to get standard input from a file instead of the keyboard.
* How to send the output from one program to the input of another program.
* How to combine commands and filters with redirections.
* What are special characters.
* Understand what do the white spaces, single quotes, double quotes, backslash, comment, pipe, command separator, tilde and how and when to use them.
* How to display a line of text.
* How to concatenate files and print on the standard output.
* How to reverse a string.
* How to remove sections from each line of files.
* What is the `/etc/passwd` file and what is its format.
* What is the `/etc/shadow` file and what is its format.

### Script Information
0. **0-hello_world** - Prints “Hello, World”, followed by a new line to the standard output.<br>
1. **1-confused_smiley** - Displays a confused smiley `"(Ôo)'`.<br>
2. **2-hellofile** - Display the content of the `/etc/passwd` file.<br>
3. **3-twofiles** - Display the content of `/etc/passwd` and `/etc/hosts`.<br>
4. **4-lastlines** - Display the last 10 lines of `/etc/passwd`.<br>
5. **5-firstlines** - Display the first 10 lines of `/etc/passwd`.<br>
6. **6-third_line** - Displays the third line of the file `iacta`. The file `iacta` will be in the working directory. You’re not allowed to use `sed`.<br>
7. **7-file** - Creates a file named exactly `\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)` containing the text `Best School` ending by a new line.<br>
8. **8-cwd_state** - Writes into the file `ls_cwd_content` the result of the command `ls -la`. If the file `ls_cwd_content` already exists, it should be overwritten. If the file `ls_cwd_content` does not exist, create it.<br>
9. **9-duplicate_last_line** - Duplicates the last line of the file `iacta`. The file `iacta` will be in the working directory.<br>
10. **10-no_more_js** - Deletes all the regular files (not the directories) with a `.js` extension that are present in the current directory and all its subfolders.<br>
11. **11-directories** - Counts the number of directories and sub-directories in the current directory. The current and parent directories should not be taken into account. Hidden directories should be counted.<br>
12. **12-newest_files** - Displays the 10 newest files in the current directory. Requirements: One file per line and sorted from the newest to the oldest.<br>
13. **13-unique** - Takes a list of words as input and prints only words that appear exactly once. Input format: One line, one word. Output format: One line, one word. Words should be sorted.<br>
14. **14-findthatword** - Display lines containing the pattern “root” from the file `/etc/passwd`.<br>
15. **15-countthatword** - Display the number of lines that contain the pattern “bin” in the file `/etc/passwd`.<br>
16. **16-whatsnext** - Display lines containing the pattern “root” and 3 lines after them in the file `/etc/passwd`.<br>
17. **17-hidethisword** - Display all the lines in the file `/etc/passwd` that do not contain the pattern “bin”.<br>
18. **18-letteronly** - Display all lines of the file `/etc/ssh/sshd_config` starting with a letter. Include capital letters as well.<br>
19. **19-AZ** - Replace all characters `A` and `c` from input to `Z` and `e` respectively.<br>
20. **20-hiago** - Removes all letters `c` and `C` from input.<br>
21. **21-reverse**- Reverses its input.<br>
22. **22-users_and_homes** - Displays all users and their home directories, sorted by users; based on the the `/etc/passwd` file.<br>
23. **100-empty_casks** - A command that finds all empty files and directories in the current directory and all sub-directories. Only the names of the files and directories should be displayed (not the entire path). Hidden files should be listed. One file name per line. The listing should end with a new line. You are not allowed to use `basename`, `grep`, `egrep`, `fgrep` or `rgrep`.<br>
24. **101-gifs** - Lists all the files with a .gif extension in the current directory and all its sub-directories. Hidden files should be listed. Only regular files (not directories) should be listed. The names of the files should be displayed without their extensions. The files should be sorted by byte values, but case-insensitive (file `aaa` should be listed before file `bbb`, file `.b` should be listed before file `a`, and file `Rona` should be listed after file `jay`). One file name per line. The listing should end with a new line. You are not allowed to use `basename`, `grep`, `egrep`, `fgrep` or `rgrep`.<br>
25. **102-acrostic** - An acrostic is a poem (or other form of writing) in which the first letter (or syllable, or word) of each line (or paragraph, or other recurring feature in the text) spells out a word, message or the alphabet. The word comes from the French acrostiche from post-classical Latin acrostichis). As a form of constrained writing, an acrostic can be used as a mnemonic device to aid memory retrieval. <a href="https://intranet.alxswe.com/rltoken/I2jXYKQIpVouDo0_1XrCJw">Read more</a>. The script decodes acrostics that use the first letter of each line. The ‘decoded’ message has to end with a new line. You are not allowed to use `grep`, `egrep`, `fgrep` or `rgrep`.<br>
26. **103-the_biggest_fan** - The script parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests. Order by number of requests, most active host or IP at the top. You are not allowed to use `grep`, `egrep`, `fgrep` or `rgrep`.<br>

### Authors
* Siphamandla Matshiane

### LICENSE
* <a href="https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiJ-L6Xt5X9AhXfQkEAHYmDAAIQFnoECDUQAQ&url=https%3A%2F%2Fwww.holbertonschool.com%2F&usg=AOvVaw3QMtFQxWuUceikrBH0XyZD">ALX SE Programme</a>
