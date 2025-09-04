import pandas as pd
import matplotlib.pyplot as plt

def analyze_month(csv_file):
    # 1. Load the data
    df = pd.read_csv(csv_file)
    
    # 2. Preprocess: make date column for grouping
    df['Date'] = pd.to_datetime(df['Period'], dayfirst=True)
    df['Weekday'] = df['Date'].dt.day_name()
    df['Week'] = df['Date'].dt.isocalendar().week

    # 3. Main stats
    expenses = df[df['Income/Expense'] == 'Exp.']
    total = expenses['Amount'].sum()
    mean = expenses['Amount'].mean()

    print(f"Total expenses: ₹{total:.2f}")
    print(f"Average expense: ₹{mean:.2f}")

    # 4. Top categories
    top_cats = expenses.groupby('Category')['Amount'].sum().sort_values(ascending=False)
    print("\nTop categories:")
    print(top_cats)

    # 5. Bar chart for food (or change to any category)
    food_expenses = expenses[expenses['Category'] == '🍜 Food']
    food_by_date = food_expenses.groupby('Period')['Amount'].sum()
    food_by_date.plot(kind='bar', color='skyblue')
    plt.title("Food Expenses by Date")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.show()

    # 6. (Example) Weekly spending
    weekly_spending = expenses.groupby('Week')['Amount'].sum()
    weekly_spending.plot(kind='bar', color='orange')
    plt.title("Weekly Spending")
    plt.xlabel("Week")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.show()

    # 7. Pie chart by category
    top_cats.plot.pie(autopct='%.1f%%', figsize=(7,7), title='Expense Share by Category')
    plt.ylabel('')
    plt.show()

    # 8. category-wise weekly spending
    category_sum = df[df["Income/Expense"] == "Exp."].groupby("Category")["Amount"].sum()
    category_sum.plot.pie(autopct = '%.1f%%' , figsize=(8, 8), title="Expense Distribution by Category")
    plt.ylabel("")
    plt.show()

    category_sum.to_csv('expense_distribution_by_category.csv')


# Example use:
analyze_month('july_expenses.csv')
# To run for August: analyze_month('august_expenses.csv')

 