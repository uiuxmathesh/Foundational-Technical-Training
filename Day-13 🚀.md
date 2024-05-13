# Day-13 🚀

# Git & Github

Git Commands

- Starting a Project

```powershell
git init
```

- File suffix and meaning
    
    U - Untracked (New files)
    
    M - Modified (Existing file. Modified)
    
    A - Added
    
- Adding all the files to staging area

```powershell
git add .
```

- For bringing back all the changes from staged changes to  Changes area

```powershell
git reset
```

- Adding particular file instead of all change

```powershell
git add #filename or Relative address
```

## Git Commits

- Committing changes

```powershell
git commit -m "Commit message here"
```

- Checking the Git’s change log

```powershell
git status
```

This will return a detailed status log. If you want a shorter version add verbose `--short` or `-s` 

## Git logs

- To see the commit log

```powershell
git log
```

- For documentation Help

```powershell
git log --help
```

- To see what are all things that are patched or changed

```powershell
git log -p
```

- Pick-axe command in git is used to log commit information particular to addition of deletion of particular instance

```powershell
git log -S(word to be searched) -p 
```

Once it is typed the output will show the changes matching the pick-axe syntax. You can highlight them using `/`  

## Undoing commit

- Revisting commit

```powershell
#For going to a particular commit
git checkout <commit_id>
#Foe coming back to master branch.
git checkout - 
```

by revisiting the commits we can know which commit to delete

- Method 1:
    
    Undoing commits using `revert` (History will be maintained)
    
    ```powershell
    git revert <commit_id>
    ```
    
    Undoing commits using `reset` (SOFT reset: For editing the commit and commiting again)
    
    ```powershell
    git reset --SOFT HEAD~1
    ```
    
    Undoing commits using `reset` (HARD reset: For deleting the commit and commiting again)
    
    ```powershell
    git reset --HARD HEAD~1
    ```
    

## Git Branches

To create a branch in git

```powershell
git  checkout -b branchName
```

Switching between branches

```powershell
git checkout branchName
```

Delete a branch

```powershell
git checkout -D branchName
```

Game for learning branches

[https://learngitbranching.js.org/](https://learngitbranching.js.org/)

rebase

stash