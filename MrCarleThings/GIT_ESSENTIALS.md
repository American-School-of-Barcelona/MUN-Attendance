# Git Essentials - Command Reference

**Copy-paste these commands.** Replace things in `[brackets]` with your info.

---

## First Time Setup (Do Once)

### Tell Git who you are:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Check it worked:

```bash
git config --global --list
```

You should see your name and email.

---

## Starting Your IA Project

### Option 1: Clone Existing Repo (If teacher created it)

```bash
# Go to where you want the project
cd ~/Documents

# Clone the repo
git clone git@github.com:your-org/ia-yourname.git

# Go into it
cd ia-yourname

# You're ready to work!
```

### Option 2: Use Template (If using "Use this template" button)

1. Go to template repo on GitHub
2. Click green "Use this template" button
3. Name it `ia-yourname`
4. Create under your org
5. Clone it:

```bash
cd ~/Documents
git clone git@github.com:your-org/ia-yourname.git
cd ia-yourname
```

---

## Daily Workflow

### 1. Before you start working:

```bash
# Get latest changes (in case you worked on another computer)
git pull
```

### 2. Do your work:

Edit files, write code, etc.

### 3. See what changed:

```bash
git status
```

Shows files you've modified (in red).

### 4. Add files to commit:

**Add everything:**
```bash
git add .
```

**Add specific file:**
```bash
git add docs/PLANNING.md
```

**Add multiple specific files:**
```bash
git add src/app.py src/database.py
```

### 5. Check what's staged:

```bash
git status
```

Now shows files in green (ready to commit).

### 6. Commit with message:

```bash
git commit -m "Added user registration feature"
```

See COMMIT_HELP.md if stuck on message!

### 7. Push to GitHub:

```bash
git push
```

### 8. Verify it worked:

Go to GitHub in browser, should see your commit!

---

## Common Workflows

### Making Your First Commit

```bash
# Make sure you're in the project directory
cd ~/Documents/ia-yourname

# Edit a file (example)
nano README.md

# See what changed
git status

# Add your changes
git add README.md

# Commit
git commit -m "Updated README with my project name"

# Push to GitHub
git push

# Check on GitHub - should see your change!
```

### Working on a Feature

```bash
# Pull latest
git pull

# Create/edit files
# ... do your work ...

# Add everything
git add .

# Commit
git commit -m "Implemented login form"

# Push
git push
```

### Multiple Commits in One Session

```bash
# Do work on feature 1
git add src/login.py
git commit -m "Added login validation"
git push

# Do work on feature 2
git add src/database.py
git commit -m "Created user table"
git push

# Update docs
git add docs/DEVELOPMENT.md
git commit -m "Documented login validation technique"
git push
```

**Tip:** Commit each time something WORKS. Don't wait!

---

## Checking Your Work

### See commit history:

```bash
git log --oneline
```

Shows your commits. Press `q` to quit.

### See what changed in a file:

```bash
git diff README.md
```

### See what you're about to commit:

```bash
git diff --staged
```

### See remote URL:

```bash
git remote -v
```

Should show your GitHub repo.

---

## Fixing Mistakes

### Undo changes to a file (before committing):

```bash
git checkout -- filename.py
```

**Warning:** This deletes your changes! Use carefully.

### Forgot to add a file to last commit:

```bash
git add forgotten-file.py
git commit --amend --no-edit
git push --force
```

**Warning:** Only if you haven't pushed yet, or be careful!

### Undo last commit (keep changes):

```bash
git reset --soft HEAD~1
```

Files stay changed, just uncommits them.

### Undo last commit (delete changes):

```bash
git reset --hard HEAD~1
```

**Warning:** Deletes your work! Use only if you're sure.

---

## Working with Branches (Advanced)

### See current branch:

```bash
git branch
```

Shows `* main` (you're on main).

### Create new branch:

```bash
git checkout -b experiment-feature
```

### Switch branches:

```bash
git checkout main
git checkout experiment-feature
```

### Merge branch into main:

```bash
git checkout main
git merge experiment-feature
git push
```

**For IA:** Usually just use `main` branch. Use feature branches only for experiments.

---

## Troubleshooting

### "Your branch is ahead of origin/main"

You committed but forgot to push:
```bash
git push
```

### "Your branch is behind origin/main"

You worked on another computer:
```bash
git pull
```

### "fatal: not a git repository"

You're not in the project folder:
```bash
cd ~/Documents/ia-yourname
```

### "Permission denied (publickey)"

SSH key not set up. See SSH_SETUP.md

### "failed to push some refs"

Someone else pushed. Pull first:
```bash
git pull
git push
```

### Made changes to wrong file?

See what you changed:
```bash
git status
git diff filename
```

Don't want those changes:
```bash
git checkout -- filename
```

### Committed to wrong branch?

**If not pushed yet:**
```bash
git reset --soft HEAD~1
git checkout correct-branch
git add .
git commit -m "Your message"
```

---

## Quick Reference Card

### Daily commands:
```bash
git pull           # Get latest
git status         # See changes
git add .          # Stage everything
git commit -m ""   # Commit with message
git push           # Send to GitHub
```

### Checking:
```bash
git log --oneline  # See history
git diff           # See changes
git status         # What's staged?
```

### Fixing:
```bash
git checkout -- file   # Undo changes
git reset --soft HEAD~1  # Undo commit
```

---

## Example Session (Copy-Paste This!)

```bash
# Start
cd ~/Documents/ia-yourname
git pull

# Do your work...

# Done? Commit!
git status
git add .
git commit -m "Describe what you did"
git push

# Check it worked
git log --oneline
```

---

## First Day Checklist

- [ ] Installed Git
- [ ] Set up SSH key (see SSH_SETUP.md)
- [ ] Configured name/email (`git config --global`)
- [ ] Cloned your IA repo
- [ ] Made first commit
- [ ] Pushed successfully
- [ ] Saw it on GitHub

---

## When Stuck

1. Check where you are: `pwd`
2. Check git status: `git status`
3. Check branch: `git branch`
4. Read error message carefully
5. Google the error
6. Ask teacher (show error message!)

---

## Good Habits

✅ **Commit often** (when something works)  
✅ **Pull before starting work** (avoid conflicts)  
✅ **Clear commit messages** (you'll thank yourself later)  
✅ **Push frequently** (so work is backed up)  
✅ **Check GitHub** (make sure it worked)

❌ **Don't:** Work for days without committing  
❌ **Don't:** Use vague messages like "stuff"  
❌ **Don't:** Forget to push (work only on your laptop = risky)

---

## Help Commands

```bash
git help          # General help
git help commit   # Help for specific command
git status        # When lost, start here
```

---

## Remember

**Git is:**
- Your backup system (code on GitHub, not just laptop)
- Your timeline (see what you did when)
- Your evidence (for IB assessment)

**Commit early, commit often!**
