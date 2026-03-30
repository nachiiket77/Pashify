# model.py

import pandas as pd
import pickle
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC

# ==============================
# 1. Load Dataset (ERROR SAFE)
# ==============================

FILE_PATH = "dataset.csv"

if not os.path.exists(FILE_PATH):
    raise FileNotFoundError("❌ dataset.csv not found in project folder")

# 🔥 Fix parser error here
data = pd.read_csv(FILE_PATH, on_bad_lines='skip')

# Keep only first 2 columns if extra columns exist
if len(data.columns) > 2:
    data = data.iloc[:, :2]

# Rename columns safely
data.columns = ['password', 'strength']

print("✅ Dataset loaded successfully")
print(data.head())

# ==============================
# 2. Preprocessing
# ==============================

data.dropna(inplace=True)
data['password'] = data['password'].astype(str)

X = data['password']
y = data['strength']

# ==============================
# 3. Feature Engineering
# ==============================

print("\n🔄 Extracting features...")

vectorizer = TfidfVectorizer(
    analyzer='char',
    ngram_range=(1, 5),   # 🔥 improves accuracy
    min_df=2
)

X_vectorized = vectorizer.fit_transform(X)

print("✅ Feature extraction done")

# ==============================
# 4. Train-Test Split
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)

print(f"\n📊 Training samples: {X_train.shape[0]}")
print(f"📊 Testing samples: {X_test.shape[0]}")

# ==============================
# 5. Train Multiple Models
# ==============================

models = {
    "Logistic Regression": LogisticRegression(max_iter=2000),
    "Naive Bayes": MultinomialNB(),
    "SVM": LinearSVC()
}

best_model = None
best_accuracy = 0
best_name = ""

print("\n🤖 Training models...\n")

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print(f"{name} Accuracy: {acc:.4f}")

    if acc > best_accuracy:
        best_accuracy = acc
        best_model = model
        best_name = name

# ==============================
# 6. Best Model Evaluation
# ==============================

print("\n🏆 Best Model:", best_name)
print(f"🔥 Best Accuracy: {best_accuracy:.4f}")

y_pred = best_model.predict(X_test)

print("\n📊 Classification Report:")
print(classification_report(y_test, y_pred))

# ==============================
# 7. Save Model
# ==============================

pickle.dump(best_model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("\n💾 Model saved successfully!")
print("✔ model.pkl")
print("✔ vectorizer.pkl")