# model.py
"""
Pashify - Password Strength Classifier Model Trainer
Trains a fast, accurate, and ultra-compact Logistic Regression model
on character-level TF-IDF features and password length.
"""

import pandas as pd
import pickle
import time
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.utils import resample
from scipy.sparse import hstack

# ==========================================
# 1. LOAD + CLEAN DATA
# ==========================================
print("[*] Loading dataset...")
data = pd.read_csv("dataset.csv", on_bad_lines='skip')

# Select only the password and strength columns
data = data.iloc[:, :2]
data.columns = ['password', 'strength']

data.dropna(inplace=True)
data.drop_duplicates(inplace=True)
data['password'] = data['password'].astype(str)

# ==========================================
# 2. BALANCE DATA
# ==========================================
print("[*] Balancing dataset classes...")
df0 = data[data.strength == 0]
df1 = data[data.strength == 1]
df2 = data[data.strength == 2]

# Downsample/Upsample so all classes match the size of df0 (89,702 samples)
df1_bal = resample(df1, replace=True, n_samples=len(df0), random_state=42)
df2_bal = resample(df2, replace=True, n_samples=len(df0), random_state=42)

data_balanced = pd.concat([df0, df1_bal, df2_bal])
X = data_balanced['password']
y = data_balanced['strength']

print(f"[+] Balanced dataset ready. Total samples: {len(X)}")

# ==========================================
# 3. FEATURE ENGINEERING
# ==========================================
print("[*] Extracting character-level n-gram features...")
t0 = time.time()
# Extracts 1 to 4-character n-grams (max 3,000 features)
vectorizer = TfidfVectorizer(
    analyzer='char',
    ngram_range=(1, 4),
    max_features=3000
)

X_vec = vectorizer.fit_transform(X)
X_length = X.apply(len).values.reshape(-1, 1)

# Horizontal stack to merge sparse TF-IDF matrix with length feature
X_final = hstack([X_vec, X_length])
print(f"[+] Feature extraction completed in {time.time() - t0:.2f}s")

# ==========================================
# 4. TRAIN TEST SPLIT
# ==========================================
X_train, X_test, y_train, y_test = train_test_split(
    X_final, y, test_size=0.2, random_state=42
)

# ==========================================
# 5. TRAINING COMPACT LOGISTIC REGRESSION
# ==========================================
print("[*] Training compact Logistic Regression classifier...")
t0 = time.time()
# High-performance solver with strong regularization (L2)
model = LogisticRegression(
    max_iter=500,
    C=1.0,
    random_state=42,
    solver='lbfgs'
)

model.fit(X_train, y_train)
print(f"[+] Model trained successfully in {time.time() - t0:.2f}s")

# ==========================================
# 6. EVALUATION
# ==========================================
print("[*] Evaluating model on test split...")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"[+] FINAL TEST ACCURACY: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ==========================================
# 7. SAVE MODEL
# ==========================================
print("[*] Saving models to disk...")
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

model_size = os.path.getsize("model.pkl") / 1024
vec_size = os.path.getsize("vectorizer.pkl") / 1024
print(f"[+] model.pkl saved successfully! Size: {model_size:.2f} KB")
print(f"[+] vectorizer.pkl saved successfully! Size: {vec_size:.2f} KB")