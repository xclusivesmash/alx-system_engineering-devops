# Shell Permissions

### Description
This project contains shell scripts that are based on shell permissions in a Linux system. The scripts were developed as part of the learnign curriculum at ALX SE programme.

### Requirements
* Language(s): `Bash`
* OS: Ubuntu 20.04 LTS
* Editor(s): `vim`, `vi`, or `emacs`
* All files must be executables.

### Objectives
* What do the commands `chmod`, `sudo`, `su`, `chown`, `chgrp` do.
* Linux file permissions.
* How to represent each of the three sets of permissions (owner, group, and other) as a single digit.
* How to change permissions, owner and group of a file.
* Why can’t a normal user chown a file.
* How to run a command with root privileges.
* How to change user ID or become superuser.

### Scripts
0. **0-iam_betty** - Creates a script that switches the current user to the user `betty`.<br>
1. **1-who_am_i** - Creates a script that prints the effective username of the current user.<br>
2. **2-groups** - prints all the groups the current user is part of.<br>
3. **3-new_owner** - changes the owner of the file `hello` to the user `betty`.<br>
4. **4-empty** - creates an empty file called `hello`.<br>
5. **5-execute** - adds execute permission to the owner of the file `hello`.<br>
6. **6-multiple_permissions** - adds execute permission to the owner and the group owner, and read permission to other users, to the file `hello`.<br>
7. **7-everybody** - adds execution permission to the owner, the group owner and the other users, to the file `hello`.<br>
8. **8-James_Bond** - sets the permission to the file `hello` as follows: Owner: no permission at all, Group: no permission at all, Other users: all the permissions.<br>
9. **9-John_Doe** - sets the mode of the file `hello` to this: `-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello`.<br>
10. **10-mirror_permissions** - sets the mode of the file `hello` the same as `olleh’s` mode.<br>
11. **11-directories_permissions** - adds execute permission to all subdirectories of the **current directory** for the owner, the group owner and all other users.<br>
12. **12-directory_permissions** - creates a directory called `my_dir` with permissions 751 in the working directory.<br>
13. **13-change_group** - changes the group owner to `school` for the file `hello`.<br>
14. **100-change_owner_and_group** - changes the owner to `vincent` and the group owner to `staff` for all the files and directories in the working directory.<br>
15. **101-symbolic_link_permissions** - changes the owner and the group owner of `_hello` to `vincent` and `staff` respectively.<br>
16. **102-if_only** - changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume`.<br>
17. **103-Star_Wars** - plays the StarWars IV episode in the terminal.<br>

### Author(s)
* Siphamandla Matshiane

### LICENSE
* ALX SE Programme
