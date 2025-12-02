# PDF to Word Converter

یک ابزار ساده و کاربردی برای تبدیل فایل‌های PDF به فرمت Word (`.docx`) با استفاده از پایتون. این ابزار از کتابخانه `pdf2docx` برای استخراج محتوا و حفظ فرمت‌بندی اسناد استفاده می‌کند.

## ✨ ویژگی‌ها

- تبدیل فایل‌های PDF به فرمت Word (`.docx`)
- حفظ ساختار اولیه سند (متن، جداول، تصاویر)
- رابط خط فرمان ساده (CLI)
- امکان تبدیل دسته‌ای (Batch Conversion)
- پشتیبانی از PDFهای چند صفحه‌ای
- گزارش پیشرفت عملیات تبدیل

## 📋 پیش‌نیازها

قبل از اجرای اسکریپت، مطمئن شوید پایتون 3.6 یا بالاتر روی سیستم شما نصب است.

## 🔧 نصب و راه‌اندازی

### 1. کلون کردن ریپازیتوری
```bash
git clone https://github.com/Arashmgbrj/pdf_convertor.git
cd pdf_convertor
```

### 2. نصب کتابخانه‌های مورد نیاز
```bash
pip install pdf2docx
```

یا با استفاده از فایل requirements.txt (در صورت وجود):
```bash
pip install -r requirements.txt
```

## 🚀 نحوه استفاده

### روش 1: تبدیل یک فایل PDF
```bash
python pdf_to_word.py -i input.pdf -o output.docx
```

### روش 2: تبدیل دسته‌ای فایل‌های PDF در یک پوشه
```bash
python pdf_to_word.py -i /path/to/pdf/folder -o /path/to/output/folder
```

### روش 3: تبدیل با رابط گرافیکی ساده
```bash
python pdf_to_word.py --gui
```

## 📖 نمونه کد

### مثال 1: تبدیل ساده یک فایل
```python
from pdf2docx import Converter

def convert_pdf_to_word(pdf_path, docx_path):
    """
    تبدیل فایل PDF به Word
    
    پارامترها:
    pdf_path (str): مسیر فایل PDF ورودی
    docx_path (str): مسیر فایل Word خروجی
    """
    try:
        # ایجاد مبدل
        cv = Converter(pdf_path)
        
        # انجام تبدیل
        cv.convert(docx_path, start=0, end=None)
        
        # بستن مبدل
        cv.close()
        
        print(f"✅ تبدیل با موفقیت انجام شد: {docx_path}")
        return True
    except Exception as e:
        print(f"❌ خطا در تبدیل: {str(e)}")
        return False

# استفاده از تابع
convert_pdf_to_word("input.pdf", "output.docx")
```

### مثال 2: تبدیل دسته‌ای
```python
import os
from pdf2docx import Converter

def batch_convert(input_folder, output_folder):
    """
    تبدیل تمام فایل‌های PDF در یک پوشه
    
    پارامترها:
    input_folder (str): مسیر پوشه حاوی فایل‌های PDF
    output_folder (str): مسیر پوشه برای ذخیره فایل‌های Word
    """
    # ایجاد پوشه خروجی در صورت عدم وجود
    os.makedirs(output_folder, exist_ok=True)
    
    # لیست تمام فایل‌های PDF
    pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        print("⚠️ هیچ
