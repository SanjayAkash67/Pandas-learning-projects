import pandas as pd

employees = pd.DataFrame({
    "EmployeeID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eva",
        "Frank",
        "Grace",
        "Henry"
    ],
    "Department": [
        "IT",
        "HR",
        "Finance",
        "IT",
        "HR",
        "Finance",
        "IT",
        "Marketing"
    ],
    "City": [
        "Chennai",
        "Coimbatore",
        "Bangalore",
        "Chennai",
        "Madurai",
        "Bangalore",
        "Coimbatore",
        "Chennai"
    ],
    "Salary": [
        60000,
        55000,
        75000,
        65000,
        52000,
        85000,
        70000,
        68000
    ]
})

sales = pd.DataFrame({
    "OrderID": range(1001, 1011),

    "EmployeeID": [
        101, 102, 103, 104, 105,
        106, 107, 108, 101, 103
    ],

    "Product": [
        "Laptop",
        "Chair",
        "Monitor",
        "Keyboard",
        "Laptop",
        "Desk",
        "Mouse",
        "Laptop",
        "Monitor",
        "Chair"
    ],

    "Category": [
        "Electronics",
        "Furniture",
        "Electronics",
        "Electronics",
        "Electronics",
        "Furniture",
        "Electronics",
        "Electronics",
        "Electronics",
        "Furniture"
    ],

    "Quantity": [
        1, 4, 2, 5, 2,
        3, 5, 1, 2, 6
    ],

    "Price": [
        55000,
        2500,
        15000,
        1200,
        55000,
        8000,
        700,
        55000,
        15000,
        2500
    ]
})

sales["Revenue"] = (
    sales["Quantity"] *
    sales["Price"]
)

targets = pd.DataFrame({
    "Department": [
        "IT",
        "HR",
        "Finance",
        "Marketing"
    ],

    "MonthlyTarget": [
        200000,
        100000,
        250000,
        150000
    ]
})

with pd.ExcelWriter(
    "data/company_data.xlsx"
) as writer:

    employees.to_excel(
        writer,
        sheet_name="Employees",
        index=False
    )

    sales.to_excel(
        writer,
        sheet_name="Sales",
        index=False
    )

    targets.to_excel(
        writer,
        sheet_name="Targets",
        index=False
    )



