### MY VARIABLES ###

f_case=input("Convert From B/D/O/H : ")
s_case=input("Convert To B/D/O/H : ")
num=input("Enter The Number : ")

########################################################

### MY MAIN FUNCTIONS ###

def fr_bi_to_de(num):
    return(int(str(num),2))
def fr_de_to_bi(num):
    return bin(num).replace("0b","")
def fr_de_to_oc(num):
    return(oct(num)).replace("0o","")
def fr_oc_to_de(num):
    return(int(str(num),8))    
def fr_de_to_hx(num):
    return(hex(num)).replace("0x","")

##################1
def fr_bi_to_oc(num):
    x_1=fr_bi_to_de(num)
    x_2=fr_de_to_oc(x_1)
    return(x_2)

##################2
def fr_oc_to_bi(num):
    x_1=fr_oc_to_de(num)
    x_2=fr_de_to_bi(x_1)
    return(x_2)
##################3
def fr_bi_to_hx(num):
    x_1=fr_bi_to_de(num)
    x_2=fr_de_to_hx(x_1)
    return(x_2)    

##################4
def fr_oc_to_hx(num):
    x_1=fr_oc_to_de(num)
    x_2=fr_de_to_hx(x_1)
    return(x_2)

##################5
def fr_hx_to_bi(num):
    return(bin(int(str(num),16))).replace("0b","")

##################6
def fr_hx_to_de(num):
    return(int(str(num),16))

##################7
def fr_hx_to_oc(num):
    return(oct(int(str(num),16))).replace("0o","")


########################################################
### NASTED IF ###

if f_case == 'B' and s_case == 'B':
    print("RESULT IS : ",num)
elif f_case == 'D' and s_case == 'D':
    print("RESULT IS : ",num)
elif f_case == 'O' and s_case == 'O':
    print("RESULT IS : ",num)
elif f_case == 'H' and s_case == 'H':
    print("RESULT IS : ",num)
elif f_case == 'B' and s_case == 'D':
    print("This from binary to decimal :",fr_bi_to_de(num))
elif f_case == 'D' and s_case == 'B':    
    print("This from decimal to binary :",fr_de_to_bi(num))
elif f_case == 'D' and s_case == 'O':
    print("This from decimal to octal :",fr_de_to_oc(num))
elif f_case == 'O' and s_case == 'D':
    print("This from octal to decimal :",fr_oc_to_de(num))
elif f_case == 'D' and s_case == 'H':
    print("This from decimal to hexa :",fr_de_to_hx(num)) 
elif f_case == 'B' and s_case == 'O':
    print("This from binary to octal :",fr_bi_to_oc(101))
elif f_case == 'O' and s_case == 'B':
    print("This from octal to binary :",fr_oc_to_bi(101))
elif f_case == 'B' and s_case == 'H':
    print("This from binary to hexa :",fr_bi_to_hx(101))
elif f_case == 'O' and s_case == 'H':
    print("This from octal to hexa :",fr_oc_to_hx(101))
elif f_case == 'H' and s_case == 'B':
    print("This from hexa to binary :",fr_hx_to_bi(101))
elif f_case == 'H' and s_case == 'D':    
    print("This from hexa to decimal :",fr_hx_to_de(101))
elif f_case == 'H' and s_case == 'O':
    print("This from hexa to octal :",fr_hx_to_oc(101)) 
else :
    print("please try again \n    $$$ NOTES $$$ \n -You Must Enter Capital Alphabet In HEXA Case\n -You Must Enter Integer Number IN Anoter Cases")
    
    