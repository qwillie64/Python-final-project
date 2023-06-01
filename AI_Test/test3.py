import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
read = pd.read_excel("C:\\Users\\ranxion\OneDrive\\文件\\GitHub\\Python-final-project\\AI_Test\\test.xlsx").values.tolist()
corpus = [row[0] for row in read]
intents = [row[1] for row in read]
print(corpus[:15])

feature_extractor = CountVectorizer(
            analyzer="word", ngram_range=(1, 2), binary=True,
            token_pattern=r'([a-zA-Z]+|\w)')
X = feature_extractor.fit_transform(corpus)
INTENT_CLASSIFY_REGULARIZATION = "l2"

lr = LogisticRegression(penalty=INTENT_CLASSIFY_REGULARIZATION,
                                         class_weight='balanced')
lr.fit(X, intents)
user_input = ['查詢明天的降雨量']
X2 = feature_extractor.transform(user_input)
lr.predict(X2)