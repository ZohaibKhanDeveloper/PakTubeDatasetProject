import pandas as pd
files_names = [
    'AdultVideo','AmateurSex','BangBros','Brazzers','BrutalFight','Camgirl','EroticVideo','FetishVideo','GayPorn',
    'HardcoreSex','Incest','LanaRhoades','LesbianSex','MiaKhalifa','NackedGirls','Nude','OnlyFansLeak','PornHub',
    'PornVideo','RedTube','SexTape','StepMom','StepSis','StreetFight','StripClub','XVideos','xxx',
    'RoadRage','PhysicalAssault','FistFight','GangFight','BloodyFight','SchoolFight','ViolentAttack','PunchVideo','PublicBrawl',
    'FightCaughtOnCamera','GunFight','WeapanFight','KnifeAttack','StreetViolence','MurderVideo','KillVideo','VerbalAbuse',
    'PublicHarassment','MolestationCaught','HarassVideo','DomesticViolence','BullyingCaught','AbuseCaughtOnCamera','TortureVideo','SlapVideo'
    ]

def merge_files(files_list,file_form,location):
    merged_files = pd.DataFrame()
    if file_form == 'csv':
        for file in files_list:
            current_file = pd.read_csv(f'{location}/{file}.csv')
            merged_files = pd.concat([merged_files, current_file], ignore_index=True) 
        merged_files.to_csv("../Finaled&CleanDatasets/CSV-Datasets/Uncleaned&MergedDataset.csv",index=False)       
    elif file_form == 'json':
        for file in files_list:
            current_file = pd.read_json(f'{location}/{file}.json')
            merged_files = pd.concat([merged_files, current_file], ignore_index=True)  
        merged_files.to_json("../Finaled&CleanDatasets/JSON-Datasets/Uncleaned&MergedDataset.json",index=False) 
    
    print(f'Files merged in {file_form} format')

merge_files(files_names,'csv','../DataScrapped-CSV-JSON/CSV-Data')
merge_files(files_names,'json','../DataScrapped-CSV-JSON/JSON-Data')
   