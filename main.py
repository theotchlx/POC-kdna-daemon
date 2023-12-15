"""
This program is started at boot by the kdna daemon. It generates a log every x seconds to demonstrate the python service.

The program takes one integer command-line argument as input, interpreted as the time in seconds between logs.

Contents:
    - :func:`main`: generates logs every x seconds (delay given as command-line argument).

:author: TCHILINGUIRIAN Théo
:email: theo.tchlx@gmail.com
:date: 2023-12-15
"""


import subprocess
import time
import sys


def main():
    """
    Main function.

    Inputs:
        No parameters.
        This function takes one command-line argument x, an integer interpreted as the time in seconds between logs.
    Ouputs:
        0 -> no errors or exceptions.
        1 -> Generic error 'Exception'.
        2 -> 'ValueError' (e.g. during type conversion).
        3 -> 'IndexError' (e.g. during sys.argv list traversal).
    """
    """
    Main function. Generates logs every on a given delay in seconds (delay given as command-line argument).

    The command-line argument is retrieved in a try/catch block. If no exceptions are raised, an infinite loop starts and the function creates logs periodically.

    :return: returns an error code among (0, 1, 2, 3)
    :rtype: int

    :raises ValueError: May occur during conversion of the command-line argument from string to integer.
    :raises IndexError: May occur during argument list traversal (empty sys.argv list, no command-line arguments).

    :note:
    The imported packages are subprocess, time and sys.
    subprocess is used to run bash commands in a shell from the program.
    time is used to wait for the chosen delay between logs.
    sys is used to retrieve command-line arguments
    """


    try:
        x = int(sys.argv[1])  # This catches the first argument (if it exists) after main.py in the command-line. Pattern example : python3 main.py arg1 arg2 arg3 ...

    except ValueError as err:
        print(f"An error occurred during argument conversion, please input an integer. The error is as follows: {err} - dated $(date)")
        return 2
    
    except IndexError as err:
        print(f"An error occurred during argument list traversal, this program requires an integer argument to define log delay. The error is as follows: {err} - dated $(date)")
        return 3
    # The catched exception messages appear in `journalctl -u kdnad` and in `systemctl status kdnad.service`

    else:  # Entered only if try was successful and no exceptions raised.
        i=0
        while 1:
            i+=1
            command = 'echo "Hi ! This log is dated $(date) - log number {} of session - and will log every {} seconds." >> /root/kdna_service/logs.txt'.format(i, x)
            subprocess.run(command, shell=True, check=True)
            time.sleep(x)  # New log every x seconds.
        return 0

    return 1  # Catches general exceptions / errors


# End of function definitions #

if __name__ == '__main__':
    main()

