import random

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
# دالة لتوليد رقم عشوائي يبدأ بـ 475 ويتكون من 16 رقم
def generate_card_number():
    return "475" + ''.join(random.choices('0123456789', k=13))

# دالة لتوليد تاريخ عشوائي من 2026 إلى 2031
def generate_random_date():
    month = random.randint(1, 7)  # شهر من 1 إلى 7
    year = random.randint(2026, 2031)  # سنة من 2026 إلى 2031
    return f"{month:02}/{year % 100:02}"  # صيغة MM/YY

# دالة لتوليد رقم عشوائي مكون من 3 أرقام
def generate_three_digit_number():
    return random.randint(100, 999)  # رقم بين 100 و 999

# توليد الأرقام
card_number = generate_card_number()
random_date = generate_random_date()
cvc_number = generate_three_digit_number()

# طباعة النتائج مع التسميات
print(f"Number: {card_number}")
print(f"Date: {random_date}")
print(f"CVC: {cvc_number}")