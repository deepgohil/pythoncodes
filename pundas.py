# import pandas as pd
# a = [1, 7, 2]
# myvar = pd.Series(a, index=["x","y","z"])
# print(myvar)

# import pandas as pd
# data = {
#     "calories":[420,380,390],
#     "duration":[50,45,40]
# }
# df = pd.DataFrame(data)
# print(df)

# print(df.loc[[0,1]])

# import pandas as pd
# data = {
#     "calories":[420,380,390],
#     "duration":[50,45,40]
# }

# df = pd.DataFrame(data, index=["day1","day2","day3"])
# print(df.loc["day2"])

import pandas as pd
df = pd.read_csv("train.csv")
print(df)
print('-------------------------------------------------------------------------------------------------------------------')
print(df.head())
print('-------------------------------------------------------------------------------------------------------------------')
print(df.tail())
print('-------------------------------------------------------------------------------------------------------------------')
print(df.info())
print('-------------------------------------------------------------------------------------------------------------------')

new_df = df.dropna(subset="Age")

# new_df = df.dropna()
print(new_df)
print('-------------------------------------------------------------------------------------------------------------------')
x = round(df["Age"].mean())
df["Age"].fillna(x,inplace=True)
print(df)


# import pandas as pd
# df = pd.read_csv("train.csv")

# print(df.describe())









