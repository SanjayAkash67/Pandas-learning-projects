import pandas as pd

FILE_PATH = "data/transactions.csv"
CHUNK_SIZE = 10_000

def analyze_transactions(file_path, chunk_size):

    total_transactions = 0
    total_revenue = 0
    high_value_count = 0
    highest_transaction = None

    category_results = []
    city_results = []
    customer_results = []

    for chunk in pd.read_csv(
        file_path,
        chunksize=chunk_size
    ):

        total_transactions += len(chunk)

        total_revenue += chunk["Revenue"].sum()

        high_value_count += (
            chunk["Revenue"] > 100000
        ).sum()

        current_max = chunk["Revenue"].max()

        if (
            highest_transaction is None
            or current_max > highest_transaction
        ):
            highest_transaction = current_max

        category_results.append(
            chunk.groupby("Category")["Revenue"].sum()
        )

        city_results.append(
            chunk.groupby("City")["Revenue"].sum()
        )

        customer_results.append(
            chunk.groupby("CustomerID")["Revenue"].sum()
        )

    return (
        total_transactions,
        total_revenue,
        high_value_count,
        highest_transaction,
        category_results,
        city_results,
        customer_results
    )


results = analyze_transactions(
    FILE_PATH,
    CHUNK_SIZE
)

(
    total_transactions,
    total_revenue,
    high_value_count,
    highest_transaction,
    category_results,
    city_results,
    customer_results
) = results


average_revenue = (
    total_revenue /
    total_transactions
)


category_sales = (
    pd.concat(category_results)
    .groupby(level=0)
    .sum()
    .reset_index()
)

category_sales.columns = [
    "Category",
    "Revenue"
]

category_sales["RevenuePercentage"] = (
    category_sales["Revenue"]
    / total_revenue
    * 100
).round(2)

category_sales = category_sales.sort_values(
    "Revenue",
    ascending=False
)


city_sales = (
    pd.concat(city_results)
    .groupby(level=0)
    .sum()
    .reset_index()
)

city_sales.columns = [
    "City",
    "Revenue"
]

city_sales["RevenuePercentage"] = (
    city_sales["Revenue"]
    / total_revenue
    * 100
).round(2)

city_sales = city_sales.sort_values(
    "Revenue",
    ascending=False
)


customer_sales = (
    pd.concat(customer_results)
    .groupby(level=0)
    .sum()
    .reset_index()
)

customer_sales.columns = [
    "CustomerID",
    "TotalRevenue"
]

customer_sales = customer_sales.sort_values(
    "TotalRevenue",
    ascending=False
)


top_customers = customer_sales.head(10)


summary = pd.DataFrame({
    "Metric": [
        "Total Transactions",
        "Total Revenue",
        "Average Transaction Revenue",
        "Highest Transaction",
        "High Value Transactions"
    ],

    "Value": [
        total_transactions,
        total_revenue,
        round(average_revenue, 2),
        highest_transaction,
        high_value_count
    ]
})


category_sales.to_csv(
    "output/category_sales.csv",
    index=False
)

city_sales.to_csv(
    "output/city_sales.csv",
    index=False
)

top_customers.to_csv(
    "output/customer_summary.csv",
    index=False
)

summary.to_csv(
    "output/summary.csv",
    index=False
)


print("Analysis complete.")
print("Total transactions:", total_transactions)
print("Total revenue:", total_revenue)
print("Average revenue:", round(average_revenue, 2))
print("Highest transaction:", highest_transaction)
print("High-value transactions:", high_value_count)