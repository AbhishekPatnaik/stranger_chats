"""
if id not in count:
            count.append(id)
            roomName = "Room" + str(random.randint(0,3))
            print(roomname_already_exists(roomName,roomChat))
            

            if roomname_already_exists(roomName,roomChat) == True:
                    roomName = shuffle_except_this_roomname(roomName)
                    room = create_rooms(roomName,id)
            else:
                    room = create_rooms(roomName,id)        
    
    This was added becasuse, every time we created a room the client_id used to reset its value to 
    a empty list. So in order to prevent that from happening we are first checking that if the random roomname
    is equal to the room already present, if it does then we reshuffle and get the room that is not equal to that 
    room. Or else simply pass it into the room that was created.

"""