from sqlalchemy import Column , String , Integer , TIMESTAMP , func , ForeignKey , Table
from sqlalchemy.orm import DeclarativeBase , relationship
class base (DeclarativeBase):
    pass

post_tags_connection = Table(
    "post_tags_connection",
    base.metadata,
    Column("post_id", ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True))

class tags(base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    posts = relationship("posts", secondary=post_tags_connection, back_populates="tags")

class posts(base):
    __tablename__ = "posts"
    
    id=Column(Integer,primary_key=True)
    topic=Column(String,nullable=True)
    content=Column(String,nullable=True)
    tags = relationship("tags", secondary=post_tags_connection, back_populates="posts")
    timecat=Column(  TIMESTAMP(timezone=True),
    server_default=func.now(),
    nullable=False)

class user(base):
    __tablename__ = "user"

    id=Column(Integer,nullable=True,primary_key=True)
    email = Column(String,nullable=True,unique=True)
    password = Column(String,nullable=True)