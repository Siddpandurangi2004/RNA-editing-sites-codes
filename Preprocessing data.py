df.info()

# Inspect unique values and their counts for relevant categorical columns
# Based on the df.head() output, 'Gene(s)' and 'Condition(s)' seem relevant.
# We also want to check 'Clinical significance (Last reviewed)', 'Review status', 'Number of submitters',
# 'Germline classification', 'Somatic clinical impact clinical significance',
# 'Somatic clinical impact review status', 'Oncogenicity classification',
# 'Oncogenicity date last evaluated', 'Oncogenicity review status'
# as these might contain values that need cleaning or indicate missingness.

print("\nValue counts for 'Gene(s)':")
display(df['Gene(s)'].value_counts(dropna=False))

print("\nValue counts for 'Condition(s)':")
display(df['Condition(s)'].value_counts(dropna=False))

print("\nValue counts for 'Clinical significance (Last reviewed)':")
display(df['Clinical significance (Last reviewed)'].value_counts(dropna=False))

print("\nValue counts for 'Review status':")
display(df['Review status'].value_counts(dropna=False))

print("\nValue counts for 'Number of submitters':")
display(df['Number of submitters'].value_counts(dropna=False))

print("\nValue counts for 'Germline classification':")
display(df['Germline classification'].value_counts(dropna=False))

print("\nValue counts for 'Somatic clinical impact clinical significance':")
display(df['Somatic clinical impact clinical significance'].value_counts(dropna=False))

print("\nValue counts for 'Somatic clinical impact review status':")
display(df['Somatic clinical impact review status'].value_counts(dropna=False))

print("\nValue counts for 'Oncogenicity classification':")
display(df['Oncogenicity classification'].value_counts(dropna=False))

print("\nValue counts for 'Oncogenicity date last evaluated':")
display(df['Oncogenicity date last evaluated'].value_counts(dropna=False))

print("\nValue counts for 'Oncogenicity review status':")
display(df['Oncogenicity review status'].value_counts(dropna=False))
