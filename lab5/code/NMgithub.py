from git import Repo, Git
import os

rep_path = "/home/student/Desktop/netman/git/NetMan/lab5/midterm_objective"

repo = Repo(rep_path)
git = Git(rep_path)

txt_file = 'router_data.txt'
jpg_file = 'CPU_Utilization_R1.jpg'
repo.git.add(txt_file)
repo.git.add(jpg_file)