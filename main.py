import requests
import json
from operator import itemgetter

###########################################
######## PLEASE READ THE README ###########
###########################################

# open file
f = open("./data/food-enforcement-0001-of-0001.json", "r")
data_dict = json.load(f)

############### Class 3 Assignment
class3 = []
for i in (data_dict['results']):
    if i['classification'] == 'Class III':
       class3.append(i)
sorted_class3 = sorted(class3, key=itemgetter('state','status'))

# Do a count per state and add to new list
myState = sorted_class3[0]['state']
myStatus = sorted_class3[0]['status']
myStateCount =0
class3_with_count = []
for i in sorted_class3:
   if (myState == i['state']):
        myStateCount+=1
   else:
      class3_with_count.append( {"state": myState, "status": myStatus, "count": myStateCount})
      myStateCount=0
   myState = i['state']
   myStatus = i['status']
class3_with_count_sorted = sorted(class3_with_count, key=itemgetter('count'), reverse=True)

# display the first 5 of the new sorted list with count
for i in range(0, 4):
   print('State', class3_with_count_sorted[i]['state'], 'and status', class3_with_count_sorted[i]['status'], ':', class3_with_count_sorted[i]['count'])


####### Average per month in 2016 project
myAvg_count = 0
for i in (data_dict['results']):
    if i['report_date'].startswith('2016'):
      myAvg_count+=1
print('Average reports per month in 2016:',round(myAvg_count/12))      


####### Top states for 2017 project
dict_2017 = []
dict_2017_with_count = []
myStateCount = 0
for i in (data_dict['results']):
    if i['report_date'].startswith('2017'):
      dict_2017.append( {"state": i["state"] } )
dict_2017_sorted = sorted(dict_2017, key=itemgetter('state'))
myState = dict_2017_sorted[0]['state']
for i in dict_2017_sorted:
   if (myState == i['state']):
        myStateCount+=1
   else:
      dict_2017_with_count.append( {"state": myState, "count": myStateCount})
      myStateCount=0
      myState = i['state']
dict_2017_with_count = sorted(dict_2017_with_count, key=itemgetter('count'), reverse=True)
# display the first 5 of the new sorted list with count
myStateCount =0
for i in range(0, 9):
   print('State', dict_2017_with_count[i]['state'], ':', class3_with_count_sorted[i]['count'])


####### Top years project
dict_years = []
myYearCount = 0
dict_year_with_count = []
# dump all years in a new list
for i in (data_dict['results']):
   dict_years.append( {"year": i['report_date'][0:4] })
#sort the list
dict_years_sorted = sorted(dict_years, key=itemgetter('year'), reverse=True)
#get the first one in the list
myYear = dict_years_sorted[0]['year']

for i in dict_years_sorted:
   if (myYear == i['year']):
        myYearCount+=1
   else:
      dict_year_with_count.append( {"year": myYear, "count": myYearCount})
      myYearCount=0
      myYear = i['year']
dict_year_with_count_sorted = sorted(dict_year_with_count, key=itemgetter('count'), reverse=True)      
print ("Highest year is", dict_year_with_count_sorted[0]['year']," with ",dict_year_with_count_sorted[0]['count']," reports")
len_list = len( dict_year_with_count_sorted) -1
print ("Lowest year is", dict_year_with_count_sorted[len_list]['year'],
     " with ",dict_year_with_count_sorted[len_list]['count']," reports")

# end
f.close()