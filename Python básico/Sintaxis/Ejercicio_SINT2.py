name= str(input("Escriba su nombre"))
last_name= str(input("Escriba su apellido"))
age= int(input("Edad"))
if age <= 2:
    stage= "Bebé"
elif age <= 11:
    stage= "Niño"
elif age <= 12:
    stage= "Preadolescente"
elif age <= 17:
    stage= "Adolescente"
elif age <= 29:
    stage= "Adulto joven"
elif age <= 59:
    stage= "Adulto"
else:
    stage= "Adulto mayor"
print(f"Your full name is {name} {last_name} and your stage is {stage}")