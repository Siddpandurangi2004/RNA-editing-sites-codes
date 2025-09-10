# 1. Use the trained model to predict the probability of each instance in the original df_cleaned DataFrame belonging to the "novel" class (class 1).
# First, ensure the df_cleaned DataFrame has the same feature columns in the same order as X used for training.
# We need to recreate the feature matrix X from the full df_cleaned DataFrame.
X_full = df_cleaned[feature_cols].copy()

# Predict probabilities
predicted_novelty_proba = model.predict_proba(X_full)[:, 1]

# 2. Store these predicted probabilities in a new column in the df_cleaned DataFrame.
df_cleaned['predicted_novelty_proba'] = predicted_novelty_proba

# 3. Define a probability threshold for identifying potential novel sites.
probability_threshold = 0.5 # This threshold can be adjusted

# 4. Create a new boolean column in df_cleaned, is_potential_novel_site, which is True if predicted_novelty_proba is above the defined threshold and False otherwise.
df_cleaned['is_potential_novel_site'] = df_cleaned['predicted_novelty_proba'] > probability_threshold

# 5. Filter the df_cleaned DataFrame to create a new DataFrame containing only the rows where is_potential_novel_site is True.
potential_novel_sites_df = df_cleaned[df_cleaned['is_potential_novel_site']].copy()

# 6. Select relevant original columns and the newly created prediction columns for the potential novel sites DataFrame.
relevant_cols = [
    'Name',
    'Protein change',
    'Accession',
    'Germline classification',
    'Germline review status',
    'predicted_novelty_proba',
    'is_potential_novel_site'
]

potential_novel_sites_display = potential_novel_sites_df[relevant_cols]

# 7. Display the first few rows of the DataFrame containing the potential novel sites.
print("Potential Novel RNA Editing Sites (based on model prediction):")
display(potential_novel_sites_display.head())

print("\nValue counts for 'is_potential_novel_site' in the full dataset:")
display(df_cleaned['is_potential_novel_site'].value_counts())
