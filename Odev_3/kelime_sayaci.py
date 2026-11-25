text=input("Enter A sentence:")   #input al ztaen string formatında döner . 
words = text.split() #diziye dönüştürdük. 
total_word_number = len(words) #dizide total kaç birim var onu hesaplıyor 
result1 = f"Total word number is : {total_word_number}" #fstring ile daha temiz gözükmesi 
lent= len(text) #uzunluğunu alıyoz. 
result2 = f"Total char ammount is equal to : {lent}"  #daha temiz
biggest_word= max(words, key = len) #Burada max komutu string verilince harf harf gezdiği için dizi verdim split ile 
biggest_word_l= len(biggest_word) #maximum olanın uzunluğu buluyoruz 
result3 =f"Longest word is {biggest_word} and has {biggest_word_l} character." #hem hangi word oldğunu hem de kaç harften oluştuğnu söylüyor. 
low_text= text.casefold() #casefold yaptım ki sonraki adımlarda tekrarlanan kelimeleri seçerken karışıklık olmasın . bazı özel karakter olabilir diye lower kullanmadım.    
low_words= low_text.split() #küçük harfli diziler oluşturdum. 
word_counts = {} #boş dict oluşturdum. 
for w in low_words : #w değeri tek tek low_words içinde gezecek 
                                                #get metodu dict den veri çekmek için kullanılır. 
    word_counts [w] = word_counts.get(w,0)+ 1   #eşitliğin sol tarafında bu dict içindeki key 
                                                #Değerleri atanıyor her kelime bir key oluyor, daha 
                                                #Sonra sağ tarafında bu key değerine value atanıyor en başta none almayalım diye (w,0) 0 atadık. 
                                                #o zamana kadar cümlede 1 kere geçmiş olduğu r için + 1 ekledim. 
print(word_counts)  #tekrar sayıları yazılır
print(result1)         # total word number yazılır  
print(result2)         #total harf sayısı yazılır 
print(result3)          #En çok harfli kelime ve kaç harf oldğu yazılır . 
