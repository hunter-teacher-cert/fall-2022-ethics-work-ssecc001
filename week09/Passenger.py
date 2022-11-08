
# we are not sure how to implement this to the exisiting shell. But it will take the passengers that did not buy seats and seat them in groups of booking.
#Passenger.txt shows how many people didnt not purchase tickets with seat selection. This will
#tell us how big the group is and how many childern are in the group. ex. A,3,1 means group of 3 and 1 child
# this algorthim will seat groups with childern first.

class Passenger:
  def individual(self, name, isChild):
    self.name = name
    self.isChild = isChild

#pull passenger groups from Passengers.txt
#treat the txt file as a csv file
import csv

## getPassengerList() returns Passenger.txt as a 2d list
def getPassengerList():
  passengerFile = open('Passengers.txt')
  passengerReader = csv.reader(passengerFile)
  passengerData = list(passengerReader)

  #convert list data from strings to numbers
  for i in passengerData:
    i[1] = int(i[1])
    i[2] = int(i[2])

  return passengerData

# Group List - Takes raw data and parses a list of individual groups into lists of individuals in groups
def makeGroupList(passengerList):
  groupList = []
  for group in passengerList:
    people = []
    child = group[2]
    adults = group[1] - group[2]
    n = 0 #passenger (n)umber for the group
    while child > 0:
      people.append(group[0]+str(n+1)+'m')
      child -= 1
      n += 1
      if adults > 0:
        people.append(group[0]+str(n+1)+'a')
        adults -= 1
        n += 1
    while adults > 0:
      people.append(group[0]+str(n+1)+'a')
      adults -= 1
      n += 1
    groupList.append(people)



#return isChild
def isChild():
  return isChild

#return name 
def name():
  return name
    
## maxGroup finds max group size in the list of passengers
def maxGroup(groupList):
  max = 0
  for group in groupList:
    if len(group) > max:
      max = len(group)
  return max

#loop down until max group size == 1

#Function to determine if there are any pairs left to be seated
#  hasGroup(List of Groups, Size of Group you are looking format
#  returns true if found, false if not found
def hasGroup(groupList, num):
  for group in groupList:
    if len(group) == num:
      return True
  return False

#would like to make an algorithm to split groups if there are not enough seats together. Groups would not be able to split up childern. If they would need to split up adults only.
