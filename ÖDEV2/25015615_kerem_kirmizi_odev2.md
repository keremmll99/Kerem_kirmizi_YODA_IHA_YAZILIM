
github  nedir : projemize ait tüm dosya ve değişikliklerin bulunduğu alan 	web tabanlı bir araçtır
neden github kullanırız : bilgisayarımızda oluşabilecek sorunlar yüzünden ilerlememizi kaybetmemek , önemli değşikliklerden önce kayıt almak için. github artık endüstri standartı olmuştur daha çok kullanılır . open source bir proje yayınladığımızda dünyanın 4 bir yanından geliştiricilerin ilgisin çekebiliriz.
 
Git bash kullanımına alışmam gerektiği söylendi ben de onu kullanıyorum mkdir diyerek yeni dosya oluşturuluyor cd yazarak da bu dosyanın içerisine giriyoruz

git remote add origin : bilgisayarımız git reposuna webdeki repoya bağlanmasını söylüyoruz

git push pull : kodları uzak repoya gönderme ve ordan almak içni gerekli komutlar 

git add "file name " ile dosyaya eklediğim şeyi tanımlıyorum 

dosyamın içine html yükledikten sonra git push ile webdeki repoya gönderdim 
 
git repo içinde commits e basarak istediğimiz commitde neler eklenmiş ("+" ile gösteriyor) neler çıkarılmış ("-" ile gösteriliyor) onları görüntüleyebilİRZ.
 

download. zip yaptığımızda starter-master gibi bir dosya iniyor burda starter dosyanın ismi master ise branch in ismi 

 

repo oluştururken: git . gitignore = olmasını istemediğimiz dosyaları belrittiğimiz kısım  
lisans da oluşturabiliriz lisans insanların kodu ne kadar nasıl kullanacağını belirlememizi sağlıyor. 


download ve clonlama arasındaki fark anladığım kadarıyla klonlarsak git özelliklerini de klonluyoruz 	

push etmeden önce commit etmemiz lazımmış yoksa gözükmüyor pushdan önceki tüm değişiklikleri alıyor push

github üzerinden de proje üzerinde değişiklikler yapabiliriz . 


şu ana kadar öğrendiklerimle alakalı örnekler vermek gerekirse: 

mkdir githubprojects ile githubprojects diye bir klasör oluşturuyorum 
cd githubprohects ile içine giriyorum 
mkdir starter ile githubprojects klasörü içinde starter diye bir klasör oluşturuyorum 
git add . ile şu ana kadar o dosya içine eklediğim her şeyi tanımlıyorum 
git commit -m "YORUM" ile commit ekleyip yorum yerine açıklama yazıyorum 
git push ile bunu web reposuna aktarıyorum 

web reposunda değişiklik yaptıktan sonra pcdeki repoda değişiklik yapıp push yapmak istersem hata alıyorum önce webdeki repodaki değişikliği almam lazım 

git pull = Git fetch + git merge yaparak bu değişiklikleri alıyoruz 

git push ve git pull yazdığımızda bir değişiklik yoksa bunu bize bildiriyor already up to date

biz git push ile şimdi göstersek bile bu commit ekranında bizim bilgisayarda değişikliği yaptığımız zamanda gösteriyor örneğin ben şimdi gönderdim ancak 8 dk önce commit edilmiş gözüküyor.


dosyanın aynı kısmına hem webde hem localde düzenleme yaptıktan sonra push uygularsak conflict uyarısı alıyoruz. 
hangisinin geçerli olmasını istiyorsak mesela local değişikliği korumak istiyorum , dosyayı açıp remote değişikliği ordan siliyorum. git status dersem dosyanın hem localde hem remote da değiştirildiğini belirten  both modified uyarısını alıyorum. sonra git add . ile tüm değişiklikleri tanımlayıp git commit -m "local değişikliği korudum" yazıp git push ile webe localdeki dosyayı dikte ettiriyorum . ( bu kısımda hatalı yerler olabilir kafam karıştı ancak temel mantığı kavradığıma inanıyorum).

yeni branch oluşturmak: 

git checkout -b isim  

git push origin branch ismi ile değişikliği remote a gönderebiliyoruz 

git branch ile branchleri görüntüleyebiliyoruz 

git branch -d branchadı ile branch silebilirzi 

açık kodlu yazılım : kullanıcılara değişiklik yapmak üzere açılması bazıları dağıtım hakkı vermeyebilirmiş

clear ile chati temizleyebiliyoruz . 

IHA KISMI: 

İHA Notları (Genişletilmiş)

İHA’nın Günlük Kullanım Alanları
İHA’lar yemek servisinde, yani kuryelik işlerinde kullanılır.
Uzun binaların ve camlı yapıların dış cephe temizliğinde insanların riskli yüksekliklere çıkmasına gerek bırakmaz.
Belirli bir alanın havadan görüntüleri alınarak 3D model çıktısı oluşturulabilir.
Arama kurtarma çalışmalarında, ulaşılması zor bölgelerin hızlıca taranmasını sağlar.
İHA Türleri
İHA’lar iki temel sınıfa ayrılır: multirotor ve sabit kanatlı.
Multirotor (Döner Kanat)
Birden fazla motora sahiptir (tricopter, hexacopter vb.).
İtkiyi motor sayısı belirler.
Dronun hızlı hareket edebilmesi için itkinin, dronun ağırlığının yaklaşık 2 katı olması gerekir.
Sabit Kanatlı İHA
Bu türde asıl hedef uzun mesafe uçabilmektir.
Kanatlar ileri hareket sırasında kaldırma kuvveti ürettiği için havada kalmak için motor gücüne daha az ihtiyaç duyar.
Kalkış ve iniş için piste ihtiyaç duyar.
Multirotor İHA Nasıl Çalışır? (Döner Kanat)
Hareket, motorların farklı devirlerde çalışmasıyla belirlenir.
Yaw: Dronun dikey eksen etrafında sağa-sola dönmesidir.
Roll: Yanal eksendeki harekettir, yani dronun sağa veya sola yatmasıdır.
Pitch: Dronun öne veya arkaya eğilerek ilerlemesidir.
Lift < weight: Kaldırma kuvveti ağırlıktan küçükse drone alçalır (notundaki “buna bak” kısmı bu şekilde düzeltildi).
Lift = weight: Drone yerdeyse kalkmaz, havadaysa sabit kalır (hovering).
Lift > weight: Drone yükselir.
Sabit Kanatlı İHA Nasıl Çalışır? (Fixed-Wing)
Bu konu videoda anlatılmadı.
İHA Mimarisi: Temel Bileşenler
Companion computer: Kod çalıştıran görev bilgisayarıdır ve İHA’nın içinde bulunur.
Flight controller: Verilen veriyi işler ve dronun stabil kalmasını sağlar.
Telemetry system: İHA ile yer istasyonu arasındaki iletişimi sağlar.
Sensors: GPS ve kamera gibi sensörlerin hepsi flight controller’a bağlıdır.
Ground control station: İHA’nın yerden izlendiği ve kontrol edildiği yer kontrol istasyonudur.
Motorlar
Dört haneli motor kodunda ilk iki rakam genişliği, son iki rakam yüksekliği ifade eder (örneğin 2205 kodunda 22 mm genişlik, 05 mm yükseklik).
KV, motorun her 1 volt başına yüksüz olarak dakikada kaç devir (RPM) döneceğini gösterir.
Uzun süre uçan dronelarda düşük KV tercih edilir.
Motor seçimi verimlilik ve güvenli sınırlar dikkate alınarak yapılır.
ESC Tanımı ve Çalışma Prensibi
ESC (elektronik hız kontrolcü), bataryadan gelen DC akımı, motorun dönmesi için üç fazlı AC akıma dönüştürür.
Bu sayede motorun devri kontrol edilebilir hale gelir.
Flight Controller
Uçuş kontrol cihazı (FC) temel uçuş dinamiğini yönetir.
GPS, lidar, airspeed, barometre ve manyetometre gibi entegre sensörlerden gelen tüm verileri kullanır.
EKF gibi yazılımlar sayesinde İHA anlık durumuna karar verir.
Görevleri şunlardır:
Stabilizasyon
Navigasyon
Motor yönetimi
Güvenlik protokolleri (acil durum inişleri ve failsafe)
Sensörler
Lidar/radar, yer ile arasındaki mesafeyi ölçer.
Manyetometre sapmaları tespit eder.
IMU, FC’nin içindedir ve İHA’nın ivmesini, dönüşünü ve yönelimini ölçer.
GPS hassas konum verir.
IMU (Inertial Measurement Unit)
İvme ölçer: İHA sabitken yer çekimini hisseder, ivmeleniyorsa bunu algılar.
Jiroskop: Ne kadar ve hangi hızla döndüğünü algılar.
PID Kontrolü
PID, dronun dengesini koruyan matematiksel bir kontrol sistemidir.
Hedeflenen durum ile gerçek durum arasındaki farkı (hatayı) sürekli azaltmaya çalışır.
Proportional: Anlık hataya tepki verir.
Integral: Zamanla biriken hatayı sıfırlar.
Derivative: Hatanın değişim hızını izler.
GPS
GPS hem position hold hem de waypoint görevi görür.
RTL (return to launch) güvenli dönüş sağlar.
RTK (real time kinematic GPS), GPS verilerini doğrular ve hata payını düşürür.
Sensör Füzyonu ve Genişletilmiş Kalman Filtresi (EKF)
Sensör füzyonu, farklı sensörlerin verilerini birleştirerek state estimation (durum kestirimi) üretme sürecidir.
EKF bu işi yapan yazılımsal filtrelerden biridir ve tek tek sensörlerden daha güvenilir bir sonuç elde edilmesini sağlar.
Görüntü Aktarım Sistemleri
1. Analog Görüntü Aktarım Sistemi
Daha çok FPV yarış dronlarında tercih edilir.
Avantajları neredeyse sıfır gecikme, düşük maliyet ve hafif olmasıdır.
Dezavantajı görüntü çözünürlüğünün düşük olmasıdır.
2. Dijital Görüntü Aktarım Sistemi
Görüntü önce sıkıştırılır, ardından dijital olarak iletilir.
Avantajları yüksek çözünürlük ve yüksek menzildir.
Dezavantajları gecikme olması ve maliyetin yüksek olmasıdır.
Companion Computer: İHA’nın Beyni
Görüntü işleme yapar.
Görev planlama yapar.
Yapay zeka (machine learning) işlerini yürütür.
Veri analizi yapar.
Autopilot Yazılımının Temel İşlevleri
Sensor fusion ve state estimation
Flight control
Mission management
Failsafe and safety system
Flight modes and user interfaces
PX4 Autopilot (Guide)
Flight Modes (Multicopter)

1. Manuel yardımlı modlar

Position mode: IMU, barometre ve GPS kullanır; rüzgâra karşı yerini korur.
Altitude mode: IMU ve barometre kullanır; aracın irtifasını sabit tutar. Notunda “Attitude” yazıyordu, PX4'teki mod adı Altitude olduğu için düzelttim.
Stabilized mode: Sadece IMU kullanır; yalnızca yatay duruşu korur.

2. Akrobatik modlar

Flip ve roll gibi hareketler yapılır.

3. Otonom modlar

Aşağıdaki “Otonom Modlar” başlığında listelenmiştir.
Flight Modes (Fixed Wing)
Position mode: Uçak düz rotada ilerler.
Altitude mode: GPS gerekmez, pilot roll kontrolünü yapar.
Stabilized mode: Pilot roll ve pitch açılarını kumandayla kontrol eder.
Otonom Modlar
Mission: Önceden planlanmış görevi uygular.
Hold: Bulunduğu konumda bekler.
Return: Kalkış noktasına geri döner.
Take off / land: Otomatik kalkış ve iniş yapar.
Orbit / follow me: Bir nokta etrafında döner veya bir hedefi takip eder.
Drone Programlama Kütüphaneleri ve İletişim Protokolleri
MAVLink: Komutlarımızı taşıyan bir iletişim protokolüdür.
PyMAVLink: MAVLink’in Python temsilidir ve kullanımı zordur.
MAVSDK: Modern ve kullanıcı dostu bir yaklaşım sunar.
ROS kütüphanesi: Robotik projelerde tercih edilir ve PX4 ile ArduPilot ile uyumludur.
DroneKit: Küçük ve orta ölçekli projeler için uygundur, eğitim amaçlı projeler için idealdir.
PX4 için en ideal seçenek MAVSDK’dir.

