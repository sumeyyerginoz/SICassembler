# SIC (Simplified Instructional Computer) Assembler

Python programlama dilinde yazılmış olan SIC (Basitleştirilmiş Eğitim Bilgisayarı) mimarisi için bir derleyici olan bir assembly dilinin temel işlemlerini gerçekleştirir. Bu işlemleri gerçekleştirirken SIC mimarisine ait olan pass1 algoritmasından yararlanılmıştır.


<img width="1440" alt="SIC PASS1" src="<img width="597" alt="Ekran Resmi 2024-04-04 22 54 53" src="https://github.com/sumeyyerginoz/SICassembler/assets/112480236/8b33d790-e908-48f8-9fcc-3500874156d4">">



Python programı, assemblyCode.txt dosyasındaki SIC dilinde yazılmış assembly kodunu işlemektedir. Programın başlangıcında “location“ adında bir değişken tanımladım. ve başlangıç değerini sıfır olarak atadım. Ayrıca “symbolTable “adında boş bir sözlük oluşturdum. Program satır satır okundukça  bu sözlük sembollerin bellek adreslerini saklamak için kullanılır. “opcodeSIC“ kümesi, geçerli SIC komutlarını içerir. 

Program, assemblyCode.txt dosyasını açar ve satır satır okur. Her satır, boşluklara göre bölünerek “zone “ adlı bir liste elde edilir. Bu liste, satırdaki etiket (label), komut (opcode) ve işlemci (operand) bilgilerini içerir. Eğer satır boşsa veya yorum satırıysa (".") işlem yapılmaz. 

zone listesinin eleman sayısına (len(zone)) göre işlem yapılır: 

ssembly kodumuzdaki satırlar  3 ayrı alandan oluşmaktadır. 

zone --->      1   2           3 

line --->    label        opcode      operand 

len(zone) == 1: Sadece komut varsa, location değeri 3 artırılır. 
len(zone) == 2: Komut ve işlemci varsa, yine location değeri 3 artırılır. 
len(zone) == 3: Etiket, komut ve işlemci varsa, ilgili komutun işlemleri gerçekleştirilir. 
Eğer komut opcodeSIC kümesinde tanımlı bir geçerli komut ise: 

Etiket sembol tablosunda yoksa (ve komut "START" değilse), symbolTable sözlüğüne eklenir ve bellek adresi (location) atanır. 
 
Komuta bağlı olarak location değeri güncellenir (WORD, RESW, RESB, BYTE gibi durumlar için). 
 
Son olarak, symbolTable sözlüğündeki semboller ve bellek adresleri symtab.txt dosyasına yazılır. Ayrıca sembol tablosu çıktısı ekrana da yazdırılır.
