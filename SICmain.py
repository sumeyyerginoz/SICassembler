#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 18:53:26 2024
@author: sumeyye
"""
location = 0
symbolTable = {}

#statik olarak opcode tanımladım
opcodeSIC = { 

    "ADD" ,
    "AND" ,
    "COMP",
    "DIV" ,
    "J"   ,
    "JEQ" , 
    "JGT" , 
    "JLT" , 
    "JSUB",
    "LDA" ,
    "LDCH", 
    "LDL" , 
    "LDX" , 
    "MUL" ,
    "OR"  ,
    "RD"  , 
    "RSUB", 
    "STA" ,
    "STCH", 
    "STL" ,
    "STX" , 
    "SUB" , 
    "TD"  , 
    "TIX" , 
    "WD"  , 
    "BYTE", 
    "WORD", 
    "RESB", 
    "RESW", 
    "END"

   
}
# OPCODE tablosunu dışarıdan dosyadan okuma
"""
with open("optab.txt", "r") as opcode_file:
    for line in opcode_file:
        opcode, value = line.strip().split()
        opcodeSIC[opcode] = value
"""

# Kaynak kodu okuma
with open("assemblyCode.txt", "r") as file:
    assemblyCode = file.read()

for line in assemblyCode.split('\n'): #her satırı ayırarak okuma işlemi gerçekleştir
    
    if line[:4] == 'COPY':
        location = int(line.split()[2], 16) #hexadecimal olarak işlem yaptığımızı belirtmek için 16 kullandık
        
    elif line.startswith('.') or not line: # . ile başlayan satırlar yorum satırıdır (herhangi bir işlem yapılmaz)
        #print("yorum satırına denk geldiniz")
        continue
    
    else: 
        
        """assembly kodumuzdaki satırlar  3 ayrı alandan oluşuyor
zone --->      1             2           3
line --->    label        opcode      operand
             
        """   
        zone = line.split() #her satırda label,opcode ve operand olmayabilir bu yüzden 
                            # 1 tane varsa opcode
                            # 2 tane varsa opcode operand
                            # 3 tane varsa label opcode operand olarak ayırma işlemi yaptım
        
        if len(zone) == 1: 
            opcode = zone[0]
            if opcode == "END":
                break
            location += 3
            
        elif len(zone) == 2:
            opcode = zone[0]
            if opcode == "END":
                break
            location += 3
            
        elif len(zone) == 3:
            label = zone[0]
            opcode = zone[1]
            operand = zone[2]
            #-------------------------------satırdaki alanları ayırma işlemi yaptıktan sonra opcode olanlar üzerinden işlem yaptım.
            if opcode in opcodeSIC:
                
                if label not in symbolTable and opcode != "START":
                    symbolTable[label] = hex(location)[2:]
                    
                if opcode == "END":  #programı bitir
                    break
                
                elif opcode == "WORD": #bellek konumu (location) 3 artırılır 
                    location += 3  
                    
                elif opcode == "RESW":
                    increase = int(operand) * 3 #operanda göre location hesaplanır artırılır
                    location += increase
                    
                elif opcode == "RESB":
                    increase = int(operand) #operanda göre location artırılır
                    location += increase
                    
                elif zone == "BYTE": # 2 durum söz konusu C VE X 
                    information = zone[2][2:-1]
                    
                    if zone[2].startswith('C'):  #SIC mimarisinde "C" ifadesi karakter olduğunu belirtir. Bu karakterin uzunluğunu hesaplayarak arttırılır.
                        increase = len(information)
                        
                    elif zone[2].startswith('X'): #SIC mimarisinde "X" ifadesi hexadecimal olduğunu belirtir.
                        increase = len(information) // 2
                    location += increase
                    
                else:
                    location += 3

# symtab.txt dosyasına ve çıktıya yazma
with open("symtab.txt", "w") as file:
    for symbol, address in symbolTable.items():
        file.write(f"{symbol}\t{address}\n")

# sembol tablosunu çıktı olarakta görebiliriz
print("Sembol tablosu symtab.txt dosyasına içeriği kaydedilmiştir.")
print("\n\tSEMBOL TABLOSU\n\n--------------------------")
print("ETİKET    ADRES")
print("--------------------------")
for symbol, address in symbolTable.items():
    print(f"{symbol}\t{address}")
