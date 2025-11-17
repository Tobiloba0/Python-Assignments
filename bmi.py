weight = int(input("Enter your weight in kg: "))
height = int(input("Enter your height in meters: "))

bmi = weight / (height * height)

if(bmi < 18.5):
    print("Underweight")


if(bmi > 18.5 and bmi < 24.9){
    print("Normal")
}

if(bmi >= 30){
    print("Obese")
}
