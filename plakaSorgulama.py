owners = {
   "34 DSF 3025": {"adı":"AHMET ASIM","memleket":"Konya","arabaAdı":"Volvo-S60", "arabaRengi":"Metalik Gri"},
   "23 ASD 2020":"MEHMET ŞEKER",
   "01 ADN 3026":"MEHMET ÇAKIR",
   "06 YRN 0125":"YAREN MELEK",
   "17 SDA 203":"ZEHRA ATEŞ",
   "81 OSM 7082": "NURAN AYŞE"
}

plaka = input("Bir Plaka Numarası Giriniz: ")




if plaka in owners:
     
     print("Aradığınız plaka " + owners[plaka]["arabaAdı"] +" kişisine aittir")
else:
     print("Plaka Hakkında bir bilgi yok")
        
    
    
 
      
       
   
    