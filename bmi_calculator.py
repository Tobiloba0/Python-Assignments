weight = int(input("Enter your weight in kg: "))
height = int(input("Enter your height in meters: "))

bmi_category = weight / (height * height)

if bmi_category < 18.5:
    print("Underweight")

elif bmi_category >= 18.5 and bmi_category <= 24.9:
    print("Normal")

elif bmi_category >= 25 and bmi_category <= 29.9:
    print("Overweight")
elif bmi_category >= 30:
    print("Obese")


