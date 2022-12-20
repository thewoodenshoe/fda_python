# fda_python
demo for playing with json data using python


Dear sasha-fedtsov,

Please understand I went for SPEED and not proper.
I'm noticing repetative requests in the list, for example question 4 goes over all years, and question 3 goes over one specific year. 

The proper way to do this to create a function "create sorting list" with input:
1. the sorting order
2. possible the new dict list items.
3. In this function the counters are uniform (myStateCount, myYearCount, etc. all become "myCount")

Then another function "display list" is created to call the function above with input:
1. Specific year or all
2. display restrictions (avg, min_max, top10)
3. Filter

END RESULT: Call the "prepare list" function. For example:

1. display_list ("all", "top10", "class3")
2. display_list (2016, "avg")
3. display_list (2017, "top10", "state")
4. display_list ("all", "min_max", "state")