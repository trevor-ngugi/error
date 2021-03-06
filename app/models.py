from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from datetime import datetime
from sqlalchemy.sql import func
from . import db


@login_manager.user_loader
def load_user(user_id):
    """
    @login_manager.user_loader Passes in a user_id to this function
    Function queries the database and gets a user's id as a response
    """
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):

    __tablename__='users'

    #columns
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index =True)
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship("Pitch", backref="user", lazy = "dynamic")
    


    # passwords securing
    @property
    def password(self):
        raise AttributeError('You can not read the password Attribute')


    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'


# #pitches class
class Pitch(db.Model):
    """
    List of pitches in each category 
    """

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String())
    category = db.Column(db.String())
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    



    def save_pitch(self):
        """
        Save the pitches 
        """
        db.session.add(self)
        db.session.commit()

    # @classmethod
    # def clear_pitches(cls):
    #     Pitch.all_pitches.clear()

    # display pitches
    @classmethod
    def get_pitches(cls):
        pitches = Pitch.query.order_by(Pitch.posted).all()
        return pitches


#category model
# class PitchCategory(db.Model):

#     __tablename__ = 'categories'

#     # table columns
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255))
#     description = db.Column(db.String(255))

#     # save pitches
#     def save_category(self):
#         db.session.add(self)
#         db.session.commit()

#     @classmethod
#     def get_categories(cls):
#         categories = PitchCategory.query.all()
#         return categories


# # comments
# class Comments(db.Model):
#     """
#     User comment model for each pitch 
#     """

#     __tablename__ = 'comments'

#     # add columns
#     id = db.Column(db. Integer, primary_key=True)
#     opinion = db.Column(db.String(255))
#     time_posted = db.Column(db.DateTime, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
#     pitches_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))


#     def save_comment(self):
#         """
#         Save the Comments/comments per pitch
#         """
#         db.session.add(self)
#         db.session.commit()

#     @classmethod
#     def get_comments(self, id):
#         comment = Comments.query.order_by(Comments.time_posted.desc()).filter_by(pitches_id=id).all()
#         return comment



# #votes
# class Votes(db.Model):
#     """
#     class to model votes
#     """
#     __tablename__='votes'

#     id = db.Column(db. Integer, primary_key=True)
#     vote = db.Column(db.Integer)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
#     pitches_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))

#     def save_vote(self):
#         db.session.add(self)
#         db.session.commit()

#     @classmethod
#     def get_votes(cls,user_id,pitches_id):
#         votes = Votes.query.filter_by(user_id=user_id, pitches_id=pitches_id).all()
#         return votes

#     def __repr__(self):
#         return f'{self.vote}:{self.user_id}:{self.pitches_id}'


#class Pitch:
  #pitch objects
  # def __init__(self,id,author,title,date):
  #   self.id = id
  #   self.author = author
  #   self.title = title
  #   self.date = date


# class PitchCategory():

#   # id
#   # name
#   # description 



#   def save_category(self):
#     pass

#   @classmethod
#   def get_categories(cls):
#     pass

# #pitches class
# class Pitch():
#     """
#     List of pitches in each category 
#     """
#     id = id
#     content = content
#     category_id = category_id 
#     user_id = users_id
#     comment = comments
#     vote = votes

#     def save_pitch(self):
#       add(self)
#       commit()

#     @classmethod
#     def clear_pitches(cls):
#       Pitch.all_pitches.clear()
