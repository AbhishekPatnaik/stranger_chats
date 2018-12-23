class Room:
    """
    class Room:  Defines the properties of a Room like room_name, client_id in the room, and 
        also the count of the clients in the room.
    """
    def __init__(self,name,id):
        self.room_name = name
        self.client_id = []

    def update_clientId(self,id):
        self.client_id.append(id)

        
    
