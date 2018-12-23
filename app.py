from flask import Flask, render_template, request
from flask_socketio import SocketIO,join_room,leave_room,rooms

from room import Room
from helper import get_free_rooms, allocate_rooms, roomname_already_exists, shuffle_except_this_roomname,create_rooms

import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

roomChat = []
count = []

    

@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    """
    Prints msg that the message is received,to be removed during production level code

    """
    print('message was received!!!')


@socketio.on('join')
def handle_my_custom_event(json, methods=['GET', 'POST']):    
        """

        Purpose: receives the users addres and handles on room segregation
        variable types:
        roomNames: Room name in which the person has to allocated
        count: Counts the number of person in a room if is greater than 2, then next room 

        """

        global roomChat
        global count
        id  = request.sid    
        print(id)

        # Assign Rooms to new ids
        if id not in count:
            count.append(id)
            roomName = "Room" + str(random.randint(0,3))
            print(roomname_already_exists(roomName,roomChat))


            if roomname_already_exists(roomName,roomChat) == True:
                    roomName = shuffle_except_this_roomname(roomName)
                    room = create_rooms(roomName,id)
            else:
                    room = create_rooms(roomName,id)        


            # if room not in roomChat(global variable to store chatRooms) then add it to roomChat and 
            # then check for freerooms i.e when no. of users < 2, select one random room from freeRooms
            if room not in roomChat:
                roomChat.append(room)
                freeRooms = get_free_rooms(roomChat)
                select_room = random.choice(freeRooms) 
                 
                select_room.update_clientId(id)  
                select_room = select_room.room_name    
                print(select_room,id)

        
        else:
            select_room = allocate_rooms(roomChat,id)
            print(select_room,id)


            
        print('received my event: ' + str(json))
        join_room(select_room)
        print(select_room)
        socketio.emit('my response', json, callback=messageReceived,room=select_room)








if __name__ == '__main__':
    socketio.run(app, debug=True)


