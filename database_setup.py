'''
This is the Configuration code, as taught in Full Stack Foundations.
This helps to get database_setup properly setup.
'''


from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

''' This is a class definition for a generic user that might login to use
the application.
'''


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

'''
This is a class definition for a generic restaurant we might use
in our application.
'''


class Restaurant(Base):

    # Restaurant table information.

    __tablename__ = 'restaurant'

    # Restaurant mapper code.

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    # Property decorator.

    @property
    def serialize(self):

        # Return object data in easily serializeable format.

        return {
            'name': self.name,
            'id': self.id,
        }

'''
This is a class definition for a generic Menu Item we might use
in our application.
'''


class MenuItem(Base):

    # Menu item table information.

    __tablename__ = 'menu_item'

    # Menu item mapper code.

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    # Property decorator.

    @property
    def serialize(self):

        # Return object data in easily serializeable format.

        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }

'''
This is the ending Configuration code, as taught in Full Stack Foundations.
This helps to get database_setup properly setup and it goes at the end of
the file.
'''


engine = create_engine('sqlite:///restaurantmenuwithusers.db')

Base.metadata.create_all(engine)
