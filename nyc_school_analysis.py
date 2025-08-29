import pandas as pd
from pathlib import Path

schools = pd.read_csv(Path("C:/Users/shawo/Desktop/NYC/schools.csv"))

print(schools.head())

# Solving Question 1
best_math_threshold = 800 * 0.8   #80% of the max possible score

best_math_schools = schools[schools['average_math'] >= best_math_threshold]
best_math_schools = best_math_schools[['school_name', 'average_math']].copy()
best_math_schools = best_math_schools.sort_values('average_math', ascending=False)
best_math_schools.reset_index(drop=True, inplace=True)

print('Best Math Schools:')
print(best_math_schools)

# Solving Question 2 (Top 10 Schools by Total SAT)
schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']

top_10_schools = schools[['school_name', 'total_SAT']].copy()
top_10_schools = top_10_schools.sort_values('total_SAT', ascending=False)
top_10_schools = top_10_schools.head(10)
top_10_schools = top_10_schools.reset_index(drop=True)

print('\nTop 10 Schools by total SAT:\n')
print(top_10_schools)

#Solving Question 3 (Which single borough has the largest standard deviation in the combined SAT score?)

borough_stats = (
    schools
        .groupby('borough')['total_SAT']
        .agg(num_schools='count', average_SAT='mean', std_SAT='std')
        .reset_index()
)

largest_std_dev = (
    borough_stats
        .sort_values('std_SAT', ascending=False)
        .head(1)
        .copy()
)

numeric_cols = ['num_schools', 'average_SAT', 'std_SAT']
largest_std_dev[numeric_cols] = largest_std_dev[numeric_cols].round(2)

print('\nBorough with largest std dev of total SAT:\n')
print(largest_std_dev)