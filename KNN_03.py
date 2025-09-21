import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("dating.csv")

# Encode the target variable (city)
city_encoder = LabelEncoder()
df["city"] = city_encoder.fit_transform(df["city"])

# Categorical columns for one-hot encoding
categorical_features = ["education_level",  "gender", "chaddhii"]

# One-hot encode categorical features
df_encoded = pd.get_dummies(df, columns=categorical_features)

# Features and target
X = df_encoded.drop("city", axis=1)
Y = df_encoded["city"]

# Train-test split
train_x, test_x, train_y, test_y = train_test_split(X, Y, test_size=0.2, random_state=42)

# Train KNN
model = KNeighborsClassifier(n_neighbors=3)
model.fit(train_x, train_y)

# Mapping dictionaries for user-friendly input
gender_map = ["male", "female"]
chaddhii_map = df["chaddhii"].unique().tolist()  # e.g., ["red", "purple", "blue"]

# Collect user input
user_input = {}
user_input["age"] = input("Enter age: ")
user_input["education_level"] = input("Enter education level: ")
user_input["height_cm"] = input("Enter height in cm: ")
user_input["body_count"] = input("Enter body count: ")
user_input["sex_hour"] = input("Enter sex hour: ")
user_input["gender"] = input(f"Enter gender ({'/'.join(gender_map)}): ").lower()
user_input["chaddhii"] = input(f"Enter chaddhii color ({'/'.join(chaddhii_map)}): ").lower()

# Convert input to dataframe
input_df = pd.DataFrame([user_input])

# Apply same one-hot encoding as training data
input_df_encoded = pd.get_dummies(input_df, columns=["gender", "chaddhii", "education_level"])

# Align input columns with training columns
input_df_encoded = input_df_encoded.reindex(columns=X.columns, fill_value=0)

# Predict
predicted_result = model.predict(input_df_encoded)
predicted_city = city_encoder.inverse_transform(predicted_result)

print(f"The predicted city is: {predicted_city[0]}")


