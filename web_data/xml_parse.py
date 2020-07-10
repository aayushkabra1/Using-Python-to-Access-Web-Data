import xml.etree.ElementTree as ET

data = ''' <person>
                <name>AAyush</name>
                <phone>312413</phone>
                <email hide="Yes" />
           </person>'''

tree = ET.fromstring(data)
print("Name: ", tree.find('name').text)
print("Email: ", tree.find('email').text                      