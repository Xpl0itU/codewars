def bmi(weight, height):
    final_bmi = weight / height ** 2
    if final_bmi <= 18.5:
        return "Underweight"
    elif final_bmi <= 25.0:
        return "Normal"
    elif final_bmi <= 30.0:
        return "Overweight"
    return "Obese"