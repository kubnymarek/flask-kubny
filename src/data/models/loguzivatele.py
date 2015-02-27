from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DateTime

from ..database import db
from ..mixins import CRUDModel

class LogUser(CRUDModel):
    __tablename__ = 'loguser'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True )
    Brand = Column(String, nullable=False, index=False)
    Time = Column(String, nullable=False, index=True)
    Size = Column(String, nullable=False, index=True)
    Type = Column(String, nullable=False, index=True)


    # Use custom constructor
    # pylint: disable=W0231
    def __init__(self, **kwargs):
        self.datum_insertu = datetime.utcnow()
        for k, v in kwargs.iteritems():
            setattr(self, k, v)
    @staticmethod
    def find_by_Brand(Brand):
        return db.session.query(LogUser).filter_by(prijmeni = Brand).all()

