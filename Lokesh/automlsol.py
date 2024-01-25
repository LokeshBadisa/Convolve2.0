from autosklearn.classification import AutoSklearnClassifier
import pandas as pd
import sklearn.metrics
import pickle

X_train = pd.read_csv('train_final.csv')
y_train = X_train['Target']
X_train = X_train.drop(['Target'], axis=1)

automl = AutoSklearnClassifier(time_left_for_this_task=36000)
automl.fit(X_train, y_train)

X_test = pd.read_csv('test_final.csv')
y_test = X_test['Target']
X_test = X_test.drop(['Target'], axis=1)

y_hat = automl.predict(X_test)
print("Accuracy score", sklearn.metrics.accuracy_score(y_test, y_hat))

with open('automlsol.pkl', 'wb') as f:
    pickle.dump(automl, f)