# What to Write for a Commit Message

**Stuck? Use this formula:**

git commit -m "This is where you put the message"

```
[VERB] + [WHAT YOU DID]
```

Your commit messages are notes to Future You about what Present You JUST DID.

Commit Messages carry timestamps, and make a great rough draft fro Crit B: Record Of Tasks



---

## Quick Decision Tree

**Did you add something new?**
→ `Added [what]`

**Did you fix something broken?**
→ `Fixed [what]`

**Did you change how something works?**
→ `Updated [what]`

**Did you remove something?**
→ `Removed [what]`

**Did you improve code without changing behavior?**
→ `Refactored [what]`

---

## Starter Verbs (Pick One)

- **Added** - new feature, file, function
- **Fixed** - bug fix
- **Updated** - modified existing thing
- **Removed** - deleted code/file
- **Refactored** - improved structure
- **Created** - new file/component
- **Implemented** - completed planned feature
- **Changed** - altered behavior

---

## Examples for Common Situations

### Created a new file?
STILL COMMIT! 
```
Added main.py with basic Flask app structure
Created database.py for SQLite connection
Added login.html template
```

###Got something working?
```
Implemented user registration
Added password hashing with bcrypt
Fixed login validation bug
```

### Changed existing code?
```
Updated login form to include email field
Refactored database functions into separate file
Changed error messages to be more helpful
```

### Just removed something?
```
Removed unused import statements
Deleted old test file
Removed debug print statements
```

### Working on tests?
```
Added test for user registration
Fixed failing test in test_login.py
Updated test data to match new schema
```

### Documentation?
```
Added comments to authentication function
Updated README with installation instructions
Created design diagram for database
```

---

## Still Stuck? Answer These:

1. **What file(s) did you change?**
   → Include the filename or feature area

2. **Why did you make this change?**
   → That's your commit message!

3. **If I undo this commit, what stops working?**
   → Describe that thing

---

## Examples with Context

### Scenario: You just added a login form

**Bad:** `stuff`  
**Bad:** `updated`  
**Good:** `Added login form HTML`  
**Better:** `Added login form with email and password fields`

### Scenario: You fixed a bug where emails weren't validating

**Bad:** `fixed`  
**Bad:** `it works now`  
**Good:** `Fixed email validation bug`  
**Better:** `Fixed email validation to reject invalid formats`

### Scenario: You created database tables

**Bad:** `database`  
**Bad:** `made tables`  
**Good:** `Created user and booking tables`  
**Better:** `Created database schema with users and bookings tables`


---
## When in Doubt

Ask yourself: **"What can I now do that I couldn't before?"**

That's your commit message.
