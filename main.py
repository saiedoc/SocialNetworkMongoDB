import SocialNetwork as SN
import User as us
import Post as po
import Comment as ct
import Friends as fr


socialNetwork = SN.SocialNetwork('localhost',27017)

users = [us.User('user1',1),us.User('user2',2),us.User('user3',3)]
posts = [po.Post(1,1,'title1','text1'),po.Post(2,1,'title2','text2'),po.Post(3,2,'title3','text3')]
comments = [ct.Comment(1,1,1,'ctext1'),ct.Comment(2,1,2,'ctext2'),ct.Comment(3,1,3,'ctext3')]
friends = [fr.Friends(1,1,2),fr.Friends(1,1,3)]

for user in users:
    socialNetwork.addUser(user)

for post in posts:
    socialNetwork.addPost(post)

for comment in comments:
    socialNetwork.addComment(comment)

for friendship in friends:
   socialNetwork.addFriendship(friendship)


print(socialNetwork.findUserByName("user1"))
print(socialNetwork.findPostByTitle("title1"))
print(socialNetwork.findCommentBySubString("ct"))