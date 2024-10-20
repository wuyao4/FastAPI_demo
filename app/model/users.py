from sqlalchemy import Column, Integer, String, DateTime
from app.model.database import Base


class UserModel(Base):
    __tablename__ = "tb_user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, comment="姓名")
    code = Column(String, index=True, comment="密钥")
    prompt = Column(String, comment="提示词")
    creat_date = Column(DateTime, comment="创建时间")


class ChatModel(Base):
    __tablename__ = "tb_chat"
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, comment="消息")
    answer = Column(String, comment="回答")
    creator = Column(Integer, comment="创建人")
    creat_date = Column(DateTime, comment="创建时间")
