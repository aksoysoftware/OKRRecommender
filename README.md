OKR (Hedef ve Anahtar Sonuçlar), bir kurumun veya bireyin belirli bir süre içinde ulaşmak istediği hedefleri ve bu hedeflere ulaşmak için alınacak önlemleri belirlemek için kullanılan bir performans yönetimi aracıdır.Google, Intel vb gibi şirketler çalışanlarını bu şekilde motive eder ve çok başarılı metodolojidir .Bu projedeki amacımız kişiye özel Hedefler belirleyen bir uygulama geliştirmektir.

Uygulama, geçmiş OKR verilerini saklamak için SQLite veritabanını kullanır. historicalOkr tablosu, CV ID, ad, talep tarihi, geçmiş, OKR, kullanıcı e-postası ve yönetici e-postası gibi bilgileri depolamak için oluşturulmuştur.


Uygulama openAI api kullanır,  Kullanıcının girişi, önceden belirlenmiş İK ile ilgili önerilerle birleştirilir ve OKR önerilerini almak için OpenAI API ile etkileşime geçilir.


send_email fonksiyonu, üretilen OKR sonuçlarını kullanıcıya ve yöneticisine içeren e-postaları göndermekle sorumludur. E-postalar, üretilen OKR içeriğini ve geçmiş OKR değerlerini içerir.




![WhatsApp Image 2023-08-15 at 19 46 14](https://github.com/aksoysoftware/okrs/assets/99371051/d99f2b26-d3f7-4684-9a2e-47c9bfdc9a1c)
![43215697-82b9-4a8f-bde4-f62b195b465f](https://github.com/aksoysoftware/okrs/assets/99371051/40fe05bd-ba43-49ec-b151-69523cf589e5)
![290904565-5b8ffe11-3da2-467e-8340-43d0585d2b1f](https://github.com/aksoysoftware/okrs/assets/99371051/1ebb1545-3305-4478-b82e-093051ae89ca)

1. Kullanıcı Bilgilerinin Girişi:
Kullanıcı, ana sayfada bulunan giriş alanlarına adını, pozisyonunu, yeteneklerini, geliştirmesi gereken becerilerini ve iletişim bilgilerini girer.
2. Sorulara Cevap Verme:
Kullanıcı, ilgili sorulara cevaplar verir. Bu sorular kullanıcının pozisyonunu, yeteneklerini, geliştirmesi gereken alanları ve fırsatları içerir. Her sorunun yanında bir "?" düğmesi bulunur, bu düğmeye tıklanarak daha fazla açıklama alınabilir.
3. OKR Önerileri Üretimi:
Kullanıcının verdiği cevaplar ve bilgiler, OpenAI API ile işlenir. Bu süreçte, kullanıcının pozisyonu, yetenekleri ve hedefleri analiz edilir. Sonuç olarak, kullanıcıya uygun ve özelleştirilmiş OKR önerileri üretilir.
4. Önerilerin Sunumu:
Kullanıcıya üretilen OKR önerileri sunulur. Bu öneriler, hedeflerin ve anahtar sonuçların bulunduğu açıklamalarla birlikte gelir. Kullanıcı, bu önerileri performans yönetimi ve hedef belirleme süreçlerinde kullanabilir.
5. E-posta Bildirimi:
Kullanıcının verdiği iletişim bilgileri (e-posta) kullanılarak, kullanıcıya ve yöneticisine üretilen OKR önerileri e-posta olarak gönderilir. Kullanıcı, bu e-postaları inceleyerek daha sonra başvurabilir.
6. Geçmiş OKR Kayıtları:
Kullanıcının daha önceki OKR önerileri kaydedilir ve kullanıcının adıyla ilişkilendirilir. Kullanıcı, bu geçmiş kayıtları gözden geçirebilir ve gelecekteki hedeflerini daha iyi belirlemek için kullanabilir.
7. Yardım ve Soruların Cevaplanması:
Kullanıcı, her sorunun yanındaki "?" düğmesine tıklayarak ilgili sorunun açıklamasını görüntüleyebilir. Bu açıklamalar, kullanıcının daha iyi anlamasını sağlar.
8. Kullanıcı Verilerinin Güvenliği:
Kullanıcının sağladığı veriler, gizlilik ve güvenlik önlemleri altında işlenir ve saklanır. Bu, kullanıcının kişisel ve iş bilgilerinin korunduğundan emin olmayı sağlar.
9. Hızlı ve Özelleştirilmiş Süreç:
OKRecommender, kullanıcıların hızlı ve özelleştirilmiş OKR önerileri almasını sağlar. Kullanıcıların hedeflerini ve yeteneklerini dikkate alarak gerçek zamanlı öneriler sunar.
10. Kolay Kullanıcı Deneyimi:
Arayüz, kullanıcı dostu ve sezgisel bir şekilde tasarlanmıştır. Kullanıcıların kolayca bilgilerini girebilmeleri ve sonuçları alabilmeleri amaçlanmıştır.


