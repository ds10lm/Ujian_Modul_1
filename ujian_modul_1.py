#Soal 1
def calculate_years(principal, interest, years) :

    future_value  = principal*((1+(0.01*interest)) ** years)
    print(round(future_value,2))

calculate_years(100000, 1.5, 3)

# #Soal 2
def expandedForm(num):
    num += '.'
    i=num.find('.')
    z=list(num)
    del z[i]   
    return '+'.join([str(int(o)*10**(i-j-1)) for j,o in enumerate(z) if '0'<o]) or '0'

print(expandedForm('32.100'))



# #Soal 3
def tower_builder() :
    k = 0
    ukuran = 10
    for i in range(1, ukuran+1):
        for j in range(1, (ukuran-i)+1):
            print(end="  ")
        while k != (2*i-1):
            print("* ", end="")
            k = k + 1
        k = 0
        print()  


tower_builder()


# maaf pak saya cmn bisa kerjain soalnya seadanya doang
