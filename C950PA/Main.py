# Student Name: Wyatt Durbin
# Student ID: 002184855
import csv
import datetime
import Graph
import PackageHashTable
import Truck
import Vertex
import time
from Package import Package


# Reads data from package csv file and created package objects.
# Objects are stored into the package hash table.
# Each of the three trucks are loaded with packages.
def load_package_data(filename):
    with open(filename) as packageFile:
        packageData = csv.reader(packageFile)

        for package in packageData:
            ID = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zip_code = package[4]
            deadline_time = package[5]
            weight = package[6]
            notes = package[7]
            status = 'At the hub.'
            delivery_time = 'Not yet delivered.'

            created_package = Package(ID, address, city, state, zip_code, deadline_time, weight, notes, status,
                                      delivery_time)
            PackageTable.insert(ID, created_package)
            # print(created_package)

            if ID in [13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40, 1]:
                truck_one.packages.append(ID)

                continue
            if "truck 2" in status or ID in [6, 12, 17, 21, 22, 23, 24, 25, 26, 27, 35, 39]:
                truck_two.packages.append(ID)
                continue
            if "Delayed" or "Wrong" or "Delivered" in status:
                truck_three.packages.append(ID)
                continue



# Creates an object for each of the three trucks available.
truck_one = Truck.Truck(16, 18, [], 0, '4001 South 700 East', datetime.timedelta(hours=8), datetime.timedelta(hours=8))
truck_two = Truck.Truck(16, 18, [], 0, '4001 South 700 East', datetime.timedelta(hours=9, minutes=10, seconds=00), datetime.timedelta(hours=9, minutes=10, seconds=00))
truck_three = Truck.Truck(8, 18, [], 0, '4001 South 700 East', datetime.timedelta(hours=12), datetime.timedelta(hours=12))
truck_one_dict = {}
adj_vertex = 0


# Sorts the packages of the truck object given.
# Tracks mileage and time of the truck.
# Truck is returned to the hub at end of run.
def dijkstra_shortest_path(graph, truck):
    undelivered_package = []
    # Moves truck's packages into a list of undelviered packages.
    for ID in truck.packages:
        package = PackageTable.search(ID)
        # Changes package 9's delivery address if it's past 10:20AM.
        if package.ID == 9 and truck.time > datetime.timedelta(hours=10, minutes=20, seconds=00):
            package.address = '410 S State St'
            package.zip = '84111'
        package.address = address_ID_dict.get(package.address)

        undelivered_package.append(package)
    # Sets the truck's packages to an empty list.
    truck.packages = []
    truck.address = 0
    # While loop that loops for the count of undelivered packages.
    while len(undelivered_package) > 0:
        smallest_dist = 0

        # For loop that runs through each undelivered package and compares it to the previous undelivered package.
        # This finds the closet package to the trucks current address (Which is the address of the last delviered package.).
        # Tracks the trucks time, mileage.
        # Records the package delivery time.

        for i in range(1, len(undelivered_package)):

            # Finds the closest distance package between the next undelivered packages, and the current closest package.
            if graph.edge_weights[int(truck.address), int(undelivered_package[i].address)] < \
                    graph.edge_weights[int(truck.address), int(undelivered_package[smallest_dist].address)]:
                smallest_dist = i
        truck.time += datetime.timedelta(
            hours=float(graph.edge_weights[int(truck.address), int(undelivered_package[smallest_dist].address)]) / 18)
        truck.mileage = truck.mileage + float(
            graph.edge_weights[int(truck.address), int(undelivered_package[smallest_dist].address)])
        truck.address = undelivered_package[smallest_dist].address
        undelivered_package[smallest_dist].delivery_time = truck.time
        undelivered_package[smallest_dist].status = "Delivered: "
        undelivered_package[smallest_dist].address = address_dict.get(undelivered_package[smallest_dist].address)
        truck.packages.append(undelivered_package[smallest_dist])
        undelivered_package.pop(smallest_dist)

    # Returns the current truck back to the hub.
    truck.time += datetime.timedelta(hours=float(graph.edge_weights[int(truck.address), 0] / 18))
    truck.mileage += float(graph.edge_weights[int(truck.address), 0])
    truck.address = '4001 South 700 East'


address_ID_dict = {}
address_dict = {}


# Adds vertices to graph object
def add_vertex(graph):
    with open('CSV/Address_File.csv') as file:
        reader = csv.reader(file)
        reader = list(reader)

        for row in reader:
            # print(row[0])
            vertices.append(Vertex.Vertex(row[0]))
            graph.add_vertex(int(row[0]))
            address_ID_dict[row[2]] = row[0]
            address_dict[row[0]] = row[2]


# Adds undirected edge to graph object
def add_edge(graph):
    with open('CSV/Distance_File.csv') as file:
        reader = csv.reader(file)
        reader = list(reader)
        x = len(graph.adjacency_list) - 1

        while x > -1:
            y = len(graph.adjacency_list) - 1
            while y > -1:
                distance = reader[x][y]
                if distance != '':
                    distance = float(distance)
                    # print(distance)
                    graph.add_undirected_edge(x, y, float(distance))
                    graph.add_directed_edge(x, y, float(distance))
                    graph.add_directed_edge(y, x, float(distance))
                y -= 1
            x -= 1

# Formats the package status based on current time and delivery time.
def delivery_update(time, truck):

    for package in truck.packages:
        if truck.start_time > time:
            package.status = 'At Hub.'
            package.delivery_time = ''
        elif package.delivery_time > time:
            package.status = 'En Route.'
            package.delivery_time = ''
        else:
            package.status = 'Delivered:'



PackageTable = PackageHashTable.PackageHashTable()
load_package_data('CSV/Package_File.csv')
graph_truck_one = Graph.Graph()
graph_truck_two = Graph.Graph()
graph_truck_three = Graph.Graph()
vertices = []
add_vertex(graph_truck_one)
add_edge(graph_truck_one)
add_vertex(graph_truck_two)
add_edge(graph_truck_two)
add_vertex(graph_truck_three)
add_edge(graph_truck_three)
dijkstra_shortest_path(graph_truck_one, truck_one)
dijkstra_shortest_path(graph_truck_two, truck_two)
dijkstra_shortest_path(graph_truck_three, truck_three)
total_miles = truck_one.mileage + truck_two.mileage + truck_three.mileage


# Creates Main class.
# Creates the Command Line Interface (CLI).
class Main:
    # CLI for the application.
    # A while loop loops the interfece so if the wrong input is entered, the CLI will restart.
    while True:
        print('Welcome to WGUPS Delivery Application')
        print('The total truck mileage for the current route is:')
        # Prints the total mileage accumulated by all three trucks.
        print(str(format(total_miles, ".2f")) + ' miles')
        print('')
        print('This application uses several keywords to bring results to the user. Keywords include:')
        print('EXIT - Closes the application.')
        print('ALL - Displays package information for all packages, based on the time entered.')
        print(
            'SEARCH - Displays package information for a specific package, based on the package ID entered, and time entered.')
        print('Please note: keywords are case sensitive')
        print('')
        # Takes user input, which will be one of the three commands: EXIT, ALL, or SEARCH.
        user_text = input('Please enter a keyword specified above. ')
        # Checks if user enters 'EXit' and closed the application if so.
        if user_text == 'EXIT':
            exit()
        # Checks if user enters 'ALL' and proceeds to ask for a time.
        elif user_text == 'ALL':
            try:
                # Takes the user's time input and runs it through the delivery update function.
                user_time = input('Please enter a time in the following format: HH:MM:SS. ')
                (hours, minutes, seconds) = user_time.split(':')
                search_time = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))
                delivery_update(search_time, truck_one)
                delivery_update(search_time, truck_two)
                delivery_update(search_time, truck_three)

            except ValueError:
                print('Please enter a valid time format.')
                print('Restarting Application...')
                time.sleep(3)
                continue

            try:
                # A loop that prints all stores package information.
                for ID in range(1, 40 + 1):
                    package = PackageTable.search(ID)
                    print(str(package.ID) + ', ' + package.address + ', ' + package.city + ', ' + str(package.zip_code) + ', '
                          + str(package.weight) + ', Delivery Deadline: ' + str(package.deadline_time)
                          + ', Delivery Status: ' + package.status + ' ' + str(package.delivery_time) )
                break

            except ValueError:
                print('Restarting Application...')
                time.sleep(3)
                continue
        # Checks if user enters 'SEARCH' and proceeds to ask for a time.
        elif user_text == 'SEARCH':
            try:
                user_time = input('Please enter a time in the following format: HH:MM:SS. ')
                (hours, minutes, seconds) = user_time.split(':')
                search_time = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))
                delivery_update(search_time, truck_one)
                delivery_update(search_time, truck_two)
                delivery_update(search_time, truck_three)

            except ValueError:
                print('Please enter a valid time format.')
                print('Restarting Application...')
                time.sleep(3)
                continue

            try:
                # Searches for the user's entered package ID and retruns the package info for that package,
                user_ID = input('Please enter a package ID. ')
                package = PackageTable.search(int(user_ID))
                print(str(package))
                break

            except ValueError:
                print('Please enter a package ID value in the range of 1 - 40')
                print('Restarting Application...')
                time.sleep(3)
                continue
