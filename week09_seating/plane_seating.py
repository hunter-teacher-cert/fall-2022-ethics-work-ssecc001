### our implementation is on the bottom of your file. We are not sure how to fully implement it.
import random


def create_plane(rows,cols):
    """
    returns a new plane of size rowsxcols
    A plane is represented by a list of lists. 
    This routine marks the empty window seats as "win" and other empties as "avail"
    """
    plane = []
    for r in range(rows):
        s = ["win"]+["avail"]*(cols-2)+["win"]
        plane.append(s)
    return plane

def get_number_economy_sold(economy_sold):
    """
    Input: a dicitonary containing the number of regular economy seats sold. 
           the keys are the names for the tickets and the values are how many
    ex:   {'Robinson':3, 'Lee':2 } // The Robinson family reserved 3 seats, the Lee family 2
    Returns: the total number of seats sold
    """
    sold = 0
    for v in economy_sold.values():
        sold = sold + v
    return sold


def get_avail_seats(plane,economy_sold):
    """
    Parameters: plane : a list of lists representing plaine
                economy_sold : a dictionary of the economy seats sold but not necessarily assigned
    Returns: the number of unsold seats
    Notes: this loops over the plane and counts the number of seats that are "avail" or "win" 
           and removes the number of economy_sold seats
    """
    avail = 0;
    for r in plane:
        for c in r:
            if c == "avail" or c == "win":
                avail = avail + 1
    avail = avail - get_number_economy_sold(economy_sold)
    return avail

def get_total_seats(plane):
    """
    Params: plane : a list of lists representing a plane
    Returns: The total number of seats in the plane
    """
    return len(plane)*len(plane[0])

def get_plane_string(plane):
    """
    Params: plane : a list of lists representing a plane
    Returns: a string suitable for printing. 
    """
    s = ""
    for r in plane:
        r = ["%14s"%x for x in r] # This is a list comprehension - an advanced Python feature
        s = s + " ".join(r)
        s = s + "\n"
    return s


def purchase_economy_plus(plane,economy_sold,name):
    """
    Params: plane - a list of lists representing a plane
            economy_sold - a dictionary representing the economy sold but not assigned
            name - the name of the person purchasing the seat
    """
    rows = len(plane)
    cols = len(plane[0])

    
    # total unassigned seats
    seats = get_avail_seats(plane,economy_sold)

    # exit if we have no more seats
    if seats < 1:
        return plane


    # 70% chance that the customer tries to purchase a window seat
    # it this by making a list of all the rows, randomizing it
    # and then trying each row to try to grab a seat

    
    if random.randrange(100) > 30:
        # make a list of all the rows using a list comprehension
        order = [x for x in range(rows)]

        # randomzie it
        random.shuffle(order)

        # go through the randomized list to see if there's an available seat
        # and if there is, assign it and return the new plane
        for row in order:
            if plane[row][0] == "win":
                plane[row][0] = name
                return plane
            elif plane[row][len(plane[0])-1] == "win":
                plane[row][len(plane[0])-1] = name
                return  plane

    # if no window was available, just keep trying a random seat until we find an
    # available one, then assign it and return the new plane
    found_seat = False
    while not(found_seat):
        r_row = random.randrange(0,rows)
        r_col = random.randrange(0,cols)
        if plane[r_row][r_col] == "win" or plane[r_row][r_col] == "avail":
            plane[r_row][r_col] = name
            found_seat = True
    return plane


# THIS WILL BE LEFT EMPTY FOR THE FIRST STAGE OF THE PROJECT
def seat_economy(plane,economy_sold,name):
    """
    This is mostly the same as the purchase_economy_plus routine but 
    just does the random assignment. 
    We use this when we're ready to assign the economy seats after most 
    of the economy plus seats are sold
 
    """
    rows = len(plane)
    cols = len(plane[0])

    found_seat = False
    while not(found_seat):
        r_row = random.randrange(0,rows)
        r_col = random.randrange(0,cols)
        if plane[r_row][r_col] == "win" or plane[r_row][r_col] == "avail":
            plane[r_row][r_col] = name
            found_seat = True
    return plane


def purchase_economy_block(plane,economy_sold,number,name):
    """
    Purchase regular economy seats. As long as there are sufficient seats
    available, store the name and number of seats purchased in the
    economy_sold dictionary and return the new dictionary
    """
    seats_avail = get_total_seats(plane)
    seats_avail = seats_avail - get_number_economy_sold(economy_sold)

    if seats_avail >= number:
        economy_sold[name]=number
    return economy_sold


def fill_plane(plane):
    """
    Params: plane - a list of lists representing a plane
    comments interspersed in the code
    """

    
    economy_sold={}
    total_seats = get_total_seats(plane)
    


    # these are for naming the pasengers and families by
    # appending a number to either "ep" for economy plus or "u" for unassigned economy seat
    ep_number=1
    u_number=1

    # MODIFY THIS
    # you will probably want to change parts of this
    # for example, when to stop purchases, the probabilities, maybe the size for the random
    # regular economy size

    max_family_size = 3
    while total_seats > 1:
        r = random.randrange(100)
        if r > 30:
            plane = purchase_economy_plus(plane,economy_sold,"ep-%d"%ep_number)
            ep_number = ep_number + 1
            total_seats = get_avail_seats(plane,economy_sold)
        else:
            economy_sold = purchase_economy_block(plane,economy_sold,1+random.randrange(max_family_size),"u-%d"%u_number)
            u_number = u_number + 1

        
    # once the plane reaches a certian seating capacity, assign
    # seats to the economy plus passengers
    # you will have to complete the seat_economy function
    # Alternatively you can rewrite this section
    for name in economy_sold.keys():
        for i in range(economy_sold[name]):
            plane = seat_economy(plane,economy_sold,name)


    return plane
    
    
    
def main():
    plane = create_plane(10,5)
    plane = fill_plane(plane)
    print(get_plane_string(plane))
if __name__=="__main__":
    main()
    
    
# partner Stacy Goldstein
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
