import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

data = {
    "message": [
        "Win money now",
        "Free entry in contest",
        "Call me later",
        "Let's meet tomorrow",
        "You won a lottery",
        "Important meeting today"
    ],
    "label": [1,1,0,0,1,0]
}

df = pd.DataFrame(data)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["message"])

model = LogisticRegression()
model.fit(X, df["label"])

pickle.dump(model, open("model.pkl","wb"))
pickle.dump(vectorizer, open("vectorizer.pkl","wb"))