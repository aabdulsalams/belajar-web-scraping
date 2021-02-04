import os.path
from os import path
import pathlib

startFrom = 188
for x in range(187):
    if str(path.exists('/Users/abdulsalam/Documents/learning/belajar-web-scraping/ScrapingIndoNetwork/data_company' + str(startFrom + x) + '.csv')) == 'True':
        if str(path.exists('/Users/abdulsalam/Documents/learning/belajar-web-scraping/ScrapingIndoNetwork/data_company' + str(startFrom + x) + '.xlsx')) == 'True':
            print(str(startFrom + x))
        else:
            print('Kosong ' + str(startFrom + x))
    else:
        print('MEMANG TIDAK ADA ' + str(startFrom + x))