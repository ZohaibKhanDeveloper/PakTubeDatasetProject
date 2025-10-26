# NOTE
# No need to run this program because i checked the data using this program some of the titles are same but 
# the descriptions (short) are change that is why all the 341489 records are neccessary.
import pandas as pd
import time
dataset = pd.read_csv("../Finaled&CleanDatasets/CSV-Datasets/Uncleaned&MergedDataset.csv")
# print(dataset)
title = dataset["Title"].tolist()
description = dataset["Description"].tolist()
article_size = dataset["Article Size (KB/Bytes)"].tolist()
word_count = dataset["Article's Words Count"].tolist()
publish_time = dataset["Publish Time"].tolist()
publish_date = dataset["Publish Date"].tolist()

cleaned_title = []
cleaned_description = []
cleaned_article_size = []
cleaned_word_count = []
cleaned_publish_time = []
cleaned_publish_date = []
start_time = time.time()
# for i in range(0,341489):
for i in range(0,50):    
    if(title[i] not in cleaned_title):
        print(f"Appending the clear data {i}")
        cleaned_title.append(title[i])
        cleaned_description.append(description[i])
        cleaned_article_size.append(article_size[i])
        cleaned_word_count.append(word_count[i])
        cleaned_publish_time.append(publish_time[i])
        cleaned_publish_date.append(publish_date[i])

print(len(cleaned_title))        
end_time = time.time() - start_time
print(end_time)
cleaned_dataset = pd.DataFrame({
        "Title":cleaned_title,
        "Description":cleaned_description,
        "Article Size (KB/Bytes)":cleaned_article_size,
        "Article's Words Count":cleaned_word_count,
        "Publish Time":cleaned_publish_time,
        "Publish Date":cleaned_publish_date
    })
print(cleaned_dataset)
# cleaned_dataset.to_csv("../Finaled&CleanDatasets/CSV-Datasets/CleanedDataset.csv",index=False)
# cleaned_dataset.to_json("../Finaled&CleanDatasets/JSON-Datasets/CleanedDataset.json",index=False)