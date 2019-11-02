#!/usr/bin/env python
# coding: utf-8

# In[53]:


#lets take the following string:1
s='I am very keen in building up my career in Data Science, but not sure from where to start. If I search the web it throws me thousands of articles, few are relevant others make me confused, again I come around to the same page. Supervised has provided me a good platform to remove all such qualms which were wrangling in my mind'
print(s)


# In[54]:


#.total length of the string
t_s = s.split()
print(t_s)


# In[55]:


avg = len(s)/len(t_s)
print(avg)
#print('Average of the String (str):' + str(avg))


# In[56]:


#2. Lower the text in the string.
print(s.lower())


# In[57]:


#3.Try to get the clean text removing the punctuation from the string.
print(s.replace(",",""))


# In[58]:


#4. Extract word "Data Science" from the string
import re
s_ds = re.search('Data Science',s)
print(re.search('Data Science',s))
print(s_ds)


# In[59]:


#5.Find the frequency of words used in the string.
from collections import Counter
counts = Counter(t_s)
print(counts)


# In[60]:


#6.Fetch the duplicate pairs used in the string.
def duplicate_count(s):
    return len(list(filter(lambda x:x[1]>1,Counter(s).items())))

duplicate_count(s)


# In[61]:


from collections import defaultdict
dic = defaultdict(set)
for i, sen in enumerate(t_s):
    for word in sen.split():
        dic[word].add(i)
        
dic


# In[62]:


#7.#Can you change the word "Supervised" to "Unsupervised" in the string
s1=s.replace('Supervised','UnSupervised')
print('before:'+s)
print('after:'+s1)


# In[63]:


#8.Splitting of the string with a dot operator(.)
print(t_s)
t_s1 = s.split("[.]")
t_s2 = s.split(".")
print(t_s1)
print(t_s2)


# In[64]:


#8.Find the words from the string which ends with "e"
c = Counter(i for i in t_s if i.endswith('e'))
print(c)


# In[65]:


#9.Figure out number of a's used in the string.
c1 = s.count('a')
print(c1)


# In[66]:


#Questions on Dictionary:
#In the weekend , I purchased 250g of apple, 500g of sugar, 2.5 kg of rice, 
#2.5 litres of milk and finally 1 dozen of egg.

#1.Can you help me frame the above purchase in the form of 
#dictionary with commodities as keys to it.

a_dict = {'apple':'250g', 'sugar':'500g', 'rice':'2.5kg', 'milk':'2.5L', 'Egg': '1 Dozen'}
print(a_dict)


# In[67]:


#2. I forgot to mention another item, 1kg of atta packet. Can you also add it ?
a_dict['atta']='1 packet'
print(a_dict)


# In[68]:


#3. Instead of 2kg of rice, I bought only 1kg of rice. Can you change the corresponding value ?
a_dict['rice']='1 kg'
print(a_dict)


# In[69]:


#4.Can you list out all these items using a loop.
for item in a_dict.items():
    print(item)


# In[70]:


#However, the cost of 1 kg apple is Rs.220, 1 kg of sugar is Rs.43, 1 Kg of rice is Rs. 45,
#1 litre of milk is Rs.30 and 1 dozen of egg is Rs. 60.
p_dict={'apple':220, 'sugar':43, 'rice':45, 'milk/lit':30, 'Egg per doz':60}
print(p_dict)


# In[71]:


#Questions on List. Listed are top AI companies in the world
AI_list = ['Amazon', 'Facebook', 'HiSilicon', 'Google', 'Apple', 'Microsoft', 'Sensetime']

#Sort the list in ascending order
AI_list.sort()
AI_list


# In[72]:


#Add multiple companies at once 'Nvidia', 'OpenAI' , 'Qualcomm' and 'Reliance' to the list
AI_list.extend(['Nvidia','OpenAI','Qualcomm','Reliance'])
AI_list


# In[73]:


#Lower the list using List comprehension
x=[i.lower() for i in AI_list]
print(x)


# In[74]:


#Elimiate 'Reliance' from the list
AI_list.remove('Reliance')
AI_list


# In[78]:


#Extract 'Facebook', 'Google' and 'Microsoft' using a single command
l =  ['Amazon', 'Facebook', 'HiSilicon', 'Google', 'Apple', 'Microsoft', 'Sensetime']
print(l[1:7:2])


# In[81]:


# Tuples
t=(220, 43, 45, 30, 60)
t


# In[84]:


min(t)


# In[86]:


max(t)


# In[88]:


t1 = ('Amazon', 'Facebook', 'HiSilicon', 'Google', 'Apple', 'Microsoft', 'Sensetime')
t1


# In[91]:


t2 = (t)+(t1)
t2


# In[93]:


len(t1)


# In[94]:


len(t)

