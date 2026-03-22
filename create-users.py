#!/usr/bin/python3

# INET4031
# Ethan Burnett
# Date Created: 3/22/26
# Date Last Modified: 3/22/26

# Import os to execute system-level commands
import os
# Import re to use regular expressions for filtering input lines
import re
# Import sys to read input from standard input (stdin)
import sys

def main():
    # Read each line of input
    for line in sys.stdin:

        # Check if the line starts with '#' 
        # These lines should be ignored 
        match = re.match("^#", line)

        # Remove whitespace and split the line into fields using ':'. 
        
        fields = line.strip().split(':')

        # Skip processing if the line is a comment OR does not contain exactly 5 fields
        # This ensures only properly formatted user records are processed
        if match or len(fields) != 5:
            continue

        # Extract user account information from the parsed fields
        username = fields[0]   # Username for the new account
        password = fields[1]   # Password for the account
        # GECOS field stores user information such as full name (First Last)
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split the group field into a list of groups (comma-separated in input)
        groups = fields[4].split(',')

        # Inform the admin that a new user account is being created
        print("==> Creating account for %s..." % (username))

        # Build the command to create a new user with a disabled password and specified GECOS info
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # Uncomment to execute the command after testing
        # os.system(cmd)

        # Inform the admin that the password is being set for the user
        print("==> Setting the password for %s..." % (username))

        # Build command to set the user's password using passwd via standard input
        # The password is echoed twice to satisfy passwd requirements
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # Uncomment to run the command when you are done
        # os.system(cmd)

        # Loops through each group and assigns the user to valid groups
        for group in groups:
            # Skips placeholder '-' which indicates no group assignment
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                # Build command to add user to the specified group
                cmd = "/usr/sbin/adduser %s %s" % (username, group)

                #  Uncomment to run the command when you are done
                # os.system(cmd)


if __name__ == '__main__':
    main()
