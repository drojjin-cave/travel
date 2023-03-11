from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, orm, BLOB
from .db_session import SqlAlchemyBase

import locale
locale.setlocale(
    category=locale.LC_ALL,
    locale="Russian"
)



class News(SqlAlchemyBase):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True, autoincrement=True)

    title = Column(String(100), nullable=True, index=True)
    content = Column(String(), nullable=True)
    date = Column(DateTime, default=datetime.now)
    img = Column(String(), default=None)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = orm.relationship('User')

    my_format_data = "%d %B %Y"
    time_format = '%H:%M'





    #def __repr__(self):
        #return f"<news {self.id}>"


'''
class Profiles(SqlAlchemyBase):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    old = db.Column(db.Integer)
    city = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"<profiles {self.id}>
''' #  TODO: для дальнейшего создания базы профилей пользователей
