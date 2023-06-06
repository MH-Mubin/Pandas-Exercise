1.How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)

import pandas as pd
#race count
df=pd.read_csv(r'/content/adult.data.csv')
race_counts= df['race'].value_counts()
print(race_counts)

2.What is the average age of men?

import pandas as pd
df=pd.read_csv(r'/content/adult.data.csv') 
male_df = df[df['sex'] == 'Male']
average_age_men = male_df['age'].mean()
print(average_age_men)

3.What is the percentage of people who have a Bachelor's degree?

import pandas as pd
df=pd.read_csv(r'/content/adult.data.csv') 
education_counts = df['education'].value_counts()
percentage_bachelors = (education_counts['Bachelors'] / df.shape[0]) * 100
print(percentage_bachelors)

4.What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?

import pandas as pd
df=pd.read_csv(r'/content/adult.data.csv') 
advanced_education = ['Bachelors', 'Masters', 'Doctorate']
filtered_df = df[df['education'].isin(advanced_education) & (df['salary'] == '>50K')]
percentage_high_income = (filtered_df.shape[0] / df[df['education'].isin(advanced_education)].shape[0]) * 100
print(percentage_high_income)

5.What percentage of people without advanced education make more than 50K?

import pandas as pd
df=pd.read_csv(r'/content/adult.data.csv') 
advanced_education = ['Bachelors', 'Masters', 'Doctorate']
filtered_df = df[~df['education'].isin(advanced_education) & (df['salary'] == '>50K')]
percentage_high_income = (filtered_df.shape[0] / df[~df['education'].isin(advanced_education)].shape[0]) * 100
print(percentage_high_income)

6.What is the minimum number of hours a person works per week?

import pandas as pd
df=pd.read_csv(r'/content/adult.data.csv') 
min_hours_per_week = df['hours-per-week'].min()
print("Minimum number of hours worked per week:", min_hours_per_week)

7.What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?

import pandas as pd
df=pd.read_csv(r'/content/adult.data.csv') 
min_hours_per_week = df['hours-per-week'].min()
filtered_df = df[(df['hours-per-week'] == min_hours_per_week) & (df['salary'] == '>50K')]
percentage_of_high_income = (filtered_df.shape[0] / df[df['hours-per-week'] == min_hours_per_week].shape[0]) * 100
print(percentage_of_high_income)

8.What country has the highest percentage of people that earn >50K and what is that percentage?

import pandas as pd
df=pd.read_csv(r'/content/adult.data.csv') 
filtered_df = df[df['salary'] == '>50K']
percentages = filtered_df['native-country'].value_counts(normalize=True) * 100
highest_percentage_country = percentages.idxmax()
highest_percentage = percentages.max()
print("Country with the highest percentage:", highest_percentage_country)
print("Percentage:", highest_percentage)

9.Identify the most popular occupation for those who earn >50K in India.

import pandas as pd
df=pd.read_csv(r'/content/adult.data.csv') 
filtered_df = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
occupation_counts = filtered_df['occupation'].value_counts()
most_popular_occupation = occupation_counts.idxmax()
print("Most popular occupation for individuals earning >50K in India:", most_popular_occupation)
