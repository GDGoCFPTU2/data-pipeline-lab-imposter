import os
import json
import glob

# Import các thành phần
from schema import UnifiedDocument
from process_unstructured import process_pdf_data, process_video_data
from quality_check import run_semantic_checks

# ==========================================
# ROLE 4: DEVOPS & INTEGRATION SPECIALIST
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DATA_DIR = os.path.join(BASE_DIR, "..", "raw_data")
OUTPUT_FILE = os.path.join(BASE_DIR, "..", "processed_knowledge_base.json")

def run_pipeline():
    final_kb = []
    
    # Xử lý Group A (PDFs)
    pdf_files = glob.glob(os.path.join(RAW_DATA_DIR, "group_a_pdfs", "*.json"))
    print(f"Found {len(pdf_files)} PDF data files.")
    
    for file_path in pdf_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
        
        # Bước 1: Gọi hàm xử lý PDF (process_pdf_data)
        processed_doc = process_pdf_data(raw_data)
        
        # Bước 2: Kiểm tra chất lượng (run_semantic_checks)
        # Giả định run_semantic_checks trả về (is_valid, doc) hoặc True/False
        if run_semantic_checks(processed_doc):
            final_kb.append(processed_doc)
            print(f"Successfully processed and validated: {file_path}")
        else:
            print(f"Quality check fail for: {file_path}")

    # Xử lý Group B (Videos)
    video_files = glob.glob(os.path.join(RAW_DATA_DIR, "group_b_videos", "*.json"))
    print(f"Found {len(video_files)} Video data files.")
    
    for file_path in video_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
        
        # Bước 3: Gọi hàm xử lý Video (process_video_data)
        processed_doc = process_video_data(raw_data)
        
        # Bước 4: Kiểm tra chất lượng
        if run_semantic_checks(processed_doc):
            final_kb.append(processed_doc)
            print(f"Successfully processed and validated: {file_path}")
        else:
            print(f"Quality check fail for: {file_path}")

    # Lưu kết quả
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(final_kb, f, indent=4, ensure_ascii=False)
        print("-" * 30)
        print(f"Pipeline finished! Total records saved: {len(final_kb)}")

if __name__ == "__main__":
    run_pipeline()