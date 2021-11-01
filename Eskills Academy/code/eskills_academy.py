#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
from openpyxl import load_workbook
import dateutil.parser as parse


# In[2]:


driver=webdriver.Chrome(r"D:\chromedriver")
driver.get("https://eskills.academy/courses")


# In[3]:


links=[]


# In[35]:


k=driver.find_elements_by_class_name("course-listing")


# In[36]:


for i in k:
    links.append("https://eskills.academy"+i.get_attribute("data-course-url"))


# In[38]:


len(links)


# In[45]:


l=driver.find_elements_by_class_name("course-price")


# In[40]:


l[0].get_attribute("src")
#image is not available in jpg/png


# In[57]:


#price=[]
#price_unit=[]
l=driver.find_elements_by_class_name("course-price")
for i in l:
    price.append(i.text.split("$")[-1])
    price_unit.append("USD")
price.remove(price[3])
price_unit.remove(price_unit[3])


# In[59]:


get_ipython().run_cell_magic('time', '', 'short_desc=[]\nfor i in links:\n    driver.get(i)\n    short_desc.append(driver.find_element_by_class_name("subheader").text)')


# In[55]:


links.remove("https://eskills.academy/p/comptia-6-courses-core-training-bundle")


# In[66]:


get_ipython().run_cell_magic('time', '', 'desc=[]\nfor i in links:\n    driver.get(i)\n    desc.append(driver.find_element_by_class_name("block__text-wrapper").text)\n#should course also be included as description')


# In[70]:





# In[72]:


get_ipython().run_cell_magic('time', '', 'review_name=[]\nreview_body=[]\nfor i in links:\n    driver.get(i)\n    t=driver.find_elements_by_class_name("block__text-with-image-grid__column__heading-text")\n    m=driver.find_elements_by_class_name("block__text-with-image-grid__column__body")\n    for j in range(len(t)):\n        review_name.append(t[j].text)\n        review_body.append(m[j].text)')


# In[87]:


u=driver.find_element_by_class_name("block__text-wrapper").text.split("\n")


# In[85]:


#driver.get("https://eskills.academy/p/master-of-information-systems-cyber-security")
for y in u.find_elements_by_tag_name("h4"):
    if y.text=="What you’ll learn:":
        flag=1
        continue
    if flag==1:
        text=y.text
        break


# In[161]:


get_ipython().run_cell_magic('time', '', 'what=[]\nfor j in links:\n    driver.get(j)\n    flag=0\n    text=" "\n    u=driver.find_element_by_class_name("block__text-wrapper")\n    try:\n        k=u.find_element_by_tag_name("h4")\n        k=u.find_elements_by_tag_name("h4")\n    except:\n        k=u.find_elements_by_tag_name("strong")\n    for y in k:\n        if "What" in y.text:\n            flag=1\n            continue\n        if flag==1:\n            text=y.text\n            break\n    u=u.text.split("\\n")\n    if text==" ":\n        what.append(" ")\n        continue\n    m=[]\n    flag=0\n    for i in u:\n        if "What" in i:\n            flag=1\n            m.append(i)\n            continue\n        elif i==text:\n            break\n        if flag==1 and i!=\'\':\n            m.append(i) \n    what.append("|".join(m))')


# In[159]:


get_ipython().run_cell_magic('time', '', 'who=[]\nfor j in range(len(links)):\n    driver.get(links[j])\n    flag=0\n    text=" "\n    u=driver.find_element_by_class_name("block__text-wrapper")\n    try:\n        k=u.find_element_by_tag_name("h4")\n        k=u.find_elements_by_tag_name("h4")\n    except:\n        k=u.find_elements_by_tag_name("strong")\n    for y in k:\n        if "Whom" in y.text or "Who" in y.text:\n            flag=1\n            continue\n        if flag==1:\n            text=y.text\n            break\n    u=u.text.split("\\n")\n    m=[]\n    flag=0\n    for i in range(len(u)):\n        if "Whom" in u[i] or "Who" in u[i]:\n            print(u[i])\n            flag=1\n            m.append(u[i])\n            continue\n        elif u[i]==text:\n            break\n        if flag==1 and u[i]!=\'\':\n            m.append(u[i])   \n    who.append("|".join(m))')


# In[169]:


df=pd.read_excel("eskills.xlsx")
df["target_students"]=who
df["what_will_learn"]=what
df["short_description"]=short_desc
df["regular_price"]=price
df["sale_price"]=price
df["partner_course_url"]=links
df["title"]=title
df["learn_type"]="Certification"
df["delivery_type"]="Online"
df["instruction_type"]="Self Paced"
df["languages"]="English"
df["subtitle_languages"]="English"
df["accessibilities"]="Lifetime Access"
df["availabilities"]="Mobile,Desktop,Tablet"
df["Display Price"]="True"
df["pricing_type"]="Paid"
df["currency"]="USD"


# In[167]:


get_ipython().run_cell_magic('time', '', 'title=[]\nfor i in links:\n    driver.get(i)\n    h=driver.find_element_by_class_name("banner__heading-group")\n    title.append(h.find_element_by_class_name("header").text)')


# In[174]:


df.to_excel("eskills.xlsx")


# In[172]:


df["review|1|reviewer_name"]=review_name[0]
df["review|2|reviewer_name"]=review_name[1]
df["review|3|reviewer_name"]=review_name[2]
df["review|1|review"]=review_body[0]
df["review|2|review"]=review_body[1]
df["review|3|review"]=review_body[2]


# In[173]:


df


# In[176]:


r_n=[]
k=[]
for i in review_name:
    k.append(i)
    if len(k)==3:
        r_n.append("|".join(k))
        k=[]


# In[181]:


len(r_n)


# In[183]:


driver.get(links[1])


# In[189]:


for i in links:
driver.find_elements_by_class_name("block__curriculum__section__list__item__lecture-name")


# In[4]:


df=pd.read_excel("eskills.xlsx")


# In[5]:


links=list(df['partner_course_url'])


# In[6]:


driver.get


# In[17]:


get_ipython().run_cell_magic('time', '', 'desc=[]\nfor j in range(4):\n    driver.get(links[j])\n    flag=0\n    text=" "\n    u=driver.find_element_by_class_name("block__text-wrapper")\n    try:\n        k=u.find_element_by_tag_name("h4")\n        k=u.find_elements_by_tag_name("h4")\n    except:\n        k=u.find_elements_by_tag_name("strong")\n    if k[0].text=="Course insights:":\n        k=k[1].text\n    else:\n        k=k[0].text\n    u=u.text.split("\\n")\n    m=[]\n    flag=0\n    for i in range(len(u)):\n        if u[i]=="":\n            continue\n        if u[i]==k:\n            break\n        m.append(u[i])\n    desc.append("|".join(m))\n    print(desc[-1])')


# In[53]:


get_ipython().run_cell_magic('time', '', '#content=[]\nfor b in range(len(links)):\n    if content[b]!="":\n        continue\n    cont=""\n    driver.get(links[b])\n    u=driver.find_element_by_class_name("block__text-wrapper")\n    try:\n        k=u.find_element_by_tag_name("h4")\n        k=u.find_elements_by_tag_name("h4")\n    except:\n        k=u.find_elements_by_tag_name("strong")\n    flag=0\n    for y in k:\n        if "Whom" in y.text or "Who" in y.text:\n            text=y.text\n    o=u.find_elements_by_tag_name("li")\n    u=u.text.split("\\n")\n    p=[]\n    for l in u:\n        if l==text:\n            break\n        if flag==1:\n            p.append(l)\n        if "What" in l:\n            flag=1\n    c=1\n    for i in range(len(o)):\n        if o[i].text in p and o[i]!="":\n            cont+=(f"<p><strong>Module {c}:</strong>{o[i].text}</p>")\n            c+=1\n    content[b]=cont\n    print(content[b])')


# In[82]:


get_ipython().run_cell_magic('time', '', 'desc=[]\nfor b in range(47):\n    print(b)\n    \'\'\'if desc[b]!="":\n        continue\'\'\'\n    cont=""\n    driver.get(links[b])\n    u=driver.find_element_by_class_name("block__text-wrapper")\n    try:\n        k=u.find_element_by_tag_name("h4")\n        k=u.find_elements_by_tag_name("h4")\n    except:\n        k=u.find_elements_by_tag_name("strong")\n    o=u.find_elements_by_tag_name("li")\n    u=u.text.split("\\n")\n    m=0\n    if len(k)<1:\n        k.append("")\n    while u[m]=="":\n        m+=1\n    if u[m]==k[0].text:\n        text=k[1].text\n        u.remove(u[m])\n    else:\n        text=k[0].text\n    p=[]\n    for l in u:\n        if l==text:\n            break\n        p.append(l)\n    for i in range(len(o)):\n        if o[i].text in p:\n            p.remove(o[i].text)\n    for i in p:\n        if i!="":\n            cont+="<p>"+i+"</p>"\n    desc.append(cont)')


# In[88]:


desc.append("")


# In[90]:


df=pd.DataFrame()
df["content"]=content
df["desc"]=desc
df.to_excel("cont+desc.xlsx")


# In[89]:


len(desc)


# In[93]:


driver.get(links[-1])


# In[94]:


get_ipython().run_cell_magic('time', '', 'who=[]\nfor j in range(len(links)):\n    driver.get(links[j])\n    flag=0\n    text=" "\n    u=driver.find_element_by_class_name("block__text-wrapper")\n    try:\n        k=u.find_element_by_tag_name("h4")\n        k=u.find_elements_by_tag_name("h4")\n    except:\n        k=u.find_elements_by_tag_name("strong")\n    for y in k:\n        if "Pre-requisites" in y.text:\n            flag=1\n            continue\n        if flag==1:\n            text=y.text\n            break\n    u=u.text.split("\\n")\n    m=[]\n    flag=0\n    for i in range(len(u)):\n        if "Pre-requisites" in u[i]:\n            print(u[i])\n            flag=1\n            m.append(u[i])\n            continue\n        elif u[i]==text:\n            break\n        if flag==1 and u[i]!=\'\':\n            m.append(u[i])   \n    who.append("|".join(m))')


# In[112]:


driver.get(links[6])


# In[ ]:




