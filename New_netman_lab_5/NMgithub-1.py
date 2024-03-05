from git import Repo, Git

try:
    rep_path = "/home/student/Desktop/netman/git/NetMan"
    repo = Repo(rep_path)
    git = Git(rep_path)
    repo.git.add(update=True)
    repo.index.commit("Detected changes and pushed through NMgithub.py")
    origin = repo.remote('origin')
    origin.push()
except Exception as e:
    print(e)
    

