import subprocess
import tkinter as tk
from tkinter import messagebox

# حالة الاتصال الحالية
is_running = False
process = None

def toggle_connection():
    global is_running, process
    if not is_running:
        try:
            # هنا بنشغل أداة البروكسي/الاتصال الخفي في الخلفية
            # (كمثال، بنشغل ملف تشغيل أو أمر خفيف يعترض حركة البيانات)
            # process = subprocess.Popen(["python", "proxy_core.py"])
            
            is_running = True
            btn.config(text="OFF (متصل)", bg="#e74c3c", fg="white")
            status_label.config(text="الحالة: التطبيق يعمل (روبلوكس متاحة)", fg="#2ecc71")
        except Exception as e:
            messagebox.showerror("خطأ", f"تعذر تشغيل التطبيق: {e}")
    else:
        try:
            if process:
                process.terminate() # إيقاف العملية في الخلفية
            is_running = False
            btn.config(text="ON (إيقاف)", bg="#2ecc71", fg="white")
            status_label.config(text="الحالة: متوقف", fg="#e74c3c")
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء الإيقاف: {e}")

# تصميم الواجهة البسيطة
root = tk.Tk()
root.title("Roblox Bypass Tool")
root.geometry("300x200")
root.resizable(False, False)
root.config(bg="#f0f2f5")

# عنوان أو نص توضيحي
title_label = tk.Label(root, text="مشروع تجاوز حجب روبلوكس", font=("Arial", 12, "bold"), bg="#f0f2f5", fg="#333")
title_label.pack(pady=20)

# الزر الوحيد (ON / OFF)
btn = tk.Button(root, text="ON (تشغيل)", font=("Arial", 14, "bold"), bg="#2ecc71", fg="white", 
                width=12, height=2, bd=0, relief="flat", command=toggle_connection)
btn.pack(pady=10)

# مؤشر الحالة
status_label = tk.Label(root, text="الحالة: متوقف", font=("Arial", 10), bg="#f0f2f5", fg="#e74c3c")
status_label.pack(pady=10)

root.mainloop()