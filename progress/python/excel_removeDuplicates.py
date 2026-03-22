import pandas as pd

input_file = "E:\\com.sandeep.org\\all_urls.xlsx"
output_file = "E:\\com.sandeep.org\\unique_urls.xlsx"
column_name = "URL"
df = pd.read_excel(input_file)
unique_values = df[column_name].dropna().unique()
unique_df = pd.DataFrame(unique_values, columns=[column_name])
unique_df.to_excel(output_file, index=False)
print(f"Unique values saved to {output_file}")
