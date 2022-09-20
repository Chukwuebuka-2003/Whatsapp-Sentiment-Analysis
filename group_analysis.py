#import libraries
import pandas as pd
import numpy as np

#read file line by line
f = open("Group.txt", encoding="utf8")
data = f.readlines()
f.close()

print('num lines: %s' %(len(data)))


#create a function to clean the data

dataset = data[1:]
cleaned_data = []

for line in dataset:
    date = line.split(",")[0]
    line_2 = line[len(date):]
    time = line_2.split("]")[0][2:]
    line_3 = line_2[len(time):]
    name = line_3.split(":")[0][4:]
    line_4 = line_3[len(name):]
    message = line_4[6:-1]


    #print the cleaned data

    (data, time, name, message)
    cleaned_data.append([date, time, name, message])
    
#create a dataframe for the dataset

df = pd.DataFrame(cleaned_data, columns = ['Date', 'Time', 'Name','Message'])

#save to excel or csv

df.to_excel('nacos_data.xlsx',index=False)

#read the data
df = pd.read_excel('nacos_data.xlsx')

print(df.head())

#import library needed for sentiment anaklysis

from textblob import TextBlob

#get the polarity score

polarity = []
for i in range(0,df.shape[0]):
    score = TextBlob(df.iloc[i][0])
    score_1 = score.sentiment[0]
    polarity.append(score_1)


#concate the score with the dataframe

df = pd.concat([df,pd.Series(polarity)], axis = 1)

print(df.head())


#rename the last column to sentiment

df.rename(columns={df.columns[4]: "Sentiment"}, inplace = True)

print(df.head())

#number of positive chats
positive = len(df[df.Sentiment > 0])

print(positive)

#number of negative chats
negative = len(df[df.Sentiment < 0])

print(negative)

#number of neutral
neutral = len(df[df.Sentiment == 0])

print(neutral)


#label the sentiments

filters = [
    (df.Sentiment > 0),
    (df.Sentiment < 0),
    (df.Sentiment == 0)
]

values = ['Positive','Negative', 'Neutral']

df['status'] = np.select(filters, values)

#print the data

print(df.tail)



count = df['status'].value_counts()


#plot a donut chart
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

plt.pie(count, labels = count.index, autopct % (100. * frac), startangle = 90,
        counterclock = False);
plt.title('Nacos 24 Chat sentiment')
plt.savefig('chat.png')

plt.show()
