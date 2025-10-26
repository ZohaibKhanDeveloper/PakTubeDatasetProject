from bs4 import BeautifulSoup
import re
import pandas as pd

size_pattern = r"(\d+)\s+KB|(\d+)\s+bytes"
word_count_pattern = r"\(([\d,]+)\s+words\)"
time_pattern = r"(\d{2}:\d{2})"
date_pattern = r"(\d{1,2}\s+\w+\s+\d{4})"

def ScrapeAndSaveData(file_path,file_name,no_of_files):
    title = []
    description = []
    size_in_kb = []
    word_count = []
    updated_time = []
    updated_date = []
    for i in range(1,no_of_files+1):
        print(f"Reading file {file_name}{i}.html from {file_path} ...")
        with open(f"{file_path}/{file_name}{i}.html",'r',encoding='utf-8') as file:
            soup = BeautifulSoup(file,'html.parser')
            title_divs = soup.find_all("div",class_="mw-search-result-heading")
            description_divs = soup.find_all("div",class_="searchresult")
            article_info_divs = soup.find_all("div",class_="mw-search-result-data")
            for index in range(len(title_divs)):
                title.append(title_divs[index].text)
                description.append(description_divs[index].text)
                size = re.search(size_pattern,article_info_divs[index].text)
                words = re.search(word_count_pattern,article_info_divs[index].text)
                time = re.search(time_pattern,article_info_divs[index].text)
                date = re.search(date_pattern,article_info_divs[index].text)
                # print(size.group())
                size_in_kb.append(size.group())
                word_count.append(int(words.group(1).replace(',', '')))
                updated_time.append(time.group(1))
                updated_date.append(date.group(1))
    scraped_data = pd.DataFrame({
        "Title":title,
        "Description":description,
        "Article Size (KB/Bytes)":size_in_kb,
        "Article's Words Count":word_count,
        "Publish Time":updated_time,
        "Publish Date":updated_date
    })
    print(scraped_data)
    scraped_data.to_csv(f"../DataScrapped-CSV-JSON/CSV-Data/{file_name}.csv",index=False)
    scraped_data.to_json(f"../DataScrapped-CSV-JSON/JSON-Data/{file_name}.json",index=False)
    
folder_file = [
    'AdultVideo','AmateurSex','BangBros','Brazzers','BrutalFight','Camgirl','EroticVideo','FetishVideo','GayPorn',
    'HardcoreSex','Incest','LanaRhoades','LesbianSex','MiaKhalifa','NackedGirls','Nude','OnlyFansLeak','PornHub',
    'PornVideo','RedTube','SexTape','StepMom','StepSis','StreetFight','StripClub','XVideos','xxx',
    'RoadRage','PhysicalAssault','FistFight','GangFight','BloodyFight','SchoolFight','ViolentAttack','PunchVideo','PublicBrawl',
    'FightCaughtOnCamera','GunFight','WeapanFight','KnifeAttack','StreetViolence','MurderVideo','KillVideo','VerbalAbuse',
    'PublicHarassment','MolestationCaught','HarassVideo','DomesticViolence','BullyingCaught','AbuseCaughtOnCamera','TortureVideo','SlapVideo'
    ]    
number_of_files = [
    10,6,4,1,10,1,7,2,4,
    4,6,1,10,1,10,10,8,1,
    6,10,10,6,1,10,10,1,10,
    10,10,9,10,10,10,10,10,6,
    5,10,1,10,10,10,10,5,
    10,2,6,10,5,2,10,6
]

for index in range(len(folder_file)):
    ScrapeAndSaveData(file_path=f'../WebPages/{folder_file[index]}',file_name=folder_file[index],no_of_files=number_of_files[index]) 
    print(f"{folder_file[index]} Scrapped and saved in csv and json")
