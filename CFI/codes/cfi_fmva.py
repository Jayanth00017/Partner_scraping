from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
from time import sleep

def cfi_fmva():
    
    course_links=[]
    certification_url='https://courses.corporatefinanceinstitute.com/collections?category=all-fmva-courses'
    base_url = 'https://courses.corporatefinanceinstitute.com'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }

    r=requests.get(certification_url,headers=headers)
    soup=BeautifulSoup(r.content,"html.parser")
    course_list=soup.findAll("div",class_="card-wrapper")
    for course in course_list:
      for link in course.findAll("a", href=True):
        course_links.append(base_url+link['href'])
    #print((course_links))

    title=[]
    short_desc=[]
    #video_url=[]
    description=[]
    what_will_learn=[]
    skills_gained=[]
    price=[]
    #skills2=[]
    content=[]
    target_students=[]
    level=[]
    duration=[]
    duration_unit=[]
    pricing_type=[]
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
    page_url=[]

    for url in course_links:
        
          try:
            r=requests.get(url, headers=headers)
            soup=BeautifulSoup(r.content,"html.parser")
          except:
            time.sleep(5)

          #page_url
          page_url.append(url)

          #title
          titles=soup.find("h1",class_="product__title").text.replace("\n","")
          title.append(titles)
        #print(title)

          #short_desc
          short=soup.find("span",class_="product__subtitle").text.replace("\n","")
          short_desc.append(short)
        #print(short_desc)

           #what_will_learn
          try:
            what=soup.find("div",class_="product-overview").findChild("ul").text.replace("\n","|")
            what_will_learn.append(what)
          except:
            pass
        #print(what_will_learn)  

          #price
          try:
            cost=soup.find("span",class_="course_prise").text.replace("\n","").replace("$","")
            price.append(cost)
          except:
            pass
          
          #skills2
          try:
            skill=soup.find("div",class_="bundle-card-content").findChild("ul",class_="features").find("li").findNext("li").text.replace("\nSkills Learned"," ")
            skills_gained.append(skill)
          except:
            pass
        #print(skills2)


          #target_students
          try:
            students=soup.find("div",class_="bundle-card-content").findChild("ul",class_="features").find("li").findNext("li").findNext("li").text.replace("\nCareer Prep","").replace(",","|")
            target_students.append(students)
          except:
            pass
        #print(target_students)

          #level
          try:
            lev=soup.find("p",class_="course-feature").text.replace("level","")
            level.append(lev)
          except:
            pass
        #print(level)

           #Content
          modules=[]
          mod=[]
          for i in soup.findAll("a", class_="chapter-list-item__link"):
            for j in i.find("span",class_="chapter-list-item__title"):
              
              modules.append(j)
          #mod.append(modules)
          content.append(modules)

          #duration
          dur=soup.find("p",class_="course-feature").findNext("p").text.replace("\nApprox\n","").replace("\nto complete\n","").replace("h","")
          duration.append(dur)
        #print(duration)

          #duration_units
          duration_unit.append("Hours")

          #pricing_type
          if 'Free' in cost:
            pricing_type.append('Free')
          else:
            pricing_type.append('Paid')
        #print(pricing_type)

          #language
          language.append("English")

          #accessibilities
          accessibilities.append('Mobile, Desktop, Tablet')

          #currency
          if 'Paid' in pricing_type:
            currency.append('USD')
          else:
            currency.append("")

          #delivery_method]
          delivery_method.append('Online')

          #instruction_type
          instruction_type.append('Self Paced')

          #description
          des=soup.find("div",class_="custom-theme").findChild("p")
          description.append(des)

          #reviewer_1_name
          
          try:
            names=soup.find("h4",class_="course-review__name").text.replace("\n","")
            reviewer_name_1.append(names)
          except:
            pass

          try:
            names_2=soup.find("h4",class_="course-review__name").findNext("h4").text.replace("\n","")
            reviewer_name_2.append(names_2)
          except:
            pass

          try:
            names_3=soup.find("h4",class_="course-review__name").findNext("h4").findNext("h4").text.replace("\n","")
            reviewer_name_3.append(names_3)
          except:
            pass

          try:
            names_4=soup.find("h4",class_="course-review__name").findNext("h4").findNext("h4").findNext("h4").text.replace("\n","")
            reviewer_name_4.append(names_4)
          except:
            pass

          #reviews
          try:
            text_1=soup.find("div", class_="course-review__text").text.replace("\n","")
            review_1.append(text_1)
          except:
            pass

          try:
            text_2=soup.find("div", class_="course-review__text").findNext("div", class_="course-review__text").text.replace("\n","")
            review_2.append(text_2)
          except:
            pass

          try:
            text_3=soup.find("div", class_="course-review__text").findNext("div", class_="course-review__text").findNext("div", class_="course-review__text").text.replace("\n","")
            review_3.append(text_3)
          except:
            pass
          
          try:
            text_4=soup.find("div", class_="course-review__text").findNext("div", class_="course-review__text").findNext("div", class_="course-review__text").findNext("div", class_="course-review__text").text.replace("\n","")
            review_4.append(text_4)
          except:
            pass

          df=pd.DataFrame.from_dict({
                                            'page_url' : page_url,
                 
                                            'course_title': title,

                                            #'course_description': course_description,
                                            
                                            'short_description': short_desc,
                                            'description':description,

                                            'skills':skills_gained,
                                            'what_will_learn':what_will_learn,
                                            'content':content,

                                            #'instructor_name':instructor_name,
                       
                                            #'instructor_bio':instructor_bio,
                       
                                            #'embedded_video_url':videoURL,
                       
                                            'level':level,
                                            'target_students':target_students,
                                            
                                            'reviewer_name_1':reviewer_name_1,
                                            'review_1':review_1,
                                            
                                            'reviewer_name_2':reviewer_name_2,
                                            'review_2':review_2,

                                            
                                            'reviewer_name_3':reviewer_name_3,
                                            'review_3':review_3,
                                            
                                            'reviewer_name_4':reviewer_name_4,
                                            'review_4':review_4,

                                            'delivery_mode': delivery_method,

                                            'price':price,
                                            'currency':currency,

                                            'pricing_type':pricing_type,

                                            #'course_content': course_content,
          
                                            #'learn_type' :learn_type,
          
                                            'total_duration' : duration,
                                            'total_duration_unit':duration_unit,
          

                                            

                                            #'logo'  : logo_site,

                                            'accessibilities' : accessibilities,
                       
                                            'language' : language,
                       
                                            'instruction_type' :  instruction_type

                                            

          }, orient='index')
                                            
                            

          df = df.transpose()
          df.to_csv("cfi_fmva.csv", index=False)
                
                                
                
                
if __name__ == '__main__':
    cfi_fmva()


