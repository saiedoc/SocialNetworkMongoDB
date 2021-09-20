from pymongo import MongoClient
from bson.json_util import dumps

class SocialNetwork:

    __host = ''
    __port = 0
    __client = None
    __db_name = 'SocialNetwork'
    __db = None
    __currentCollection = None

    def __init__(self,host,port):
        self.__host = host
        self.__port = port
        self.__client = MongoClient(host,port)
        self.__db = self.__client[self.__db_name]


    def __setCurrentCollection(self,name):
        self.__currentCollection = self.__db[name]


    #function that adds a user to the database
    def addUser(self,user):
        self.__setCurrentCollection("user")
        self.__currentCollection.insert_one(user.__dict__)

    #function that adds a post to the database
    def addPost(self,post):
        self.__setCurrentCollection("post")
        self.__currentCollection.insert_one(post.__dict__)

    #function that add a comment to the database
    def addComment(self,comment):
        self.__setCurrentCollection("comment")
        self.__currentCollection.insert_one(comment.__dict__)

    #function that add a friendship to the database
    def addFriendship(self,friendship):
        self.__setCurrentCollection("friends")
        self.__currentCollection.insert_one(friendship.__dict__)


    #function that returns all the users in the social network
    def getAllUsers(self):
        self.__setCurrentCollection("user")
        users = self.__currentCollection.find()
        return dumps(users)

    #function that returns all the users in the social network
    def getAllPosts(self):
        self.__setCurrentCollection("post")
        posts = self.__currentCollection.find()
        return dumps(posts)

    #function that returns all the users in the social network
    def getAllComments(self):
        self.__setCurrentCollection("comment")
        comments = self.__currentCollection.find()
        return dumps(comments)

    #function that returns all the friendships in the social network
    def getAllFriendships(self):
        self.__setCurrentCollection("friends")
        friends = self.__currentCollection.find()
        return dumps(friends)

    #function that finds a user by name
    def findUserByName(self,username):
        self.__setCurrentCollection("user")
        user = self.__currentCollection.find({"_User__userName":username})
        return dumps(user)

    #function that finds a post by title
    def findPostByTitle(self,title):
        self.__setCurrentCollection("post")
        post = self.__currentCollection.find({"_Post__postTitle":title})
        return dumps(post)

    #function that finds a comment by a substring of it
    def findCommentBySubString(self,substring):
        self.__setCurrentCollection("comment")
        comment = self.__currentCollection.find({"_Comment__commentText":   {'$regex': f".*{substring}.*", '$options': 'i'}})
        return dumps(comment)





