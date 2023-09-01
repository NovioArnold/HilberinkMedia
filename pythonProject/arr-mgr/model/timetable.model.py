from typing import List , Optional
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class TimeTable(Base):
    __tablename__ = "timetable"
    id  = Column(Integer, primary_key=True, autoincrement=True)
    session_name  = Column(String, nullable=False)
    session_date  = Column(DateTime, nullable=False)
    session_is_active = Column(Boolean, nullable=False)
    consists : Mapped[int] = mapped_column(Integer, ForeignKey("consist.id"), nullable=False)
    consist = relationship("Consist", back_populates="timetable", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"Timetable {self.session_name} on {self.session_date}"


class Consist(Base):
    __tablename__ = "consist"
    id = Column(Integer, primary_key=True, autoincrement=True)
    consist_name = Column(String, nullable=False)
    consist_is_active = Column(Boolean, nullable=False, default=False)
    engineer_id = Column(Integer, ForeignKey("crew.id"), nullable=True, default=None)
    conductor_id = Column(Integer, ForeignKey("crew.id"), nullable=True, default=None)
    engine_id: Mapped[List[int]] = mapped_column(Integer, ForeignKey("engine.id"), nullable=True, default=None)
    car_id: Mapped[List[int]] = mapped_column(Integer, ForeignKey("car.id"), nullable=True, default=None)
    engine: Mapped[List[int]] = relationship("Engine", back_populates="consist")
    car: Mapped[List[int]] = relationship("Car", back_populates="consist")

    def __repr__(self) -> str:
        return f"Consist {self.consist_name}"


class Crew(Base):
    __tablename__ = "crew"
    id = Column(Integer, primary_key=True, autoincrement=True)
    crew_name = Column(String, nullable=False)
    crew_roles: Mapped[int] = mapped_column(Integer, ForeignKey("crew_role.id"), nullable=False)
    is_staff = Column(Boolean, nullable=False, default=False)
    is_active = Column(Boolean, nullable=False, default=False)
    is_assigned = Column(Boolean, nullable=False, default=False)
    is_ready = Column(Boolean, nullable=False, default=False)
    consist = relationship("Consist", back_populates="crew")
    crew_role: Mapped[List[int]] = relationship("CrewRole", back_populates="crew")

    def __repr__(self) -> str:
        return f"Crew {self.crew_name} and has roles {self.crew_roles}"


class CrewRole(Base):
    __tablename__ = "crew_role"
    id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String, nullable=False)
    role_description = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"Crew role {self.role_name}"


class Engine(Base):
    __tablename__ = "engine"
    id = Column(Integer, primary_key=True, autoincrement=True)
    railroad_company = Column(String, nullable=False)
    road_number_prefix = Column(String, nullable=False)
    road_number = Column(Integer, nullable=False)
    is_assigned_to_consist = Column(Boolean, nullable=False, default=False)
    location_id = Column(Integer, ForeignKey('location.id'), nullable=True, default=None)
    type = Column(String, nullable=False)
    name = Column(String, nullable=False)
    fuel_type = Column(String, nullable=False)
    wheel_configuration = Column(String, nullable=False)
    is_assigned_to_crew = Column(Boolean, nullable=False, default=False)
    has_tender = Column(Boolean, nullable=False, default=False)
    last_time_serviced = Column(DateTime, nullable=True, default=None)
    consist = relationship("Consist", back_populates="engine")
    location = relationship("Location", back_populates="engine")

    def __repr__(self) -> str:
        if self.consist is False:
            return f"Engine {self.name} is available at {self.location}"
        else:
            return f"Engine {self.name} is assigned to consist {self.consist}"


class Car(Base):
    __tablename__ = "car"
    id = Column(Integer, primary_key=True, autoincrement=True)
    railroad_company = Column(String, nullable=False)
    road_number_prefix = Column(String, nullable=False)
    road_number = Column(Integer, nullable=False)
    is_assigned_to_consist = Column(Boolean, nullable=False, default=False)
    location_id = Column(Integer, ForeignKey('location.id'), nullable=True, default=None)
    type = Column(String, nullable=False)
    is_loaded = Column(Boolean, nullable=False, default=False)
    cargo_name = Column(String, nullable=False, default='Empty')
    cargo_quantity = Column(Integer, nullable=False, default=0)
    can_be_loaded_with: Mapped[List[int]] = mapped_column(Integer, ForeignKey("product.id"), nullable=True, default=None)
    destination = Column(String, nullable=False, default='None')
    consist = relationship("Consist", back_populates="car")
    location = relationship("Location", back_populates="car")
    product: Mapped[List[int]] = relationship("Product", back_populates="car")

    def __repr__(self) -> str:
        if self.consist is False:
            return f"Car {self.type} {self.road_number_prefix}{self.road_number} is currently at {self.location}"
        else:
            return f"Car {self.type} is assigned to consist {self.consist}"


class Location(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name_location = Column(String, nullable=False)
    industry_id: Mapped[int] = mapped_column(Integer, ForeignKey("industry.id"), nullable=True, default=None)
    yard_id: Mapped[int] = mapped_column(Integer, ForeignKey("yard.id"), nullable=True, default=None)
    description = Column(String, nullable=False)
    track_plan = Column(String, nullable=False)
    engine = relationship("Engine", back_populates="location")
    car = relationship("Car", back_populates="location")
    industry: Mapped[List[int]] = relationship("Industry", back_populates="location")
    yard: Mapped[List[int]] = relationship("Yard", back_populates="location")

    def __repr__(self) -> str:
        return f"Location {self.name_location} is {self.description}"


class Industry(Base):
    _tablename__ = "industry"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name_industry = Column(String, nullable=False)
    location_id = Column(Integer, ForeignKey('location.id'), nullable=False)
    input_1 = Column(String, nullable=False)
    in_stock_input_1 = Column(Integer, nullable=False, default=0)
    max_hold_input_1 = Column(Integer, nullable=False, default=0)
    input_2 = Column(String, nullable=True, default=None)
    in_stock_input_2 = Column(Integer, nullable=True, default=None)
    max_hold_input_2 = Column(Integer, nullable=True, default=None)
    input_3 = Column(String, nullable=True, default=None)
    in_stock_input_3 = Column(Integer, nullable=True, default=None)
    max_hold_input_3 = Column(Integer, nullable=True, default=None)
    output_1 = Column(String, nullable=False)
    in_stock_output_1 = Column(Integer, nullable=False, default=0)
    max_hold_output_1 = Column(Integer, nullable=False, default=0)
    output_2 = Column(String, nullable=True, default=None)
    in_stock_output_2 = Column(Integer, nullable=True, default=None)
    max_hold_output_2 = Column(Integer, nullable=True, default=None)
    location = relationship("Location", back_populates="industry")


class Yard(Base):
    __tablename__ = "yard"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name_yard = Column(String, nullable=False)
    location_id = Column(Integer, ForeignKey('location.id'), nullable=False)
    track_id: Mapped[int] = mapped_column(Integer, ForeignKey("track.id"), nullable=False)
    type_of_yard = Column(String, nullable=False)
    number_of_tracks = Column(Integer, nullable=False, default=0)
    number_of_tracks_occupied = Column(Integer, nullable=False, default=0)
    number_of_engines = Column(Integer, nullable=False, default=0)
    number_of_cars = Column(Integer, nullable=False, default=0)
    location = relationship("Location", back_populates="yard")
    track = relationship("Track", back_populates="yard")

    
class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name_product = Column(String, nullable=False)
    max_quantity = Column(Integer, nullable=False, default=0)
    car = relationship("Car", back_populates="product")








