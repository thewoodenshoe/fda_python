import requests
import json
from operator import itemgetter

###########################################
######## PLEASE READ THE README
###########################################

##### INIT ####
# open file
f = open("./data/food-enforcement-0001-of-0001.json", "r")
data_dict = json.load(f)

###########################################
# ############### Class 3 Assignment
###########################################
# 1. Create a filtered list on class 3 and sort it
# 2. Loop through the sorted list and do count+=1 until you find a change in state.
# 3. If you find a change in stage, add a row to list "class3_with_count" with state, status and count.
# 4. Sort the list class3_with_count (desc), I made a new list "class3_with_count_sorted"
# 4.a. you could simply overwrite. But this was quicker with testing. And i went for speed.
# 5. Print the first 5 in the list "class3_with_count_sorted".

# Create a new list class3, fill this up with only the Class III and sort it at the end.
class3 = []
for i in (data_dict['results']):
    if i['classification'] == 'Class III':
        class3.append(i)
sorted_class3 = sorted(class3, key=itemgetter('state', 'status'))


# Do a count per state and add to new list
myState = sorted_class3[0]['state']
myStatus = sorted_class3[0]['status']
myCounter = 0
class3_with_count = []
for i in sorted_class3:
    # loop through the list and if the state is the same, add +1 to the counter.
    # if the new record state is not the same, add the  previous state to a new list with the count and reset.
    if (myState == i['state']):
        myCounter += 1
    else:
        class3_with_count.append({"state": myState, "status": myStatus, "count": myCounter})
        myCounter = 0
    myState = i['state']
    myStatus = i['status']
# now sort the list desc, made a new list for the ease of the conversation
class3_with_count_sorted = sorted(class3_with_count, key=itemgetter('count'), reverse=True)

# display the first 5 of the new sorted list with count
for i in range(0, 4):
    print('State', class3_with_count_sorted[i]['state'], 'and status', class3_with_count_sorted[i]['status'], ':',
          class3_with_count_sorted[i]['count'])





###########################################
####### Average per month in 2016 project
###########################################
# 1. loop through the list and check if report_date = 2016
# 2. If that's the case, then add +1 to the counter.
# 3. The result is a total count of the year
# 3. print the count /12 months and you have the avg per month
myCounter = 0
for i in (data_dict['results']):
    if i['report_date'].startswith('2016'):
        myCounter += 1
print('Average reports per month in 2016:', round(myCounter / 12))




###########################################
####### Top states for 2017 project
###########################################
# 1. Loop through the json file and filter out the report-date = 2017, add this to a new list
# 2. create  new list and sort it (for conversation)
# 3. grab the first state value in the new sorted list
# 4. Loop through the list and do counter+=1 if the state is the same. If not, add previous to a new list with count.
# 5. Sort, and print the first 10
dict_2017 = []
dict_2017_with_count = []
myCounter = 0
for i in (data_dict['results']):
    if i['report_date'].startswith('2017'):
        dict_2017.append({"state": i["state"]})
dict_2017_sorted = sorted(dict_2017, key=itemgetter('state'))

# Grab the first state value in the new sorted list
myState = dict_2017_sorted[0]['state']
for i in dict_2017_sorted:
    if myState == i['state']:
        myCounter += 1
    else:
        dict_2017_with_count.append({"state": myState, "count": myCounter})
        myCounter = 0
        myState = i['state']
dict_2017_with_count = sorted(dict_2017_with_count, key=itemgetter('count'), reverse=True)
# display the first 5 of the new sorted list with count
myCounter = 0
for i in range(0, 9):
    print('State', dict_2017_with_count[i]['state'], ':', class3_with_count_sorted[i]['count'])

###########################################
####### Top years project
###########################################
# 1. loop through json file and create a new list with only the year and create a new list sorted
# 2. loop through sorted list and do a counter per year. if year changes, add to new list with the count
# 3. grab the first item in the list, since it's sorted, and print it
# 4. grab the last item in the list, since it's sorted, and print it
dict_years = []
myCounter = 0
dict_year_with_count = []
# dump all years in a new list
for i in (data_dict['results']):
    dict_years.append({"year": i['report_date'][0:4]})
# sort the list
dict_years_sorted = sorted(dict_years, key=itemgetter('year'), reverse=True)
# get the first one in the list
myYear = dict_years_sorted[0]['year']

for i in dict_years_sorted:
    if (myYear == i['year']):
        myCounter += 1
    else:
        dict_year_with_count.append({"year": myYear, "count": myCounter})
        myCounter = 0
        myYear = i['year']
dict_year_with_count_sorted = sorted(dict_year_with_count, key=itemgetter('count'), reverse=True)

# grap the first item in the list, since it's sorted
print("Highest year is", dict_year_with_count_sorted[0]['year'], " with ", dict_year_with_count_sorted[0]['count'],
      " reports")

# grab the last item in the list, since it's sorted, and print it
len_list = len(dict_year_with_count_sorted) - 1
print("Lowest year is", dict_year_with_count_sorted[len_list]['year'],
      " with ", dict_year_with_count_sorted[len_list]['count'], " reports")

# end
f.close()
