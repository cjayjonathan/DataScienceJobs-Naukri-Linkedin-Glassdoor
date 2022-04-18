#!/usr/bin/env python
# coding: utf-8

# In[30]:


# Importing relevant libraries
import requests
from bs4 import BeautifulSoup as soup
import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook


# In[31]:


# I also brought in the excel functions where I expect my output to be loaded into
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Data Science Jobs on Glassdoor'
sheet.append(['job title', 'company', 'location', 'job url'])


# In[40]:


# This would enable servers and network peers identify the application, OS and or the version of the requesting browser 
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.39'}


# In[42]:



html = requests.get('https://www.glassdoor.co.in/Job/india-data-scientist-jobs-SRCH_IL.0,5_IN115_KO6,20.htm', headers = headers)
html.status_code


# In[41]:


# bsobj represents the entire html web pages for parsing while the lxml allows for easy handling of XML and http files
bsobj = soup(html.content,'lxml')
bsobj


# In[36]:


url_list = []
for i in range (1,15):
    url = 'https://www.glassdoor.co.in/Job/india-data-scientist-jobs-SRCH_IL.0,5_IN115_KO6,20.htm?p='+str(i)


# In[44]:


job_title = []
for title in bsobj.findAll('div',{'class':'jobContainer'}):
    job_title.append(title.findAll('a')[1].text.strip())
    
job_title
print(job_title)


# In[45]:


company_name =[]
for company in bsobj.findAll('div',{'class':'jobHeader'}):
    company_name.append(company.a.text.strip())
    
company_name
print(company_name)


# In[46]:


location = []
for i in bsobj.findAll('div',{'class':'jobInfoItem empLoc'}):
    location.append(i.span.text.strip())
    
location
print(location)


# In[47]:


links = []
for i in bsobj.findAll('div',{'class':'jobContainer'}):
    link = 'https://www.glassdoor.co.in'+ i.a['href']
    links.append(link)
    
links
print(links)


# In[48]:


description = []

for link in links:
    page = requests.get(link,headers=headers)
    bs = soup(page.content,'lxml')
    for job in bs.findAll('div',{'id':'JobDescriptionContainer'})[0]:
        description.append(job.text.strip())


# In[15]:


description


# In[49]:


sheet.append([job_title, company_name, location, links])
excel.save('Data Science Jobs on Glassdoor.xlsx')
export(excel.save)


# In[ ]:




