# CFW-BOT
> Cloudflare workers bot

ربات وورکر کلادفلر! بدون نیاز به سرور می‌تونید هر تعداد کانفیگ Xray بسازید،  به راحتی در [PythonAnywhere] جرا میشه. یک مسیر کوتاه برای دسترسی به اینترنت آزاد ✨


<p align="left">
  <br><img src="https://github.com/NiREvil/workers-cloudflare/blob/main/Other/pics/CFW%203.png" width="420px">
</p>

## آموزش کامل در یوتیوب: 
[![YouTube Video](https://img.youtube.com/vi/ejgTbf_yJJQ/0.jpg)](https://www.youtube.com/watch?v=ejgTbf_yJJQ)


> بهتره ویدئو قبلی که کامل هست مشاهده بشه، در صورت داشتن مشکل هنگام ساخت یا اجرای ربات داخل موبایل مشاهده این آموزش نیز خالی از لطف نیست، لطفا دانلود نکنید و از یوتیوب ببینید چون بنده خدا برای رکورد ویدئوها کلی زحمت کشیده.
 
آموزش تکمیلی با موبایل:  [![YouTube Video](https://img.youtube.com/vi/xSRcZjAQeR4/1.jpg)](https://www.youtube.com/watch?v=xSRcZjAQeR4)



           

## فهرست مطالب
- [این چیه؟](#این-چیه؟)
  - [ویژگی‌ها](#ویژگی‌ها)
  - [پیش‌نیازها](#پیش‌نیازها)
  - [نصب آسان](#نصب-آسان)
  - [نجوه استفاده از ربات](#نحوه-استفاده-از-ربات)
- [نکته](#نکته)
- [آموزش ایجاد بک اند مخزن آی‌پی تمیز کلادفلر](#آموزش-ایجاد-بک-اند-مخزن-آی‌پی-تمیز-کلادفلر)
- [نوشته Ni](#نوشته-Ni)

# این چیه؟
این ربات تلگرام پایتونی با استفاده از وورکر کلادفلر ساخت کانفیگ‌های Xray رو آسون میکنه! نیازی ب راه‌اندازی‌های پیچیده سمت سرور نیست، فقط این مراحل ساده رو دنبال کنید:

## برخی قابلیت های کلی ربات 
- ایجاد و حذف وورکر کلادفلر
- تعیین proxyIP از داخل ربات
- لینک ساب برای هر کاربر
- پشتیبانی لینکهای ساب از IP_API که می‌تونید با قرار دادن آی‌پی‌ های جدید در لحظه کانفیک های داخل لینک ساب رو بروزرسانی کنید.
- حل مشکل ساپورت نکردن سایت‌های پشت کلادفلر (البته دو انتخاب دارید:
> یا از آی‌پی تمیز عادی کلادفلر استفاده می‌کنید پینگ و سرعت خوبی هم دارن و همچنین هوش مصنوعی‌هایی مث GPT و Gemini و... راحت باز میشن، احتمال باز نشدن سایت‌های پشت کلادفلر 20 - 30 درصده ک اونم واسه خیلیا اهنیتی نداره اصلا چندتا سایت باز بشن یانه، می‌تونید راحت با یه آی‌پی ساده استفاده کنید، برای مثال آی‌پی های ربات تلگرام «YeBeKhe» بد نیستن [@cfcleanipbot](https://t.me/cfcleanipbot).
> کمی پایینتر روش های بیشتری نوشتم برای دریافت آی‌پی تمییز و ساخت بک‌اند.

> > ولی اونایی ک کارو زندگیشون تو خود کلادفلر هست یا تو سایت های پشت اون مث speedtest.net و check-host.net و whoer.net و یه سری سایت های دیگه:


> شما لطفا برید [از این مخزن پروکسی](https://github.com/NiREvil/vless/blob/main/sub/ProxyIP.md) آموزش پیدا کردن پروکسی آی‌پی رو یاد بگیرید و یا از آی‌پی های آماده ایی ک اونجا هست بردارید و داخل ربات تو مرحله دوم که ازتون آی‌پی میخواد براش ارسال کنید،
- قابلبیت تغییر لینک API از داخل خود ربات
- حل مشکل نصب نشدن پیش نیازها بر روی PythonAnyWhere
## ویژگی‌ها
- **راه‌اندازی آسان**: بدون نیاز به هیچ سروری قابل اجرا بر روی میزبان‌های رایگان پایتون مانند PythonAnyWhere و یا هرکدوم دیگه.
- **پایگاه داده**: از SQLite برای مدیریت پایگاه داده استفاده میکنه، به این صورت همیشه به لیست کاربران و لینکهای آنها در خود ربات دسترسی دارید. 
- **مدیریت کاربر**: ایجاد و مدیریت چندین کاربر ب آسونی. هر کاربر به لینک‌های تولید شده خودش در هر زمان دسترسی داره.
- **راه‌اندازی بهینه**: با استفاده از Wrangler می‌تونید با سرعت کاربرهای خودتون را بسازید و اون رر بر روی کلادفلر اجرا کنید.

 ## پیش‌نیازها
- یک دامنه ثبت‌شده در کلادفلر
> بدون دامنه هم ممکنه، با دامنه ی خود وورکر (workers.dev) ولی عملکردش قرار نیست عالی باشه، خیلی معمولیه
- دسترسی به حساب کلادفلر
- توکن ربات تلگرام (دریافت از `BotFather` تلگرام)
- توکن API کلادفلر `API Tokens`
- آی دی بخش وورکرز اکانت کلادفلر `Account id`
- آی دی عددی اکانت تلگرامی که می‌خواهید از ربات بر روی اون اکانتتون استفاده کنید (ربات فقط برای اکانت ارائه شده کار خواهد کرد)

## نصب آسان
1. یک حساب رایگان در [PythonAnywhere](https://www.pythonanywhere.com) بسازید.
2. توکن‌های مورد نیاز رو بدست بیارین و همه رو یکجا یادداشت کنید لازمشون داریم.
   - توکن ربات تلگرامی ایجاد شده توسط ربات [BotFather](https://t.me/BotFather)
   - توکن API کلادفلر از داشبورد کلادفلر (تو قسمت سرچ داخل کلادفلر تایپ کنید `api tokens`. میتونید از الگوی پیشفرض `Edit Cloudflare Workers` استفاده کنید و فقط به اون دسترسی `EDIT` رو در همه بخش‌ها بدید)
   - آی‌دی عددی اکانت تلگرامتون رو می‌تونید از طریق این بات به دست بیارید: [@useridinfobot](https://t.me/useridinfobot) و یا هر بات مشابه دیگه‌ای که می‌شناسید
   - آی‌دی اکانت کلادفلر را می‌تونید از سمت راست صفحه وورکرز در کلادفلر پیدا کنید
4. در وبسایت [PythonAnywhere](https://www.pythonanywhere.com) در صفحه داشبورد؛ تب فایل‌ها را انتخاب کرده و بر روی `Open Bash Consol here` کلیک کنید.
5. حالا که توکن های مورد نیاز رو آماده کردید، می‌تونیم بریم برای اجرای کد و رباتمون. در مرحله اول پروژه را کلون کنید با دستور:
 ```bash
 git clone https://github.com/NiREvil/CFW-BOT.git
  ```
6. به فولدر پروژه برید:
```bash
cd CFW-BOT
```
7. فایل  requirement.sh را به حالت اجرایی در بیارید و آن را اجرا کنید:
```
 chmod +x requirement.txt && bash requirement.txt
```
 
8. فایل پایتون install.py را اجرا کنید، این فایل با پرسیدن مقادیر API و یوزر آیدی تنظیمات لازم را برای شروع اجرا بات به صورت خودکار انجام میدهد.
```bash
 python3 install.py
 ```
   9. حالا میتونید بات را اجرا کنید:
 ```bash
 python3 cfw.py
 ```
### نکته:
اگر بعد دوهفته یکماه یه موقع دیدید که ربات کار نمی‌کنه و به درخواست‌های شما هیچ پاسخی نمیده قطعا بخاطر سایت pythonanywhere هستش، لازمه که برید توی سایت و bash console رو باز کنید، فقط دقت کنید اگر صفحه کنسول خالی بود نیاز نیست تمام دستورات رو از ابتدا اجرا کنید نه اصلا، از قبل کلون شدن فایل‌ها، پیش نیازها نصب شدن و آماده ان، فقط کافیه که با دستور 

    cd CFW-BOT
 
وارد دایرکتوری شده و با دستور 

    python3 cfw.py
 
ربات رو اجرا کنید.



## نحوه استفاده از ربات
وقتی ربات در حالت اجراست، فقط کافیست یک کاربر جدید در تلگرام بسازید.
برای ساخت کاربر جدید و تنظیم ساب دامنه نیازی به تنظیم کردن ساب دامنه از قبل ندارید، به صورت خودکار هر مقداری از ساب دامنه که اجرا کنید وارد میشود. ولی حتما باید دامنه آن از قبل در کلادفلر ست شده باشد.
مانند هر ورکر دیگری برای اتصال نیاز به پروکسی کلادفلر دارد ، که میتواند آی پی یا وب سایتی باشد که پشت کلادفلر است . 
## پیدا کردن آی‌پی یا دامنه کلادفلیربا سرعت بالا:
شما از هر روشی که بلد هستید میتونید استفاده کنید راه پیشنهادی من:
از پلتفرم‌هایی مانند fofa.info برای پیدا کردن آی‌پی‌ها یا دامنه‌های کلادفلیر استفاده کنید.برای مثال در  fofa.info بنویسید:
```bash
server=="cloudflare" && port=="443" && country=="NL" && city=="Amsterdam"
```

برای آموزش های بیشتر در رابطه پیدا کردن با آی‌پی تمییز به بخش بعدی برید، دو پاراگراف پایین تر [ایجاد بک اند](https://github.com/NiREvil/CFW-BOT/blob/main/CFW_Worker_Sub.md)

## نکته
این ربات به صورتی نوشته شده تا ارزان و سبک باشد و بر پلتفرم رایگانی مانند PyhtonAnyWhere حتی بعد از رد کردن ریت لیمیت آن قابل اجرا بماند. 

ورکر استفاده شده در فایل `index.sh` توسط من نوشته نشده و نویسنده اصلی آن را متاسفانه نمیشناسم. بعد از جستجو در بین ورکرهای موجود از این استفاده شده است، ولی بات قابلیت تنظیم شدن با ورکرهای جدید را دارد که تنها باید 
جهت استفاده در بات کمی تغییر داده شود.

این پروژه تنها شروع است و جای زیادی برای توسعه دارد. مسلما توجه شما نسبت بهش انگیزه من را برای ارتقا دادنش افزایش میده. 
ایده هایی برای آینده 
- گرفتن پشتیبان از پایگاه داده
- تعیین محدودیت زمانی یا در صورت امکان حجمی برای کاربران
- استفاده از اسکریپتهای ورکر مختلف
- اتصال به گیتهاب برای ایجاد لینک اشتراک
- نمایش اطلاعات پروکسی کلادفلر، مانند لوکیشن آن

# آموزش ایجاد بک اند مخزن آی‌پی تمیز کلادفلر

آموزش ایجاد مخزن آی‌پی تمیز کلادفلرو و بک اند برای لینک ساب ربات رو هم یاد بگیرید چون مخزن پیشفرض در معرض دید عموم قرار داده و فیلترچی میتونه کارش رو یکسره کنه، ده دقیقه ای برای خودتون رو بسازید حرفه ای پر گودرتتت  🤪
[ساخت بک اند برای لینک ساب ربات CFW](https://github.com/NiREvil/CFW-BOT/blob/main/CFW_Worker_Sub.md)

# نوشته Ni
من کد رو از مخزن شماره یک برداشتم و 85 درصدش رو ادیت کردم گذاشتم تو گیت‌هاب خودم، چون خیلی تغییرات لازم داشت خیلی زیادی از سورس کد، تمام آی‌پی کلادفلرها تمام آیپی پروکسی های وورکر دامنه و هاست ها واسه‌ی چین بود و عمرا نمیتونست سایت‌های پشت کلادفلر رو باز بکنه بقیه رو هم با مصیبت باز میکرد، فقط میشد یوتیوب و توئیتر و تلگرام گردی کرد لاکپشتی، و دوست عزیزمون فقط از مخزن شماره دوم کپی پست کرده و ویدئو براش ساخته بود.بذار اینجوری بگم، تنها چیزی که تغییر نکرده ویدئوهای یوتیوب هستن
دم هردوشون گرم کارشون عالی بود 


[مخزن شماره یک  - دوست ایرانمون](https://github.com/2ri4eUI/CFW-BOT)
  
[مخزن شماره دو - دوست چینی مون](https://github.com/cmliu?tab=repositories)

   ------
  **~هر سوالی از هر بخش که داشتید تو تلگرام داخل کامنت‌ها بپرسید.**

  
[![Telegram Badge](https://img.shields.io/badge/Telegram-Profile-informational?style=flat&logo=telegram&logoColor=white&color=1CA2F1)](https://t.me/F_NiREvil)
   


#### کنجکاو باشید 🤍🪐
