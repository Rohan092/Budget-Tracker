from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__,template_folder='template')

# Define file to store data
DATA_FILE = 'budget_tracker_data.json'

def load_data():
    """Load data from JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {'income': [], 'expenses': []}

def save_data(data):
    """Save data to JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/')
def home():
    """Display the home page."""
    data = load_data()
    total_income = sum(item['amount'] for item in data['income'])
    total_expenses = sum(item['amount'] for item in data['expenses'])
    remaining_budget = total_income - total_expenses
    return render_template('index.html', 
                           income=data['income'], 
                           expenses=data['expenses'], 
                           total_income=total_income, 
                           total_expenses=total_expenses, 
                           remaining_budget=remaining_budget)

@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    """Add income or expense."""
    if request.method == 'POST':
        transaction_type = request.form['transaction_type']
        category = request.form['category']
        amount = float(request.form['amount'])
        
        data = load_data()
        transaction = {'category': category, 'amount': amount}
        
        if transaction_type == 'income':
            data['income'].append(transaction)
        elif transaction_type == 'expense':
            data['expenses'].append(transaction)
        
        save_data(data)
        return redirect(url_for('home'))
    
    return render_template('add.html')

@app.route('/analyze')
def analyze_expenses():
    """Provide insights on expenses."""
    data = load_data()
    expense_categories = {}
    
    for expense in data['expenses']:
        category = expense['category']
        amount = expense['amount']
        if category in expense_categories:
            expense_categories[category] += amount
        else:
            expense_categories[category] = amount
    
    return render_template('analyze.html', expenses=expense_categories)


@app.route('/delete/<transaction_type>/<int:index>')
def delete_transaction(transaction_type, index):
    """Delete a transaction by index."""
    data = load_data()
    if transaction_type == 'income':
        if 0 <= index < len(data['income']):
            del data['income'][index]
    elif transaction_type == 'expenses':
        if 0 <= index < len(data['expenses']):
            del data['expenses'][index]
    
    save_data(data)
    return redirect(url_for('home'))


@app.route('/view/<transaction_type>')
def view_transactions(transaction_type):
    """View all transactions of a specific type."""
    data = load_data()
    transactions = data.get(transaction_type, [])
    return render_template('view.html', transaction_type=transaction_type, transactions=transactions)

if __name__ == "__main__":
    app.run(debug=True)
    
