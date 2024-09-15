from OSMPythonTools.api import Api
from OSMPythonTools.overpass import Overpass
from OSMPythonTools.overpass import overpassQueryBuilder
from OSMPythonTools.nominatim import Nominatim

api = Api()
overpass = Overpass()
nominatim = Nominatim()

query = overpassQueryBuilder(elementType='node', area=nominatim.query('Blacksburg, VA'), selector=['"name"~"Kroger"'])

transitCenterOrangeQuery = overpassQueryBuilder(elementType='node', area=nominatim.query('Blacksburg, Virginia'), selector=['"name"~"Orange Loop Bay 13"'])
transitCenterOrangeQuery2 = nominatim.query(37.2305167926052, -80.42647804794724, reverse=True)
transitCenterOrange = overpass.query(transitCenterOrangeQuery).nodes()[0]

transitCenterMaroonQuery = overpassQueryBuilder(elementType='node', area=nominatim.query('Blacksburg, Virginia'), selector=['"name"~"Maroon Loop Bay 3"'])
transitCenterMaroonQuery2 = nominatim.query(37.23189712142836, -80.42493507728743, reverse=True)
transitCenterMaroon = overpass.query(transitCenterMaroonQuery).nodes()[0]

ucbKrogerQuery = overpassQueryBuilder(elementType='node', area=nominatim.query('Blacksburg, Virginia'), selector=['"name"~"Wells Fargo"'])
ucbKrogerQuery2 = nominatim.query(37.23608908750317, -80.43370135203027, reverse=True)
ucbKroger = overpass.query(ucbKrogerQuery).nodes()[0]

mainStreetKrogerQuery = overpassQueryBuilder(elementType='node', area=nominatim.query('Blacksburg, Virginia'), selector=['"name"~"Gables Shopping Center"'])
mainStreetKrogerQuery2 = nominatim.query(37.21578794148806, -80.40039157853643, reverse=True)
mainStreetKroger = overpass.query(mainStreetKrogerQuery).nodes()[0]

walmartQuery = overpassQueryBuilder(elementType='node', area=nominatim.query('Christiansburg, Virginia'), selector=['"name"~"Barnes & Noble"'])
walmartQuery2 = nominatim.query(37.16174986117525, -80.42566142295796, reverse=True)
walmart = overpass.query(walmartQuery).nodes()[0]

withinTransitCenterOrange = overpassQueryBuilder(elementType='node', bbox=[transitCenterOrange.lat() - 0.00458, transitCenterOrange.lon() - 0.00916, transitCenterOrange.lat() + 0.00362, transitCenterOrange.lon() + 0.00458])
withinTransitCenterMaroon = overpassQueryBuilder(elementType='node', bbox=[transitCenterMaroon.lat() - 0.00458, transitCenterMaroon.lon() - 0.00916, transitCenterMaroon.lat() + 0.00362, transitCenterMaroon.lon() + 0.00458])
withinUcbKroger = overpassQueryBuilder(elementType='node', bbox=[ucbKroger.lat() - 0.00362, ucbKroger.lon() - 0.00458, ucbKroger.lat() + 0.00362, ucbKroger.lon() + 0.00458])
withinMainStreetKroger = overpassQueryBuilder(elementType='node', bbox=[mainStreetKroger.lat() - 0.00362, mainStreetKroger.lon() - 0.00458, mainStreetKroger.lat() + 0.003625, mainStreetKroger.lon() + 0.00458])
withinWalmart= overpassQueryBuilder(elementType='node', bbox=[walmart.lat() - 0.00362, walmart.lon() - 0.00458, walmart.lat() + 0.00362, walmart.lon() + 0.00458])

input = "University Mall"
for node in overpass.query(withinTransitCenterOrange).nodes():
    if node.tags() != None:
        if 'name' in node.tags():
            if node.tags()['name'] == input:
                print("Transit Center Orange")
for node in overpass.query(withinTransitCenterMaroon).nodes():
    if node.tags() != None:
        if 'name' in node.tags():
            if node.tags()['name'] == input:
                print("Transit Center Maroon")
for node in overpass.query(withinUcbKroger).nodes():
    if node.tags() != None:
        if 'name' in node.tags():
            if node.tags()['name'] == input:
                print("UCB Kroger")
for node in overpass.query(withinMainStreetKroger).nodes():
    if node.tags() != None:
        if 'name' in node.tags():
            if node.tags()['name'] == input:
                print("Main Street Kroger")
for node in overpass.query(withinWalmart).nodes():
    if node.tags() != None:
        if 'name' in node.tags():
            if node.tags()['name'] == input:
                print("Walmart")