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
