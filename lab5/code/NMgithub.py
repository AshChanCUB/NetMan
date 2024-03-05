from git import Repo, Git

rep_path = "/home/student/Desktop/netman/git/NetMan/lab5/midterm_objective"

repo = Repo(rep_path)
git = Git(rep_path)

txt_file = 'router_data.txt'
jpg_file = 'CPU_Utilization_R1.jpg'


diff_txt = repo.git.diff("--", txt_file)
diff_jpg = repo.git.diff("--", jpg_file)

if diff_txt or diff_jpg:
    repo.git.add(txt_file)
    repo.git.add(jpg_file)

    print('Changes detected')
    repo.index.commit("Detected changes and pushed through NMgithub.py")

    origin = repo.remote.origin
    origin.push()
else:
    print('No changes detected')

