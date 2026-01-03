import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

df = pd.read_csv("data/logistics_data.csv")

le = LabelEncoder()
for col in ['traffic_level','weather','delivery_slot']:
    df[col] = le.fit_transform(df[col])

X = df.drop(['delay_minutes','delivery_cost'], axis=1)
y = df[['delay_minutes','delivery_cost']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, pred))

joblib.dump(model, "model/delay_cost_model.pkl")
