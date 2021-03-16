import subprocess
import sys


if(len(sys.argv) <= 1):
    print("IP address belum diberikan")
else:
    cmd = ['ping', '-c1', sys.argv[1]]
    res = subprocess.check_output(cmd)
    if(res):
        print('UP')
    else:
        print('DOWN')





