from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service(r"C:\Users\PMLS\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s)

def DownloadPages(link,destination,file_name):
    driver.get(link)
    with open(f"{destination}/{file_name}.html",'w',encoding='utf-8') as page:
        page.write(driver.page_source)
    time.sleep(2)
    
# Below for Keyword : Porn Hub
DownloadPages(
    link="https://en.wikipedia.org/w/index.php?title=Special:Search&limit=500&offset=0&ns0=1&search=Pornhub",
    destination="../WebPages/PornHub",
    file_name="PornHub1"
    )    

# Below for Keyword : Lana Rhoades
DownloadPages(
    link="https://en.wikipedia.org/w/index.php?title=Special:Search&limit=100&offset=0&ns0=1&search=Lana+Rhoades",
    destination="../WebPages/LanaRhoades",
    file_name="LanaRhoades1"
    )    

# Below for Keyword : Mia Khalifa
DownloadPages(
    link="https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset=0&ns0=1&search=Mia+Khalifa",
    destination="../WebPages/MiaKhalifa",
    file_name="MiaKhalifa1"
    ) 

# Below for Keyword : xvidoes
DownloadPages(
    link="https://en.wikipedia.org/w/index.php?title=Special:Search&limit=50&offset=0&ns0=1&search=XVideos",
    destination="../WebPages/XVideos",
    file_name="XVideos1"
    )         

# Below for Keyword : red tube
offset = 0
for i in range(0,10):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=RedTube",
        destination="../WebPages/RedTube",
        file_name=f"RedTube{i+1}"
        ) 
    offset += 1000

# Below for Keyword : xxx
offset = 0
for i in range(0,10):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=xxx",
        destination="../WebPages/xxx",
        file_name=f"xxx{i+1}"
        ) 
    offset += 1000   

# Below for Keyword : Hardcore Sex
offset = 0
for i in range(0,4):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Hardcore+sex",
        destination="../WebPages/HardcoreSex",
        file_name=f"HardcoreSex{i+1}"
        ) 
    offset += 1000

# Below for Keyword : Nude
offset = 0
for i in range(0,10):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=nude",
        destination="../WebPages/Nude",
        file_name=f"Nude{i+1}"
        ) 
    offset += 1000

# Below for Keyword : Naked Girls
offset = 0
for i in range(0,10):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Naked+girls",
        destination="../WebPages/NakedGirls",
        file_name=f"NackedGirls{i+1}"
        ) 
    offset += 1000

# Below for Keyword : sex tape
offset = 0
for i in range(0,10):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Sex+tape",
        destination="../WebPages/SexTape",
        file_name=f"SexTape{i+1}"
        ) 
    offset += 1000


# Below for Keyword : adult video
offset = 0
for i in range(0,10):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Adult+Video",
        destination="../WebPages/AdultVideo",
        file_name=f"AdultVideo{i+1}"
        ) 
    offset += 1000
    
# Below for Keyword : onlyfans leaks
offset = 0
for i in range(0,8):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=only+fans+leak",
        destination="../WebPages/OnlyFansLeak",
        file_name=f"OnlyFansLeak{i+1}"
        ) 
    offset += 1000    

# Below for Keyword : erotic video
offset = 0
for i in range(0,7):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Erotic+video",
        destination="../WebPages/EroticVideo",
        file_name=f"EroticVideo{i+1}"
        ) 
    offset += 1000   

# Below for Keyword : Porn Video
offset = 0
for i in range(0,6):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Porn+video",
        destination="../WebPages/PornVideo",
        file_name=f"PornVideo{i+1}"
        ) 
    offset += 1000   

# Below for Keyword : Step Mom
offset = 0
for i in range(0,6):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Step-mom",
        destination="../WebPages/StepMom",
        file_name=f"StepMom{i+1}"
        ) 
    offset += 1000   

# Below For Keyword : Step sis
DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset=0&ns0=1&search=Step+sis",
        destination="../WebPages/StepSis",
        file_name=f"StepSis1"
        ) 

# Below For Keyword : incest
offset = 0
for i in range(0,6):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Incest",
        destination="../WebPages/Incest",
        file_name=f"Incest{i+1}"
        ) 
    offset += 1000  

# Below For Keyword : bangbros
offset = 0
for i in range(0,4):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Bang+Bros",
        destination="../WebPages/BangBros",
        file_name=f"BangBros{i+1}"
        ) 
    offset += 1000  

# Below For Keyword : brazzers
DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=200&offset=0&ns0=1&search=Brazzers",
        destination="../WebPages/Brazzers",
        file_name=f"Brazzers1"
        ) 

# Below For Keyword : fetish video
offset = 0
for i in range(0,2):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Fetish+video",
        destination="../WebPages/FetishVideo",
        file_name=f"FetishVideo{i+1}"
        ) 
    offset += 1000  

# Below For Keyword : Strip club
offset = 0
for i in range(0,10):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Strip+club",
        destination="../WebPages/StripClub",
        file_name=f"StripClub{i+1}"
        ) 
    offset += 1000  

# Below For Keyword : Cam girl
DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset=0&ns0=1&search=Camgirl",
        destination="../WebPages/Camgirl",
        file_name=f"Camgirl1"
        ) 

# Below For Keyword : Amateur Sex
offset = 0
for i in range(0,6):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Amateur+sex",
        destination="../WebPages/AmateurSex",
        file_name=f"AmateurSex{i+1}"
        ) 
    offset += 1000  

# Below For Keyword : Street fight
offset = 0
for i in range(0,10):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Street+fight",
        destination="../WebPages/StreetFight",
        file_name=f"StreetFight{i+1}"
        ) 
    offset += 1000 

# Below For Keyword : Brutal fight
offset = 0
for i in range(0,10):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Brutal+fight",
        destination="../WebPages/BrutalFight",
        file_name=f"BrutalFight{i+1}"
        ) 
    offset += 1000 

# Below For Keyword : Road Rage
offset = 0
for i in range(0,10):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Road+rage",
        destination="../WebPages/RoadRage",
        file_name=f"RoadRage{i+1}"
        ) 
    offset += 1000 

# Below For Keyword : Physical Assault
offset = 0
for i in range(0,10):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Physical+assault",
        destination="../WebPages/PhysicalAssault",
        file_name=f"PhysicalAssault{i+1}"
        ) 
    offset += 1000 

# Below For Keyword : Fist Fight
offset = 0
for i in range(0,9):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Fist+Fight",
        destination="../WebPages/FistFight",
        file_name=f"FistFight{i+1}"
        ) 
    offset += 1000 

# Below For Keyword : Gang Fight
offset = 0
for i in range(0,10):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Gang+fight",
        destination="../WebPages/GangFight",
        file_name=f"GangFight{i+1}"
        ) 
    offset += 1000 

# Below For Keyword : Bloody Fight
offset = 0
for i in range(0,10):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Bloody+Fight",
        destination="../WebPages/BloodyFight",
        file_name=f"BloodyFight{i+1}"
        ) 
    offset += 1000 

# Below For Keyword : School Fight
offset = 0
for i in range(0,10):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=School+Fight",
        destination="../WebPages/SchoolFight",
        file_name=f"SchoolFight{i+1}"
        ) 
    offset += 1000 

# Below For Keyword : Violent attack
offset = 0
for i in range(0,10):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Violent+attack",
        destination="../WebPages/ViolentAttack",
        file_name=f"ViolentAttack{i+1}"
        ) 
    offset += 1000 

# Below For Keyword : Punch Video
offset = 0
for i in range(0,10):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Punch+video",
        destination="../WebPages/PunchVideo",
        file_name=f"PunchVideo{i+1}"
        ) 
    offset += 1000 

# Below For Keyword : Public Brawl
offset = 0
for i in range(0,6):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=public+brawl",
        destination="../WebPages/PublicBrawl",
        file_name=f"PublicBrawl{i+1}"
        ) 
    offset += 1000

# Below For Keyword : Fight Caught on Camera
offset = 0
for i in range(0,5):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=fight+caught+on+camera",
        destination="../WebPages/FightCaughtOnCamera",
        file_name=f"FightCaughtOnCamera{i+1}"
        ) 
    offset += 1000

# Below For Keyword : Gun Fight
offset = 0
for i in range(0,10):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Gun+fight",
        destination="../WebPages/GunFight",
        file_name=f"GunFight{i+1}"
        ) 
    offset += 1000

# Below For Keyword : Weopan Fight
offset = 0
for i in range(0,1):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Weapan+fight",
        destination="../WebPages/WeapanFight",
        file_name=f"WeaponFight{i+1}"
        ) 
    offset += 1000

# Below For Keyword : Knife Attack
offset = 0
for i in range(0,10):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Knife+attack",
        destination="../WebPages/KnifeAttack",
        file_name=f"KnifeAttack{i+1}"
        ) 
    offset += 1000

# Below For Keyword : Street Violence
offset = 0
for i in range(0,10):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Street+violence",
        destination="../WebPages/StreetViolence",
        file_name=f"StreetViolence{i+1}"
        ) 
    offset += 1000

# Below For Keyword : Murder Video
offset = 0
for i in range(0,10):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Murder+video",
        destination="../WebPages/MurderVideo",
        file_name=f"MurderVideo{i+1}"
        ) 
    offset += 1000

# Below For Keyword : Murder Video
offset = 0
for i in range(0,10):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Kill+video",
        destination="../WebPages/KillVideo",
        file_name=f"KillVideo{i+1}"
        ) 
    offset += 1000

# Below For Keyword : Verbal Abuse
offset = 0
for i in range(0,5):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Verbal+abuse",
        destination="../WebPages/VerbalAbuse",
        file_name=f"VerbalAbuse{i+1}"
        ) 
    offset += 1000

# Below For Keyword : Public Harassment
offset = 0
for i in range(0,10):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Public+harassment",
        destination="../WebPages/PublicHarassment",
        file_name=f"PublicHarassment{i+1}"
        ) 
    offset += 1000

# Below For Keyword : Molestation Caught
offset = 0
for i in range(0,2):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Molestation+caught",
        destination="../WebPages/MolestationCaught",
        file_name=f"MolestationCaught{i+1}"
        ) 
    offset += 1000

# Below For Keyword : Harass Video
offset = 0
for i in range(0,6):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Harass+video",
        destination="../WebPages/HarassVideo",
        file_name=f"HarassVideo{i+1}"
        ) 
    offset += 1000

# Below For Keyword : Domestic Violence
offset = 0
for i in range(0,10):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Domestic+violence",
        destination="../WebPages/DomesticViolence",
        file_name=f"DomesticViolence{i+1}"
        ) 
    offset += 1000

# Below For Keyword : Bullying Caught
offset = 0
for i in range(0,5):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Bullying+caught",
        destination="../WebPages/BullyingCaught",
        file_name=f"BullyingCaught{i+1}"
        ) 
    offset += 1000

# Below For Keyword : Abuse caught on Camera
offset = 0
for i in range(0,2):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Abuse+caught+on+camera",
        destination="../WebPages/AbuseCaughtOnCamera",
        file_name=f"AbuseCaughtOnCamera{i+1}"
        ) 
    offset += 1000

# Below For Keyword : Torture Video
offset = 0
for i in range(0,10):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Torture+video",
        destination="../WebPages/TortureVideo",
        file_name=f"TortureVideo{i+1}"
        ) 
    offset += 1000

# Below For Keyword : Slap Video
offset = 0
for i in range(0,6):
    DownloadPages(
        link=f"https://en.wikipedia.org/w/index.php?title=Special:Search&limit=1000&offset={offset}&ns0=1&search=Slap+video",
        destination="../WebPages/SlapVideo",
        file_name=f"SlapVideo{i+1}"
        ) 
    offset += 1000
