The ``commondata.eg`` package
=============================

`Common data <https://github.com/lsaffre/commondata>`_ about
Egypt. Freely available and maintained in Python.

This currently includes a list of Egyptian places with zip codes.[ The problem about ZIP code that I don't think that we have specific range]

DISCLAIMER: This comes with no warranty at all.
+ Ver 0.0.2:
    Add Arabic name to Cities and Country
+ Ver 0.0.1:
    Based
Usage examples:

>>> from commondata.eg.places import root
>>> egypt = root()
>>> print(', '.join([x.name_en for x in egypt.children]))
El-Marg, Al Salam, Ain Shams, Al-Matariyyah, Al Zeitoun, Haddaq Al Qubbah, Al Nuzhah, Misr Al Jadidah, Al Waili, Al Zawiyah Al Hamra, Al Sharabiyah, Al Sajil, Shobra, Rud Al Faraj, Bulaq, Al Azbakeya, Manshiyat Naser, Mokattam, Madinat Nasr, Qasr al Nil, Al Zamalek, Abdin, Al Muski, Bab Al-Shaariyah, Al Azhar, Al Jamaliyah, Al-Darb al Ahmar, Al Sayidah Zaynab, Misr Al Qadimah, Al Khalifa, Al Basatin, Maadi, Turah, 15 May, Helwan, Al-Tabin, Qahirah al Jadidah, Al Shuruq, Badr, Others, Giza, Al Haram, King Faisel, Memphis, 6th of October, Sheikh Zayed, Others, Alexandria, Montazah, Alexandria Shark (East), Alexandria Wassat (Middle), Gomrok, Agami, Amriya, Borg El Arab, Others, Damietta, Ras El Bar, New Damietta, Faraskur, Al Zarqa, Kafr Saad, Others, Port Said, Port Fouad, Others
>>> print(', '.join([x.name_ar for x in egypt.children]))
المرج, السلام, عين شمس, المطرية, الزيتون, حدائق القبة, النزهة, مصر الجديدة, الوايلي, الزاوية الحمراء, الشرابية, السجل, شبرا, روض الفرج, بولاق, الأزبكية, منشية نصر, المقطم, مدينة نصر, قصر النيل, الزمالك, عبدين, الموسكي, باب الشعرية, الأزهر, الجمالية, الدرب الأحمر, السيد زينب, مصر القديمة, الخليفة, البساتين, المعادي, طرة, 15 مايو, حلوان, التبين, القاهرة الجديدة, الشروق, بدر, اخرى, الجيزة, الهرم, الملك فيصل, ممفيس, السادس من اكتوبر, الشيخ زايد, اخرى, الإسكندري, المنتزة, شرق الإسكندرية, غرب الإسكندرية, الجمرك, العجمي, الاميرية, برج العرب, اخرى, دمياط, رأس البر, دمياط الجديدة, فارسكور, الزرقا, كفر سعد, اخرى, بورسعيد, بورفؤاد, اخرى




 Online version of this document on:

    https://github.com/lsaffre/commondata
    http://www.iamdevops.com/blog/2015/0117.html