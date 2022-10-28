import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# User Table
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastnamename = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    comment_relationship = relationship("comment")
    post_relationship = relationship("post")
    Follower_relationship = relationship("UserFollower", backref= "user")

# User Comments Table
class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

# User Post Table    
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id')) 
    comment_relationship = relationship("comment")
    media_relationship = relationship("media")

# User Media Table
class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum, nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id')) 

# User User-Follower Table
class UserFollower(Base):
    __tablename__ = 'userfollower'
    id = Column(Integer, primary_key=True)
    followerToUser= Column(Integer, ForeignKey('user.id'))
    userToFollower= Column(Integer, ForeignKey('follower.id')) 

# User Follower Table
class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id= Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id')) 
    
## Render Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Render Done, check Diagram.png")
except Exception as err:
    print("There was a problem rendering the diagram")
    raise err