from flask import Flask, render_template
import os

# إنشاء تطبيق Flask
app = Flask(__name__)

# ---------------------------
# مسارات الصفحات (Routes)
# ---------------------------

@app.route('/')
def home():
    """الصفحة الرئيسية"""
    return render_template('index.html')

@app.route('/<page>')
def serve_page(page):
    """
    مسار ديناميكي لجميع الأدوات.
    على سبيل المثال: /email-gen سيعرض email-gen.html
    """
    # التأكد من أن الملف موجود قبل محاولة عرضه
    template_path = os.path.join('templates', f'{page}.html')
    if os.path.exists(template_path):
        return render_template(f'{page}.html')
    else:
        return "الصفحة غير موجودة", 404

# ---------------------------
# تشغيل السيرفر
# ---------------------------
if __name__ == '__main__':
    # سيتم تشغيل السيرفر على http://127.0.0.1:5000
    app.run(debug=True, port=5000)
