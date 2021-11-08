from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Company(Base):
    id = Column(Integer,primary_key = True, index=True)
    company_ko = Column(String)
    company_en = Column(String)
    company_ja = Column(String)


class Tag(Base):
    id = Column(Integer,primary_key = True, index=True)
    tag_ko = Column(String)
    tag_en = Column(String)
    tag_ja = Column(String)
    company_id = Column(Integer, ForeignKey('company.id'))
    company = relationship("User",back_populates="jobs")