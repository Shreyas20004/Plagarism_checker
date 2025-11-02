# utils/db.py
import os
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

DB_FILE = "plagiarism.db"
engine = create_engine(f"sqlite:///{DB_FILE}", echo=False, connect_args={"check_same_thread": False})
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    docs = relationship("Document", back_populates="owner")
    reports = relationship("Report", back_populates="user")

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True)
    filename = Column(String)
    text = Column(Text)
    uploaded_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    owner = relationship("User", back_populates="docs")

class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    doc_id = Column(Integer, ForeignKey("documents.id"))
    report_path = Column(String)
    diff_path = Column(String, nullable=True)
    overall_score = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="reports")

def init_db():
    if not os.path.exists(DB_FILE):
        Base.metadata.create_all(bind=engine)

def get_session():
    return SessionLocal()

# Convenience helpers:
def get_or_create_user(username):
    session = get_session()
    user = session.query(User).filter_by(username=username).first()
    if not user:
        user = User(username=username)
        session.add(user)
        session.commit()
    session.close()
    return user

def add_document(filename, text, uploaded_by=None):
    session = get_session()
    doc = Document(filename=filename, text=text, uploaded_by=uploaded_by)
    session.add(doc)
    session.commit()
    doc_id = doc.id
    session.close()
    return doc_id

def list_documents():
    session = get_session()
    docs = session.query(Document).all()
    result = [{"id": d.id, "filename": d.filename, "text": d.text} for d in docs]
    session.close()
    return result

def list_documents_for_user(user_id):
    session = get_session()
    docs = session.query(Document).filter_by(uploaded_by=user_id).all()
    result = [{"id": d.id, "filename": d.filename} for d in docs]
    session.close()
    return result

def save_report(user_id, doc_id, report_path, diff_path, overall_score):
    session = get_session()
    r = Report(user_id=user_id, doc_id=doc_id, report_path=report_path, diff_path=diff_path, overall_score=overall_score)
    session.add(r)
    session.commit()
    session.close()

def list_reports_for_user(user_id):
    session = get_session()
    reps = session.query(Report).filter_by(user_id=user_id).order_by(Report.created_at.desc()).all()
    out = [{"id": r.id, "report_path": r.report_path, "diff_path": r.diff_path, "overall_score": r.overall_score, "created_at": r.created_at} for r in reps]
    session.close()
    return out
