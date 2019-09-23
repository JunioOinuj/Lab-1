#!/usr/bin/env python
# coding: utf-8

# # Seattle Staff Demographics Dataset
# June 
# 
# 9/23/19

# ## Abstract

# In this lab we want to be able to tell a story with the dataset we ownloaded. More specifically, the story between the Age and Hourly Rate data.  

# ## Dataset Preparation

# In[18]:


#open the file
staff = open("City_of_Seattle_Staff_Demographics.csv", "r");

#create an empty list to store the data
demo_data = [];

#put all lines from the file into a list
for row in staff:
    demo_data.append(row);
    
#close the file. It's the courteous and clean thing to do
staff.close();

print(demo_data[:5]);


# In[ ]:





# In[21]:


#remove the first element (column header)
del demo_data[0];

#create empty lists for westbound and eastbound bikes
Age = [];
Wage = [];    
for item in range(len(demo_data)):
    #make into a list of lists of just numbers
    demo_data[item] = demo_data[item].split(",")
    
    #add data to specific lists for west and east
    Age.append(int(demo_data[item][1]))
    Hourly Rate.append(int(demo_data[item][2]))

Agemin = min(Age)    
Agemax = max(Age)
Wagemin = min(Hourly Rate)
Wagemax = max(Hourly Rate)
    
print(Age)
print(Wage)


# ## Data Modeling

# In[8]:


someNbrs.sort();  # sort the list. It's that easy

import math;
halfwayPoint = math.floor(nbrListItems/2);

#to determine if a number is even or odd, take the modulo of 2 and check remainder; 
# 0 remainder means even
if (nbrListItems) == 0: 
    median = (someNbrs[halfwayPoint] + someNbrs[halfwayPoint-1])/2;
else: # the halfway point is an odd number, so the median is the middle number
    median = someNbrs[halfwayPoint];
    
print("Nbr List items", nbrListItems, "Halfway point: ", halfwayPoint, "Median: ", median);


# ## Data Analysis and Conclusion

# 

# ## Acknowledgements

# In[ ]:


Ms. Sconyers: 
- Thank you for letting me not only copy and use your codes, but for explaining what to do for each part of this lab.
    
Ziah:
- Thank you for helping organize m
Navya:
Mark:
Rihan:

