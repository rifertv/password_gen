import string, random

def sp():
  with open('password.txt', 'a') as f:
    f.write(password + "\n")

dl = int(input("Желаемая длина пароля "))
sch = input("Допускать спец символы в пароле? (Да/Нет): ")
upal = input("Допускать большие буквы в пароле?(Да/Нет): ")
ch = input("Допускать цифры в пароле?(Да/Нет): ")

ss = [".", ":", ";","*", "-", "<", ">", "@", "_", "$", "#"]

first = string.ascii_lowercase
specs = ''.join(ss)
upper = string.ascii_uppercase
digits = string.digits

password = ''

ol = [first]

if sch == "Да":
  ol.append(specs)
if upal == "Да":
  ol.append(upper)
if ch == "Да":
  ol.append(digits)

hau = random.sample(''.join(ol), dl)
password += ''.join(hau)

print("Получившийся пароль: " + password)

save = input("Сохранить ваш пароль?(Да/Нет): ")

if save == "Да":
  sp()
  print("Пароль сохранен!")
else:
  exit
