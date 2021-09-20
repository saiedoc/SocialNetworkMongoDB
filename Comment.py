

class Comment:

    __commentID = 0
    __postID = 0
    __userID = 0
    __commentText = ''


    def __init__(self,commentID,postID,userID,commentText):
        self.__commentID = commentID
        self.__postID = postID
        self.__userID = userID
        self.__commentText = commentText


    def get_commentID(self):
        return self.__commentID

    def get_postID(self):
        return self.__postID

    def get_userID(self):
        return self.__userID

    def get_commentText(self):
        return self.__commentText

    def set_postID(self,postID):
        self.__postID = postID

    def set_userID(self,userID):
        self.__userID = userID

    def set_commentText(self,commentText):
        self.__commentText = commentText

