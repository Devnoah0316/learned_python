# -*- coding: utf-8 -*-

'''
- 체중(kg)과 키(cm)를 입력하여 BMI(체질량 지수)를 구한 후에 BMI의 값이 20.0 이상 25.0 미만이면 "표준입니다"를 출력하고 그렇지 않으면 "체중관리가 필요합니다"를 출력하는 프로그램을 만드시면 됩니다.
- BMI = weight / tall² (체중 / 키²)
- 위 수식에서 몸무게의 단위는 kg이고, 키의 단위는 m입니다. **(cm가 아님에 주의하세요!)**

- 프로그램 실행 예시

```
몸무게(kg)와 키(cm) 입력: 66 185.6
체중관리가 필요합니다.
```
'''

weight, tall = input("몸무게(kg)와 키(cm) 입력: ").split()
weight = float(weight)
tall = float(tall) / 100

bmi =  weight / (tall**2)
print(bmi)
if (bmi >= 20.0) and (bmi < 25.0):
    print("표준입니다")

else:
    print("체중관리가 필요합니다")
