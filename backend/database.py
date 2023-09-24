from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)

class Note(Base):
    __tablename__ = 'notes'
    note_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    content = Column(String)
    parent_id = Column(Integer, ForeignKey('notes.note_id'))

# Create SQLite database and tables
engine = create_engine('sqlite:///./test.db')
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_or_create_user(session, email, name):
    user = session.query(User).filter_by(email=email).first()
    if not user:
        user = User(email=email, name=name)
        session.add(user)
        session.commit()
    return user
