from .tables import Base
from sqlalchemy import (Column, Integer, String, Text)


class ALTNAMES(Base):
    __tablename__ = 'ALTNAMES'
    OLDCODE = Column(String(19), index=True)
    NEWCODE = Column(String(19), index=True, primary_key=True)
    LEVEL = Column(String(1))


class DOMA(Base):
    __tablename__ = 'DOMA'
    NAME = Column(String(40))
    KORP = Column(String(10))
    SOCR = Column(String(10))
    CODE = Column(String(19), primary_key=True)
    INDEX = Column(String(6))
    GNINMB = Column(String(4))
    UNO = Column(String(4))
    OCATD = Column(String(11))
    flatHouseList = Column(Text)


class EisHouse(Base):
    __tablename__ = 'eisHouse'
    ID_HOUSE = Column(Integer, primary_key=True)
    HOUSE = Column(String(10))
    KORPUS = Column(String(10))
    ID_PREFIX = Column(Integer)


class FLAT(Base):
    __tablename__ = 'FLAT'
    NAME = Column(String(20))
    CODE = Column(String(23), primary_key=True)
    INDEX = Column(String(6))
    GNINMB = Column(String(4))
    UNO = Column(String(4))
    NP = Column(String(4))


class InfisAREA(Base):
    __tablename__ = 'infisAREA'
    CODE = Column(String(3), primary_key=True)
    NAME = Column(String(20))
    GROUP = Column(String(3))
    CODEO = Column(String(2))
    NU = Column(Integer)
    KLADR = Column(String(13))


class InfisREGION(Base):
    __tablename__ = 'infisREGION'
    CODE = Column(String(5), primary_key=True)
    AREA = Column(String(3))
    NAME = Column(String(20))
    KLADR = Column(String(13))
    kladrPrefix = Column(String(3))


class KLADR(Base):
    __tablename__ = 'KLADR'
    NAME = Column(String(40))
    SOCR = Column(String(10))
    CODE = Column(String(13), primary_key=True)
    INDEX = Column(String(6))
    GNINMB = Column(String(4))
    UNO = Column(String(4))
    OCATD = Column(String(11))
    STATUS = Column(String(1))
    parent = Column(String(13))
    infis = Column(String(5))
    prefix = Column(String(2))
    id = Column(Integer)
