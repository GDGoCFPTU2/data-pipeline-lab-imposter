import re
from datetime import datetime

# ==========================================
# ROLE 2: ETL/ELT BUILDER
# ==========================================

def process_pdf_data(raw_json: dict) -> dict:
    # Bước 1: Làm sạch nhiễu (Header/Footer) khỏi văn bản
    raw_text = raw_json.get("extractedText", "")
    
    cleaned_content = re.sub(r'(HEADER_PAGE_\d+|FOOTER_PAGE_\d+)', '', raw_text)
    # Làm sạch thêm khoảng trắng thừa sau khi xóa header/footer
    cleaned_content = cleaned_content.strip()
    
    # Bước 2: Map dữ liệu thô sang định dạng chuẩn của UnifiedDocument
    unified_doc = {
        "document_id": raw_json.get("docId"),
        "source_type": "PDF",
        "author": raw_json.get("metadata", {}).get("authorName", "Unknown"),
        "category": raw_json.get("docCategory", "General"),
        "content": cleaned_content,
        "timestamp": raw_json.get("createdAt", datetime.now().isoformat())
    }
    
    return unified_doc

def process_video_data(raw_json: dict) -> dict:
    # Map dữ liệu thô từ Video sang định dạng chuẩn (giống PDF)
    # Lưu ý: Transcript của video sẽ được map vào trường 'content'
    unified_doc = {
        "document_id": raw_json.get("video_id"),
        "source_type": "Video",
        "author": raw_json.get("creator_name", "Unknown"),
        "category": raw_json.get("category", "General"),
        "content": raw_json.get("transcript", ""),
        "timestamp": raw_json.get("published_timestamp", datetime.now().isoformat())
    }
    
    return unified_doc