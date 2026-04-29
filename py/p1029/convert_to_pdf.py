# Python 코드를 PDF로 변환하는 스크립트
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

def convert_python_to_pdf(python_file_path, output_pdf_path):
    # PDF 문서 생성
    doc = SimpleDocTemplate(output_pdf_path, pagesize=A4)
    story = []
    
    # 스타일 설정
    styles = getSampleStyleSheet()
    
    # 제목 추가
    title = Paragraph("로또번호 맞추기 프로그램", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 12))
    
    # Python 파일 읽기
    try:
        with open(python_file_path, 'r', encoding='utf-8') as file:
            code_content = file.read()
        
        # 코드 내용을 PDF에 추가
        code_para = Preformatted(code_content, styles['Code'])
        story.append(code_para)
        
        # PDF 생성
        doc.build(story)
        print(f"PDF 파일이 성공적으로 생성되었습니다: {output_pdf_path}")
        
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {python_file_path}")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

# 실행
if __name__ == "__main__":
    python_file = "p10.random(로또).py"
    pdf_file = "로또번호_맞추기_프로그램.pdf"
    
    convert_python_to_pdf(python_file, pdf_file)