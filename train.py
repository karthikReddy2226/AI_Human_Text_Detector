import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from features import extract_features
import joblib

data = pd.read_csv('data.csv')

feature_list = [extract_features(text) for text in data['text']]
X = pd.DataFrame(feature_list)
y = data['label'].map({'human': 0, 'ai': 1})

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)

print(classification_report(y_test, model.predict(X_test)))
joblib.dump(model, 'text_detector_model.pkl')

from sklearn.metrics import accuracy_score
# Predict test labels
y_pred = model.predict(X_test)
# Print accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
