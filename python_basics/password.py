import random
import string

def create_all_combination(length):
  if length < 4:
    print("Not possible to generate with number , symbol , lowercase and uppercase letter🙅‍♀️")
  password = ""
  password1 = ""
  password2 = ""
  password3 = ""
  final_len = length
  while length > 0:
    list_of_sym = ["@","#","$","%","&"]
    choosen_sym = random.choices(list_of_sym , k = 1)
    sym_string = "".join(choosen_sym)
    password1 = "".join(sym_string + password )
    if len(password1) >= final_len:
      password = password1
      break

    list_of_num = ["0" , "1" , "2" , "3" , "4" ,"5" , "6" , "7" , "8" , "9"]
    choosen_num = random.choices(list_of_num , k = 1)
    num_string = "".join(choosen_num)
    password2 = "".join( num_string + password1)
    if len(password2) >= final_len:
      password = password2
      break

    choosen_lower = "".join(random.choices(string.ascii_lowercase , k = 1))
    lower_string = "".join(choosen_lower)
    password3 = "".join( password2 + lower_string)
    if len(password) >= final_len:
      password = password3
      break

    choosen_upper = "".join(random.choices(string.ascii_uppercase , k = 1))
    upper_string = "".join(choosen_upper)
    password = "".join(password3 + upper_string)
    if len(password) >= final_len:
      break
    length = length - 4

  password_list = list(password)
  random.shuffle(password_list)
  password = "".join(password_list)
  print("you password is : " , password)

def create_num_combination(length):
  password = ""
  final_len = length
  while length > 0:

    list_of_num = ["0" , "1" , "2" , "3" , "4" ,"5" , "6" , "7" , "8" , "9"]
    choosen_num = random.choices(list_of_num , k = 1)
    num_string = "".join(choosen_num)
    password = "".join( num_string + password)
    if len(password) >= final_len:
      break
    length = length - 1

  password_list = list(password)
  random.shuffle(password_list)
  password = "".join(password_list)
  print("you password is : " , password)


def create_num_sym_combination(length):
  password = ""
  password1 = ""
  final_len = length
  while length > 0:
    list_of_sym = ["@","#","$","%","&"]
    choosen_sym = random.choices(list_of_sym , k = 1)
    sym_string = "".join(choosen_sym)
    password1 = "".join(sym_string + password )
    if len(password1) >= final_len:
      password = password1
      break

    list_of_num = ["0" , "1" , "2" , "3" , "4" ,"5" , "6" , "7" , "8" , "9"]
    choosen_num = random.choices(list_of_num , k = 1)
    num_string = "".join(choosen_num)
    password = "".join( num_string + password1)
    if len(password) >= final_len:
      break  
    length = length - 2

  password_list = list(password)
  random.shuffle(password_list)
  password = "".join(password_list)
  print("you password is : " , password)


#different fucntion call
def create_password(length ,include_num , include_sym , include_case):
  if include_num == "yes" and include_sym == "yes" and include_case == "yes":
    create_all_combination(length)
  
  elif include_num == "yes" and include_sym == "no" and include_case == "no":
    create_num_combination(length)

  elif include_num == "yes" and include_sym == "yes" and include_case == "no":
    create_num_sym_combination(length)
  else:
    print("wrong inputss")


leng = int(input("enter length: "))
num = input("do you want to include numbers? ")
sym = input("do you want to include special symbols? ")
case = input("do you want both upper case letter and lower case letter? ")
create_password(leng , num , sym , case)