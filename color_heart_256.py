
import os

# تابع برای تغییر رنگ در ترموکس با استفاده از کدهای 256 رنگی
def set_color(color_code):
    os.system(f"tput setaf {color_code}")

# تابع برای نمایش قلب
def show_heart():
    print("    ******       ******")
    print("  **      **   **      **")
    print(" **        ** **        **")
    print(" **         ***         **")
    print("  **       ** **       **")
    print("   **     **   **     **")
    print("     ** **       ** **")
    print("       **           **")

# دریافت رنگ از کاربر
def main():
    print("Available colors (0-255):")
    for i in range(256):
        print(f"{i}: ", end="")
        set_color(i)  # تنظیم رنگ بر اساس کد
        print(f"Color {i}", end="\t")
        if i % 10 == 9:  # برای زیباتر کردن نمایش هر ده رنگ رو در یک خط نشون میده
            print()
    
    color = int(input("\nEnter a color number between 0 and 255: "))
    
    # تنظیم رنگ
    set_color(color)
    
    # نمایش قلب
    show_heart()
    
    # بازگشت به رنگ پیش‌فرض
    os.system("tput sgr0")

if __name__ == "__main__":
    main()
