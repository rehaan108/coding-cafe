# Lab 4 Notes

## Answer 1
When you use --global, it means the setting applies to every repository on your computer for your specific user account.
Without --global, Git defaults to --local. The configuration will only apply to the current Git repository you are actively working in inside your terminal. It will not affect any other folders or projects.

## Answer 2
'ls' command showed me the folders/files in coding cafe whereas 'ls -a' also showed the hidden files like .git and other files which start with a dot in coding-cafe.
.git is where Git stores the repository's data, like the commit history and settings, which is why it appeared after git init.
To look inside I ran the 'ls .git' command which showed me some other files and folders in it like HEAD, index and logs.

## Answer 3
git is offering me 5 files/folders to track which are .DS_Store, "Icon\r", lab4/, week01/, week02/.
Yes, two macOS system files are there in the list which i did not write .DS_Store and "Icon\r".

## Answer 4
The two macOS system files, .DS_Store and Icon\r, disappeared from the untracked list. 
Before .gitignore, Git offered to track them, but once .gitignore listed those names, Git started ignoring them. 
The other items (lab4/, week01/, week02/) stayed, and .gitignore itself appeared as a new untracked file.

## Answer 5
.gitignore should be committed, not ignored. 
It is part of the project, and committing it means the ignore rules are saved in the history and shared with anyone who clones the repo, so they don't accidentally commit files like .venv/.

## Answer 6
README.md moved from "Changes not staged for commit" to "Changes to be committed". 
In the three-places model, git add moved the change from the working directory to the staging area. It isn't in the repository yet, because that needs a commit.

## Answer 7
Git printed [main 33e5f20] Lab work so far, then 5 files changed, 86 insertions(+), followed by a "create mode" line for each new file (.gitignore, lab4/notes.md, and the week01 and week02 files).
 So the commit went on main, and 5 new files were saved with 86 added lines.

## Answer 8
'33e5f20' are the first 7 characters of the commit.
These character limits are designed to make project histories easy to read, search, and navigate within terminal screens and development tools.

## Answer 9
The four steps are: edit the file, check with 'git status', stage with 'git add', and save with 'git commit'. Then 'git log' shows the new commit in the history.

## Answer 10
GitHub shows 'README.md' automatically on the repository's front page, so it needs that exact name and has to be in the top folder. It is the first thing a visitor reads, so it explains what the project is.

## Answer 11
'gh auth login' logged me in to GitHub through the browser and saved my login credentials on my computer. It also set up Git to use them, so when I push, Git uses that saved login instead of asking for a password.

## Answer 12
The front page shows the contents of 'README.md', displayed as formatted text and not markdown. This is because GitHub automatically shows the README of a repository on its main page.
It shows the content i copied from section 6.

## Answer 13
No, pushing did not change my local history. 'git log --oneline' shows the same commits as before, because push only copies my commits to GitHub.

## Answer 14
A private repository still exists on GitHub, and only I and the people I invite can see it. 
A repository that does not exist on GitHub has no online copy at all, so there is no backup and nobody can be invited to see it.

