df_preprocessed = df.copy()
df_preprocessed['Protein change'] = df_preprocessed['Protein change'].fillna('Unknown')

def extract_protein_features(protein_change):
    if protein_change == 'Unknown':
        return 'Unknown', 'Unknown'
    parts = protein_change.split(',')
    # Take the first part as the primary change
    primary_change = parts[0].strip()
    if 'del' in primary_change.lower():
        change_type = 'Deletion'
        amino_acid_change = primary_change
    elif 'ins' in primary_change.lower():
        change_type = 'Insertion'
        amino_acid_change = primary_change
    elif '>' in primary_change:
        change_type = 'Substitution'
        amino_acid_change = primary_change.split('(')[-1].replace(')', '')
    else:
        change_type = 'Other'
        amino_acid_change = primary_change
    return change_type, amino_acid_change

protein_features = df_preprocessed['Protein change'].apply(lambda x: pd.Series(extract_protein_features(x)))
protein_features.columns = ['ChangeType', 'AminoAcidChange']

df_preprocessed = pd.concat([df_preprocessed, protein_features], axis=1)
display(df_preprocessed[['Protein change', 'ChangeType', 'AminoAcidChange']].head())
