import requests
import pandas as pd
from bs4 import BeautifulSoup
import pandas as pd
#creating array for the URL
urlArray = []
urlArray.append("https://www.futurelearn.com/experttracks/applied-ai-on-microsoft")
urlArray.append("https://www.futurelearn.com/experttracks/ai-engineer-with-microsoft-azure")
urlArray.append("https://www.futurelearn.com/experttracks/supercharge-your-career")
urlArray.append("https://www.futurelearn.com/experttracks/data-analysis-fundamentals-with-excel")
urlArray.append("https://www.futurelearn.com/experttracks/data-science-fundamentals-microsoft-azure")
urlArray.append("https://www.futurelearn.com/experttracks/data-science-microsoft-azure-python-programming")
urlArray.append("https://www.futurelearn.com/experttracks/introduction-data-science-microsoft-azure-using-r-programming")
urlArray.append("https://www.futurelearn.com/experttracks/advanced-ai-microsoft-azure")
urlArray.append("https://www.futurelearn.com/experttracks/coding-app-marketing")
urlArray.append("https://www.futurelearn.com/experttracks/advanced-ai-ethics-research")
urlArray.append("https://www.futurelearn.com/experttracks/implementing-devops-environments-and-solutions")
urlArray.append("https://www.futurelearn.com/experttracks/microsoft-business-applications-sales-functional-consultants")
urlArray.append("https://www.futurelearn.com/experttracks/digital-communicate-collaborate-thrive")
urlArray.append("https://www.futurelearn.com/experttracks/certificate-in-corporate-training")




def process_accredation_1_name(soupObject):
    image = ""
    img_ins = soupObject.find('div', attrs={'class':'PageHeader-supportingContent_20zcq'}).findNext('div',attrs={'class':'PageHeader-organisation_1JgOo'}).findNext('div',attrs={'class':'PageHeader-organisation_1JgOo'})
    for imgg in img_ins.findAll('img'):
        image = image + imgg['alt']
    return image


def process_accredation_1_logo(soupObject):
    image = ""
    img_ins = soupObject.find('div', attrs={'class': 'PageHeader-supportingContent_20zcq'}).findNext('div', attrs={'class': 'PageHeader-organisation_1JgOo'}).findNext('div', attrs={'class': 'PageHeader-organisation_1JgOo'})
    for imgg in img_ins.findAll('img'):
        image = image + imgg['src']
    return image

def process_accredation_1_description(soupObject):
    image = ""
    img_ins = soupObject.find('div', attrs={'class': 'spotlight-wrapper_iYZi7 spotlight-isTransparent_2KoYF spotlight-isMirrored_2mAva spotlight-isLogo_VnwVr'}).findNext('h2').getText()
    for imgg in img_ins:
        image = image + imgg
    return image


scriptReport = []   #array of dictionary




for row in urlArray:
    response = requests.get(row)  #bringing url
    pageData = {}    #creating dictionary
    soupObject = BeautifulSoup(response.content, 'html5lib') #parsing the html into soupObject

    pageData['partner_course_url'] = row
    pageData['title'] = soupObject.title.get_text()
    pageData['accredation_1_name'] = process_accredation_1_name(soupObject)
    pageData['accredation_1_logo'] = process_accredation_1_logo(soupObject)
    pageData['accredation_description'] = process_accredation_1_description(soupObject)
    scriptReport.append(pageData)

df = pd.DataFrame.from_dict(scriptReport)
df.to_csv('expert_track_accredation.csv', index=True, header=True)