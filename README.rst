The ``commondata.eg`` package
=============================

`Common data <https://github.com/lsaffre/commondata>`_ about
Egypt. Freely available and maintained in Python.

This currently includes a list of Egyptian places with zip codes.[ The problem about ZIP code that I don't think that we have specific range]

DISCLAIMER: This comes with no warranty at all.

Usage examples:

>>> from commondata.eg.places import root
>>> egypt = root()
>>> print(', '.join([x.name for x in egypt.children]))
El-Marg, Al Salam, Ain Shams, Al-Matariyyah, Al Zeitoun, Haddaq Al Qubbah, Al Nuzhah, Misr Al Jadidah, Al Waili, Al Zawiyah Al Hamra, Al Sharabiyah, Al Sajil, Shobra, Rud Al Faraj, Bulaq, Al Azbakeya, Manshiyat Naser, Mokattam, Madinat Nasr, Qasr al Nil, Al Zamalek, Abdin, Al Muski, Bab Al-Shaariyah, Al Azhar, Al Jamaliyah, Al-Darb al Ahmar, Al Sayidah Zaynab, Misr Al Qadimah, Al Khalifa, Al Basatin, Maadi, Turah, 15 May, Helwan, Al-Tabin, Qahirah al Jadidah, Al Shuruq, Badr, Others, Giza, Al Haram, King Faisel, Memphis, 6th of October, Sheikh Zayed, Others, Alexandria, Montazah, Alexandria Shark (East), Alexandria Wassat (Middle), Gomrok, Agami, Amriya, Borg El Arab, Others, Damietta, Ras El Bar, New Damietta, Faraskur, Al Zarqa, Kafr Saad, Others, Port Said, Port Fouad, Others





 Online version of this document on:

    https://github.com/lsaffre/commondata
    http://www.iamdevops.com/blog/2015/0117.html