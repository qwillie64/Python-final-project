from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import random
from collections import defaultdict
import pandas as pd
#健立訓練資料
mushrooms = defaultdict(lambda: [])
def checkType(size, length):
    if size < 10: return '發財蘑菇'
    if size < 15: return '幸運蘑菇'
    if length > 15:
        return '發財蘑菇'
    return '神秘蘑菇'
for i in range(100):
    size = random.randint(1, 20)
    length = random.randint(1, 20)
    mushrooms['type'].append(checkType(size, length))
    mushrooms['size'].append(size)
    mushrooms['length'].append(length)
data = pd.DataFrame.from_dict(mushrooms)
y = data['type']                   # 變出 y 資料
X = data.drop(['type'], axis=1)    # 變出 X 資料，將 type 丟棄
#設立模型
X_train, X_test, y_train, y_test = train_test_split(X.values, y, test_size=0.2)
#訓練
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
#察看結果
model.score(X_test, y_test)
#比對答案
y_predict = model.predict(X_test)
accuracy_score(y_test, y_predict)
answers =  []    # 存放真正答案
predictss = []    # 存放預測結果
for i in range(10000):
    size = random.randint(1, 20)
    length = random.randint(1, 20)
    answers.append(checkType(size, length))
    predictss.append(model.predict([[size, length]]))
print(accuracy_score(answers, predictss))