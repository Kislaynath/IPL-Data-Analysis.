import pandas as pd
matches = pd.read_csv(r'C:\Project\IPL DATASET\data\matches.csv')

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
import os

# Create visuals folder if not exists
os.makedirs('visuals', exist_ok=True)

# Plot 1: Matches played per season
season_counts = matches['Season'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(season_counts.index, season_counts.values)
plt.title('Matches Played Per Season')
plt.xlabel('Season')
plt.ylabel('Matches')
plt.tight_layout()
plt.savefig('visuals/matches_played_per_season.png')   # <-- SAVE HERE
plt.close()

# Plot 2: Top 10 teams by wins
top_teams = matches['winner'].value_counts().head(10)
plt.figure(figsize=(10, 6))
plt.barh(top_teams.index, top_teams.values)
plt.title('Top 10 Teams by Wins')
plt.xlabel('Wins')
plt.tight_layout()
plt.savefig('visuals/top_teams_by_wins.png')           # <-- SAVE HERE
plt.close()

# Plot 3: Toss decision distribution
toss_counts = matches['toss_decision'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(toss_counts, labels=toss_counts.index, autopct='%1.1f%%')
plt.title('Toss Decision Distribution')
plt.tight_layout()
plt.savefig('visuals/toss_decision_distribution.png')  # <-- SAVE HERE
plt.close()