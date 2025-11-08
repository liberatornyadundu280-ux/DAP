import pandas as pd
series = pd.Series(['apple', 'banana', 'cherry', 'date'])
print(f"Original Pandas Series (type: {type(series)}):")
print(series)
python_list = series.tolist()
print(f"\nConverted Python list (type: {type(python_list)}):")
print(python_list)
