"""
ImageData SQLAlchemy model
"""
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base


class ImageData(Base):
    """
    ImageData model for storing image information and analysis results
    """
    __tablename__ = "image_data"

    id = Column(Integer, primary_key=True, index=True)
    tc_image_id = Column(String(255), nullable=False, index=True)
    raw_image_path = Column(String(500), nullable=False)
    processed_image_path = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    histogram_path = Column(String(500), nullable=True)
    intensity_average = Column(Float, nullable=True)
    focus_score = Column(Float, nullable=True)
    classification_label = Column(String(255), nullable=True)

    def __repr__(self):
        return f"<ImageData(id={self.id}, tc_image_id='{self.tc_image_id}')>"
