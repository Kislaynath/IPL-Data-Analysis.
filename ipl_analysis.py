import pandas as pd
matches = pd.read_csv(r'C:\Users\kishl\OneDrive\Desktop\IPL DATASET\data\matches.csv')

print("Shape of dataset:", matches.shape)
print("\nFIRST 5 ROWS: ")
print(matches.head())
print("\nColumn Names:\n", matches.columns)
print("\nDataset Info:")
print(matches.info())
print("\nMissing values: \n", matches.isnull().sum())

# 1️ Matches per season
print("\nTotal Matches Per Season:")
print(matches['Season'].value_counts())

# 2️ Most successful teams
print("\nMost Successful Teams:")
print(matches['winner'].value_counts().head(10))

# 3️ Toss decision preference
print("\nToss Decision Counts:")
print(matches['toss_decision'].value_counts())

# 4️ Most Player of the Match awards
print("\nTop 10 Player of the Match winners:")
print(matches['player_of_match'].value_counts().head(10))

# 5️ Top venues by matches
print("\nTop Venues by Matches:")
print(matches['venue'].value_counts().head(5))

import matplotlib.pyplot as plt
import seaborn as sns
import os
os.makedirs('visuals', exist_ok=True)
plt.style.use('seaborn-v0_8-darkgrid')

# 1️ Matches per season
season_counts = matches['Season'].value_counts().sort_index()
plt.figure(figsize=(8,4))
sns.barplot(x=season_counts.index, y=season_counts.values)
plt.title('Matches Played Per Season')
plt.xlabel('Season')
plt.ylabel('Matches')
plt.savefig('visuals/matches_per_season.png', bbox_inches='tight')
plt.show()

# 2️ Most successful teams
top_teams = matches['winner'].value_counts().head(10)
plt.figure(figsize=(8,4))
sns.barplot(x=top_teams.values, y=top_teams.index)
plt.title('Top 10 Teams by Wins')
plt.xlabel('Wins')
plt.ylabel('Teams')
plt.savefig('visuals/matches_per_season.png', bbox_inches='tight')
plt.show()

# 3️ Toss decision
plt.figure(figsize=(5,4))
matches['toss_decision'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Toss Decision Distribution')
plt.ylabel('')
plt.savefig('visuals/matches_per_season.png', bbox_inches='tight')
plt.show()