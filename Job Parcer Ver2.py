#  Job Parcer Ver2
#  Creator: Me

import webbrowser
import requests
import time


#  Sites contain all of the settings. Saves time having to re-enter each filter.
sites = {
    "linkedin" : {
        "url" : "https://uk.linkedin.com/jobs/search?location=Greater%20Bristol%20Area%2C%20United%20Kingdom&geoId=90009475&f_PP=103615590&f_TPR=r86400&f_E=1%2C2&position=1&pageNum=0",
        "url-param" : "keywords"
    },
    "JobSora" : {
        "url" : "https://uk.jobsora.com/jobs?location=Bristol",
        "url-param" : "query"
    }
    , 
    "GRB" : {
        "url" : "https://www.grb.uk.com/internships?",
        "url-param" : "keywords"
    },
    "GradCracker" : {
        "url" : [
            "https://www.gradcracker.com/search/computing-technology/software-work-placements-internships-in-bristol",
            "https://www.gradcracker.com/search/computing-technology/data-science-work-placements-internships-in-bristol",
            "https://www.gradcracker.com/search/computing-technology/information-technology-work-placements-internships-in-bristol",
            "https://www.gradcracker.com/search/computing-technology/artificial-intelligence-work-placements-internships-in-bristol"
        ]
    }
}

roles = ["IT", "Service Desk", "Cyber Security", "Data", "Software"]

web = webbrowser
for index, site in enumerate(sites):
    for role in roles:
        #  Prepare role search and prepare URL
        if "url-param" in dict(sites[site]).keys():
            param = {sites[site]["url-param"] : role}
            url = str(requests.get(sites[site]["url"], params=param).url)
            print(url)
        else:
            url = sites[site]["url"]
            for link in url:
                print(link)
            break

        # print(index, site)
        # print(sites[site])
        
        # print(type(url))

        #  Open websites  -  Some websites links get redirected. Little Point opening them.
        continue

        time.sleep(2)
        if index == 0:
            web.open_new_tab(url=url)
        else:
            web.open_new_tab(url=url)