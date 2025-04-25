# Simple post-processing script to create a clean subset of tree data
#     - JRz, for personal use and not indended for real-world applications
 
#  NOTE: This is eliminating valid, useful data in lieu of something easier to visualize
#        It's possible that this will mask trends, as it is often VERY likely that missing data are non-randomly distributed (e.g. more missing data pre-1955 in this dataset)


import csv
import re

def passes_filter(row, company):
    # Filter criteria:
    # only games published by major layoff developers. 
    if (company not in row['developer'] and company not in row['publisher']):
        return False
    
    date = row['releaseDate']
    if (date):
        year = date[0:4]
        if (int(year) < 2020): 
            return False
    else:
        return False
    
    return True
    

# -----------------------------------------------------------------------------------------------------

# import and run passes_filter
data = []
header = []
companies = []

with open('majorlayoffs.csv','r') as f2:
    layoffs = csv.DictReader(f2)
    for row in layoffs:
        company = row['Company']
        companies.append(company)


with open('metacritic.csv','r',encoding='utf-8') as f1:
    
        games = csv.DictReader(f1)

        header = games.fieldnames

        for game in games:
            for company in companies:
                if (passes_filter(game, company)):
                    game['metacritic'] = float(game['metacritic'])
                    # e.g. splitting up qSpecies
                    data.append(game)

print(len(data))

# export to new CSV       
with open('metacriticFILTERED.csv','w', encoding='utf-8', newline = '') as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)
