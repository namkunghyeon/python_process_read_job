import subprocess

def subprocessOpen(command):
    return subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)


if __name__ == '__main__':
    (stdoutdata, stderrdata) = subprocessOpen('ps -eo pid,lstart,cmd  | grep -v grep').communicate()
    print stdoutdata
