

class Friends:

    __friendshipID = 0
    __user1ID = 0
    __user2ID = 0

    def __init__(self,friendshipID,user1ID,user2ID):
        self.__friendshipID = friendshipID
        self.__user1ID = user1ID
        self.__user2ID = user2ID

    def getFrienshipID(self):
        return self.__friendshipID

    def getUser1ID(self):
        return self.__user1ID

    def getUser2ID(self):
        return self.__user2ID

    def setFriendshipID(self,friendshipID):
        self.__friendshipID = friendshipID

    def setUser1ID(self,user1ID):
        self.__user1ID = user1ID

    def setUser2ID(self,user2ID):
        self.__user1ID = user2ID
