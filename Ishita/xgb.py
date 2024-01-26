from pathlib import Path
import pandas as pd
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


df = pd.read_csv('/content/cleantrain2nahan.csv')
numerical_cols = df.select_dtypes(include=['int', 'float']).columns

imputer = SimpleImputer(strategy='mean')
df[numerical_cols] = imputer.fit_transform(df[numerical_cols])

y = df['Target']
X = df.drop('Target', axis=1)
numerical_cols = numerical_cols[1:]
scaler = StandardScaler()
X[numerical_cols] = scaler.fit_transform(X[numerical_cols])

model_xgb = xgb.XGBClassifier(random_state=42)
model_xgb.fit(X, y)

df_test = pd.read_csv('/content/cleantest2nahan.csv')
numerical_cols = df_test.select_dtypes(include=['int', 'float']).columns
imputer = SimpleImputer(strategy='mean')
df_test[numerical_cols] = imputer.fit_transform(df_test[numerical_cols])

y_test = df_test['Target']
X_test = df_test.drop('Target', axis=1)
numerical_cols = numerical_cols[1:]

scaler = StandardScaler()
X_test[numerical_cols] = scaler.fit_transform(X_test[numerical_cols])

y_pred = model_xgb.predict(X_test)
report = classification_report(y_test, y_pred)
print(report)
print(accuracy_score(y_test, y_pred))
