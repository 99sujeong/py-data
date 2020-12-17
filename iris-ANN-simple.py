from sklearn.datasets import load_iris
import pandas as pd
# iris데이터셋을 iris라는 변수에 저장
iris = load_iris()
# to excel... by Uchang
df = pd.DataFrame(data=iris['data'], columns = iris['feature_names'])
df.to_excel('iris.xlsx', index=False)

print(iris['data'][0:10])
X = iris['data']
y = iris['target']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(10,10,10))
mlp.fit(X_train, y_train)
predictions = mlp.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))