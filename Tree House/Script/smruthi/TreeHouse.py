#!/usr/bin/env python
# coding: utf-8

# In[3]:


from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
from openpyxl import load_workbook
import dateutil.parser as parse


# In[48]:


driver=webdriver.Chrome("D:\chromedriver")


# In[194]:


driver.get("https://teamtreehouse.com/tracks/stem-learning-for-kids")


# In[139]:


driver.get("https://teamtreehouse.com/tracks/start-your-coding-journey")


# In[218]:


driver.get("https://teamtreehouse.com/tracks/skills-for-a-modern-entrepreneur-or-business-owner")


# In[276]:


driver.get("https://teamtreehouse.com/tracks/web-programming-skills-for-graphic-designers")


# In[292]:


driver.get("https://teamtreehouse.com/tracks/skills-for-modern-marketing-business")


# In[306]:


driver.get("https://teamtreehouse.com/tracks/intermediate-android")


# In[322]:


driver.get("https://teamtreehouse.com/tracks/intermediate-c-2")


# In[339]:


driver.get("https://teamtreehouse.com/tracks/full-stack-javascript")


# In[350]:


driver.get("https://teamtreehouse.com/tracks/digital-literacy")


# In[362]:


driver.get("https://teamtreehouse.com/tracks/algorithms-and-data-structures")


# In[372]:


driver.get("https://teamtreehouse.com/tracks/exploring-flask-with-peewee")


# In[383]:


driver.get("https://teamtreehouse.com/tracks/beginning-security")


# In[394]:


driver.get("https://teamtreehouse.com/tracks/learn-ruby")


# In[404]:


driver.get("https://teamtreehouse.com/tracks/learn-react")


# In[416]:


driver.get("https://teamtreehouse.com/tracks/beginning-data-analysis")


# In[427]:


driver.get("https://teamtreehouse.com/tracks/intermediate-python")


# In[428]:


block=driver.find_elements_by_class_name("card-box")
urls=[]
for i in block:
    urls.append(i.get_attribute("href"))


# In[429]:


len(urls)


# In[430]:


urls


# In[431]:


urls.remove("https://teamtreehouse.com/library/welcome-to-intermediate-python")


# In[432]:


get_ipython().run_cell_magic('time', '', 'import requests\nfrom bs4 import BeautifulSoup\nsoup=[]\nfor i in urls:\n    r = requests.get(i)\n    soup.append(BeautifulSoup(r.content,"html.parser")) # If this line causes an error, run \'pip install html5lib\' or install html5lib')


# In[433]:


get_ipython().run_cell_magic('time', '', 'title=[]\nfor i in soup:\n    title.append(i.find(\'title\').text)\ndesc=[]\nwhat=[]\nfor i in soup:\n    try:\n        temp=\'\'\n        temp2=\'\'\n        flag=0\n        t=i.find(id="syllabus-description").text.split("\\n")\n        for j in t:\n            if j==\'\':\n                continue\n            if j=="What you\'ll learn":\n                flag=1\n                continue\n            if flag==1:\n                temp2+=j+"|"\n                continue\n            if flag==0:\n                temp+=j+"|"\n        what.append(temp2)\n        desc.append(temp)\n    except:\n        try:\n            temp=\'\'\n            temp2=\'\'\n            flag=0\n            t=i.find(id="workshop-description").text.split("\\n")\n            for j in t:\n                if j==\'\':\n                    continue\n                if j=="What you\'ll learn":\n                    flag=1\n                    continue\n                if flag==1:\n                    temp2+=j+"|"\n                    continue\n                if flag==0:\n                    temp+=j+"|"\n            what.append(temp2)\n            desc.append(temp)\n        except:\n            desc.append("")\n            what.append("")\nins_name=[]\nins_bio=[]\nfor i in soup:\n    try:\n        a=i.find(id="syllabus-authors").text.split("\\n")\n        b=[]\n        for i in a:\n            if i!=\'\' and i!=\'Teacher\' and i!=\'Teachers\':\n                b.append(i)\n        ins_name.append("")\n        ins_bio.append("|".join(b))\n    except:\n        try:\n            a=i.find(id="workshop-authors").text.split("\\n")\n            b=[]\n            for i in a:\n                if i!=\'\' and i!=\'Teacher\' and i!=\'Teachers\':\n                    b.append(i)\n            ins_name.append("")\n            ins_bio.append("|".join(b))\n        except:\n            ins_name.append("")\n            ins_bio.append("")\ndur=[]\nunit=[]\nfor i in soup:    \n    y=(i.find(attrs={"class":"markdown-zone"}).text.split("\\n")[1].split(" ")[4])\n    y=y.split("-")\n    dur.append(y[0])\n    unit.append(y[-1])\nt=[]\nfor i in urls:\n    driver.get(i)\n    try:\n        img=driver.find_elements_by_class_name("instructor-avatar")\n        imgs=""\n        for i in img:\n            j=i.get_attribute("style")\n            j=j.split("url(")[-1]\n            imgs+=j.split(\'"\')[1]+"|"\n        t.append(imgs)\n    except:\n        print("NOPE!")\n        t.append("")\nlevel=[]\nfor i in soup:\n    try:\n        level.append(i.find(id="syllabus-skill-level").text)\n    except:\n        level.append(i.find(id="workshop-skill-level").text)\n        ')


# In[434]:


df2 = pd.DataFrame(columns = ['title', 'desc','content','what_u_learn',"duration","duration_unit","ins_name","ins_bio","ins_photo","level","url"])


# In[435]:


df2['ins_photo']=t
df2['url']=urls
df2['duration']=dur
df2['ins_name']=ins_name
df2['ins_bio']=ins_bio
df2['desc']=desc
df2["what_u_learn"]=what
df2['title']=title
df2["duration_unit"]=unit
df2["level"]=level


# In[436]:


df2


# In[437]:


df2.to_excel("intermediate_python.xlsx")


# In[337]:


driver.get(urls[6])


# In[235]:


soup[13].find(id="syllabus-skill-level").text


# In[160]:


title=[]
for i in soup:
    title.append(i.find('title').text)


# In[161]:


desc=[]
what=[]
for i in soup:
    try:
        temp=''
        temp2=''
        flag=0
        t=i.find(id="syllabus-description").text.split("\n")
        for j in t:
            if j=='':
                continue
            if j=="What you'll learn":
                flag=1
                continue
            if flag==1:
                temp2+=j+"|"
                continue
            if flag==0:
                temp+=j+"|"
        what.append(temp2)
        desc.append(temp)
    except:
        desc.append("")
        what.append("")
t=[]
for i in urls:
    driver.get(i)
    try:
        img=driver.find_element_by_class_name("instructor-avatar").get_attribute("style")
        img=img.split("url(")[-1]
        img=img.split('"')[1]
        t.append(img)
    except:
        print("NOPE!")
        t.append("")


# In[130]:


len(desc)


# In[162]:


ins_name=[]
ins_bio=[]
for i in soup:
    try:
        a=i.find(id="syllabus-authors").text.split("\n")
        b=[]
        for i in a:
            if i!='' and i!='Teacher':
                b.append(i)
        ins_name.append(b[0])
        ins_bio.append(b[-1])
    except:
        ins_name.append("")
        ins_bio.append("")


# In[15]:


#driver.get(urls[0])
w=driver.find_elements_by_class_name("stage-meta")
for i in w:
    print("|".join(i.text.split("\n")))
    #print(i.text.split("\n")[0])
    #print(i.text.split("\n")[0]+"|"+i.text.split("\n")[1])
    print()
#should we only append the names or along with the subheadings?


# In[210]:


soup[0].find_all()


# In[217]:


#driver.get(urls[0])
w=driver.find_elements_by_xpath("//*[@class='steps-list ']/li/a/h4")
'''x=driver.find_elements_by_class_name("stage-meta")
for i in x:
    print(i.text.split("\n")[0])
    driver.find_element_by_link_text(i.text.split("\n")[0]).click()
    for j in w:
        print(j.text)'''
driver.find_element_by_class_name("radial-progress").click()


# In[163]:


t=[]
for i in urls:
    driver.get(i)
    try:
        img=driver.find_element_by_class_name("instructor-avatar").get_attribute("style")
        img=img.split("url(")[-1]
        img=img.split('"')[1]
        t.append(img)
    except:
        print("NOPE!")
        t.append("")


# In[108]:


len(t)


# In[164]:


dur=[]
unit=[]
for i in soup:    
    y=(i.find(attrs={"class":"markdown-zone"}).text.split("\n")[1].split(" ")[4])
    y=y.split("-")
    dur.append(y[0])
    unit.append(y[-1])


# In[166]:


df['ins_photo']=t
df['url']=urls
df['duration']=dur
df['ins_name']=ins_name
df['ins_bio']=ins_bio
df['desc']=desc
df["what_u_learn"]=what
df['title']=title
df["duration_unit"]=unit


# In[167]:


df


# In[111]:


df2 = pd.DataFrame(columns = ['title', 'desc','content','what_u_learn',"duration","duration_unit","ins_name","ins_bio","ins_photo","url"])


# In[133]:


df2['ins_photo']=t
df2['url']=urls
df2['duration']=dur
df2['ins_name']=ins_name
df2['ins_bio']=ins_bio
df2['desc']=desc
df2["what_u_learn"]=what
df2['title']=title
df2["duration_unit"]=unit


# In[134]:


df2


# In[147]:


urls[3]


# In[169]:


df2.to_excel("start_ur_coding_journey.xlsx")


# In[ ]:


for i in urls:
    driver.get(i)
    time.sleep(5)
    pri=(driver.find_elements_by_class_name("stage-meta"))
    for j in pri:
        prnt=(j.text.replace(":","").replace("questions","").replace("\n","|"))
        res = ''.join([i for i in prnt if not i.isdigit()])
        print(res)


# In[49]:


get_ipython().run_cell_magic('time', '', 'cont=[]\nfor i in range(len(urls)):\n    driver.get(urls[i])\n    time.sleep(3)\n    a=driver.find_elements_by_class_name("toggle-steps")\n    for k in range(len(a)-1):\n        time.sleep(2)\n        try:\n            a[k].click()\n        except:\n            pass\n    time.sleep(2)\n    content=[]\n    pri=(driver.find_elements_by_class_name("featurette"))\n    for j in pri:\n        prnt=(j.text.replace(":","").replace("questions","").replace("\\n","|").replace("||","|"))\n        res = \'\'.join([i for i in prnt if not i.isdigit()])\n        content.append(res)\n    #cont[i]=("|".join(content))\n    cont.append("|".join(content))')


# In[417]:


df=pd.DataFrame(pd.read_excel("lexploring_flask_with_peewee.xlsx"))


# In[428]:


df.to_excel("lexploring_flask_with_peewee.xlsx")


# In[418]:


urls=list(df['url'])


# In[50]:


cont


# In[424]:


len(cont)


# In[425]:


len(urls)


# In[46]:


urls=["https://teamtreehouse.com/library/working-with-the-fetch-api"]


# In[426]:


df["content"]=cont


# In[427]:


df["learn_type"]="Certification"
df["delivery_method"]="Online"
df["Instruction_type"]="Instructor Paced"
df["Languages"]="English"


# In[242]:


df["url"]


# In[143]:


df


# In[43]:


driver.get(urls[6])


# In[60]:


df["content"][7]=cont[0]


# In[52]:


c=list(df["content"])


# In[57]:


c[7]


# In[111]:


driver.get(urls[0])


# In[13]:


driver.find_elements_by_class_name("stage-meta")[1].text.split("\n")


# In[154]:


a=driver.find_elements_by_class_name("featurette")


# In[155]:


get_ipython().run_cell_magic('time', '', 'for i in a:\n    print(i.text)')


# In[7]:


files=["beginning_data_science.xlsx","exploring_flask_with_peewee.xlsx","intermediate_python.xlsx","intermediate_c#.xlsx","digital_literacy.xlsx","Stem_learning.xlsx","start_ur_coding_journey.xlsx","skills_for_a_modern_entrepreneur.xlsx","web_programming_for_graphic_designer.xlsx","skills_for_modern_marketing.xlsx","intermediate_andriod.xlsx","fullstack_javascript.xlsx","algorithms-and-data-structures.xlsx","beginning_security_task.xlsx","lern_ruby.xlsx","learn_react.xlsx","lexploring_flask_with_peewee.xlsx"]


# In[440]:


df=pd.DataFrame(pd.read_excel(files[0]))


# In[444]:


for i in range(1,len(files)):
    df2=pd.DataFrame(pd.read_excel(files[i]))
    df=df.append(df2)


# In[445]:


df


# In[45]:


df.to_excel("f.xlsx")


# In[20]:


df=pd.DataFrame(pd.read_excel('f.xlsx'))


# In[41]:


'''title=[]
desc=[]
what=[]
cont=[]
dur=[]
dur_unit=[]
level=[]
url=[]'''
ins1_name=[]
ins1_bio=[]
ins1_photo=[]
for i in files:
    '''df2=pd.DataFrame(pd.read_excel(i))
    title.extend(list(df2['title']))
    desc.extend(list(df2['desc']))
    cont.extend(list(df2['content']))
    what.extend(list(df2['what_u_learn']))
    dur.extend(list(df2['duration']))
    dur_unit.extend(list(df2['duration_unit']))
    level.extend(list(df2['level']))
    url.extend(list(df2['url']))'''
    try:
        ins1_name.extend(list(df2['instructor|1|_name']))
        ins1_bio.extend(list(df2["instructor|1|_bio"]))
        ins1_photo.extend(list(df2["instructor|1|_photo"]))
    except:
        ins1_name.extend(list(df2['ins_name']))
        ins1_bio.extend(list(df2["ins_bio"]))
        ins1_photo.extend(list(df2["ins_photo"]))


# In[34]:


len(url)


# In[28]:


df['title']=title
df['total_duration_unit']=dur_unit
df['total_duration']=dur
df['what_will_learn']=what
df['level']=level
df['partner_course_url']=url
df['content']=cont
df["description"]=desc
df['delivery_method']="Online"
df['learn_type']="Certification"
df["instruction_type"]="Instructor Paced"


# In[29]:


df


# In[43]:


df['instructor|1|name']=ins1_name
df["instructor|1|instructor_bio"]=ins1_bio
df["instructor|1|instructor_image"]=ins1_photo


# In[42]:


ins1_name


# In[ ]:




