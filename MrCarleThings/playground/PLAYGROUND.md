# Playground

**Purpose:** A place for experiments, tutorials, and "does this work?" code.

**Rule:** If it's not part of your actual IA project yet, put it here.

---



## What Goes Here?

✅ **Tutorial code you're following**
- Flask tutorial examples
- Authentication guide code
- Database examples from a book

✅ **Quick experiments**
- Testing if bcrypt works
- Trying different form layouts
- "Can I connect to the database?"

✅ **Prototype attempts**
- Login approach #1 (before deciding on final)
- Testing different algorithms
- UI mockup experiments

✅ **Learning snippets**
- Code from Stack Overflow you're trying
- Examples from documentation
- "How does this library work?" tests

---

## How to Use It

### Create a folder for each thing:

```
playground/
├── flask_tutorial/
│   └── app.py
├── bcrypt_test/
│   └── test_hashing.py
├── database_experiment/
│   ├── create_tables.py
│   └── test.db
└── ui_mockups/
    └── login_v1.html
```

### Name folders clearly:

**Good:**
- `flask_auth_tutorial/`
- `database_connection_test/`
- `password_hashing_experiment/`

**Bad:**
- `stuff/`
- `test/` (too vague)
- `asdf/`

### Add a quick note in each folder:

Create a `README.md` or comment at top of file:

```python
# Playground: Testing bcrypt password hashing
# Following: https://flask.palletsprojects.com/en/2.0.x/tutorial/
# Date: 2024-01-15
# Result: Works! Using this approach in src/auth.py

from bcrypt import hashpw, gensalt
# ... your test code ...
```

---

## Commit It!

**Yes, commit your playground code.**

**Why?**
- Shows your learning journey
- Can reference in RECORDS.md: "Tested approach in playground/bcrypt_test"
- IB likes to see your process
- Helps you remember what you tried

**Commit message examples:**
```bash
git commit -m "Added Flask tutorial code to playground"
git commit -m "Tested bcrypt in playground - it works!"
git commit -m "Experimented with three login form layouts"
```

---

## When Code Graduates from Playground

**Code worked? Move it to your real project:**

```bash
# You tested it in playground
playground/auth_test/login.py

# Now it's ready - move the good parts to src/
src/auth.py  # ← The actual code
src/templates/login.html

# Keep the playground version - shows your work!
```

**In your commit message:**
```bash
git commit -m "Implemented authentication (based on playground/auth_test)"
```

**In RECORDS.md or DEVELOPMENT.md:**
```markdown
I experimented with password hashing in `playground/bcrypt_test/` 
and determined bcrypt with salt rounds of 12 was appropriate.
```

---

## Playground vs Real Project

| Aspect | Playground | src/ (Real Project) |
|--------|-----------|---------------------|
| Purpose | Learning, testing | Actual IA product |
| Quality | Rough, experimental | Clean, working |
| Documentation | Quick notes | Full comments |
| Tests | Optional | Required |
| Organization | Loose | Structured |
| Commits | Frequent, rough messages | Clear messages |

**Think of it like:** Playground = your notebook, src/ = your final essay

---

## .gitignore Note

Some things in playground probably shouldn't be committed:

- Database files (`*.db`)
- Virtual environments (`venv/`)
- Large downloads
- API keys (never commit these!)

Check `.gitignore` - it handles most of this automatically.

---

## Examples of Good Playground Use

### Example 1: Tutorial

```
playground/flask_mega_tutorial/
├── chapter1/
│   └── hello.py
├── chapter2/
│   └── templates.py
├── chapter3/
│   └── forms.py
└── README.md  # Links to tutorial, notes on what I learned
```

### Example 2: Testing Approaches

```
playground/login_approaches/
├── basic_auth.py       # Tried first - too simple
├── flask_login.py      # Tried second - this works!
├── oauth_test.py       # Tried third - overkill
└── decision.md         # Why I chose flask_login
```

### Example 3: Quick Experiments

```
playground/
├── can_i_connect_to_db.py
├── does_bcrypt_work.py
├── test_email_validation.py
└── ui_experiments/
    ├── layout1.html
    ├── layout2.html
    └── layout3.html  # ← Liked this one, used in real project
```

---

## Tips

**Do:**
- ✅ Create a folder for each experiment/tutorial
- ✅ Add quick notes about what you're testing
- ✅ Commit your playground work
- ✅ Reference it in RECORDS.md when relevant
- ✅ Keep it even after code moves to src/

**Don't:**
- ❌ Mix playground and real project code
- ❌ Dump everything in one file
- ❌ Delete playground code (it shows your process!)
- ❌ Use playground as excuse for messy commits

---

## FAQ

**Q: Should I commit tutorial code?**  
A: Yes! Shows you're learning. Just note it's from a tutorial.

**Q: My playground is messy, is that OK?**  
A: Yes! That's the point. It's your workspace.

**Q: Can I delete playground code later?**  
A: Keep it! Shows your journey. Just don't let it clutter your final product.

**Q: Should playground code be as clean as real code?**  
A: No. Playground can be rough. Clean it up when moving to src/.

**Q: What if an experiment doesn't work?**  
A: Commit it anyway! Note in commit: "Tested X in playground - didn't work, trying Y next"

---

## Remember

**Playground is for:**
- 🎮 Playing with ideas
- 📚 Learning new things  
- 🧪 Testing approaches
- 🎨 Experimenting

**Not for:**
- ❌ Your final IA code (that's src/)
- ❌ Hiding messy work (it's OK to be messy here!)
- ❌ Skipping commits (commit playground work too!)

**The playground shows you're THINKING, not just copying tutorials.**


# Commit it
cd ../..
git add playground/my_experiment
git commit -m "Tested Flask-Login in playground - works well!"
git push
```

**That's it!** Now you have proof you tried it.
