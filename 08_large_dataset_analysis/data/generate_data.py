import pandas as pd
import numpy as np

ROWS = 100_000

np.random.seed(42)

df = pd.DataFrame({
    "TransactionID": range(1, ROWS + 1),

    "CustomerID": np.random.randint(
        1000,
        5000,
        ROWS
    ),

    "City": np.random.choice(
        [
            "Chennai",
            "Coimbatore",
            "Bangalore",
            "Madurai",
            "Salem",
            "Hyderabad"
        ],
        ROWS
    ),

    "Category": np.random.choice(
        [
            "Electronics",
            "Furniture",
            "Clothing",
            "Books",
            "Sports"
        ],
        ROWS
    ),

    "Quantity": np.random.randint(
        1,
        10,
        ROWS
    ),

    "Price": np.random.randint(
        100,
        100000,
        ROWS
    )
})

df["Revenue"] = df["Quantity"] * df["Price"]

df.to_csv(
    "08_large_dataset_analysis/data/transactions.csv",
    index=False
)