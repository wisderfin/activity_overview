import subprocess
from time import sleep

date = list()
with open("date.txt", "r") as file:
    line = file.readline()
    while line:
        line = file.readline()
        if len(line) >= 8:
            l = line.strip().split('.')
            date.append(f'20{l[2]}-{l[1]}-{l[0]}')


for i in date:
    with open("temp-date.txt", "a") as file:
        file.write(f"{i}\n")
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "add", "temp-date.txt"])
        sleep(0.1)
        subprocess.run(["git", "commit", f"--date='{i}'", "-m", f"{i}"])
        sleep(0.1)

sleep(5)
subprocess.run(["git", "push"])

