from git import Repo
import os

repo_path = "/home/student/Desktop/netman/git/NetMan/lab5/code"

# Check if the .git directory exists in the specified path
if os.path.isdir(os.path.join(repo_path, '.git')):
    repo = Repo(repo_path)
else:
    print(f"No Git repository found at {repo_path}. Please check the path or initialize a repository.")
    exit(1)

# Check if there are any commits in the repository
if not repo.heads:
    print("The repository has no commits yet.")
    # Here, you might want to handle the case where there are no commits
    # For example, you might want to make an initial commit if appropriate
else:
    # Check for unstaged changes
    changed_files = repo.index.diff(None)

    # Check for staged but uncommitted changes
    staged_files = repo.index.diff('HEAD')

    if changed_files or staged_files:
        print('Changes detected.')

        # Stage all changes
        repo.git.add(A=True)

        # Commit changes
        repo.index.commit("Detected changes and pushed through NMgithub.py")

        # Push changes to remote
        origin = repo.remotes.origin
        origin.push()
    else:
        print('No changes detected.')

