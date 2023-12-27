# # 

# import mysql.connector
# import requests
# from bs4 import BeautifulSoup

# # Establish a connection to the MySQL server
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="jeeva12345",
#     database="scraping",
# )
# mycursor = mydb.cursor()
# columns = [
#         "Name", "Position", "Telephone", "Email", "Website", "Address", "Postcode",
#         "Area_served", "Notes", "Additional_Website", "Parking_available", "Time_of_day",
#         "Session_Information", "Age_Groups", "Related_links", "cost_Details", "Accessibility",
#         "Social_Media", "Parking_details", "Accreditation_details", "Venue_Email",
#         "Venue_Website", "Transport"
# ]
    
# for i in range(1, 10):
#     url = f"https://infolink.suffolk.gov.uk/kb5/suffolk/infolink/results.page?qt=&term=London%2C+Little%2C+Suffolk&sorttype=distance&page={i}"

#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Find all 'a' elements with class 'flex-grow-1' and extract their 'href' attributes
#     links = soup.find_all('a', class_='flex-grow-1')
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

#                 values = {}
#                 for dt, dd in zip(data1, data2):
#                     values[dt.text.strip()] = dd.text.strip()

            

    
import mysql.connector
import requests
from bs4 import BeautifulSoup

# Establish a connection to the MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jeeva12345",
    database="scraping"
)
mycursor = mydb.cursor()
columns = [
        "Name", "Position", "Telephone", "Email", "Website", "Address", "Postcode",
        "Area_served", "Notes", "Additional_Website", "Parking_available", "Time_of_day",
        "Session_Information", "Age_Groups", "Related_links", "cost_Details", "Accessibility",
        "Social_Media", "Parking_details", "Accreditation_details", "Venue_Email",
        "Venue_Website", "Transport"
]

for i in range(1, 10):
    url = f"https://infolink.suffolk.gov.uk/kb5/suffolk/infolink/results.page?qt=&term=London%2C+Little%2C+Suffolk&sorttype=distance&page={i}"

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all 'a' elements with class 'flex-grow-1' and extract their 'href' attributes
        links = soup.find_all('a', class_='flex-grow-1')
        for link in links:
            href = link.get('href')
            if href:
                full_url = 'https://infolink.suffolk.gov.uk/kb5/suffolk/infolink/' + href

                response = requests.get(full_url)

                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')

                    element = soup.find('section', class_='field_section')
                    data1 = element.find_all('dt')
                    data2 = element.find_all('dd')

                    values = {}
                    for dt, dd in zip(data1, data2):
                        values[dt.text.strip()] = dd.text.strip()

                    # Convert the dictionary to a list preserving the order of the columns
                    sql_values = [values.get(column, "") for column in columns]

                    # Prepare SQL query and data for insertion
                    sql = "INSERT INTO func (Name, Position, Telephone, Email, Website, Address, Postcode, Area_served, Notes, Additional_Website, Parking_available, Time_of_day, Session_Information, Age_Groups, Related_links, cost_Details, Accessibility, Social_Media, Parking_details, Accreditation_details, Venue_Email, Venue_Website, Transport) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

                    # Execute the query
                    mycursor.execute(sql, sql_values)

# Commit the changes and close the connection
mydb.commit()
mydb.close()



# # 

# import mysql.connector
# import requests
# from bs4 import BeautifulSoup

# # Establish a connection to the MySQL server
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="jeeva12345",
#     database="scraping",
# )
# mycursor = mydb.cursor()
# columns = [
#         "Name", "Position", "Telephone", "Email", "Website", "Address", "Postcode",
#         "Area_served", "Notes", "Additional_Website", "Parking_available", "Time_of_day",
#         "Session_Information", "Age_Groups", "Related_links", "cost_Details", "Accessibility",
#         "Social_Media", "Parking_details", "Accreditation_details", "Venue_Email",
#         "Venue_Website", "Transport"
# ]
    
# for i in range(1, 10):
#     url = f"https://infolink.suffolk.gov.uk/kb5/suffolk/infolink/results.page?qt=&term=London%2C+Little%2C+Suffolk&sorttype=distance&page={i}"

#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Find all 'a' elements with class 'flex-grow-1' and extract their 'href' attributes
#     links = soup.find_all('a', class_='flex-grow-1')
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

#                 values = {}
#                 for dt, dd in zip(data1, data2):
#                     values[dt.text.strip()] = dd.text.strip()

            