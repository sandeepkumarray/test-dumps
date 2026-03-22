import pandas as pd

def compare_csv(file1, file2, row_start, row_end, col_start, col_end):
    # Read CSV files
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    
    # Ensure row_end and col_end are within bounds
    row_end = min(row_end, len(df1), len(df2))
    col_end = min(col_end, len(df1.columns), len(df2.columns))
    
    # Select relevant rows and columns
    df1_subset = df1.iloc[row_start:row_end, col_start:col_end]
    df2_subset = df2.iloc[row_start:row_end, col_start:col_end]
    
    # Compare values
    comparison = df1_subset.eq(df2_subset)
    
    # Find mismatched values
    mismatches = [(i + row_start, df1.columns[j + col_start], df1_subset.iat[i, j], df2_subset.iat[i, j])
                  for i in range(len(comparison))
                  for j in range(len(comparison.columns))
                  if not comparison.iat[i, j]]
    
    if mismatches:
        print("Differences found:")
        for row, col, val1, val2 in mismatches:
            print(f"Row {row}, Column '{col}': File1 -> {val1}, File2 -> {val2}")
    else:
        print("No differences found in the specified range.")

# Example usage
compare_csv("C:\\Users\\Sandeep\\Downloads\\MOCK_DATA.csv", "C:\\Users\\Sandeep\\Downloads\\MOCK_DATA_copy.csv", row_start=0, row_end=10, col_start=0, col_end=13)
