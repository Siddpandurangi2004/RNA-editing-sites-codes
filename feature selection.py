# Identify feature columns
# Exclude the target variable ('is_novel_site') and identifier/descriptive columns.
# Exclude placeholder columns that are all None.
# Based on df_cleaned.info() and the engineered features, the following columns are potential features:
# 'GRCh37Chromosome', 'GRCh37Location', 'GRCh38Chromosome', 'GRCh38Location',
# 'VariationID', 'AlleleID(s)', 'Canonical SPDI', 'Variant type', 'Molecular consequence',
# 'Gene(s)_NCL', 'Gene(s)_PPT1', conditions_list, 'Sequence_Context', 'GC_Content',
# 'Gene_Region', 'is_known_editing_site'

# Columns to exclude:
# 'Name': Identifier
# 'Protein change': Descriptive, potentially useful but complex to encode for a simple model
# 'Accession': Identifier
# 'Germline classification': Source of the target variable, should not be a feature
# 'Germline review status': Descriptive
# 'Secondary_Structure', 'Read_Depth', 'Mismatch_Frequency', 'Distance_from_Known_SNP': All None placeholders

# Let's keep numerical features, one-hot encoded categorical features, and the engineered GC_Content.
# 'Canonical SPDI', 'Variant type', 'Molecular consequence', 'Sequence_Context', 'Gene_Region' are categorical/object types.
# We need to decide how to handle these. 'Canonical SPDI' is likely an identifier.
# 'Variant type' and 'Molecular consequence' are categorical and can be one-hot encoded.
# 'Sequence_Context' is complex, and the placeholder is not useful.
# 'Gene_Region' is currently all 'Exon', so not useful as a feature unless more regions are added.
# 'is_known_editing_site' is highly correlated with the target, could lead to data leakage. Exclude it.

# Selected features:
# Numerical: 'GRCh37Chromosome', 'GRCh37Location', 'GRCh38Chromosome', 'GRCh38Location', 'VariationID', 'AlleleID(s)', 'GC_Content'
# One-Hot Encoded (from previous steps): 'Gene(s)_NCL', 'Gene(s)_PPT1', conditions_list
# Categorical that need encoding: 'Variant type', 'Molecular consequence'

# Let's one-hot encode 'Variant type' and 'Molecular consequence'.
df_cleaned = pd.get_dummies(df_cleaned, columns=['Variant type', 'Molecular consequence'], drop_first=True)


# Define the list of selected feature columns after one-hot encoding
feature_cols = [
    'GRCh37Chromosome', 'GRCh37Location', 'GRCh38Chromosome', 'GRCh38Location',
    'VariationID', 'AlleleID(s)', 'GC_Content',
    'Gene(s)_NCL', 'Gene(s)_PPT1'
] + conditions_list + [col for col in df_cleaned.columns if col.startswith('Variant type_') or col.startswith('Molecular consequence_')]


# Remove any columns from feature_cols that might not exist in the DataFrame after processing
feature_cols = [col for col in feature_cols if col in df_cleaned.columns]

# Create feature matrix X
X = df_cleaned[feature_cols].copy()

# Create target vector y
y = df_cleaned['is_novel_site'].copy()

# Display the first few rows of X and y
print("First 5 rows of features (X):")
display(X.head())

print("\nFirst 5 rows of target (y):")
display(y.head())

# Print the list of selected feature columns
print("\nSelected feature columns:")
print(feature_cols)
