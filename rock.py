Temperature = 22
moisture = 36

if Temperature > 35:
    print("High Temperature alert")
elif Temperature < 10:
    print("Low Temperature alert")
else:
    print("Temperature acceptable")

if moisture < 30:
    print("Plants need water")
else:
    print("Soil moisture acceptable")