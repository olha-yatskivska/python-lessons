# 💻 Terminal & Codespaces Essentials

This guide covers the most frequently used commands within the GitHub Codespaces environment.

## 📁 File System Navigation
These commands help you move around and manage your folders.

| Command | Description | Example |
| :--- | :--- | :--- |
| `pwd` | **Print Working Directory**: Shows where you are right now. | `pwd` |
| `ls` | **List**: Shows all files and folders in the current directory. | `ls -la` (shows hidden files) |
| `cd` | **Change Directory**: Moves you to a different folder. | `cd functions/exercises` |
| `cd ..` | **Go Up**: Moves you back to the parent folder. | `cd ..` |
| `mkdir` | **Make Directory**: Creates a new folder. | `mkdir new-lesson` |
| `rm` | **Remove**: Deletes a file. | `rm old-file.py` |
| `clear` | **Clear**: Cleans the terminal screen. | `clear` |



---

## 🛠 Git Workflow (The Big Four)
As we discussed, Git doesn't sync automatically. You need these to talk to GitHub.

1.  **Check Status**: `git status` (See what has changed).
2.  **Add Changes**: `git add .` (Prepare all new/modified files).
3.  **Commit**: `git commit -m "Your message here"` (Save the snapshot).
4.  **Push/Pull**: 
    * `git push origin main` (Send your code to GitHub).
    * `git pull origin main` (Get the latest code from GitHub).

---

## 🐍 Python Commands
Since you are learning Python, these are your daily drivers.

* **Run a script**: `python3 filename.py`
* **Check version**: `python3 --version`
* **Install a library**: `pip install requests` (Useful later for API testing).

---

## 🧪 Terminal for Test Analysts
In a professional QA role, the terminal is used for more than just Git:

* **Running Tests**: `pytest` or `unittest` commands are usually run from here.
* **Viewing Logs**: `tail -f app.log` (Shows real-time updates of a log file to catch errors).
* **Checking Environment**: Checking if the server or database is "up" using `ping` or `curl`.

---

## ⌨️ Codespaces Keyboard Shortcuts
| Shortcut | Action |
| :--- | :--- |
| `Ctrl + ` ` (Backtick) | Open / Close the Terminal |
| `Ctrl + Shift + P` | Open Command Palette (Search for any setting) |
| `Tab` | **Auto-complete**: Type the first letters of a file and press Tab to finish it! |
| `Up Arrow` | Cycle through your previous commands (saves time typing). |

## 🗄️ SQLite 
| Shortcut | Action |
| :--- | :--- |
| `sqlite3 --version` |  Checks the installed SQLite version in the terminal |
| `sqlite3 trackdb.sqlite` | Opens the trackdb.sqlite database file (or creates it if it doesn't exist)|
| `sqlite> .databases` |  Lists the names and files of attached databases |
| `sqlite> .tables` | Lists all tables in the current database|
| `sqlite> .schema <table_name>` | Shows the CREATE statement for a specific table (useful for checking structure) |
| `sqlite> .quit` | Exits the SQLite prompt and returns to the standard terminal|


##  📊 Output Formatting (For Better Readability)
| Shortcut | Action |
| :--- | :--- |
| `sqlite> .headers on` |  Displays column names at the top of query results |
| `sqlite> .mode column` | Aligns data into neat columns (essential for manual data analysis)|


> [!TIP]
> Use the **Up Arrow** key to find a long command you typed 5 minutes ago instead of typing it again!
