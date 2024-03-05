from git import Repo, Git

try:
    rep_path = "/home/student/Desktop/netman/git/NetMan/lab5/code"
    repo = Repo(rep_path)
    git = Git(rep_path)
    repo.git.add(update=True)
    repo.index.commit("Detected changes and pushed through NMgithub.py")
    origin = repo.remote('origin')
    origin.push()
except Exception as e:
    print(e)
    


