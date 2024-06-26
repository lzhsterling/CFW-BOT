---

$$\color{silver} \Huge \text{\R $\sum{\vil_c = \mathbb{N\infty}}$}$$

---
---
# $\color{gold} \large \text{CFW-BOT}$
> $\color{silver} \large \text{Cloudflare workers bot}$

[🇬🇧 Dive into the English descriptions](README.md)
### ربات تلگرامی برای ایجاد وورکر کلادفلر و کانفیگ‌های xray ریموت

بدون نیاز به سرور، به راحتی می‌تونید هر تعداد کانفیگ vless-ws-tls بسازید، با چند کلیک از داخل ربات، این قطعه کد پایتون در phytonanywhere یا هر سرویس دیگه‌ای که از کد پایتون میزبانی کنه میشه اجرا کرد.
یه میانبر کوچک برای **دسترسی به اینترنت آزاد 🤍✨**


<p align="left">
  <br><img src="https://github.com/NiREvil/workers-cloudflare/blob/main/Other/pics/CFW%203.png" width="240px">
</p>

## آموزش کامل در یوتیوب: 
[![YouTube Video](https://img.youtube.com/vi/ejgTbf_yJJQ/0.jpg)](https://www.youtube.com/watch?v=ejgTbf_yJJQ)


> بهتره ویدئو قبلی که کامل هست مشاهده بشه، در صورت داشتن مشکل هنگام ساخت یا اجرای ربات داخل موبایل مشاهده این آموزش نیز خالی از لطف نیست، لطفا دانلود نکنید و از یوتیوب ببینید چون بنده خدا برای رکورد ویدئوها کلی زحمت کشیده.
 
آموزش تکمیلی با موبایل:  [![YouTube Video](https://img.youtube.com/vi/xSRcZjAQeR4/1.jpg)](https://www.youtube.com/watch?v=xSRcZjAQeR4)



           

## فهرست مطالب
- [این چیه؟](#این-چیه؟)
- [تغییرات در نسخه جدید](#تغییرات_در_نسخه_جدید)
  - [ویژگی‌ها](#ویژگی‌ها)
  - [پیش‌نیازها](#پیش‌نیازها)
  - [نصب آسان](#نصب-آسان)
  - [نصب عادی](#نصب_عادی)
  - [آپدیت ربات به نسخه آخر](#آپدیت_ربات_به_نسخه_آخر)
  - [نجوه استفاده از ربات](#نحوه-استفاده-از-ربات)
  - [پیدا کردن آسان proxyIP](#پیدا_کردن_آسان_ProxyIP)
- [نکته](#نکته)
- [نکته آخر](#نکته_آخر)
- [آموزش ایجاد بک اند مخزن آی‌پی تمیز کلادفلر](#آموزش-ایجاد-بک-اند-مخزن-آی‌پی-تمیز-کلادفلر)
- [نوشته Ni](#نوشته-Ni)

## این چیه؟
این ربات تلگرام پایتونی با استفاده از وورکر کلادفلر ساخت کانفیگ‌های Xray رو آسون میکنه! نیازی ب راه‌اندازی‌های پیچیده سمت سرور نیست، فقط این مراحل ساده رو دنبال کنید:
## تغییرات در نسخه جدید
برخی از ویژگی های اضافه شده در نسخه (v.0.03)
- بخش proxies.txt به ربات اضافه شد، حالا میتونید لیست پروکسی‌آی‌پی و آی‌پی کلادفلر‌های مورد علاقه خودتون رو در ربات ذخیره کنید و موقع ساخت یوزر جدید با یک کلیک از اون‌ها مستقیما استفاده کنید.
- قابلیت تغییر آی‌پی کاربر از قبل ایجاد شده
- لیست آی‌پی های اخیرا استفاده شده
- قابلیت ادیت وورکر به ربات اضافه شد، حالا میتونید وورکرهایی که قبلا ایجاد کردید رو ادیت کرده و از نو Deploy کنید.
- میتونید همه آی‌پی های یوزر هارو به یکباره تغییر بدید.
- کانفیگ No TLS اضافه شده، مناسب کاربرانی که دامنه شخصی بر روی کلادفلر ندارن و از لینک دامنه وورکر استفاده می‌کنند.
- اشکال حذف نشدن subworker رفع شد, حالا وقتی یوزر رو حذف می کنید؛ subscripton worker نیز حذف میشود

## برخی قابلیت های کلی ربات 
- ایجاد و حذف وورکر کلادفلر
- تعیین proxyIP از داخل ربات
- لینک ساب برای هر کاربر
- پشتیبانی لینکهای ساب از IP_API که می‌تونید با قرار دادن آی‌پی‌ های جدید در لحظه کانفیک های داخل لینک ساب رو بروزرسانی کنید.
- حل مشکل ساپورت نکردن سایت‌های پشت کلادفلر (البته دو انتخاب دارید:
> یا از آی‌پی تمیز عادی کلادفلر استفاده می‌کنید پینگ و سرعت خوبی هم دارن و همچنین هوش مصنوعی‌هایی مث GPT و Gemini و... راحت باز میشن، احتمال باز نشدن سایت‌های پشت کلادفلر 20 - 30 درصده ک اونم واسه خیلیا اهنیتی نداره اصلا چندتا سایت باز بشن یانه، می‌تونید راحت با یه آی‌پی ساده استفاده کنید، برای مثال آی‌پی های ربات تلگرام «YeBeKhe» بد نیستن [@cfcleanipbot](https://t.me/cfcleanipbot).
> کمی پایینتر روش های بیشتری نوشتم برای دریافت آی‌پی تمییز و ساخت بک‌اند.

> > ولی اونایی ک کارو زندگیشون تو خود کلادفلر هست یا تو سایت های پشت اون مث speedtest.net و check-host.net و whoer.net و یه سری سایت های دیگه.

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
> بدون دامنه هم ممکنه، با دامنه ی خود وورکر (workers.dev) ولی عملکردش قرار نیست عالی باشه
- دسترسی به حساب کلادفلر
- توکن ربات تلگرام (دریافت از `BotFather` تلگرام)
- توکن API کلادفلر `API Tokens`
- آی دی بخش وورکرز اکانت کلادفلر `Account id`
- آی دی عددی اکانت تلگرامی که می‌خواهید از ربات بر روی اون اکانتتون استفاده کنید (ربات فقط برای اکانت ارائه شده کار خواهد کرد)

# نصب آسان 
در صورت بروز خطا و اجرا نشدن از پروسه نصب عادی پیروی کنید.
```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/NiREvil/CFW-BOT/main/install.sh)"
```

## نصب عادی
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
7. دسترسی لازم برای اجرا شدن فایل  requirement.sh رو به اون بدید:
```bash
chmod +x requirement.sh
```
8. و فایل را فراخوانی کنید:
```bash
./requirement.sh
```

 "اگر به مشکلاتی در اجرای requirement.sh در PythonAnywhere همچنین برخورد کردید، کنسول را با `close` ببندید و وارد منوی Files شده و فایل requirement.sh را باز کنید سپس با `ctrl+s` آن را ذخیره کرده و ببیندید و مجدد آن را اجرا کنید. این بار به خطایی برخورد نمیکنید ."
   اگر همچنان مشکل ادامه داشت تنها کافی است فایل `requirement.sh` را با dos2unix کانورت کنید از آنجایی که سایت PythonAnyWhere از این ابزار پشتیبانی نمیکند میتونید برای اینکار از `dos2unix.py` که در پوشه پروژه قرار دارد استفاده کنید و سپس مجدد فایل `requirement.sh` را اجرا کنید.
```bash
python3 dos2unix.py
```
 
9. فایل پایتون `install.py` را اجرا کنید، این فایل با پرسیدن مقادیر API و یوزر آیدی تنظیمات لازم را برای اجرای بات به صورت خودکار انجام میدهد:
```bash
python3 install.py
```
 10. در نهایت با این دستور بات را اجرا کنید:
 ```bash
 python3 cfw.py
 ```
# نکته:
اگر بعد دوهفته یکماه یه موقع دیدید که ربات کار نمی‌کنه و به درخواست‌های شما هیچ پاسخی نمیده قطعا بخاطر سایت pythonanywhere هستش، لازمه که برید توی سایت و bash console رو باز کنید، فقط دقت کنید اگر صفحه کنسول خالی بود نیاز نیست تمام دستورات رو از ابتدا اجرا کنید نه اصلا، از قبل کلون شدن فایل‌ها، پیش نیازها نصب شدن و آماده ان، فقط کافیه که با دستور:
```bash
cd CFW-BOT
```
وارد دایرکتوری شده و سپس
با ارسال این دستور چک می‌کنه اگر آپدیت‌ جدیدی وجود داشت اون‌‌ها رو از مخزن گیت‌هاب کپی و اعمال میکنه روی دستگاه:
```bash
git pull
```

و در نهای با دستور ربات رو اجرا کنید.
```bash
python3 cfw.py
```

## آپدیت ربات به نسخه آخر
> **مورد مصرف:** موقع از کار افتادن کنسول پایتون یا نیاز به آپدیت کردن کد ربات به نسخه آخر از تک دستور زیر استفاده میکنیم:

با این دستور وارد فولدر ربات شده و مخزن گیت‌هاب پروژه رو چک کرده در صورت مشاهده تغییرات در هرکدام از فایل‌ها؛ آن ها را در سورس دستگاه اعمال کرده و در نهایت بات را اجرا میکند.
```bash
cd CFW-BOT && git pull && python3 cfw.py
```

## نحوه استفاده از ربات
وقتی ربات در حالت اجراست، فقط کافیست یک کاربر جدید در تلگرام بسازید.
برای ساخت کاربر جدید و تنظیم ساب دامنه نیازی به تنظیم کردن ساب دامنه از قبل ندارید، به صورت خودکار هر مقداری از ساب دامنه که اجرا کنید وارد میشود. ولی حتما باید دامنه آن از قبل در کلادفلر ست شده باشد.
مانند هر ورکر دیگری برای اتصال نیاز به پروکسی کلادفلر دارد، که میتواند آی پی یا وب سایتی باشد که پشت کلادفلر است.

## پیدا کردن آی‌پی یا دامنه کلادفلر:
شما از هر روشی که بلد هستید میتونید استفاده کنید (آموزش های بیشتر در رابطه پیدا کردن با آی‌پی تمییز به بخش بعدی برید، دو پاراگراف پایین تر [ایجاد بک اند](https://github.com/NiREvil/CFW-BOT/blob/main/CFW_Worker_Sub.md)).

## پیدا کردن آسان proxyIP
برای بدست آوردن آسان و سریع پروکسی‌آی‌پی مخصوص داخل وورکر پیشنهاد میکنم به این آموزش مراجعه کنید. [ده ها پروکسی آی‌پی جدید در کمتر از 60 ثانیه](https://github.com/NiREvil/vless/blob/main/sub/ProxyIP.md)

## نکته
این ربات به صورتی نوشته شده تا ارزان و سبک باشد و بر پلتفرم رایگانی مانند PyhtonAnyWhere حتی بعد از رد کردن ریت لیمیت آن قابل اجرا بماند. 

ورکر استفاده شده در فایل `index.sh` توسط من نوشته نشده و نویسنده اصلی آن را متاسفانه نمیشناسم. بعد از جستجو در بین ورکرهای موجود از این استفاده شده است، ولی بات قابلیت تنظیم شدن با ورکرهای جدید را دارد که تنها باید جهت استفاده در بات کمی تغییر داده شود.


## آموزش ایجاد بک اند مخزن آی‌پی تمیز کلادفلر

آموزش ایجاد مخزن آی‌پی تمیز کلادفلرو و بک اند برای لینک ساب ربات رو هم یاد بگیرید چون مخزن پیشفرض در معرض دید عموم قرار داده و فیلترچی میتونه کارش رو یکسره کنه، ده دقیقه ای برای خودتون رو بسازید حرفه ای پر گودرتتت  🤪
[ساخت بک اند برای لینک ساب ربات CFW](https://github.com/NiREvil/CFW-BOT/blob/main/CFW_Worker_Sub.md)

## نوشته Ni
من کد رو از مخزن شماره یک برداشتم و 85 درصدش رو ادیت کردم گذاشتم تو گیت‌هاب خودم، چون خیلی تغییرات لازم داشت خیلی زیادی از سورس کد، تمام آی‌پی کلادفلرها تمام آیپی پروکسی های وورکر دامنه و هاست ها واسه‌ی چین بود و عمرا نمیتونست سایت‌های پشت کلادفلر رو باز بکنه بقیه رو هم با مصیبت باز میکرد، فقط میشد یوتیوب و توئیتر و تلگرام گردی کرد لاکپشتی، و دوست عزیزمون فقط از مخزن شماره دوم کپی پست کرده و ویدئو براش ساخته بود.بذار اینجوری بگم، تنها چیزی که تغییر نکرده ویدئوهای یوتیوب هستن
دم هردوشون گرم کارشون عالی بود 

## نکته آخر
بعضی وقتا ممکنه در داخل ربات هنگام ساخت یوزر جدید و در مرحله ایجاد وورکر خطا بده بگه یوزر ساخته نشد و به Log های توی کنسول سر بزنید، این بخاطر استفاده از وی‌پی‌ان پیش میاد، دوتا راه داریم، یا تب مروگر که توش pythonanywhere باز هست رو ببندیم یا کلا مرورگر رو ببندیم که توی پس زمینه در حال اجرا نباشه و یا اینکه vpn خودمون رو خاموش کنیم و از پروکسی تلکرام استفاده کنیم.این مشکل بیشتر وقتی پیش میاد که مرورگر در پس زمینه در حال اجراست و ما از وی‌پی‌ان های بی کیفیت استفاده میکنیم مثل کانفیگ های v2ray، موقع استفاده از vpn های خوب مانندwindscribe, proton, pia, express, hotspotshield, nord و ... این مشکل پیش نمیاد به هیچ وجه.
سوالی بود تو کامنت‌های تلگرام بپرسید بچه ها راهنماییتون میکنن


[مخزن شماره یک  - دوست ایرانمون](https://github.com/2ri4eUI/CFW-BOT)
  
[مخزن شماره دو - دوست چینی مون](https://github.com/cmliu?tab=repositories)

  ------
  
[![Telegram Badge](https://img.shields.io/badge/Telegram-Profile-informational?style=flat&logo=telegram&logoColor=white&color=1CA2F1)](https://t.me/F_NiREvil)
   


#### کنجکاو باشید 🤍🪐
