import pandas as pd

df = pd.read_csv('/content/clinvar_result (NCL).txt', sep='\t')
display(df.head())
