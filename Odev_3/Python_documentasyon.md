Pythonda girintiler ve çıkıntılar önemli, diğer programlama dillerinde süslü parantez gibi şeyler kullanılırken pythonda girinti çıkıntılar kullanılır

&#x20;örneğin : if 7>2:

&#x20;          	print("Hello Yoda")



\# ile comment bırakbiliriz .



pythonda variable atarken c deki gibi int x=8 gibi bir kullanım yok bunun yerine direkt olarak x=8 yazabiliriz.



aynı zamanda eğer 8 i int değil de float veya string olarak atamak istiyorsak x=float(8) x=str(8) komutlarını kullanabiliriz.



type(x) ile x in type ını elde edebiliriz örneğin print(type(x)) yazarak x in tipini yazdırabiliriz.

pythonda tek tırnak veya çift tırnak kullanılabilir string ataması yaparken örneğin :



x= "hello"

y= 'hello' bu 2si de hata vermez ve geçerlidir .



python case sensetivedir . name=7 Name=7 dersek 2 farklı variable atanmış olur büyük harfe duyarlıdır .



pek çok dilde olduğu gibi pythonda da variable ismi rakam ile başlayamaz örneğin 2name geçersizdir. alt çizgi ile başlayabilir örneğin \_name geçerlidir. Yalnızca alfa-sayısal ifadeler ve alt çizgi içerebilir anahtar ifadeler de geçersizdir.



genelde birden fazla kelime ile variable kullanırken camelCase tarzı yazım kullanılır örneğin : myName ilk kelime küçük harf diğerleri büyük harf ile başlar. Ancak diğer yazımlar da tercih edilebilir ben snake case kullanacağım.: my\_name



aynı anda variable atamak mümkündür x,y,z = 1 , 2 , 3 (Variable ve değer sayısı aynı olmalıdır)



a = b = c = "red" (Bu kullanım da geçerlidir 3 variable tek değere atanabilir)



name = "kerem"

last\_name = name

print(last\_name) komutu çıktı olarak kerem verir mantık bu.



variable larda unpacking:



colors  = \["white","black","red"]

x , y, z = colors   #bu atama ile sırasına göre x y z değerleri white black ve red olarak atanır.







print içinde birden fazla variable olabilir. örnerğin :



x = k

y = a



print(x,y) = k a





aynı zamanda bu kulalnım da geçerlidir : print (x+y) = ka #artı olarak birleştirirsek arasında boşluk olmaz biz kendimiz ekleyebiliriz virgülde ise default olarak boşlukludur.



\+ ile yazdırmak için 2 değişkenin tipi aynı olmalıdır.



Global variables hem function içinde hem function dışında kullanılabilir

local variables sadece function içinde tanımlıdır ve sadece orada kullanılır.





function içindeki variable başına global yazarak local variable ı global yapabiliriz : global x = 3



listler \[] ile ayrılır ve çoklu veri tutmaya yarar .



tüple ve list farkı ise değiştiremezsin kafana göre veri sokamıyorsun .  tuple() ile gösterilir .



range ise sayı dizisi oluşturur range(7) 0dan 7ye kadar oluşan bir sayı dizisi oluşturur : my\_range=range(7) print(\*my\_range) : 0 1 2 3 4 5 6 ( 0 dan başlar 7 dahil değildir.)



dict {} süslü parantez . anahtar ve değer çiftlerinden oluşur örneğin :



my\_dict= {"name":"kerem","age":"21"}



burada name ve kerem anahtar değer çiftidir .



, ile çiftleri ayırırız .



set data types ise tek değer tutar ve yine {} ile gösterilir . set esnek iken frozen set daha katıdır . frozen set ({}) ile gösterilri .





bool veri tipi true ya da false değerleri alır .





my\_bool = True





none type boş olduğunu belrtir .





import sys

sys.getsizeof() ile variable ın ne kadar byte kapladığını öğrnebilrz



name= b "python" byte tipinde varaible oluşur str değildri .  
İL

bytes veri tipi ASCII ile çalışır .



name = bytearray(\[65]) : A çıktısı verir çünkü 65 ascii de A ya eştir .

memoryview veri üzerinde işlem yaparken kullanılır.



x= input() ile kullanıcıdan x e input girmesi istenri .



random sayı üretmek için seed metodu kulalnılır eğer siz seed girecekseniz random.seed() kullanılırken eğer siz seed girmek istemiyorsanız direkt olarak print(random.random()) yazarak sistem saatinden bir algoritma ile kendi seedini çekip her seferinde rastgele sayı üretiyor eğer seed girersenize seede göre belirli random sayılar üretilir .





random.getrandbits() ile içeri yazdığımız bit sayısında random sayı üretir.

randrange ise belirlenen aralıkta rastgele sayı döndürür : print(random.range(1,10)) 1 dahilken 10 değildir  3. parametre girerek artış miktarına göre rastgele sayılar üretilebilir örneğin : print(random.range(1,10,3)) 1 4 7 sayıları rastgele olarak döner durur .





listeden random seçim yaparken hem olaslığı belirleyebilir hem de şu şekilde rastgele seçim yapabiliriz :

myList=\["cherry","strawberry","grape","banana"]



print(random.choices(myList,weights=\[10,1,1,1],k=10))

burda cherry diğerlerine göre 10 kat daha ihtimalli print edilir .

shufle komutu ise bir seriyi alıp rastgele sırayla tekrar yazar örneğin :



myList=\["skoda","bmw","audi","nissan","toyota","volvo","ford"]



random.shuffle(myList)

print(myList)

== \['ford', 'audi', 'bmw', 'skoda', 'nissan', 'volvo', 'toyota'] sırası değişir

sample ise şöylek kullanılır ve belirli sayıda rastgele birim getirir :



print(random.sample(myList,k=2)) (rastgele 2 aadet araba markası gelir. )



arrayler 0 ile başlar 1 ile başlamaz .



string de aslında array olarak depolanır yani bir stirngde eleman çağırabiliriz örneğin :



text="Hello, Python!"

print(text\[0]) : H verir

&#x20;



len komutu ile str nin uzunluğunu elde ederiz .

bir metinde bir ifadenin varlığını in komutu ile öğrenebiliriz örneğin :

text="The best languages in life are free!"



print("free" in text)

bu metinde free geçtiği için bize output olarak True verilri .

bir variable atayarak da bu işlemi yapabilirzi

a="free"
print(a in text) bize True verirdi yine

bunların hepsi case sensetive dir



not in de olmayanı arar aynı şeyler geçerlidir .



string de başlangıc ve son belirterek dilimleme yapaibliriz

text="python is weird"



print(text\[1:5])

1den başlar 5. karaktere kadar 5 dahil değildir . (0dan başlandığını unutma) içeriyi - yaparak sondan başlayabiliriz sondan da 0 dan başlar değişen bir durum yok

ile print içinde veya variable atayarak birleştirme yapabilriz .



text. yanına yazacağımız bazı komutlar ile stringlerde düzenleme yapabiliriz : mesela text.upper text.lower büyük harf ve küçük harfe dönüşür .

split() ile bir stringi istediğimiz bir karakterden önce ve sonra bölebiliriz :

text="Hello, Python! java, c#"

result=text.split("!")

print(result) : 'Hello , Python' , 'java, c#'

&#x20;

kaçış karakterleri şunlarıdr :

\\ : single quote
\\\\ : backslash

\\n : new line
\\r : carriage return

\\t : tab
\\b : backspace
\\ooo : octal value
\\xhh : hexadecimal value :



bana ilginç gelen kaçış karakteri \\r oldu imleç başa dönüp önceki stringin üstüne sonraaki stringi yazıyor örneğin :



text="Hello\\rPy"



print(text) : Pyllo

\\b ise sadec1  sola kaydırılarak aynı işlemi yapıyor .





.format metodu ile stringleri formatlayabiliriz. mesela :

age=21

name="Kerem"

text="My name is {}, I am {}".format(name, age)

print(text)



.format metodu ile bu boşluklara string aralarına ismimi ve yaşımı yazabilirim normal şartlar altında yaşımı str(age) ile kullanmam gerekirdi .





f stringler :



age=21

name="Kerem"

text=f"My name is {name}, I am {age}"

print(text)





aynı işlemi çok daha temiz yapar .



input her zaman string döndürürmüş kanım dondu .



f-string içinde koşullu önerme de olabilir :



puan = 55

print(f"Sonuç: {'Geçti' if puan >= 50 else 'Kaldı'}")   # Sonuç: Geçti



casefold lowerdan daha güçlüdür.



title her kelimenin ilk harfini büyük yazar .  Rakam gördükten sonraski kısmı da büyük yazar .

swapcase büyüğü küçük küçüğü büyük yapar .

islower isupper true false döndürür



.center stringi ortaya alır (içine) 2 parametre girilebilir . (20 , "\*") 20 karakterin ortasına stringimiz gelcek kalan yerlere \* gelecek . default hali boşluktur .



.count() kaç kere geçtiğini söyler . ("world",11,15) 11den 15e kadara world ü arar mesela .



.startwith and .endwith belirtilen değerle başlıyor ya da bitiyor ise True değeri döndürür



.find() stringde aranan yerin indisini döndürür .





.index findın aksine bulunamazsa -1 yerine hata mesajı verir .

.isalnum alfanümerik sadece ve sadece harf ve rakam -boşluk bile olmayacak- varsa true döner

.isalpha alfabetik olacak rakam da olmayacak



max(something , key = someotherthing) bu komut ile bir şeyi bir şey bakımından max olmaya göre ayarlıyoruz örneğin sayıları büyüklüğe göre max olanı seçiyoruz burda key = bir şeyler neye göre max olduğunu belirtiyor.

&#x20;

dictler sıralıdır. değiştirilebilir . yinelenemez anahtarlar benzersizdir.



dict{} ile oluşturulur



dict\[keyword] ile değere ulaşılır.



dict\[adress]= 6 gibi bir örnek ile key olarak adress ekleyip 6 değerini atıyorm

.get ile dict den veri alabiliriz



list de her türlü veri tipi birlikte listelenebilir

liste ve stringi liste ve sayıyı birleştiremezsin listeye ekleme ypaarken ekleme yapacağın şeyi de listeye çevirmen gerekir .



.append() ile listenin sonuna eleman ekleyebiliriz.

.insert() ile listenin istediğiniz yerine ekleme yapabilrsinz eklediğin index teki item sağa kayar

.extend() ile listeleri genişletebilirsiniz ekleyerek. sağdakini sona ekler



list=new\_list komutu kopyalamada doğru değildir. birine bir şey eklersen 2sine de ekleniyor.

list = new\_list.copy() ya da list = list(new\_list) de olabilir .





tüple ve list birbirine eklenebilir .



for döngüsü c ye göre biraz daha farklı burda

for item in list : gibi kullanılır
print(item)





for içinde else bloğu diğer dillerin aksine kullanılır ve döngü bitince çalışır break ile sonlandıysa çalışmaz

if bloğu içinde pass kullanılabilir daha sonra kodlayacağımız şeyler için mesela .





enumarete bizi ek değişken atamaktan kurtarır .



zip ile de 2 listeyi birleştirebiliriz. listelerin boyutları matchleştiği sürece yapar yoksa görmezden gelir.



function def ile tanımlanır . eğer kaç tane parametre girileceğini bilmiyorsak örneğin inputla belirlenecekse \* kulalnılır . def my\_function(\*args) : gibi iki tane \*\* ile keywords sayısı bilinmiyorsa atanabilir : örneğin
def my\_name( \*\* kwargs):

print("His lastname is "+kwargs\["lastname"])



my\_name(firstname="Kerem", lastname="Kırmızı")  : output olarak bize function içinde printin keywordü lastname olduğu için kırmızı değerini verir .



function içinde return kullanmak daha iyi kod yazımını sağlar

&#x20;



içi boş olan function varsa hata almamak için pass komutu girebiliriz bir sıkıntı yaşatmaz.



&#x20;\* ile key = value argümanları oluştururuz.



döngü içlerinde returnler olabilir yani birden fazla return mümkündür.



7\*\*2 7 üzeri 2 demektir.



iç içe functionlar olabilir



def outer\_function(name):

def greeting():

return f"Hello, {name}!"

return greeting()



print(outer\_function("Kerem"))





Veri tipleri Python'un hazır sınıflarıdır, class ile kendi veri tipimizi tanımlarız.

class my\_class : ile sınıf oluşturabiliriz 



class ların içindeki variable lar properties olarak adlandırılır. 



class vehicle :

&#x09;brand  ="Skoda"

&#x09;model  = "Suberb"

&#x09;color = "White"

car\_c = vehicle() 

print("Brand = " , car\_c.brand)

print("Model=",car\_c.model)

print("Color=",car\_c.color)




class ların içindeki functionlar metod olarak adlandırılır . ile properties ya da metods çağrılır . 



self yer tutucusu birden fazla objeyi tek klastan üretmek için çok önemlidir örneğin : 



class Vehicle:

def init\_(self,brand,model,color): #constructor method

self.brand=brand #instance variables

self.model=mode1

self.color=color



car1\_obj=Vehicle("Skoda","Superb","White")

car2\_obj=Vehicle("Honda","Civic","Green")



print(car1\_obj.brand,"-",car1\_obj.model,"-",car1\_obj.color)

print(car2\_obj.brand,"-",car2\_obj.model,"-",car2\_obj.color)

self burda car1\_obj ve car2\_obj variable larının yerini tutar onlar atanınca onlar self in yerine geçer ve class çalışır . 



insance variable lar self ile oluşturulur self.age gibi . 



dunder / magic metodları 

\_\_init\_\_(self)

&#x09;print() 



\_\_str\_\_(self): 

&#x09;return f"Name:{self.name} \\n Age : {self.age} 

&#x20; 
 class içindeki değerler daha sonradan değiştirilebilri . 



del ile class değişkenini silebiliriz komple objecti de silebiliriz aynı komutla .





class ii boş bırakılamaz bu yüzden yine pass kullanırız. 



