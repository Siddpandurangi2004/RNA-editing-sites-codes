# Define the values in 'Germline classification' that are considered non-novel (0)
non_novel_classifications = ['Benign', 'Likely benign']

# Create the 'is_novel_site' column
# Assign 0 if the classification is in non_novel_classifications, and 1 otherwise.
df_cleaned['is_novel_site'] = (~df_cleaned['Germline classification'].isin(non_novel_classifications)).astype(int)

# Display the value counts of the newly created target variable
print("Value counts for 'is_novel_site':")
display(df_cleaned['is_novel_site'].value_counts())
