import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import pandas as pd

# 載入資料
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target  # 加入分類欄位
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})  # 可讀性更好

# 繪製散佈圖
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x='sepal length (cm)',
    y='petal length (cm)',
    hue='species',
    palette='Set1'
)
plt.title("Petal Length vs. Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title='Species')
plt.grid(True)
plt.show()