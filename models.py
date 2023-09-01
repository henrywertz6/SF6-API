from sqlmodel import SQLModel, Field
from typing import Optional
class Move(SQLModel, table=True):
    character: str
    id: Optional[int] = Field(primary_key=True)
    name: str
    type: str
    startup: Optional[int] = None
    active: Optional[int] = None
    recovery: Optional[int] = None
    onHit: Optional[int] = None
    onBlock: Optional[int] = None
    cancel: str
    damage: Optional[int] = None
    comboScaling: str
    dgHitIncrease: Optional[int] = None
    dgBlockDecrease: Optional[int] = None
    dgPunishDecrease: Optional[int] = None
    superArtIncrease: Optional[int] = None
    hitboxProperty: str
    extraInfo: str

class Character(SQLModel, table=True):
    name: str = Field(primary_key=True)
    vitality: int
    height: str
    weight: str