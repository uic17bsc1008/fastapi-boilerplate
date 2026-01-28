from sqlalchemy import DateTime, func, Column
from database import Base

class Model(Base):

    __abstract__ = True

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())