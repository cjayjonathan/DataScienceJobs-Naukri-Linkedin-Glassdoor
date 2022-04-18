#!/usr/bin/env python
# coding: utf-8

# In[54]:


# Importing relevant libraries
import requests
from bs4 import BeautifulSoup as soup
import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook


# In[55]:


# I also brought in the excel functions where I expect my output to be loaded into
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Data Science Jobs on Naukri'
sheet.append(['job title', 'company', 'location', 'job url'])


# In[58]:



# This would enable servers and network peers identify the application, OS and or the version of the requesting browser 
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.39'}


# In[60]:


html = requests.get('https://www.naukri.com/data-scientist-jobs-in-india', headers = headers)
html.status_code


# In[61]:


# bsobj represents the entire html web pages for parsing while the lxml allows for easy handling of XML and http files
bsobj = soup(html.content,'lxml')
bsobj


# In[62]:


url_list = []
for i in range (1,15):
    url = 'https://www.naukri.com/data-scientist-jobs-in-india?p='+str(i)


# In[69]:


job_title = []
for title in bsobj.findAll('string (//div', 'span', 'ul', 'li[@title]',{'class':'jobContainer'}):
    job_title.append(title.findAll('a')[1].text.strip())
    
job_title
print(job_title)


# In[74]:


company_name =[]
for company in bsobj.findAll('string (//div', 'span', 'span', 'span[@class]',{'class':'jobHeader'}):
    company_name.append(company.a.text.strip())
    
company_name
print(company_name)


# In[75]:


location = []
for i in bsobj.findAll('string (//div', 'span', 'span[@class]',{'class':'jobInfoItem empLoc'}):
    location.append(i.span.text.strip())
    
location
print(location)


# In[77]:


links = []
for i in bsobj.findAll('string (//di/@data-url'):
    link = 'https://www.naukri.com'+ i.a['href']
    links.append(link)
    
links
print(links)


# In[78]:


description = []

for link in links:
    page = requests.get(link,headers=headers)
    bs = soup(page.content,'lxml')
    for job in bs.findAll('div',{'id':'JobDescriptionContainer'})[0]:
        description.append(job.text.strip())


# In[79]:


sheet.append([job_title, company_name, location, links])
excel.save('Data Science Jobs on Naukri.xlsx')
export(excel.save)

