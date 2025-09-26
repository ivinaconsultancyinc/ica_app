from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    policies = relationship("Policy", back_populates="client")

class Policy(Base):
    __tablename__ = "policies"
    id = Column(Integer, primary_key=True, index=True)
    policy_number = Column(String, unique=True, nullable=False)
    client_id = Column(Integer, ForeignKey("clients.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String)
    client = relationship("Client", back_populates="policies")
    product = relationship("Product", back_populates="policies")
    premiums = relationship("Premium", back_populates="policy")
    claims = relationship("Claim", back_populates="policy")

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    policies = relationship("Policy", back_populates="product")

class Premium(Base):
    __tablename__ = "premiums"
    id = Column(Integer, primary_key=True, index=True)
    policy_id = Column(Integer, ForeignKey("policies.id"))
    amount = Column(Float, nullable=False)
    due_date = Column(Date)
    paid_date = Column(Date)
    policy = relationship("Policy", back_populates="premiums")

class Commission(Base):
    __tablename__ = "commissions"
    id = Column(Integer, primary_key=True, index=True)
    agent_id = Column(Integer, ForeignKey("agents.id"))
    amount = Column(Float, nullable=False)
    date = Column(Date)
    agent = relationship("Agent", back_populates="commissions")

class Claim(Base):
    __tablename__ = "claims"
    id = Column(Integer, primary_key=True, index=True)
    policy_id = Column(Integer, ForeignKey("policies.id"))
    claim_number = Column(String, unique=True, nullable=False)
    amount = Column(Float)
    status = Column(String)
    filed_date = Column(Date)
    settled_date = Column(Date)
    policy = relationship("Policy", back_populates="claims")

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String)

class Agent(Base):
    __tablename__ = "agents"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String)
    commissions = relationship("Commission", back_populates="agent")

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    file_path = Column(String)
    uploaded_date = Column(DateTime)

class Audit(Base):
    __tablename__ = "audit"
    id = Column(Integer, primary_key=True, index=True)
    action = Column(String, nullable=False)
    user = Column(String)
    timestamp = Column(DateTime)
    details = Column(Text)

class Ledger(Base):
    __tablename__ = "ledger"
    id = Column(Integer, primary_key=True, index=True)
    entry_date = Column(Date)
    description = Column(Text)
    amount = Column(Float)
    entry_type = Column(String)  # e.g., debit/credit

class Reinsurance(Base):
    __tablename__ = "reinsurance"
    id = Column(Integer, primary_key=True, index=True)
    policy_id = Column(Integer, ForeignKey("policies.id"))
    reinsurer = Column(String)
    coverage_amount = Column(Float)
    start_date = Column(Date)
    end_date = Column(Date)

