from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
from time import sleep

def knowledgehut():
  title=[]
  short_desc=[]
  video_url=[]
  description=[]
  what_will_learn=[]
  skills_gained=[]
  price=[]
  skills2=[]
  target_students=[]
  level=[]
  urls=[]
  duration=[]
  pricing_type=[]
  prerequisites=[]
  currency=[]
  language=[]
  accessibilities=[]
  delivery_method=[]
  instruction_type=[]
  reviewer_name_1=[]
  reviewer_name_2=[]
  reviewer_name_3=[]
  reviewer_name_4=[]
  review_1=[]
  review_2=[]
  review_3=[]
  review_4=[]
  content=[]


  urls=['https://www.knowledgehut.com/big-data/machine-learning-with-apache-mahout',
  'https://www.knowledgehut.com/programming/python-programming-certification-training',
  'https://www.knowledgehut.com/programming/c-sharp',
  'https://www.knowledgehut.com/programming/ruby-101',
  'https://www.knowledgehut.com/programming/aspnet-training',
  'https://www.knowledgehut.com/programming/r-deep-dive-training',
  'https://www.knowledgehut.com/programming/ruby-deep-dive',
  'https://www.knowledgehut.com/programming/master-swift',
  'https://www.knowledgehut.com/programming/asp-net-mvc',
  'https://www.knowledgehut.com/programming/python-deep-dive',
  'https://www.knowledgehut.com/web-development/ui-ux-design-training',
  'https://www.knowledgehut.com/web-development/drupal',
  'https://www.knowledgehut.com/web-development/spring-framework-training',
  'https://www.knowledgehut.com/web-development/spring-boot',
  'https://www.knowledgehut.com/web-development/groovy-and-grails']
        
  for url in urls:
    try:
      r=requests.get(url)
      soup=BeautifulSoup(r.content,"html.parser")
    except:
      time.sleep(3)

    #url
    urls.append(url)


    #title
    try:
      titles=soup.find("h1").text
      title.append(titles)
    except:
      pass

    #what_will_learn
    sk=[]
    try:
      skills=soup.findAll("div",class_="item")
      for i in skills:
        s=i.find("h4").text.replace(",","|")
        sk.append(s)
      what_will_learn.append(sk)
    
    except:
      pass

    #prerequisites
    try:
      pre=soup.find("div",class_="col-md-10").text
      prerequisites.append(pre)
    except:
      pass
    


  #print(title)


    #short_desc
    try:
      short=soup.find("div",class_="col-lg-7 col-md-6").find("h2").text
      short_desc.append(short)
    except:
      pass

    #desc
    try:
      desc=soup.find("div",class_="editor-content overview-view-more").text
      description.append(desc)
    except:
      pass

    #duration
    try:
      dur=soup.find("ul",class_="course-sum clearfix").li.h3.text
      duration.append(dur)
    except:
      duration.append("NA")

    #target_students
    try:
      target=soup.find("section",class_="who-should-attend-1").text.replace("Who Should Attend","")
      target_students.append(target)
    except:
      target_students.append("NA")

    #content
    try:
      cont=soup.find("div",class_="panel-group accordion").text
      content.append(cont)
    except:
      content.append("NA")
    
    df=pd.DataFrame.from_dict({'url':urls,
                              'title':title,
                              'short_desc':short_desc,
                              'description':description,
                              'content':content,
                              'prerequisites':prerequisites,
                              'what_will_learn':what_will_learn,
                              'target_students':target_students,
                              'duration':duration},orient='index')
    df = df.transpose()
    df.to_csv("knowledgehut.csv", index=False)
    
                
                                
                
                
if __name__ == '__main__':
    knowledgehut()

                             

    



 


  

  
    
                      
    
    
    
  






  




  
 
  

    
   
    
  
 




