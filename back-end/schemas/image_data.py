"""
Pydantic schemas for ImageData
"""
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional


class ImageDataBase(BaseModel):
    """Base ImageData schema with common attributes"""
    tc_image_id: str = Field(..., description="Teracyte image ID")
    raw_image_path: Optional[str] = Field(None, description="URL/path to raw image")
    processed_image_path: Optional[str] = Field(None, description="URL/path to processed image")
    histogram_path: Optional[str] = Field(None, description="URL/path to histogram")
    intensity_average: Optional[float] = Field(None, description="Average intensity value")
    focus_score: Optional[float] = Field(None, description="Focus quality score")
    classification_label: Optional[str] = Field(None, description="Image classification label")


class ImageDataCreate(ImageDataBase):
    """Schema for creating a new image data record"""
    pass


class ImageDataUpdate(BaseModel):
    """Schema for updating image data (all fields optional)"""
    raw_image_path: Optional[str] = None
    processed_image_path: Optional[str] = None
    histogram_path: Optional[str] = None
    intensity_average: Optional[float] = None
    focus_score: Optional[float] = None
    classification_label: Optional[str] = None


class ImageDataResponse(ImageDataBase):
    """Schema for image data response"""
    id: int
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
