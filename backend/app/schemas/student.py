from datetime import datetime
from sqlalchemy import (Integer, String,DateTime, func)

from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Student(Base):
    __tablename__ = "students"

    id : Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key= True,nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    email: Mapped[str] = mapped_column(Integer, nullable=False, unique=True)
    mobile_no: Mapped[int] = mapped_column(String(150), nullable=False, unique=True)
    department: Mapped[str] = mapped_column(String(150), nullable=False)
    roll: Mapped[int] = mapped_column(Integer, nullable=False,unique=True)
    photo: Mapped[str] = mapped_column(String(150), nullable=False)  
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now()) 
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now()) 

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}')>"