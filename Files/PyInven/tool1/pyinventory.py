import pandas as pd

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

df = pd.DataFrame(list(zip(*[list1, list2, list3]))).add_prefix('Col')

df.to_csv('file.csv', index=False)

print(df)
