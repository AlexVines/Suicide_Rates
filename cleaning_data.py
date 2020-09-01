import pandas as pd

desired_width = 20000
pd.set_option('display.width', desired_width)
pd.set_option("display.max_columns", 10)

df = pd.read_csv('master.csv')

print(df.columns)
df2 = df.drop(['country-year', 'HDI for year', ' gdp_for_year ($) '], axis = 1)
#print(df.groupby(''))
#print(df2.groupby('country').suicides_no.mean())
suic_sum = pd.DataFrame(df['suicides_no'].groupby(df['country']).sum())
#print(df2.describe())
df['min_age'] = df['age'].apply(lambda x: x.split()[0].split('-')[0])
df['min_age'] = df['age'].apply(lambda x: x.split()[0].split('-')[1])
print(df.min_age)
