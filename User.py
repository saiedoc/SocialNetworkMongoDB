class User:

    __userID = 0
    __userName = ''

    def __init__(self,userName,userID):
        self.__userName = userName
        self.__userID = userID


    def get_userName(self):
        return self.__userName

    def get_userID(self):
        return self.__userID

    def set_userName(self,userName):
        self.__userName = userName

    def set_userID(self,userID):
        self.__userID = userID
