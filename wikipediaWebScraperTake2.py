import pandas
import requests

from bs4 import BeautifulSoup

website_text = requests.get('https://en.wikipedia.org/wiki/List_of_Greek_and_Latin_roots_in_English/A%E2%80%93G').text
soup = BeautifulSoup(website_text, 'xml')

for table in soup.find_all('table', {'class':'wikitable sortable'}):
    table_rows = table.find_all('tr')

    data = []
    rowsSize = 0

    for row in table_rows:
        data.append([t.text.strip() for t in row.find_all('td')])
        rowsSize += 1

    print(rowsSize)

    dataSize = len(data)
    dataIndex = 1

    entireString = ""

    while dataIndex < dataSize:

        stringOfData = str(data[dataIndex])
        stringOfData = stringOfData[2:len(stringOfData)]
        endIndex = stringOfData.find('\'')
        stringOfData = stringOfData[0:endIndex]

        if (stringOfData.find('[') != -1):
            endIndex = stringOfData.find('[')
            stringOfData = stringOfData[0: endIndex]

        if (stringOfData.find('(') != -1):
            endIndex = stringOfData.find('(')
            stringOfData = stringOfData[0: endIndex]

        entireString += stringOfData + ", "
        dataIndex += 1

    entireString = entireString[0:(len(entireString) - 2)]
    print(entireString)

    rootList = entireString.split(", ")

    File_object = open("rootWords.txt", "a")

    index = 0
    while index < len(rootList):
        if (str(rootList[index])[0] == '-'):
            print(rootList[index])
            rootList[index] = str(rootList[index])[1:(len(str(rootList[index])))]
            print(rootList[index])

        File_object.write(rootList[index] + "\n")
        index += 1
