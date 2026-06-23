def check_bmi(w, h_cm):
    h_m = h_cm / 100
    res = w / (h_m ** 2)
    return round(res, 2)

def get_status(bmi):
    if bmi < 18.5:
        return "저체중"
    elif bmi < 23:
        return "정상"
    elif bmi < 25:
        return "과체중"
    else:
        return "비만"

def show_exercise():
    print("\n[추천 HIIT 운동 루틴]")
    print("1. 제자리 걷기 (3분)")
    print("2. 버피 테스트 (30초 전력) -> 휴식 (30초) -> 4세트 반복")
    print("3. 스쿼트 (30초 전력) -> 휴식 (30초) -> 4세트 반복")
    print("4. 스트레칭 마무리 (3분)")

def main():
    print("=== BMI 건강 계산기 ===")

    try:
        name = input("이름: ")
        height = float(input("키(cm): "))
        weight = float(input("현재 몸무게(kg): "))
        target = float(input("목표 몸무게(kg): "))
        
        my_bmi = check_bmi(weight, height)
        status = get_status(my_bmi)
        
        print(f"\n[{name}님 결과]")
        print(f"BMI 지수: {my_bmi} (결과: {status})")
        
        diff = weight - target
        if diff > 0:
            print(f"목표까지 {round(diff, 1)}kg 감량이 필요합니다.")
            show_exercise()
        elif diff < 0:
            print(f"목표까지 {round(abs(diff), 1)}kg 증량이 필요합니다.")
        else:
            print("현재 목표 체중입니다.")
            
    except:
        print("숫자만 입력해주세요.")

if __name__ == "__main__":
    main()



