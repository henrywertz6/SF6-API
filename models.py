from database import Base
from sqlalchemy import Column, Integer, String
class Character(Base):
    __tablename__ = "moves"

    id = Column(Integer, primary_key=True, nullable=False)
    
    name = Column(String, nullable=False)
    startup = Column(Integer)
    active = Column(Integer)
    recovery = Column(Integer)
    onHit = Column(String)
    onBlock = Column(Integer)
    cancel = Column(String)
    damage = Column(Integer)
    comboScaling = Column(String)
    dgHitIncrease = Column(Integer)
    dgBlockDecrease = Column(Integer)
    dgPunishDecrease = Column(Integer)
    superArtIncrease = Column(Integer)
    hitboxProperty = Column(String)
    extraInfo = Column(String)

