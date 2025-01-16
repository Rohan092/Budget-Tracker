# Budget-Tracker
A budget tracker web app that allows users to manage their income and expenses. The app performs basic financial operations, including adding transactions, viewing them, analyzing expenses by category, and deleting transactions. It stores data in a local JSON file.<br/>
The code provided outlines a simple Flask web application for tracking a budget with functionalities such as adding income and expenses, analyzing expenses by category, and deleting transactions.

# Key features
## 1. Data Persistence with JSON:
The app stores budget data (income and expenses) in a budget_tracker_data.json file, ensuring persistence across server restarts.<br/>
## 2. Home Page:
Displays total income, total expenses, remaining budget, and lists all transactions for a quick financial overview.<br/>
## 3. Add Transaction:
Users can add income or expense transactions through a form, with data saved in the JSON file, and a redirect to the home page after submission.<br/>
## 4. Analyze Expenses:
The app categorizes expenses and displays the total amount for each category, helping users understand spending patterns.<br/>
## 5. Delete Transaction:
Users can delete specific income or expense transactions by index, with the updated data saved back to the file.<br/>
## 6. View Transactions:
Displays all transactions of a specific type (income or expense) for a focused financial view.<br/>

# Key Insights
## 1. Modularity:
The app uses well-defined routes to handle specific tasks (viewing, adding, deleting, and analyzing transactions), keeping the code organized.<br/>
## 2. Template Rendering:
Flask’s render_template function renders dynamic HTML templates to display financial data on the frontend.<br/>
## 3. Dynamic Data Handling:
Real-time data updates are possible through dynamic loading, modification, and saving of data in the JSON file.<br/>
## 4. Simplified Budget Tracking:
Focuses on basic functionality: adding, viewing, and analyzing income/expenses, making it easy for users to manage their finances.<br/>
## 5. Scalability:
The app can be expanded with additional features like handling different currencies, recurring expenses, or user authentication for multi-user support.<br/>

# Repository Structure
• Data : https://github.com/Rohan092/Budget-Tracker/blob/main/Budget%20Tracker.zip<br/>
• Python Code : [Expense (.py) File](https://github.com/Rohan092/Budget-Tracker/blob/main/expense.py)<br/>
• HTML Code : [Index (.html) File](https://github.com/Rohan092/Budget-Tracker/blob/main/index.html)<br/>
• Image 1 : ![p1](https://github.com/user-attachments/assets/b5f0f1c4-8bf3-4bbb-a331-4f21761d4eef)<br/>
• Image 2 :![p2](https://github.com/user-attachments/assets/1c12e63c-3e47-4892-ae51-0bc3d55a15d4)</br>

# Feedback & Collabration
Your feedback is always appreciated! If you’re interested in collaborating on similar projects or discussing new opportunities, feel free to reach out. I’m always open to connecting and sharing insights!
