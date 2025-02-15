import os

file_path = "/Users/vishwarajsaxena/Desktop/Project1/DATA/cleaned_data.csv"

if os.path.exists(file_path):
    print("✅ File exists!")
else:
    print("❌ File NOT found! Check the path.")
