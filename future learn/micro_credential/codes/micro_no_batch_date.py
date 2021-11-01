import requests
from bs4 import BeautifulSoup
import pandas as pd
urlArray = []
urlArray.append("https://www.futurelearn.com/microcredentials/microsoft-ai-track")
urlArray.append("https://www.futurelearn.com/microcredentials/data-driven-decision-making")
urlArray.append("https://www.futurelearn.com/microcredentials/research-methods")
def process_description(soupObject):
    desc = ""
    description = soupObject.find('div',attrs={'class':'MarkdownWrapper-wrapper_2DF3- MarkdownWrapper-stripMargin_2aard'}).find_all('p')
    for descri in description:
        description = description
    return description

def process_skills(soupObject):
    skills = ""
    skill = soupObject.find('div',attrs={'class':'sectionContainer-module_wrapper__1aVvO sectionContainer-module_altAdjacent__1Kz6F'}).findChildren('li')
    for ski in skill:
        skills = skills + ski.getText() + "|"
    return skills

def process_what_will_learn(soupObject):
    what = ""
    what_will = soupObject.find('div',attrs={'class':'spacer-module_default__3N2H9 spacer-module_top-6__39_cj'}).findNext('ul',attrs={'class':'Grid-module_grid__17adB'}).find_all('li')
    for whatt in what_will:
        what = what + whatt.getText() + "|"
    return what

def process_logo(soupObject):
    logo = "https://assets.futurelearn.com/packs/app/assets/images/fl_logo-f9d7f37a61915a2fbf8a26cbb285fed0.svg"
    return logo


def process_prerequisites(soupObject):
    pre = ""
    preq = soupObject.find('section',attrs={'class':'sectionContainer-module_wrapper__1aVvO sectionContainer-module_altAdjacent__1Kz6F'}).findNext('div',attrs={'class':'MarkdownWrapper-wrapper_2DF3-'}).getText()
    for prereq in preq:
        pre = pre +  prereq
    return pre

def process_target_students(soupObject):
    target = ""
    targets = soupObject.find('section',attrs={'class':'sectionContainer-module_wrapper__1aVvO sectionContainer-module_altAdjacent__1Kz6F'}).findNext('div',attrs={'class':'MarkdownWrapper-wrapper_2DF3-'}).findNext('div',attrs={'class':'MarkdownWrapper-wrapper_2DF3-'}).getText()
    for tar in targets:
        target = target + tar
    return target

def process_content(soupObject):
    contents = ""
    content = soupObject('div',attrs={'class':'Title-wrapper_11axP'})
    for cont in content:
        contents = contents + cont.getText()
    return content


def process_level(soupObject):
    levels = ""
    level = soupObject.find('div',attrs={'class':'index-module_wrapper__2aztW index-module_isHall__3dNbG'}).findNext('div',attrs={'class':'keyInfo-module_itemText__3w63w'}).findNext('div',attrs={'class':'keyInfo-module_itemText__3w63w'}).findNext('div',attrs={'class':'keyInfo-module_itemText__3w63w'}).findNext('div',attrs={'class':'keyInfo-module_itemText__3w63w'}).findNext('div',attrs={'class':'keyInfo-module_itemText__3w63w'}).findNext('span',attrs={'class':'keyInfo-module_content__1K_85'}).getText()
    for lev in level:
        levels = levels + lev
    return levels

def process_regular_price(soupObject):
    price = ""
    pricing = soupObject.find('div',attrs={'class':'index-module_wrapper__2aztW index-module_isHall__3dNbG'}).findNext('div',attrs={'class':'keyInfo-module_itemText__3w63w'}).findNext('div',attrs={'class':'keyInfo-module_itemText__3w63w'}).findNext('div',attrs={'class':'keyInfo-module_itemText__3w63w'}).findNext('span',attrs={'class':'keyInfo-module_content__1K_85'}).getText()
    for pri in pricing:
        price = price + pri
    return price

def process_currency(soupObject):
    curr = "USD"
    return curr

def process_duration(soupObject):
    duration = ""
    durations = soupObject.find('div',attrs={'class':'index-module_wrapper__2aztW index-module_isHall__3dNbG'}).findNext('div',attrs={'class':'keyInfo-module_itemText__3w63w'}).findNext('div',attrs={'class':'keyInfo-module_itemText__3w63w'}).findNext('span',attrs={'class':'keyInfo-module_content__1K_85'}).getText()
    for dur in durations:
        duration = duration + dur
    return duration

def process_duration_unit(soupObject):
    unit = "weeks"
    return unit


def process_inst_type(soupObject):
    inst = " Self Paced"
    return inst

def process_delivery_method(soupObject):
    delivery = "Online"
    return delivery

def process_learn_type(soupObject):
    learn = "Certification"
    return learn


def process_language(soupObject):
    language = "English"
    return language

def process_availabilities(soupObject):
    access = "Lifetime Acess"
    return access

def process_reviewer_1_review(soupObject):
    name = ""
    names = soupObject.find('section',attrs={'class':'sectionedTestimonials-wrapper_3Pb2q'}).findNext('div',attrs={'class':'Testimonial-quoteBlock_2_cuK Testimonial-right_2nmie'}).findNext('p').getText()
    for nam in names:
        name = name + nam
    return name

def process_review_1_name(soupObject):
    name = ""
    names = soupObject.find('section', attrs={'class': 'sectionedTestimonials-wrapper_3Pb2q'}).findNext('div',attrs={'class':'Testimonial-quoteBlock_2_cuK Testimonial-right_2nmie'}).findNext('figcaption').getText()
    for rev in names:
        name = name + rev
    return name

def process_reviewer_1_rating(souopObject):
    rating = "5"
    return rating

def process_reviewer_2_name(soupObject):
    name = ""
    names = soupObject.find('section', attrs={'class': 'sectionedTestimonials-wrapper_3Pb2q'}).findNext('div', attrs={'class': 'Testimonial-quoteBlock_2_cuK Testimonial-right_2nmie'}).findNext('div', attrs={'class': 'Testimonial-quoteBlock_2_cuK Testimonial-right_2nmie'}).findNext('figcaption').getText()
    for rev in names:
        name = name + rev
    return name

def process_reviewer_2_review(soupObject):
    name = ""
    names = soupObject.find('section', attrs={'class': 'sectionedTestimonials-wrapper_3Pb2q'}).findNext('div', attrs={'class': 'Testimonial-quoteBlock_2_cuK Testimonial-right_2nmie'}).findNext('div', attrs={'class': 'Testimonial-quoteBlock_2_cuK Testimonial-right_2nmie'}).findNext('p').getText()
    for nam in names:
        name = name + nam
    return name

def process_reviewer_2_rating(soupObject):
    rating = "5"
    return rating

def process_short_description(soupObject):
    shorrrt=""
    short = soupObject.find('div',attrs={'class':'PageHeader-mainContent_1klMz'}).findNext('p').getText()
    for short_desc in short:
        shorrrt = shorrrt + short_desc
    return shorrrt

def process_institute(soupObject):
    institute = ""
    insti = soupObject.find('section',attrs={'class':'sectionContainer-module_wrapper__1aVvO sectionContainer-module_hasOverflow__16j2t'}).findNext('h2').getText()
    for ins in insti:
        institute = institute + ins
    return institute


scriptReport = []  # array of dictionary

for row in urlArray:
    response = requests.get(row)  # bringing url
    pageData = {}  # creating dictionary
    soupObject = BeautifulSoup(response.content, 'html5lib')  # parsing the html into soupObject

    pageData['partner_course_url'] = row
    pageData['title'] = soupObject.title.get_text()
    pageData['description'] = process_description(soupObject)
    pageData['short_description'] = process_short_description(soupObject)
    pageData['skills'] = process_skills(soupObject)
    pageData['what_will_learn'] = process_what_will_learn(soupObject)
    pageData['logo'] = process_logo(soupObject)
    pageData['prerequisites'] = process_prerequisites(soupObject)
    pageData['target_students'] = process_target_students(soupObject)
    pageData['content'] = process_content(soupObject)
    pageData['level'] = process_level(soupObject)
    pageData['regular_pricing'] = process_regular_price(soupObject)
    pageData['currency'] = process_currency(soupObject)
    pageData['duration'] = process_duration(soupObject)
    pageData['duration_unit'] = process_duration_unit(soupObject)
    pageData['instruction_type'] = process_inst_type(soupObject)
    pageData['delivery_method'] = process_delivery_method(soupObject)
    pageData['learn_type'] = process_learn_type(soupObject)
    pageData['language'] = process_language(soupObject)
    pageData['availabilities'] = process_availabilities(soupObject)
    pageData['reviewer_1_name'] = process_review_1_name(soupObject)
    pageData['reviewer_1_review'] = process_reviewer_1_review(soupObject)
    pageData['reviewer_1_rating'] = process_reviewer_1_rating(soupObject)
    pageData['reviewer_2_name'] = process_reviewer_2_name(soupObject)
    pageData['reviewer_2_review'] = process_reviewer_2_review(soupObject)
    pageData['reviewer_2_rating'] = process_reviewer_2_rating(soupObject)
    pageData['institute'] = process_institute(soupObject)
    scriptReport.append(pageData)

df = pd.DataFrame.from_dict(scriptReport)
df.to_csv('micro_no_batch.csv', index=True, header=True)