
import subprocess

for i in range(20):
    print(i)
    if i > 10:
        cmd = 'echo sendEmail > /home/pi/Documents/rpiWebServer/test_fifo'
        print(subprocess.check_output(cmd, shell=True))
        break
