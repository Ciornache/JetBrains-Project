import subprocess
import sys

# I am using the subprocess module to ensure communication between processes. 
# Popen creates a child process in master.py and then uses exec on this child process to run slave.py on it
# Subprocess.PIPE creates an Anonymous PIPE between master.py and slave.py, providing a way for the master.py process to communicate with slave.py. 
# One head in the PIPE is for reading, and the other for writing


if __name__ == '__main__':
    childProcess = subprocess.Popen([sys.executable, "slave.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr = subprocess.PIPE, text=True)
    childProcess.stdin.write("Hi\n"); childProcess.stdin.flush()
    response = childProcess.stdout.readline()
    if response.strip() == 'Hi':
        print('Master: The slave program said Hi')
    else:
        print('Master: The slave program is not functioning properly')
        childProcess.kill()
        exit(0)
    l:list[int] = []
    for _ in range(0, 100):
        childProcess.stdin.write("GetRandom\n"); childProcess.stdin.flush()
        response = childProcess.stdout.readline()
        l.append(int(response))
    childProcess.terminate()
    l.sort(); print(f'Master: The sorted list is {l}')
    print(f'Master: The median from the list is: {l[(len(l)-1) // 2]}')
    print(f'Master: The average from the list is: {sum(l) / len(l)}')