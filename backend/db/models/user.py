from datetime import datetime, timezone
from sqlalchemy import Column, Enum, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship

from backend.db.base_class import Base

class UserRole(Base):
    DOG_WALKER = "walker"
    DOG_OWNER = "owner"
    ADMIN = "admin"

# TODO: phonenumbers + schema validation (Pydantic)
class User(Base):
    __tablename__ = "users"


    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.DOG_OWNER, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    dog_owner_profile = relationship("DogOwnerProfile", back_populates="user", uselist=False)
    dog_walker_profile = relationship("DogWalkerProfile", back_populates="user", uselist=False)

# class DogOwnerProfile(Base):
#     __tablename__ = "owner_profile"
#
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#
#     user = relationship("User", back_populates="owner_profile")
#     dogs = relationship("Dog", back_populates="owner")
#
# class Dog(Base):
#     __tablename__ = "dogs"
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     breed = Column(String, nullable=True)
#     age = Column(Integer, nullable=True)
#     temperament = Column(String, nullable=True)
#     medical_history = Column(Text, nullable=True)
#     owner_id = Column(Integer, ForeignKey("dog_owner_profiles.id"), nullable=False)
#
#     owner = relationship("DogOwnerProfile", back_populates="dogs")
#
# class DogWalkerProfile(Base):
#     __tablename__ = "walker_profiles"
#
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     bio = Column(Text, nullable=True)
#     availability = Column(Text, nullable=True)
#
#     user = relationship("User", back_populates="walker_profiles")
#     walks = relationship("DogWalk", back_populates="walker")
#
# class Booking(Base):
#     __tablename__ = "bookings"
#
#     id = Column(Integer, primary_key=True)
#     dog_id = Column(Integer, ForeignKey("dogs.id"), nullable=False)
#     walker_id = Column(Integer, ForeignKey("dog_walker_profiles.id"), nullable=False)
#     start_time = Column(DateTime, nullable=False)
#     end_time = Column(DateTime, nullable=False)
#     status = Column(String, default="pending")
#     payment_status = Column(String, default="unpaid")
#
#     dog = relationship("Dog")
#     walker = relationship("DogWalkerProfile")
#     gps_tracks = relationship("GPSTrack", back_populates="booking")