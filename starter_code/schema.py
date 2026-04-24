from pydantic import BaseModel, Field
from datetime import datetime

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================

class UnifiedDocument(BaseModel):
    """
    Hệ thống cần 6 trường thông tin chuẩn (document_id, source_type, author, category, content, timestamp). 
    """
    document_id: str = Field(..., description="Unique identifier for the document")
    source_type: str = Field(..., description="Type of source: 'pdf' or 'video'")
    author: str = Field(..., description="Author or creator name")
    category: str = Field(..., description="Content category")
    content: str = Field(..., description="Cleaned text content")
    timestamp: str = Field(..., description="Publication timestamp in ISO format")
