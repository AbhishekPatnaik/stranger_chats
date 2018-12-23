from room import Room
import random

def create_rooms(roomName,id):
    room = Room(roomName,id)
    return room

def allocate_rooms(roomNames,id):
    select_room = ""
    for i in roomNames:
                for j in i.client_id:
                    if j == id:
                        print(i)
                        select_room = i.room_name
    return select_room  


def get_free_rooms(roomNames):
    freeRooms = []
    for room in roomNames:
        
        if len(room.client_id) < 2:
            freeRooms.append(room)

    return freeRooms        

def roomname_already_exists(roomName,roomChat):
    for rooms in roomChat:
        if rooms.room_name == roomName:
            return True
    return False            


def shuffle_except_this_roomname(roomName):
    newName = "Room" + str(random.randint(0,3))
    if newName == roomName:
        shuffle_except_this_roomname(roomName)
    else:
        return newName    
