import requests
from bs4 import BeautifulSoup
import pandas as pd
urlArray = []
urlArray.append("https://www.springboard.com/courses/introduction-to-analytics/")
urlArray.append("https://www.springboard.com/courses/introduction-to-design")
urlArray.append("https://www.springboard.com/courses/software-engineering-career-track-prep")

def process_description(soupObject):
    desc = ""
    descrip = soupObject.find('div', attrs={'class':'styles__Description-sc-1qc8ar1-2 goMsFf'})
    for des in descrip:
        desc = desc + descrip.getText()
    return desc

def process_logo(soupObject):
    logo=""
    logo_tag = soupObject.find('div', attrs={'class':'logoWrapper'})
    if(logo_tag is None):
        return logo
    for img in logo_tag.findAll('img'):
        logo = logo + img['src']
    return logo

def process_content(soupObject):
    cont = ""
    contents = soupObject.find('div', attrs={'class':'tabContentWrapper'})
    for what in contents:
        cont = cont + what.getText()
    return cont

def process_prereq(soupObject):
    pre = ""
    prereq = soupObject.find('div', attrs={'class':'styles__FAQWrapper-sc-1kvblrw-1 eqXAKi'}).findNext('div',attrs={'class':'detail'}).findNext('div',attrs={'class':'detail'}).findNext('div',attrs={'class':'detail'}).getText()
    for pree in prereq:
        pre = pre + pree
    return pre

def process_what_will_learn(soupObject):
    what = ""
    what_learn = soupObject.find('div', attrs={'class':'styles__TabsWrapper-vim170-0 bPMJJS'}).findChildren('p',attrs={'class':'description'})
    for whatt in what_learn:
        what = what + whatt.getText()
    return what

def process_short_desc(soupObject):
    short = ""
    short_desc = soupObject.find('div', attrs={'class':'content'}).find('p',attrs={'class':'description'}).getText()
    for dessc in short_desc:
        short = short + dessc
    return short

def process_delivery(soupObject):
    delivery = soupObject.find('div', attrs={'class':'content'}).find('p',attrs={'class':'summary'}).getText()
    if delivery.find('OFFLINE')!=-1:
        return "Offline"
    else:
        return "Online"

def process_instruction_type(soupObject):
    instruct = soupObject.find('div', attrs={'class','content'}).find('p',attrs={'class':'summary'}).getText()
    if instruct.find('LIVE 1:1 MENTORSHIP')!=-1:
        return "Self Paced"
    else:
        return "Instructor Paced"

def process_target(soupObject):
    target =""
    targ_stu = soupObject.find('div',attrs={'class':'styles__QuestionsPanelWrapper-sc-1kvblrw-0 finXth'}).findChildren('p')
    for tar in targ_stu:
        target = target + tar.getText() + "|"
    return target


def process_reviewer_1_name(soupObject):
    name = ""
    name_rev = soupObject.find('div', attrs={'class':'name'}).getText()
    for namm in name_rev:
        name = name + namm
    return name

def process_reviewer_2_name(soupObject):
    name = ""
    return name


def process_review_1_review(soupObject):
    review =""
    revv = soupObject.find('div', attrs={'class':'avatar-quote'}).getText()
    for reev in revv:
        review = review + reev
    return review

def process_review_2_review(soupObject):
    review =""

    return review

def process_reviewer_1_image(soupObject):
    rev_image_Data = ""
    rev_image_Data_tag = soupObject.find('div', attrs={'class':'avatar-image'})
    if (rev_image_Data_tag is None):
        return rev_image_Data
    for img in rev_image_Data_tag.findAll('img'):
        rev_image_Data = rev_image_Data + img['src']
    return (rev_image_Data)



def process_reviewer_2_image(soupObject):
    rev_image_Data = ""

    return (rev_image_Data)



def process_course_duration(soupObject):
    duration=""
    dur = soupObject.find('div',attrs={'class':'content'}).findNext('p')
    for durr in dur:
        duration = duration + dur.getText()
    return duration

def process_course_duration_unit(soupObject):
    unit = "month"
    return unit

def process_regular(soupObject):
    reg_price = ""
    regg = soupObject.find('div',attrs={'class':'styles__Container-s7q1m0-0 bvNfKp'}).findNext('h3').findNext('h3').getText()
    for pricee in regg:
        reg_price = reg_price + pricee
    return reg_price

def process_sale_price(soupObject):
    sale_price =""
    salee = soupObject.find('div',attrs={'class':'styles__Container-s7q1m0-0 bvNfKp'}).findNext('h3').findNext('h3').getText()
    for sale_pc in salee:
        sale_price = sale_price + sale_pc
    return sale_price

def process_language(soupObject):
    lang = "English"
    return lang

def process_price_type(soupObject):
    salee = "Paid"
    return salee

def process_instructor_1_name(soupObject):
    name = ""
    name_ins = soupObject.find('div',attrs={'class':'styles__Title-sc-1xm0qrl-3 gLluVi'}).getText()
    for nnam in name_ins:
        name = name + nnam
    return name

def process_instructor_1_designation(soupObject):
    desig = ""
    desig_ins = soupObject.find('div', attrs={'class': 'styles__SubTitile-sc-1xm0qrl-4 hJyCMM'}).getText()
    for ddesig in desig_ins:
        desig = desig + ddesig
    return desig

def process_instructor_2_name(soupObject):
    name = ""
    name_ins = soupObject.find('div',attrs={'class':'styles__Title-sc-1xm0qrl-3 gLluVi'}).findNext('div',attrs={'class':'styles__Title-sc-1xm0qrl-3 gLluVi'}).getText()
    for nnam in name_ins:
        name = name + nnam
    return name

def process_instructor_2_designation(soupObject):
    desig = ""
    desig_ins = soupObject.find('div', attrs={'class': 'styles__SubTitile-sc-1xm0qrl-4 hJyCMM'}).findNext('div', attrs={'class': 'styles__SubTitile-sc-1xm0qrl-4 hJyCMM'}).getText()
    for ddesig in desig_ins:
        desig = desig + ddesig
    return desig

def process_instructor_3_name(soupObject):
    name = ""
    name_ins = soupObject.find('div',attrs={'class':'styles__Title-sc-1xm0qrl-3 gLluVi'}).findNext('div',attrs={'class':'styles__Title-sc-1xm0qrl-3 gLluVi'}).findNext('div',attrs={'class':'styles__Title-sc-1xm0qrl-3 gLluVi'}).getText()
    for nnam in name_ins:
        name = name + nnam
    return name

def process_instructor_3_designation(soupObject):
    desig = ""
    desig_ins = soupObject.find('div', attrs={'class': 'styles__SubTitile-sc-1xm0qrl-4 hJyCMM'}).findNext('div', attrs={'class': 'styles__SubTitile-sc-1xm0qrl-4 hJyCMM'}).findNext('div', attrs={'class': 'styles__SubTitile-sc-1xm0qrl-4 hJyCMM'}).getText()
    for ddesig in desig_ins:
        desig = desig + ddesig
    return desig


def process_instructor_4_name(soupObject):
    name = ""
    name_ins = soupObject.find('div',attrs={'class':'styles__Title-sc-1xm0qrl-3 gLluVi'}).findNext('div',attrs={'class':'styles__Title-sc-1xm0qrl-3 gLluVi'}).findNext('div',attrs={'class':'styles__Title-sc-1xm0qrl-3 gLluVi'}).findNext('div',attrs={'class':'styles__Title-sc-1xm0qrl-3 gLluVi'}).getText()
    for nnam in name_ins:
        name = name + nnam
    return name

def process_instructor_4_designation(soupObject):
    desig = ""
    desig_ins = soupObject.find('div', attrs={'class': 'styles__SubTitile-sc-1xm0qrl-4 hJyCMM'}).findNext('div', attrs={'class': 'styles__SubTitile-sc-1xm0qrl-4 hJyCMM'}).findNext('div', attrs={'class': 'styles__SubTitile-sc-1xm0qrl-4 hJyCMM'}).findNext('div', attrs={'class': 'styles__SubTitile-sc-1xm0qrl-4 hJyCMM'}).getText()
    for ddesig in desig_ins:
        desig = desig + ddesig
    return desig

def process_currency(soupObject):
    currency = "USD"
    return currency

def process_job_assistance(soupObject):
    if "Job" in soupObject.title.getText():
        return "TRUE"
    else:
        return "FALSE"




scriptReport = []
for row in urlArray:
    response = requests.get(row)  #bringing url
    pageData = {}    #creating dictionary
    soupObject = BeautifulSoup(response.content, 'html5lib') #parsing the html into soupObject

    pageData['partner_course_url'] = row
    pageData['title'] = soupObject.title.get_text()
    pageData['description'] = process_description(soupObject)
    pageData['logo'] = process_logo(soupObject)
    pageData['content'] = process_content(soupObject)
    pageData['prerequisites'] = process_prereq(soupObject)
    pageData['what_will_learn'] = process_what_will_learn(soupObject)
    pageData['short_desc'] = process_short_desc(soupObject)
    pageData['delivery_type'] = process_delivery(soupObject)
    pageData['target_students'] = process_target(soupObject)
    pageData['reviewer_1_name'] = process_reviewer_1_name(soupObject)
    pageData['reviewer_1_review'] = process_review_1_review(soupObject)
    pageData['reviewer_1_image'] = process_reviewer_1_image(soupObject)
    pageData['reviewer_2_name'] = process_reviewer_2_name(soupObject)
    pageData['reviewer_2_review'] = process_review_2_review(soupObject)
    pageData['reviewer_2_image'] = process_reviewer_2_image(soupObject)
    pageData['course_duration'] = process_course_duration(soupObject)
    pageData['course_duration_unit'] = process_course_duration_unit(soupObject)
    pageData['regular_price'] = process_regular(soupObject)
    pageData['sale_price'] = process_sale_price(soupObject)
    pageData['currency'] = process_currency(soupObject)
    pageData['language'] = process_language(soupObject)
    pageData['pricing_type'] = process_price_type(soupObject)
    pageData['instructor_1_name'] = process_instructor_1_name(soupObject)
    pageData['instructor_1_designation'] = process_instructor_1_designation(soupObject)
    pageData['instructor_2_name'] = process_instructor_2_name(soupObject)
    pageData['instructor_2_designation'] = process_instructor_2_designation(soupObject)
    pageData['instructor_3_name'] = process_instructor_3_name(soupObject)
    pageData['instructor_3_designation'] = process_instructor_3_designation(soupObject)
    pageData['instructor_4_name'] = process_instructor_4_name(soupObject)
    pageData['instructor_4_designation'] = process_instructor_4_designation(soupObject)
    pageData['Job_Assistance'] = process_job_assistance(soupObject)
    scriptReport.append(pageData)

df = pd.DataFrame.from_dict(scriptReport)
df.to_csv('spring_board_3.csv', index=True, header=True)