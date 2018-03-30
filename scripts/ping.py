import shlex,subprocess
import threading


def run_cmd(command):
    '''
    Run ping command and print IP if there is response
    '''
    args = shlex.split(command)
    p = subprocess.Popen(args, stdout=subprocess.PIPE)
    out,err = p.communicate()
    lines = out.split("\n")
    for line in lines:
        if "bytes from" in line:
           print line.split(" ")[3].split(":")[0]

#create thread for each ping command
thread_list = []
for i in range(1,255):
    command = 'ping -c 1 10.11.1.{0}'.format(i)
    t = threading.Thread(target=run_cmd,args=(command,))
    thread_list.append(t)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()



