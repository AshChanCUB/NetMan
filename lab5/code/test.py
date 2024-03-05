from git import Repo, Git
import os

rep_path = "/home/student/Desktop/netman/git/NetMan/lab5/code"


if os.path.isdir(os.path.join(rep_path, '.git')):
    repo = Repo(rep_path)
    git = Git(rep_path)
else:
    print(f"No Git repository found at {rep_path}. Please check the path or initialize a repository.")
    exit(1)



txt_file = 'router_data.txt'
jpg_file = 'CPU_Utilization_R1.jpg'

with open(txt_file, 'r') as file:
    file_contents = file.read()
print(file_contents)


diff_txt = repo.git.diff("--", txt_file)
diff_jpg = repo.git.diff("--", jpg_file)

print(diff_txt)
print(diff_jpg)

if diff_txt or diff_jpg:
    repo.git.add(update=True)

    print('Changes detected')
    repo.index.commit("Detected changes and pushed through NMgithub.py")

    origin = repo.remote.origin
    origin.push()
else:
    print('No changes detected')

    print("------------------------OBJECTIVE 2 [TCP DUMP]-------------------------")
    subprocess.run(['python3', 'NMtcpdump.py'])
    print("------------------------OBJECTIVE 2 [DHCP Server IPv4]-------------------------")
    subprocess.run(['python3', 'NMdhcpserver.py'])

    print("------------------------OBJECTIVE 3 [SNMP]-------------------------")
    subprocess.run(['sudo python3', 'scapyLoad.py'])
    subprocess.run(['python3', 'NMsnmp.py'])

    print("------------------------OBJECTIVE 4 [GitHUB]-------------------------")
    subprocess.run(['python3', 'NMgithub.py'])

