### 🧐 What this expense tracker does?

It’s a simple command-line program that helps you keep track of your expenses. You can add, remove, and view expenses with just a few inputs, and it even gives you a basic layer of privacy with password authentication.

---

### ✨ What features are currently there?

Let’s break it down:

- 🔐 **User authentication**
    
- ➕ **Adding expenses**
    
- ➖ **Removing expenses**
    
- 👁️ **Viewing all expenses**
    
- 📅 **Chronological sorting**
    
- 🏷️ **Category tagging**
    
- 🧠 **Password change via master key**
    

---

### 💡 How to use this tiny program efficiently?

#### 🧍 User Level Functionality

---

#### ➕ Adding an Expense

Just follow the prompts:

- Enter the date (must be in `DD-MM-YYYY` format),
    
- Choose a category (like Food, Transport, etc.),
    
- Enter the amount (in ₹).
    

Your expense is logged and saved in a file. That’s it!

---

#### ➖ Removing an Expense

This is super easy. Even a caveman can do it 🪨.

- You'll see a list of expenses with serial numbers.
    
- Just enter the number of the expense you want to delete.
    
- Done.
    

---

#### 👁️ Viewing Expenses

- You can see all your expenses at once.
    
- They are sorted by date so you get a clear timeline.
    
- Bonus: each entry shows date, category, and amount.
    

---

### 🛠️ Under The Hood

Here’s what’s going on behind the scenes:

- 🗂️ **File-based storage**: All data is stored in `data/expense.txt`. When you add or remove something, this file gets updated.
    
- 🔐 **Authentication system**: On the first run, you set up a username and password. The app stores it in `data/credentials.txt`. Only the correct user can access the app.
    
- 🛡️ **Master password for recovery**: If you forget your password, you can reset it using a predefined master password (`root` by default).
    
- 📅 **Smart sorting**: Expenses are sorted chronologically using Python’s `datetime` module. So the list stays neat.
    
- 🚫 **Input validation**: The date must follow `DD-MM-YYYY` format, and the app checks for that.
    

> ⚠️ Note: There’s no strong encryption here, but storing credentials and files in a structured way lays the foundation for later improvements.

---

### 🧪 How to Run the Program

Make sure you have Python 3.x installed. Then:

1. Navigate to the project folder.
    
2. Run it using:
    `python expense_tracker.py`

If you run it for the first time, it'll ask you to set up a username and password.

### 🚀 Future Improvements (My Wishlist)

Here are some features I plan to add soon:

- 🔐 Stronger encryption for stored data
    
- 📊 Graphical visualisation of expenses (monthly charts, category distribution)
    
- 🧾 Exporting data to CSV
    
- 🖼️ GUI version with `tkinter` or `PyQt`
    
- 📤 Cloud sync (maybe even Firebase?)
    
- 📧 Monthly email summaries
    
- 👥 Multiple user profiles
    

---

### 🧑‍💻 Author Notes

I built this project to get better at:

- File handling in Python
    
- Basic CLI design
    
- Date and string manipulation
    
- User authentication systems
    

It’s a humble tool, but it gets the job done for managing my daily expenses. It’ll evolve with me as I keep learning.
