import requests
import pandas as pd
from bs4 import BeautifulSoup
import pandas as pd
#creating array for the URL
urlArray = []
urlArray.append("https://www.futurelearn.com/experttracks/applied-ai-on-microsoft")
urlArray.append("https://www.futurelearn.com/experttracks/advanced-cybersecurity-skills")
urlArray.append("https://www.futurelearn.com/experttracks/ai-engineer-with-microsoft-azure")
urlArray.append("https://www.futurelearn.com/experttracks/become-successful-baker-bbc-good-food")
urlArray.append("https://www.futurelearn.com/experttracks/supercharge-your-career")
urlArray.append("https://www.futurelearn.com/experttracks/cybersecurity-foundations")
urlArray.append("https://www.futurelearn.com/experttracks/data-analysis-fundamentals-with-excel")
urlArray.append("https://www.futurelearn.com/experttracks/data-science-fundamentals-microsoft-azure")
urlArray.append("https://www.futurelearn.com/experttracks/data-science-microsoft-azure-python-programming")
urlArray.append("https://www.futurelearn.com/experttracks/introduction-data-science-microsoft-azure-using-r-programming")
urlArray.append("https://www.futurelearn.com/experttracks/advanced-ai-microsoft-azure")
urlArray.append("https://www.futurelearn.com/experttracks/coding-app-marketing")
urlArray.append("https://www.futurelearn.com/experttracks/digital-security-training")
urlArray.append("https://www.futurelearn.com/experttracks/advanced-ai-ethics-research")
urlArray.append("https://www.futurelearn.com/experttracks/fashion-brand-management")
urlArray.append("https://www.futurelearn.com/experttracks/planning-for-success-in-conflict-affected-regions")
urlArray.append("https://www.futurelearn.com/experttracks/financial-analysis-and-strategy-et")
urlArray.append("https://www.futurelearn.com/experttracks/business-innovation-and-entrepreneurship-et")
urlArray.append("https://www.futurelearn.com/experttracks/business-strategy-and-decision-making-skills")
urlArray.append("https://www.futurelearn.com/experttracks/local-seo-agency-course")
urlArray.append("https://www.futurelearn.com/experttracks/information-security-systems")
urlArray.append("https://www.futurelearn.com/experttracks/fintech-innovations")
urlArray.append("https://www.futurelearn.com/experttracks/international-leadership-et")
urlArray.append("https://www.futurelearn.com/experttracks/international-logistics-et")
urlArray.append("https://www.futurelearn.com/experttracks/international-marketing-et")
urlArray.append("https://www.futurelearn.com/experttracks/implementing-devops-environments-and-solutions")
urlArray.append("https://www.futurelearn.com/experttracks/leading-people-and-teams")
urlArray.append("https://www.futurelearn.com/experttracks/microsoft-business-applications-sales-functional-consultants")
urlArray.append("https://www.futurelearn.com/experttracks/healthy-cooking")
urlArray.append("https://www.futurelearn.com/experttracks/network-security-defence-management-et")
urlArray.append("https://www.futurelearn.com/experttracks/project-management-et")
urlArray.append("https://www.futurelearn.com/experttracks/public-health-nursing")
urlArray.append("https://www.futurelearn.com/experttracks/healthcare-leadership-and-management")
urlArray.append("https://www.futurelearn.com/experttracks/future-fashion-media")
urlArray.append("https://www.futurelearn.com/experttracks/ielts-preparation")





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

def process_logo(soupObject):
    logo = "https://assets.futurelearn.com/packs/app/assets/images/fl_logo-f9d7f37a61915a2fbf8a26cbb285fed0.svg"
    return logo


def process_prerequisites(soupObject):
    pre = ""
    preq = soupObject.find('section',attrs={'class':'sectionContainer-module_wrapper__1aVvO sectionContainer-module_altAdjacent__1Kz6F'}).findNext('div',attrs={'class':'MarkdownWrapper-wrapper_2DF3-'}).find_all('p')
    for prereq in preq:
        pre = pre +  prereq.getText()+'|'
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
    price = "39"
    return price

def process_currency(soupObject):
    currency = "USD"
    return currency

def process_duration(soupObject):
    duration = ""
    durations = soupObject.find('div',attrs={'class':'index-module_wrapper__2aztW index-module_isHall__3dNbG'}).findNext('div',attrs={'class':'keyInfo-module_itemText__3w63w'}).findNext('span',attrs={'class':'keyInfo-module_content__1K_85'}).getText()
    for dur in durations:
        duration = duration + dur
    return duration

def process_duration_unit(soupObject):
    unit = "weeks"
    return unit

def process_efforts_per_week_(soupObject):
    efforts = ""
    effort = soupObject.find('div',attrs={'class':'index-module_wrapper__2aztW index-module_isHall__3dNbG'}).findNext('div',attrs={'class':'keyInfo-module_itemText__3w63w'}).findNext('p').findNext('p').getText()
    for eff in effort:
        efforts = efforts + eff
    return effort

def process_learn_type(soupObject):
    learn = "Certification"
    return learn

def process_inst_type(soupObject):
    inst = " Self Paced"
    return inst


def process_language(soupObject):
    language = "English"
    return language

def process_availabilities(soupObject):
    access = "Lifetime Access"
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

def process_delivery_method(soupObject):
    delivery = "Online"
    return delivery

def process_short_description(soupObject):
    shorrrt=""
    short = soupObject.find('div',attrs={'class':'PageHeader-mainContent_1klMz'}).findNext('p').getText()
    for short_desc in short:
        shorrrt = shorrrt + short_desc
    return shorrrt

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

def process_institute(soupObject):
    institute = ""
    insti = soupObject.find('section',attrs={'class':'sectionContainer-module_wrapper__1aVvO sectionContainer-module_hasOverflow__16j2t'}).findNext('h2').getText()
    for ins in insti:
        institute = institute + ins
    return institute

scriptReport = []   #array of dictionary


for row in urlArray:
    response = requests.get(row)  #bringing url
    pageData = {}    #creating dictionary
    soupObject = BeautifulSoup(response.content, 'html5lib') #parsing the html into soupObject

    pageData['partner_course_url'] = row
    pageData['title'] = soupObject.title.get_text()
    pageData['description'] = process_description(soupObject)
    pageData['short_description'] = process_short_description(soupObject)
    pageData['skill'] = process_skills(soupObject)
    pageData['prerequisites'] = process_prerequisites(soupObject)
    pageData['target_students'] = process_target_students(soupObject)
    pageData['delivery_method'] = process_delivery_method(soupObject)
    pageData['content'] = process_content(soupObject)
    pageData['level'] = process_level(soupObject)
    pageData['regular_price'] = process_regular_price(soupObject)
    pageData['currency'] = process_currency(soupObject)
    pageData['course_duration'] = process_duration(soupObject)
    pageData['duration_unit'] = process_duration_unit(soupObject)
    pageData['efforts_per_week'] = process_efforts_per_week_(soupObject)
    pageData['learn_type'] = process_learn_type(soupObject)
    pageData['instruction_type'] = process_inst_type(soupObject)
    pageData['language'] = process_language(soupObject)
    pageData['availabilities'] = process_availabilities(soupObject)
    pageData['reviewer_1_name'] = process_review_1_name(soupObject)
    pageData['reviewer_1_review'] = process_reviewer_1_review(soupObject)
    pageData['reviewew_1_rating'] = process_reviewer_1_rating(soupObject)
    pageData['reviewer_2_name'] = process_reviewer_2_name(soupObject)
    pageData['reviewer_2_review'] = process_reviewer_2_review(soupObject)
    pageData['reviewer_2_rating'] = process_reviewer_2_rating(soupObject)
    pageData['institute'] = process_institute(soupObject)
    pageData['logo'] = process_logo(soupObject)
    scriptReport.append(pageData)

df = pd.DataFrame.from_dict(scriptReport)
df.to_csv('expert_track_no_instructor.csv', index=True, header=True)