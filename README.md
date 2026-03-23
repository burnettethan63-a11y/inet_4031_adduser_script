# inet_4031_adduser_script
# Program Description:
This program automates the process of creating user accounts on Ubuntu systems. It makes the process of system administration much quicker, consistent, and is much less error-prone than adding one user at a time. Normally, a system admin would use the command line to create new users. They would use the sudo adduser username or sudo useradd -m username command, then assign passwords and create home directories. As you can see, this process looks like it takes a while and is pretty repetitive. This Python script uses the same Ubuntu user-management commands and runs them automatically through the program, so the user does not have to type each command manually every time.  

# Program User Operation:
The purpose of this scripting program is to automate the creation of user accounts on an Ubuntu system from an input file. Instead of manually typing in all of the user information commands, all the administrator has to do is create a list of all the users they need. After that, the script then processes the user records, creates the accounts, sets passwords, and adds users to their respective groups if needed. On top of that, the script has a dry run feature that allows the administrator to view the script before actually running it. 

# Input file format:
The file contains one user per line, and each of the lines must have five fields that are separated by colons. username:password:last:first: groups. 
* Purpose of each field:
* Username: Login name for the new account
* Password: The accounts' assigned password
* Last: User's last name
* First: User's first name
* Groups: any assigned groups

# Command Execution
To run the code, you need to make the Python file executable by using (chmod +x create-users.py). Then redirect input to the file by using (./create-users.py < create-users.input). Then run it by using (sudo ./create-users.py < create-users.input)

# Dry run
You can complete a dry run by putting a '#' next to the operating lines of code. This way, you can test to see what your program does without it actually making any changes to your system. It prints the commands that would have run, which lets you see if your code works correctly. 
