# Processes and signals

## Description
> This repository contains scripts that are created as part of the learning objectives of programming at ALX SE programme. The emphasis is on enforcing problem solving skills through programming and other technologies. The Bash files created are for a deeper understanding of processes and signals in shell scripting.

## Learning Objectives
- What is a PID
- What is a process
- How to find a process’ PID
- How to kill a process
- What is a signal
- What are the 2 signals that cannot be ignored

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
0. **0-what-is-my-pid** - Write a Bash script that displays its own PID.
<br>

1. **1-list_your_processes** - Write a Bash script that displays a list of currently running processes.
    * Must show all processes, for all users, including those which might not have a TTY
    * Display in a user-oriented format
    * Show process hierarchy
<br>

2. **2-show_your_bash_pid** - write a Bash script that displays lines containing the `bash` word, thus allowing you to easily get the PID of your Bash process.
    * You cannot use `pgrep`
    * The third line of your script must be `# shellcheck disable=SC2009`
<br>

3. **3-show_your_bash_pid_made_easy** - Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.
    * You cannot use `ps`
<br>

4. **4-to_infinity_and_beyond** - Write a Bash script that displays `To infinity and beyond` indefinitely.
    * In between each iteration of the loop, add a `sleep 2`
<br>

5. **5-dont_stop_me_now** - Write a Bash script that stops `4-to_infinity_and_beyond` process.
    * You must use `kill`
<br>

6. **6-stop_me_if_you_can** - Write a Bash script that stops `4-to_infinity_and_beyond` process.
    * You cannot use `kill` or `killall`
<br>

7. **7-highlander** - Write a Bash script that displays:
    * `To infinity and beyond` indefinitely
    * With a `sleep 2` in between each iteration
    * `I am invincible!!!` when receiving a `SIGTERM` signal
<br>

8. **8-beheaded_process** - Write a Bash script that kills the process `7-highlander`.
<br>

9. **100-process_and_pid_file** - Write a Bash script that:
    * Creates the file `/var/run/myscript.pid` containing its PID
    * Displays `To infinity and beyond` indefinitely
    * Displays `I hate the kill command` when receiving a SIGTERM signal
    * Displays `Y U no love me?!` when receiving a SIGINT signal
    * Deletes the file `/var/run/myscript.pid` and terminates itself when receiving a SIGQUIT or SIGTERM signal
<br>

10. **101-manage_my_process, manage_my_process** - Write a `manage_my_process` Bash script that:
    * Indefinitely writes `I am alive!` to the file `/tmp/my_process`
    * In between every `I am alive!` message, the program should pause for 2 seconds
    * Write Bash (init) script `101-manage_my_process` that manages `manage_my_process`. (both files need to be pushed to git)
        * When passing the argument `start`
            * Starts `manage_my_process`
            * Creates a file containing its PID in `/var/run/my_process.pid`
            * Displays `manage_my_process` started
        * When passing the argument `stop`
            * Stops `manage_my_process`
            * Deletes the file `/var/run/my_process.pid`
            * Displays `manage_my_process` stopped
        * When passing the argument `restart`
            * Stops `manage_my_process`
            * Deletes the file `/var/run/my_process.pid`
            * Starts `manage_my_process`
            * Creates a file containing its PID in `/var/run/my_process.pid`
            * Displays `manage_my_process` restarted
        * Displays `Usage: manage_my_process {start|stop|restart}` if any other argument or no argument is passed
<br>

11. **102-zombie.c** - Write a C program that creates 5 zombie processes.
    * For every zombie process created, it displays `Zombie process created, PID: ZOMBIE_PID`
    * Your code should use the Betty style. It will be checked using `betty-style.pl` and `betty-doc.pl`
    * When your code is done creating the parent process and the zombies, use the function bellow
<br>

---
## Author
* Siphamandla Matshiane, [![Twitter](http://i.imgur.com/wWzX9uB.png)](https://twitter.com/sbumatshiane916) 

## LICENSE
[ALX Software Engineering](https://www.alxafrica.com/software-engineering/)
