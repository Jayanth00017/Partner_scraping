#!/usr/bin/env python
# coding: utf-8

# In[396]:


import pandas as pd
from bs4 import BeautifulSoup
from bs4.element import Comment
import requests
import urllib.request
import cssutils
import re
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from datetime import datetime
import dateutil.parser as parser


# In[383]:


driver=webdriver.Chrome(r"C:\ProgramData\chocolatey\bin\chromedriver")


# In[384]:


pd.set_option("display.max_columns", 156)


# In[385]:


op_df=pd.DataFrame(pd.read_csv("output.csv"))


# In[386]:


op_df


# In[397]:


f=open("links.txt","r")

url=[]
for i in f:
    url.append(i)


# In[398]:


urls=[]
for i in url:
    urls.append(i.replace("\n",""))


# In[399]:


html_content=[]
soup=[]

for i in range (len(urls)):
    html_content.append(requests.get(urls[i]).text)
    soup.append(BeautifulSoup(html_content[i], "lxml"))


# In[400]:


title=[]
for i in soup:
    title.append(i.title.text)
op_df["title"]=title


# In[401]:


descr=[]
for i in soup:
    try:
        descr.append(i.find(class_="col-md-9").find(class_="editor-content").text)
    except:
        pr=(i.find(class_="editor-content").find_next("p").find_next("p").find_next("p").find_next("p").find_next("p").text)
        prx=(i.find(class_="editor-content").find_next("p").find_next("p").find_next("p").find_next("p").find_next("p").find_next("p").text)
        descr.append(pr+prx)
op_df["description"]=descr


# In[402]:


short_dsescr=[]
for i in soup:
    try:
        short_dsescr.append(i.find(class_="col-lg-7 col-md-6").find("h2").text)
    except:
        short_dsescr.append(i.find(class_="pane-small m-tb-33 border-right-ul").find("p").text)
op_df["short_description"]=short_dsescr


# In[403]:


#9th and 10th links have errors
for i in soup:
    try:
        print(i.find(class_="col-md-9 col-md-offset-3").find("h6"))
    except:
        print("nil")


# In[404]:


what_will_learn=[]
x=1
for i in soup:
    what_will=[]
    what_will_=[]
    
    x+=1
    try:
        err=[10,11]
        if x in err:
            what_will_learn.append("")
            continue
        prt=(i.find(class_="what-will-you-learn").find_all("li"))
        for j in prt:
            
            what_will.append(j.text)
        what_will_learn.append(what_will)
    except:
        
        pri=(i.find_all(class_="col-md-4 col-sm-6"))
        for i in pri:
            
            if((i.find("h4")) is None):
                print("")
            else:
                what_will_.append(i.find("h4").text)
        what_will_learn.append(what_will_)
        
    
op_df["what_will_learn"]=what_will_learn   


# In[405]:


target_stud=[]
jd=0
for i in soup:
    
    jd+=1
    prt=(i.find_all("ul",class_="clearfix"))
    if(jd in err):
        target_stud.append(" ")
    q=0
    for j in prt:
        
        q+=1
        if(q==9):
            target_stud.append(j.text)
op_df["target_students"]=target_stud


# In[406]:


prereq=[]
cv=0
err=[9,10]
for i in soup:
    
    cv+=1
    if cv in err:
        prereq.append("")
    else:
        prereq.append(i.find(class_="col-md-10").text)
op_df["prerequisites"]=prereq


# In[407]:


op_df["partner_course_url"]=urls


# In[408]:


dur=[]
dur_unit=[]
for i in soup:
    try:
        pt=(i.find(class_="course-sum clearfix").find("h3").text)
        res = "".join([i for i in pt if i.isdigit()])
        
        dur.append(res)
        dur_unit.append("Hours")
    except:
        dur.append("")
        dur_unit.append("")
op_df["total_duration"]=dur
op_df["total_duration_unit"]=dur_unit


# In[409]:


links=[]
for i in url:
    links.append(i.replace("\n","/schedule"))  


# In[410]:


html_content_=[]
soup_=[]

for i in range (len(links)):
    html_content_.append(requests.get(links[i]).text)
    soup_.append(BeautifulSoup(html_content_[i], "lxml"))


# In[411]:


price_o=[]
price_disc=[]
currency=[]
pricing_type=[]
disp_price=[]
for i in soup_:
    try:
        prt= (i.find(class_="price-1 actual-price").text.replace(" ",""))
        prit=(i.find(class_="price-2 early-bird-price").text.replace(" ",""))
        price="".join([i for i in prit if i.isdigit()])
        prc_ori=price="".join([i for i in prt if i.isdigit()])
        price_o.append(prc_ori)
        price_disc.append(price)
        currency.append("INR")
        pricing_type.append("Paid")
        disp_price.append("TRUE")
    except:
        price_o.append("")
        price_disc.append("")
        currency.append("")
        pricing_type.append("")
        disp_price.append("TRUE")
op_df["sale_price"]=price_disc
op_df["regular_price"]=price_o
op_df["currency"]=currency
op_df["pricing_type"]=pricing_type
op_df["Display Price"]=disp_price


# In[412]:


add_inf=[]
course_financing=[]
sm=0
for i in soup_:
    try:
        add_inf.append(i.find(class_="text-capitalize pull-left").text.replace("\r","").replace("\n",""))
        course_financing.append("TRUE")
    except Exception as erro:
        print(erro)
        add_inf.append("")
        course_financing.append("FALSE")

op_df["additional_pricing_details"]=add_inf

op_df["course_financing_available"]=course_financing


# In[415]:


lang=[]
for i in soup:
    lang.append("English")
op_df["languages"]=lang
op_df["subtitle_languages"]=lang


# In[416]:


live_class=[]
for i in soup:
    if(i.text.find("Live")>=1):
        live_class.append("True")
    else:
        live_class.append("False")
op_df["live_class"]=live_class


# In[418]:


batch_1_start=[]
batch_1_end=[]
for i in soup_:
    pr=(i.find(class_="mob-date"))
    
    p=0
    try:
        
        for j in pr:
            
            pri=(j.text.replace(" ","").replace("\n","").split("-"))
            if p==0:
                
                p+=1
                bat=(''.join([i for i in pri[0] if i.isdigit()])+" "+''.join([i for i in pri[0] if not i.isdigit()])+" 2021")
                batc=(''.join([i for i in pri[1] if i.isdigit()])+" "+''.join([i for i in pri[1] if not i.isdigit()])+" 2021")
                start_date = parser.parse(bat)
                batch_1_start.append(start_date.isoformat())
                end_date = parser.parse(batc)
                batch_1_end.append(end_date.isoformat())
    except:
        batch_1_start.append("None")
        batch_1_end.append("None")
op_df["batch|1|batch_start_date"]=batch_1_start
op_df["batch|1|batch_end_date"]=batch_1_end


# In[444]:


content=[]
o=1
for i in soup:
    try:
        to=(i.find_all(class_="right"))
        po=[]
        for j in to:
            po.append(j.text)
        content.append(po)
    except:
        print("Error")
        print(i.find(class_="panel-heading active"))
    o+=1

op_df["content"]=content


# In[540]:


review=[]
review_name=[]
o=1
d=[9,10]
for i in soup:
    try:
        pt=(i.find(class_="tab-pane fade user-voice active in").find(class_="media").text.split("\xa0"))
        pri=(pt[0].split("."))
        revi=(pri[0])
        
        pr=(pt[1].split("  "))
        try:
            rev+(pri[1])
        except:
            print(" ")
        review.append(revi)
        try:
            review_name.append(pr[2])
            
            
            
        except:
            print("err")
        
        
        
    except:
        review_name.append(" ")
        review.append(" ")
    
    o+=1
op_df["review|1|review"]=review
op_df["review|1|reviewer_name"]=review_name


# In[ ]:





# In[542]:


op_df.to_excel("Vas.xlsx")


# In[ ]:





# In[ ]:




