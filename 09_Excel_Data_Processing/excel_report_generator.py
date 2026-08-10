import pandas as pd


INPUT_FILE = "data/company_data.xlsx"
OUTPUT_FILE = "output/company_analysis_report.xlsx"


# --------------------------------------------------
# 1. LOAD DATA
# --------------------------------------------------

def load_data(file_path):

    excel_file = pd.ExcelFile(file_path)

    employees = pd.read_excel(
        excel_file,
        sheet_name="Employees"
    )

    sales = pd.read_excel(
        excel_file,
        sheet_name="Sales"
    )

    targets = pd.read_excel(
        excel_file,
        sheet_name="Targets"
    )

    return employees, sales, targets


# --------------------------------------------------
# 2. VALIDATE DATA
# --------------------------------------------------

def validate_data(employees, sales, targets):

    # Check duplicate Employee IDs
    if employees["EmployeeID"].duplicated().any():
        raise ValueError(
            "Duplicate EmployeeID found."
        )

    # Check missing Employee IDs
    if employees["EmployeeID"].isna().any():
        raise ValueError(
            "Missing EmployeeID found."
        )

    # Check missing Revenue
    if sales["Revenue"].isna().any():
        raise ValueError(
            "Missing Revenue found."
        )

    # Verify Revenue calculation
    calculated_revenue = (
        sales["Quantity"] *
        sales["Price"]
    )

    if not sales["Revenue"].equals(
        calculated_revenue
    ):
        raise ValueError(
            "Revenue calculation mismatch."
        )

    print("Data validation passed.")


# --------------------------------------------------
# 3. CREATE SALES DETAILS
# --------------------------------------------------

def create_sales_details(employees, sales):

    sales_details = pd.merge(
        sales,
        employees,
        on="EmployeeID",
        how="left"
    )

    return sales_details


# --------------------------------------------------
# 4. DEPARTMENT REPORT
# --------------------------------------------------

def create_department_report(
    sales_details,
    targets
):

    department_sales = (
        sales_details
        .groupby("Department")["Revenue"]
        .sum()
        .reset_index()
    )

    department_sales.columns = [
        "Department",
        "Revenue"
    ]

    report = pd.merge(
        department_sales,
        targets,
        on="Department",
        how="left"
    )

    report["AchievementPercent"] = (
        report["Revenue"]
        / report["MonthlyTarget"]
        * 100
    ).round(2)

    report["Status"] = (
        report["Revenue"]
        >= report["MonthlyTarget"]
    ).map({
        True: "Target Achieved",
        False: "Below Target"
    })

    return report


# --------------------------------------------------
# 5. EMPLOYEE REPORT
# --------------------------------------------------

def create_employee_report(sales_details):

    report = (
        sales_details
        .groupby(
            [
                "EmployeeID",
                "Name",
                "Department"
            ]
        )
        .agg(
            Orders=("OrderID", "count"),
            TotalQuantity=("Quantity", "sum"),
            TotalRevenue=("Revenue", "sum")
        )
        .reset_index()
    )

    return report.sort_values(
        "TotalRevenue",
        ascending=False
    )


# --------------------------------------------------
# 6. PRODUCT REPORT
# --------------------------------------------------

def create_product_report(sales_details):

    report = (
        sales_details
        .groupby("Product")
        .agg(
            TotalQuantity=("Quantity", "sum"),
            TotalRevenue=("Revenue", "sum"),
            AveragePrice=("Price", "mean")
        )
        .reset_index()
    )

    return report.sort_values(
        "TotalRevenue",
        ascending=False
    )


# --------------------------------------------------
# 7. CITY REPORT
# --------------------------------------------------

def create_city_report(sales_details):

    report = (
        sales_details
        .groupby("City")
        .agg(
            Orders=("OrderID", "count"),
            TotalQuantity=("Quantity", "sum"),
            TotalRevenue=("Revenue", "sum")
        )
        .reset_index()
    )

    return report.sort_values(
        "TotalRevenue",
        ascending=False
    )


# --------------------------------------------------
# 8. CATEGORY REPORT
# --------------------------------------------------

def create_category_report(sales_details):

    report = (
        sales_details
        .groupby("Category")
        .agg(
            Orders=("OrderID", "count"),
            TotalQuantity=("Quantity", "sum"),
            TotalRevenue=("Revenue", "sum")
        )
        .reset_index()
    )

    return report.sort_values(
        "TotalRevenue",
        ascending=False
    )


# --------------------------------------------------
# 9. EXECUTIVE SUMMARY
# --------------------------------------------------

def create_summary(
    sales,
    employee_report,
    product_report,
    department_report
):

    best_employee = employee_report.iloc[0]

    best_product = product_report.iloc[0]

    best_department = department_report.iloc[
        department_report["Revenue"].idxmax()
    ]

    total_revenue = sales["Revenue"].sum()

    average_revenue = sales["Revenue"].mean()

    summary = pd.DataFrame({
        "Metric": [
            "Total Revenue",
            "Total Orders",
            "Average Order Revenue",
            "Best Employee",
            "Best Product",
            "Best Department"
        ],

        "Value": [
            total_revenue,
            len(sales),
            round(average_revenue, 2),
            best_employee["Name"],
            best_product["Product"],
            best_department["Department"]
        ]
    })

    return summary


# --------------------------------------------------
# 10. EXPORT REPORT
# --------------------------------------------------

def export_report(
    output_file,
    summary,
    department_report,
    employee_report,
    product_report,
    city_report,
    category_report,
    sales_details
):

    with pd.ExcelWriter(
        output_file
    ) as writer:

        summary.to_excel(
            writer,
            sheet_name="Executive Summary",
            index=False
        )

        department_report.to_excel(
            writer,
            sheet_name="Department Report",
            index=False
        )

        employee_report.to_excel(
            writer,
            sheet_name="Employee Report",
            index=False
        )

        product_report.to_excel(
            writer,
            sheet_name="Product Report",
            index=False
        )

        city_report.to_excel(
            writer,
            sheet_name="City Report",
            index=False
        )

        category_report.to_excel(
            writer,
            sheet_name="Category Report",
            index=False
        )

        sales_details.to_excel(
            writer,
            sheet_name="Sales Details",
            index=False
        )

    print(
        f"Report generated: {output_file}"
    )


# --------------------------------------------------
# 11. MAIN PIPELINE
# --------------------------------------------------

def generate_report():

    # Load
    employees, sales, targets = load_data(
        INPUT_FILE
    )

    # Validate
    validate_data(
        employees,
        sales,
        targets
    )

    # Merge
    sales_details = create_sales_details(
        employees,
        sales
    )

    # Reports
    department_report = (
        create_department_report(
            sales_details,
            targets
        )
    )

    employee_report = (
        create_employee_report(
            sales_details
        )
    )

    product_report = (
        create_product_report(
            sales_details
        )
    )

    city_report = (
        create_city_report(
            sales_details
        )
    )

    category_report = (
        create_category_report(
            sales_details
        )
    )

    # Summary
    summary = create_summary(
        sales,
        employee_report,
        product_report,
        department_report
    )

    # Export
    export_report(
        OUTPUT_FILE,
        summary,
        department_report,
        employee_report,
        product_report,
        city_report,
        category_report,
        sales_details
    )


# --------------------------------------------------
# 12. PROGRAM ENTRY POINT
# --------------------------------------------------

if __name__ == "__main__":
    generate_report()