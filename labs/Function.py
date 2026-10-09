def deposit(money):
    print(f"ยอดเงินเริ่มต้น: {money} บาท")
    user_input = input("กรอกจำนวนเงินที่ต้องการฝาก: ")
    print()  # บรรทัดว่างเพื่อความสวยงามตรงตามตัวอย่าง
    
    try:
        amount = float(user_input)
        if amount <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")
    except ValueError as e:
        # ดักจับทั้งกรณีแปลงเป็นตัวเลขไม่ได้ และกรณีฝากเงิน <= 0 ที่ถูก raise ขึ้นมา
        if str(e).startswith("could not convert"):
            print("เกิดข้อผิดพลาด: กรอกข้อมูลไม่ถูกต้อง (ต้องเป็นตัวเลขเท่านั้น)")
        else:
            print(f"เกิดข้อผิดพลาด: {e}")
    else:
        money += amount
        print("ฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {money:.2f} บาท")
    finally:
        print("สิ้นสุดรายการฝากเงิน")

# --- ทดลองใช้งานฟังก์ชัน ---
balance = 1000
deposit(balance)