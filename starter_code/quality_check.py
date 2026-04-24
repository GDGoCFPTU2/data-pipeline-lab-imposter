# ==========================================
# ROLE 3: OBSERVABILITY & QA ENGINEER
# ==========================================

def run_semantic_checks(doc_dict: dict) -> bool:
    content = doc_dict.get("content", "")
    
    # 1. Kiểm tra độ dài: Nếu content trống hoặc < 10 ký tự -> False
    if not content or len(content.strip()) < 10:
        print(f"QA Failed: Content too short ({len(content) if content else 0} chars).")
        return False
    
    # 2. Kiểm tra từ khóa lỗi (Toxic/Error Keywords)
    toxic_keywords = ["Null pointer exception", "OCR Error", "Traceback"]
    
    # Chuyển content về lower case để kiểm tra không phân biệt hoa thường (case-insensitive)
    content_lower = content.lower()
    
    for keyword in toxic_keywords:
        if keyword.lower() in content_lower:
            print(f"QA Failed: Found error keyword '{keyword}' in content.")
            return False
            
    # Nếu vượt qua tất cả các bài kiểm tra
    return True