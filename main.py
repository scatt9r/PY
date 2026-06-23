def main():
    print("=== BMI 건강 계산기 ===")

    try:
        name = input("이름: ")
        height = float(input("키(cm): "))
        weight = float(input("현재 몸무게(kg): "))
        target = float(input("목표 몸무게(kg): "))
        
        my_bmi = check_bmi(weight, height)
        status = get_status(my_bmi)
