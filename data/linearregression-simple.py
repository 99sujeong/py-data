# linearregression-simple.py 프로그램 참조
# 2차원 배열을 만들어 'data'라는 변수에 할당
from sklearn.linear_model import LinearRegression
import pandas as pd
data = {'x' : [156.5, 160.6, 169.5, 167.9, 154.8, 163.0],
        'y' : [51.7, 54.8, 62.3, 61.3, 49.8, 55.8]}

# data라는 변수의 값을 data frame 형태로 변환
data = pd.DataFrame(data)

data.plot(kind="scatter",  # 산점도를 그리시오
          x='x', y='y',           
          figsize=(5,5),   # 가로 5인치, 세로 5인치 크기의 박스를 설정
          color="blue")    # 산점도 상의 점 색상을 파랑색으로 지정

# linear_model 모듈이 포함하고 있는 Linearregression() 함수를 'linear_regression'이라고 하는 변수에 할당
linear_regression =LinearRegression()
linear_regression.fit(X = pd.DataFrame(data["x"]), y = data["y"])
# 선형 회귀식의 세로축 절편 'linear_regression.intercept_'를 구하여 출력한다.
print('a value(절편값) = ', linear_regression.intercept_)
# 선형 회귀식의 기울기 'linear_regression.coef_'를 구하여 출력한다.
print('b balue(기울기) =', linear_regression.coef_)

mydata = {'x' : [165.0],  'y' : [ ]}
prediction = linear_regression.predict(X = pd.DataFrame(mydata["x"]))
print("165cm의 체중 예측=>", prediction)
