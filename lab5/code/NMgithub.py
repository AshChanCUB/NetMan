from git import Repo, Git
import os

rep_path = "/home/student/Desktop/netman/git/NetMan/lab5/code"


if os.path.isdir(os.path.join(rep_path, '.git')):
    repo = Repo(rep_path)
    git = Git(rep_path)
else:
    print(f"No Git repository found at {rep_path}. Please check the path or initialize a repository.")
    exit(1)


changed_files = repo.index.diff(None)
staged_files = repo.index.diff('HEAD') 


if changed_files or staged_files:
    repo.git.add(A=True)

    print('Changes detected')
    repo.index.commit("Detected changes and pushed through NMgithub.py")

    origin = repo.remote.origin
    origin.push()
else:
    print('No changes detected')

