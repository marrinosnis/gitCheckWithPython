import git
import os
from tkinter.filedialog import askdirectory
from pathlib import Path
from subprocess import call, STDOUT


while True:
    out_path = input("Please give the directory path to check if it has repository")
    path = Path(out_path)

    if call(["git", "-C", path, "branch"], stderr=STDOUT, stdout=open(os.devnull, 'w')) != 0:
        print("The current directory is NOT a git repository. Try another\n")
    else:
        break

repo = git.Repo("~/Desktop/gitTest")

# find all local branches
local_branches = []
for branch in repo.branches:
    local_branches.append(branch)
    print(branch)

# print(local_branches)

nameBranch = "master"
try:
    if not repo.remotes.origin.pull():
        print("No changes in the current branch")
    else:
        ask = input("There are new changes from the fetch action.\nWould you like to merge the fetched changes")
        if ask == "yes":
            # repo.remotes.origin.fetch()
            # repo.git.execute('git merge')
            repo.remotes.origin.pull()
            print("\nThe new changes have been merge in your current branch!!")
        else:
            print("You didn't merge the new changes from the fetch action")

except Exception as error:
    print(error, "\nProbably you should add the ssh key in the project\nExecution of command to add the key...")
    os.system("ssh-add")
    print("Now your ssh key must have been add it in the project")

    if not repo.remotes.origin.fetch():
        print("No changes in the current branch")
    else:
        ask = input("There are new changes from the fetch action.\nWould you like to merge the fetched changes")
        if ask == "yes":
            # repo.remotes.origin.fetch()
            # repo.git.execute('git merge')
            repo.remotes.origin.pull()
            print("\nThe new changes have been merge in your current branch!!")
        else:
            print("You didn't merge the new changes from the fetch action")
