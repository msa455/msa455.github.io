
import pandas as pd


#Location of the data
Location = r'JEOPARDY_CSV.csv'

#term frequencies dictionary to be separated by years
freqs = {}

#load the dataframe
df = pd.read_csv(Location, names = ['Show Number', 'Air Date', 'Round',
                                    'Category', 'Value', 'Question', 'Answer'])

#find overall termfrequencies
Frequents = df["Category"].value_counts()
#plot overall term frequencies
Frequents[:20].plot(kind="bar")

#sort by date
df.sort(["Air Date"],inplace=True)

#go through the dates and add the most common terms to a dictionary
for year in range(1984,2013):
    curYear = df.loc[df["Air Date"].str.contains(str(year))]
    curYearFreqs = curYear["Category"].value_counts()  
    curYearIndexes = curYearFreqs.index
    freqs[year] = [[curYearFreqs[0],curYearIndexes[0]],
                   [curYearFreqs[1],curYearIndexes[1]],
                   [curYearFreqs[2],curYearIndexes[2]],
                   [curYearFreqs[3],curYearIndexes[3]],
                   [curYearFreqs[4],curYearIndexes[4]],
                  ]     

#to do: properaly plot all the subplots of the different years' term freqs
print(freqs)

