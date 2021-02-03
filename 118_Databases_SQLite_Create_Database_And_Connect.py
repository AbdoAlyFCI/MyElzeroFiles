# --------------------------------------------------------
# -- Databases => SQLite => Create Database And Connect --
# --------------------------------------------------------
# - Connect
# - Execute
# - Close
# --------------------------------------------------------

# Import SQLite
import sqlite3

# Create Database And Coonect
db = sqlite3.connect("app.db")

# Create The Tables and Fields
db.execute("Create Table if not exists skills (name TEXT, prgress integer, user_id integer)")

# Close Database
db.close()