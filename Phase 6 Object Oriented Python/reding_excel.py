import pandas as pd

pd.set_option('display.max_columns', 1000)  # or 1000
pd.set_option('display.max_rows', 1000)  # or 1000
pd.set_option('display.max_colwidth', 1000)

xlsx = pd.ExcelFile("files/student_details.xlsx", engine='openpyxl')
df = pd.read_excel(xlsx, engine='openpyxl')

print(df)

