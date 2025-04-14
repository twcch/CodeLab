from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. 載入資料
iris = load_iris()
X, y = iris.data, iris.target

# 2. 切割資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. 建立 Random Forest 模型
rf = RandomForestClassifier(
    n_estimators=100,       # 森林中的樹數量
    max_depth=5,            # 每棵樹的最大深度
    random_state=42
)
rf.fit(X_train, y_train)

# 4. 預測與評估
y_pred = rf.predict(X_test)

print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\n📊 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\n🧾 Classification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))