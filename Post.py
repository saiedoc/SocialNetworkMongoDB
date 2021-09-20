

class Post:

    __postID = 0
    __userID = 0
    __postTitle = ''
    __postText = ''


    def __init__(self,postID,userID,postTitle,postText):
        self.__postID = postID
        self.__userID = userID
        self.__postTitle = postTitle
        self.__postText = postText


    def get_postID(self):
        return self.__postID

    def get_userID(self):
        return self.__userID

    def get_postTitle(self):
        return self.__postTitle

    def get_postText(self):
        return self.__postText

    def set_postID(self,postID):
        self.__postID = postID

    def set_userID(self,userID):
        self.__userID = userID

    def set_postTitle(self,postTitle):
        self.__postTitle = postTitle

    def set_postText(self,postText):
        self.__postText = postText

