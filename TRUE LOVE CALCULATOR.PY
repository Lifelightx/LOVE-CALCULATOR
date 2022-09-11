your_name = input("Enter your name: ")
up_your_name = your_name.upper()
gf_name = input("Enter your GF name: ")
up_gf_name = gf_name.upper()
add = up_your_name + up_gf_name
nam1 = add.count("T")
nam2 = add.count("R")
nam3 = add.count("U")
nam4 = add.count("E")
name1 = add.count("L")
name2 = add.count("O")
name3 = add.count("V")
name4 = add.count("E")
sum1 = nam1+nam2+nam3+nam4
sum2 = name1+name2+name3+name4
percentage = str(sum1)+str(sum2)
print("PERCENTAGE OF LOVE IS: ",percentage)