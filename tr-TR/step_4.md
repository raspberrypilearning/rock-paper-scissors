## Sonucu Kontrol Et

Şimdi kimin kazandığını görmek için kodu ekleyelim.

+ Kimin kazandığını görmek için `oyuncu` ve `bilgisayar` değişkenlerini karşılaştırmanız gerekiyor.
    
    Eğer tercihleri aynıysa bu beraberliktir:
    
    ![ekran görüntüsü](images/rps-draw.png)

+ Bir beraberlik elde edene kadar birkaç kez oyunu oynayarak kodunuzu test edin.
    
    Yeni bir oyuna başlamak için `Run` (çalıştır) 'a tıklaman gerekir.

+ Şimdi oyuncunun 't' (taş)'ı seçtiği ancak bilgisayarın yapmadığı durumlara bakalım.
    
    Bilgisayar 'm' (makas)'ı seçerse, oyuncu kazanır (taş makası yener).
    
    Bilgisayar 'k' (kağıt)'ı seçerse, o zaman bilgisayar kazanır (kağıt, taşı yener).
    
    Oyuncunun *ve* bilgisayarın seçimini `and` fonksiyonunu kullanarak kontrol edebiliriz.
    
    ![ekran görüntüsü](images/rps-player-rock.png)

+ Şimdi oyuncunun 'k' (kağıt)'ı seçtiği ancak bilgisayarın yapmadığı durumlara bakalım:
    
    ![ekran görüntüsü](images/rps-player-paper.png)

+ Sonunda, oyuncu 'm' (makas)'ı seçtiğinde ve bilgisayar taş veya kağıt seçtiğinde kazananı kontrol etmek için kod ekleyebilir misin?

+ Şimdi kodunuzu test etmek için oyunu oynayın.
    
    ![ekran görüntüsü](images/rps-play.png)
    
    Yeni bir oyuna başlamak için `Run` (çalıştır) 'a tıklayın.