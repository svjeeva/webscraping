51



# # for url in url:
# import requests
# from bs4 import BeautifulSoup
# import csv

# data_list = []

# for i in range(1, 6):
#     url = f"https://infolink.suffolk.gov.uk/kb5/suffolk/infolink/results.page?qt=&term=London%2C+Little%2C+Suffolk&sorttype=distance&page={i}"

#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Find all 'a' elements with class 'flex-grow-1' and extract their 'href' attributes
#     links = soup.find_all('a', class_='flex-grow')
#     for link in links:
#         href = link.get('href')
#         if href:
#             full_url = 'https://infolink.suffolk.gov.uk/kb5/suffolk/infolink/' + href

#             response = requests.get(full_url)

#             if response.status_code == 200:
#                 soup = BeautifulSoup(response.content, 'html.parser')

#                 element = soup.find('section', class_='field_section')
#                 data1 = element.find_all('dt')
#                 data2 = element.find_all('dd')

#                 for dt, dd in zip(data1, data2):
#                     data_list.append([dt.text.strip(), dd.text.strip()])

# # Writing the data to a CSV file
# with open('output.csv', 'a', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Field', 'Value'])  # Write header
#     writer.writerows(data_list)

