#!/usr/bin/env python
# coding: utf-8

# In[34]:


# Importing relevant libraries
from bs4 import BeautifulSoup
import requests
import openpyxl


# In[35]:


# I bring in the excel component
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Data Science Jobs on LinkedIn'
sheet.append(['job title', 'company', 'location', 'job url'])


# In[36]:


# Introduced the URL of interest for parsing
source = requests.get('https://www.linkedin.com/jobs/search/?keywords=data%20scientist')
soup = BeautifulSoup(source.text, 'html.parser')


# In[24]:


#Trying to get the right attributes for each category from the html output
jobs_on_linkedin = soup.find('ul', class_='jobs-search__results-list').find_all('li')
print(jobs_on_linkedin)


# In[37]:



#I will now print the jobs
for job in jobs:
    job_name = job.find('div', 'base-card base-card--link base-search-card base-search-card--link job-search-card').span.get_text(strip=True)
    company_name = job.find('div', 'base-card base-card--link base-search-card base-search-card--link job-search-card').h4.get_text(strip=True)
    location_ = job.find('span', 'job-search-card__location').get_text(strip=True)
    link = job.find('a', 'base-card__full-link')['href'] 
 

    


# In[30]:


#Print would display the output I am looking for
print(job_name)
print(company_name)
print(location_)
print(link)


# In[44]:


# I intend wrapping it up a;; in an excvel document
sheet.append([job_name, company_name, location_, link])
excel.save('Data Science Jobs on LinkedIn.xlsx')
print(excel.save)
excel.close()


# In[ ]:




