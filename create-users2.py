#!/usr/bin/python3

# INET4031
# Ethan Burnett
# Date Created: 3/22/26
# Date Last Modified: 3/22/26

# Import os to run Linux system commands from Python
import os
# Import re to detect comment lines that begin with #
import re
# Import sys to read lines from standard input
import sys

def main():
    # Ask the user whether to do a dry run or actually execute the commands
    run_mode = input("Run in dry-run mode? (Y/N): ") if sys.stdin.isatty() else open('/dev/tty').readline().strip().upper()
    dry_run = (run_mode == "Y")

    # Process the input file one line at a time from standard input
    for line in sys.stdin:
        original_line = line.strip()

        # Check whether the line starts with # so it can be skipped as a comment
        match = re.match("^#", line)

        # Split the line into fields using : as the delimiter
        fields = line.strip().split(':')

        # Skip lines that are marked with # and optionally report that in dry-run mode
        if match:
            if dry_run:
                print("Skipping line: %s" % original_line)
            continue

        # Skip lines that do not contain exactly 5 fields and optionally report the error in dry-run mode
        if len(fields) != 5:
            if dry_run:
                print("Error: invalid line format: %s" % original_line)
            continue

        # Store the user account data from the input file fields
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split the comma-separated group list into individual groups
        groups = fields[4].split(',')

        # Build the command to create the user account
        print("==> Creating account for %s..." % username)
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        if dry_run:
            print(cmd)
        else:
            os.system(cmd)

        # Build the command to set the user's password
        print("==> Setting the password for %s..." % username)
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/passwd %s" % (password, password, username)
        if dry_run:
            print(cmd)
        else:
            os.system(cmd)

        # Add the user to each listed group unless the placeholder - is used
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                if dry_run:
                    print(cmd)
                else:
                    os.system(cmd)

if __name__ == '__main__':
    main()
