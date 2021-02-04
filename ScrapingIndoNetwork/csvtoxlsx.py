import pandas as pd

startFrom = 1
for x in range(187):
    try:
        read_file = pd.read_csv (r'/Users/abdulsalam/Documents/learning/belajar-web-scraping/ScrapingIndoNetwork/data_company' + str(startFrom + x) + '.csv')
    except Exception:
        continue

    read_file.to_excel (r'/Users/abdulsalam/Documents/learning/belajar-web-scraping/ScrapingIndoNetwork/data_company' + str(startFrom + x) + '.xlsx', index = None, header=True)