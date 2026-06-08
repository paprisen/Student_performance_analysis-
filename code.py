import pandas as pd

df = pd.read_csv("student_data.csv", sep=r"\s+")

print(df.head())
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nStatistics:")
print(df.describe())

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8,5))
plt.hist(df["FinalGrade"], bins=5)

plt.title("Final Grade Distribution")
plt.xlabel("Final Grade")
plt.ylabel("Number of Students")

plt.show()


plt.figure(figsize=(6,4))
sns.countplot(x="Gender", data=df)

plt.title("Gender Distribution")

plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(
    x="StudyHoursPerWeek",
    y="FinalGrade",
    data=df
)

plt.title("Study Hours vs Final Grade")

plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(
    x="AttendanceRate",
    y="FinalGrade",
    data=df
)

plt.title("Attendance vs Final Grade")

plt.show()

plt.figure(figsize=(8,6))

corr = df.select_dtypes(include='number').corr()

sns.heatmap(corr,
            annot=True,
            cmap="Blues")

plt.title("Correlation Heatmap")

plt.show()

# Save cleaned dataset
df.to_csv("cleaned_student_data.csv", index=False)
print("Cleaned dataset saved successfully!")
