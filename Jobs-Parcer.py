#  Jobs Parcer
#  Creator: Me

#  Note - Doesnt work on all websites, as some dont load all information as apart of the html.
# - Some websites cannot be parsed correctly, as they load the content after a delay, resulting in the response not containing the information.


import bs4
import requests


# sites = {
    # "linkedin" : {
    #     "url" : "https://uk.linkedin.com/jobs/software-developer-jobs?",  # Site
    #     "search-param" : "keywords",  # Search url parameters
    #     "container_class" : ["a", "base-card__full-link"],  # Under what name is the content stored.
    #     "id_Class" : "class",    
    #     "offset" : 1
    # }
    # ,
    # "GRB-Internships" : {
    #     "url" : "https://www.grb.uk.com/internships?",
    #     "search-param" : "keywords",  # Search url parameters
    #     "container_class" : ["div", "vacancy-listing"],  # Under what name is the content stored.
    #     "container_search" : "class",
    #     "offset" : 0
    # }
    # ,
    # "NHS" : {
    #     "url" : "",
    #     "title-element" : ""
    # },
    # "GradCracker" : {
    #     "url" : "",
    #     "title-element" : ""
    # },
    # "JobSora" : {
    # }
# }


Keywords = [
            # "IT", 
            # "Data", 
            # "Software", 
            # "Games", 
            # "Service", 
            # "Cyber Security", 
            "developer"]

req = requests.models.PreparedRequest()

# def searchLinkedin():
#     jobs_list = {}
#     for word in Keywords:
#         site = "linkedin"
#         jobs_list[site] = []
#         print(sites[f"{site}"]["search-param"])
#         req.prepare_url(sites[f"{site}"]["url"], {sites[f"{site}"]["search-param"] : word})
#         print(req.url)
#         with requests.get(req.url) as s:
#             try:
#                 s.raise_for_status()

#                 soup = bs4.BeautifulSoup(s.text, "html.parser")
#                 # print(s.text)
#                 container_class = sites[site]["container_class"]
#                 for i in soup.find_all(container_class[0], attrs={"class" : container_class[1]}):
#                     # print(type(i))
#                     print(i)

#                     title = i.contents[sites[site]["offset"]].text
#                     link = i.get("href")

#                     title = title.replace("  ", "")
#                     title = title.strip("\n")
#                     # print(title)
#                     # print(len(title))
#                     # print(link)
#                     jobs_list[site].append({"role" : title, "href" : link})
#                 print(jobs_list)
#             except Exception as err:
#                 print("--", err)
#         return jobs_list

# searchLinkedin()

# //*[@id="main-content"]/section[2]/ul
# /html/body/div[3]/div/main/section[2]/ul

#  GRB
# //*[@id="vacancyList"]
# /html/body/div[1]/div[2]/section/div/div[2]/div/div[1]/div/div/div/div/div/div[2]/div

# Linkedin - works

url = "https://uk.linkedin.com/jobs/search?location=Greater%20Bristol%20Area%2C%20United%20Kingdom&geoId=90009475&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0&"
htmlElement = "a"
elementName = "base-card__full-link"
Keywords = {"keyword" : "IT"}

def count_element(elementName, text):
    print(elementName in str(text))
    print(str(text).count(elementName))
    print(str(text).find(elementName))
    print(str(text)[str(text).find(elementName) - 100 : int(str(text).find(elementName)) + 300])
        

    return str(text).count(elementName)


print("--")
try:
    req = requests.models.PreparedRequest()
    req.prepare_url(url, Keywords)
    url = requests.get(req.url)
    text = bs4.BeautifulSoup(url.text, "html.parser")
    print("Apple" in text.text)

    x = count_element(elementName, text)
    if x == 1:
        if x == 0:
            raise
        else:
            print("=== Based on the number of results, this code might not work on this website. ===".upper())

    
    for i in text.find_all(htmlElement):
        # print(" ".join(str(i["class"])))
        if i.has_attr("class"):
            # print("===> ", "a" in str(i))
            # print(", ".join(i["class"]))
            # print("++")
            # print(", ".join(i["class"]))
            # print(elementName in ", ".join(i["class"]))
            if elementName in ", ".join(i["class"]) == True:
                break
            if elementName in ", ".join(i["class"]):
                print("found")
                print(i.text)
                print(i.get("href"))
                continue
        elif i.has_attr("id"):
            # print("**")
            if elementName in ", ".join(i["id"]):
                print(i.text)
                continue
    # print(text.select(f'[class*="{elementName}"]'))
    
    # print(text.select(f".{elementName}"))

    # for i in text.select(f".{elementName}"):
    #     print(i.get_text())

except Exception as err:
    print(err)