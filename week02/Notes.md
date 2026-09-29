Answer 1 :- 'pwd' is the pathway director and it prints the folder i am currently in. In my case it came /Users/rehaan.

Answer 2 :- 'ls' shows the folders in 'rehaan' folder whereas 'ls -a' shows all folders including the ones which are hidden. There are dots infront of them too.Like .Trash , .vscode , etc.

Answer 3 :- 'drwx------@' indicates ile type and permissions. The d means it's a directory. The next 9 characters are permissions in three groups of three (owner/group/others): rwx for the owner (read, write, execute), then ------ means the group and everyone else have no permissions at all.

Answer 4 :- That's a relative path because it doesn't start with a / .Relative paths are interpreted starting from your current working directory (wherever you are when you run the command, i.e. whatever pwd would show).

Answer 5 :- mv README-backup.md week01/ :-this moved the file to a different location (into the week01 folder), without changing its name.
mv README-backup.md old-readme.md  :— this renamed the file, without changing its location (still in week01, just a new name).

Answer 6 :- There are 15 folders on my PATH.

Answer 7 :- /Library/Frameworks/Python.framework/Versions/3.14/bin/python3

Answer 8 :- No they are not the same because different order of folders in PATH means different installs get "found first" even if we both have multiple Pythons installed.He installed Python via Homebrew,whereas I intalled the version that ships with macOS.

Answer 9 :- zsh: command not found: pyton3
When i typed it, the shell searched through each folder listed in my PATH variable, one by one, looking for an executable file with that exact name.But couldn't find any and hence reports command not found.

Answer 10 :- .venv didn't show up with plain ls because it starts with a dot (.), which makes it a hidden file/folder.Plain ls does not show hidden folders.

Answer 11 :- It modified the shell's PATH for this session, putting .venv/bin at the very front.That prefix is your shell's way of telling you that you're now inside an activated virtual environment.

Answer 12 :- /Users/rehaan/coding-cafe/.venv/bin/python3
No, they're not the same path they're two different files in two different locations.
'activate' didn't create a new Python or move anything it just temporarily rearranged the PATH so the virtual environment's copy wins the search, for as long as this environment stays activated.

Answer 13 :- Before I installed anything, pip list only showed pip itself. After I ran pip install requests, the second pip list showed 6 packages instead of just 1. The new ones were requests, urllib3, idna, charset-normalizer, and certifi.

Answer 14 :- /Library/Frameworks/Python.framework/Versions/3.14/bin/python3
This confirms that deactivate undoes what activate did it removes .venv/bin from the front of your PATH, so the shell goes back to searching in the normal order.

Answer 15 :- '-h' stands for "human-readable." Normally, ls -l shows file sizes in raw bytes (like 608 or 1048576), which is hard to read at a glance. Adding -h makes ls convert those numbers into more familiar units like 1.0K, 2.3M, or 1.5G so you can quickly tell how big a file actually is without doing math in your head. 

Answer 16 :- Pressing Ctrl + C interrupted whatever was running, but kept me inside Python, I still saw the >>> prompt afterward. Pressing Ctrl + D actually closed Python and took me back to my normal terminal prompt (%), the same way typing exit() would have.