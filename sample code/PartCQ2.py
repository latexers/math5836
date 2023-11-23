import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA


# Load the dataset
df = pd.read_csv("dataset.csv")

# Separate features and target
X = df.drop("target", axis=1)
y = df["target"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Explore different preprocessing approaches
# Approach 1: Impute missing values and scale numeric features
# 处理None值，如果无None值，这一步可以删去
imputer = SimpleImputer(strategy='mean')
X_train_imputed = pd.DataFrame(imputer.fit_transform(X_train), columns=X_train.columns)
X_test_imputed = pd.DataFrame(imputer.transform(X_test), columns=X_test.columns)

scaler = StandardScaler()
X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train_imputed), columns=X_train_imputed.columns)
X_test_scaled = pd.DataFrame(scaler.transform(X_test_imputed), columns=X_test_imputed.columns)

# Build the Random Forest classifier
# rf_classifier = RandomForestClassifier(random_state=42, n_jobs=-1)
rf_classifier = RandomForestClassifier(min_samples_leaf=43,max_leaf_nodes=45,max_depth=50)
# Train the model
rf_classifier.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = rf_classifier.predict(X_test_scaled)

# Evaluate the model
report = classification_report(y_test, y_pred)
print("Classification Report:\n", report)

# Check if precision and recall criteria are met
precision_criteria = report.split('\n')[3].split()[2]
recall_criteria = report.split('\n')[4].split()[2]

if float(precision_criteria) >= 0.8 and float(recall_criteria) >= 0.85:
    best_model_task1 = rf_classifier
    print("Best model meets precision and recall criteria.")
else:
    print("Precision or Recall criteria not met. Adjust the model or preprocessing steps accordingly.")


# Use PCA for dimensionality reduction with an explained variance ratio of 95%
pca = PCA(n_components=0.95)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

# Build the Random Forest classifier on the reduced dataset
rf_classifier_task2 = RandomForestClassifier(random_state=42, n_jobs=-1)

# Train the model
rf_classifier_task2.fit(X_train_pca, y_train)

# Make predictions on the test set
y_pred_task2 = rf_classifier_task2.predict(X_test_pca)

# Evaluate the model
report_task2 = classification_report(y_test, y_pred_task2)
print("Classification Report with PCA:\n", report_task2)

# Save the best model in the variable named best_model_task2
best_model_task2 = rf_classifier_task2