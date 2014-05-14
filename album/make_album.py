import csv

min_duration = 10
song2count = {}

with open('AlbumVotes.csv', 'rb') as csvfile:
     reader = csv.reader(csvfile, delimiter=',', quotechar='|')

     first = True
     for row in reader:
         if not first:
             duration = row[2]
             fav = row[7]
             
             if float(duration) > min_duration:
                 if fav not in song2count:
                     song2count[fav] = 1
                 else:
                     song2count[fav] = song2count[fav]+1
         else:
             first = False

count2song = []
for k,v in song2count.items():
    count2song.append((v,k))

count2song.sort()
count2song.reverse()

for c,s in count2song:
    print str(c) + ' ' + s


