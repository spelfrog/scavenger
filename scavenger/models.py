import enum

from sqlalchemy import Column, Integer, String, ForeignKey, Text, Enum, MetaData
from sqlalchemy.orm import  relationship

from scavenger.db import Base


class ChatType(enum.Enum):
    private = 'private'
    group = 'group'
    supergroup = 'supergroup'
    channel = 'channel'


class Chat(Base):
    __tablename__ = 'chat'

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(Integer, unique=True)
    admin = Column(String(128), default=False)
    chat_type = Column(Enum(ChatType),)

    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    username = Column(String(128), nullable=True)
    language_code = Column(String(128), nullable=True)


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat = Column(ForeignKey(Chat.id))
    text = Column(Text, nullable=True)
    caption = Column(Text, nullable=True)
    media = Column(String(128))


class Question(Base):
    __tablename__ = 'question'

    id = Column(Integer, primary_key=True, autoincrement=True)
    answer = Column(String(128))
    next_question_id = Column(ForeignKey('question.id'))
    body = Column(Text, nullable=False)
    media = Column(String(128))

    next_question = relationship("question", back_populates="previous_question")
    hints = relationship("hint", back_populates="question")


class Hint(Base):
    __tablename__ = 'hint'

    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(ForeignKey(Question.id))
    body = Column(Text)
    media = Column(String(128), nullable=True)

    question = relationship(Question, back_populates="hints")

