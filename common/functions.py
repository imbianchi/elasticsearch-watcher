import os
import subprocess
import pprint


# run OS commands
def cmd(cmd=str, message=str, output=False):
    pprint.pprint(message)

    if output:
        try:
            output = subprocess.check_output(cmd, shell=True)
        except subprocess.CalledProcessError as grepexc:
            return grepexc

    else:
        os.system(cmd)
