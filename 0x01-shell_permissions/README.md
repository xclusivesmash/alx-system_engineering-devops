# Shell - Permissions

### Description
This repository was created for primarily learning shell permissions through the alx software engineering programme.

### Requirements
* Languages: Bash
* OS: Ubuntu 20.04 LTS
* Editors: ```vi```, ```vim```, or ```emacs```.

### Concepts
* What do the commands ```chmod```, ```sudo```, ```su```, ```chown```, ```chgrp``` do.
* Linux file permissions
* How to represent each of the three sets of permissions (owner, group, other) as a single digit.
* how to change permissions, owner and group of a file.
* Why can't a normal user ```chown``` a file.
* How to run commands wit root priviledges.
* How to change user ID or become superuser.

### SCRIPT DESCRIPTION

1. **0-iam_betty** switches the current user to ther user betty.<br>
2. **1-who_am_i** prints the effective username of the current user.<br>
3. **2-groups** prints all the groups that the current user is part of.<br>
4. **3-new_owner** changes the owner of the file *hello* to the user *betty*<br>
5. **4-empty** creates an empty file called *hello*.<br>
6. **5-execute** adds execute permissions to the owner of the file *hello*.<br>
7. **6-multiple_permissions** add executive permissions to the owner and the group owner, and read permissions to other users to the file *hello".<br>
8. **7-everybody** adds execusion permission to the owner, group owner, and the other users, to the file hello.<br>
9. **8-James_Bond** gives some permissions to the file hello.<br>
10. **9-John_Doe** sets the mode of the file *hello* to 753.<br>
11. **10-mirror_permissions** sets the mode of the file *hello> the same as *olleh's* mode.<br>
12. **11-directories_permissions** sets execute permissions to all subdirectories of the current directory for the owner, the group owner and all others.<br>
13. **12-directory_permissions** creates a directory *my_dir* with permission 751 in the current directory.<br>
14. **13-change_group** changes the group owner to *school* for the file *hello*.<br>
15. **100-change_the_owner_and_group** changes the owner to 'vincent' and group ownert to 'staff' for all files and directories in the current directory.<br>
16. **101-symbolic_link_permissions** changes the owner and the group owner of *_hello* to "vincent" and "staff" respectively.<br>
17. **102-if_only** changes the owner of the file *hello* to *betty* only if it is owned by the user "guillaume".<br>
18. **103-Star_Wars** simply plays the StarWarsa IV episode in the terminal.<br>

### Authors
* Siphamandla Matshiane

### License
* The Holberton School/ALX SE Programme
