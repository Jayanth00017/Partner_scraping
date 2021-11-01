import requests
from bs4 import BeautifulSoup
import pandas as pd
urlArray = []
urlArray.append("https://www.futurelearn.com/microcredentials/agile-leadership-and-management")
urlArray.append("https://www.futurelearn.com/microcredentials/change-management")
urlArray.append("https://www.futurelearn.com/microcredentials/aws-machine-learning-foundations")
urlArray.append("https://www.futurelearn.com/microcredentials/aws-solutions-architect")
urlArray.append("https://www.futurelearn.com/microcredentials/business-management-financial-accounting-for-non-financial-roles")
urlArray.append("https://www.futurelearn.com/microcredentials/fundamentals-of-management-accounting")
urlArray.append("https://www.futurelearn.com/microcredentials/business-management-improving-organisational-practice")
urlArray.append("https://www.futurelearn.com/microcredentials/marketing-principles-and-practice")
urlArray.append("https://www.futurelearn.com/microcredentials/business-management-project-management")
urlArray.append("https://www.futurelearn.com/microcredentials/change-management")
urlArray.append("https://www.futurelearn.com/microcredentials/cisco-ccna")
urlArray.append("https://www.futurelearn.com/microcredentials/cisco-devops-using-devnet")
urlArray.append("https://www.futurelearn.com/microcredentials/cisco-python-programming")
urlArray.append("https://www.futurelearn.com/microcredentials/climate-change-polar-regions")
urlArray.append("https://www.futurelearn.com/microcredentials/cybersecurity-operations")
urlArray.append("https://www.futurelearn.com/microcredentials/data-analytics-for-decision-making")
urlArray.append("https://www.futurelearn.com/microcredentials/data-driven-leadership-skills")
urlArray.append("https://www.futurelearn.com/microcredentials/digital-collaborative-learning")
urlArray.append("https://www.futurelearn.com/microcredentials/digital-photography-discover-your-genre")
urlArray.append("https://www.futurelearn.com/microcredentials/fashion-business")
urlArray.append("https://www.futurelearn.com/microcredentials/tesol-language-teaching-methodology")
urlArray.append("https://www.futurelearn.com/microcredentials/trauma-aware-teachers")
urlArray.append("https://www.futurelearn.com/microcredentials/teacher-training-embedding-mental-health-in-the-curriculum")
urlArray.append("https://www.futurelearn.com/microcredentials/tackling-the-climate-crisis")
urlArray.append("https://www.futurelearn.com/microcredentials/practical-project-management")
urlArray.append("https://www.futurelearn.com/microcredentials/online-teaching-improving-and-evaluating-courses")
urlArray.append("https://www.futurelearn.com/microcredentials/online-teaching-embedding-social-race-and-gender-related-equity")
urlArray.append("https://www.futurelearn.com/microcredentials/online-teaching")
urlArray.append("https://www.futurelearn.com/microcredentials/online-teaching-accessibility-and-inclusive-learning")
urlArray.append("https://www.futurelearn.com/microcredentials/management-of-uncertainty-leadership-decisions-and-action")
urlArray.append("https://www.futurelearn.com/microcredentials/management-of-change-organisation-development-and-design")
urlArray.append("https://www.futurelearn.com/microcredentials/fashion-sustainability")
urlArray.append("https://www.futurelearn.com/microcredentials/food-and-medicine-final")
urlArray.append("https://www.futurelearn.com/microcredentials/food-control-systems")
urlArray.append("https://www.futurelearn.com/microcredentials/learn-french-for-global-communication-level-1")
urlArray.append("https://www.futurelearn.com/microcredentials/learn-spanish-for-global-communication-level-1")


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

def process_instructor_1_name(soupObject):
    name = ""
    names = soupObject.find('div',attrs={'class':'educators-column_3xSeo'}).findNext('div',attrs={'class':'mediaElement-body_a-46R'}).findNext('span').getText()
    for ins in names:
        name = name + ins
    return name

def process_instructor_1_designation(soupObject):
    desg = ""
    designation = soupObject.find('div',attrs={'class':'educators-shortDescription_1ORQE'}).getText()
    for desig in designation:
        desg = desg + desig
    return desg

def process_instructor_1_image(soupObject):
    image = ""
    img_ins = soupObject.find('div',attrs={'class':'mediaElement-image_AzGLg'}).findNext('div',attrs={'class':'avatar-module_wrapper__3joaZ avatar-module_extraExtraLarge__2crrt avatar-module_bubble__3cpmd'})
    for imgg in img_ins.findAll('img'):
        image = image + imgg['src']
    return image

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

def process_batch_start_date_1(soupObject):
    batch = ""
    batches = soupObject.find('div',attrs={'class':'align-module_itemsWrapper__utBam align-module_sBreakpointSpacing3__2Wmck align-module_sBreakpointAlignspaceBetween__3Yfrh align-module_sBreakpointAlignItemsstretch__3p0X7 align-module_mBreakpointAlignItemscenter__1-LUt align-module_noWrap__3BT6z'}).findNext('div',attrs={'class':'align-module_item__oiojU'}).findNext('div',attrs={'class':'align-module_item__oiojU'}).findNext('div',attrs={'class':'align-module_item__oiojU'}).findNext('div',attrs={'class':'align-module_item__oiojU'})
    for bat in batches.findAll('time'):
        batch = batch + bat['datetime']
    return batch





scriptReport = []
for row in urlArray:
    response = requests.get(row)  #bringing url
    pageData = {}    #creating dictionary
    soupObject = BeautifulSoup(response.content, 'html5lib') #parsing the html into soupObject

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
    pageData['instructor_1_name'] = process_instructor_1_name(soupObject)
    pageData['instructor_1_bio'] = process_instructor_1_designation(soupObject)
    pageData['instructor_1_image'] = process_instructor_1_image(soupObject)
    pageData['institute'] = process_institute(soupObject)
    pageData['batch_start_date_1'] = process_batch_start_date_1(soupObject)


    scriptReport.append(pageData)

df = pd.DataFrame.from_dict(scriptReport)
df.to_csv('micro_cred_1.csv', index=True, header=True)

