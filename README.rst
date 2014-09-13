The ``commondata.ee`` package
=============================

`Common data <https://github.com/lsaffre/commondata>`_ about
Estonia. Freely available and maintained in Python.

Note: we are discussing whether this package is meaningful.  
See http://lino-framework.org/tickets/109.html

This currently includes a list of Estonian places with zip codes.

DISCLAIMER: This comes with no warranty at all.

Usage examples:

>>> from commondata.ee.places import root
>>> eesti = root()
>>> print(', '.join([x.name for x in eesti.children]))
Harju, Hiiu, Ida-Viru, Jõgeva, Järva, Lääne, Lääne-Viru, Põlva, Pärnu, Rapla, Saare, Tartu, Valga, Viljandi, Võru
>>> raplamaa = eesti.children[9]
>>> print(', '.join([x.name for x in raplamaa.children]))
Kehtna, Rapla, Märjamaa, Järvakandi, Juuru, Kaiu, Käru, Kohila, Vigala, Raikküla
>>> vigala = raplamaa.children[8]
>>> len(vigala.children)
26
>>> print(', '.join([x.name for x in vigala.children]))
...  #doctest: +NORMALIZE_WHITESPACE
Vana-Vigala, Kivi-Vigala, Kojastu, Palase, Tiduvere, Paljasmaa,
Rääski, Naravere, Oese, Araste, Kurevere, Manni, Vaguja, Tõnumaa,
Ojapere, Kausi, Vängla, Kesu, Pallika, Jädivere, Sääla, Läti, Leibre,
Konnapere, Päärdu, Avaste

>>> v6rumaa = eesti.children[14]
>>> print(v6rumaa.name)
Võru
>>> print(', '.join([x.name for x in v6rumaa.children]))
Vastseliina, Võru, Antsla, Varstu, Sõmerpalu, Rõuge, Mõniste, Haanja, Urvaste, Lasva, Misso, Meremäe, Kirumpää, Navi, Meegomäe
>>> haanja = v6rumaa.children[7]
>>> print(haanja.name)
Haanja
>>> print(', '.join([x.name for x in haanja.children]))
...  #doctest: +NORMALIZE_WHITESPACE
Pausakunnu, Andsumäe, Mustahamba, Mäe-Suhka, Mäe-Tilga, Tsiamäe,
Soodi, Trolla, Purka, Posti, Kirbu, Vaarkali, Kääraku, Tsiiruli,
Haavistu, Tsilgutaja, Lillimõisa, Saluora, Märdimiku, Rusa,
Vastsekivi, Käänu, Holdi, Vaalimäe, Tõnkova, Mäe-Palo, Pressi,
Kergatsi, Kuiandi, Ihatsi, Kaldemäe, Raagi, Horoski, Pillardi, Külma,
Kaaratautsa, Sarise, Saika, Hulaku, Palanumäe, Preeksa, Naapka,
Kriguli, Ala-Suhka, Sormuli, Vihkla, Kuklase, Palli, Ruusmäe,
Loogamäe, Meelaku, Murati, Uue-Saaluse, Lüütsepä, Ala-Palo, Mallika,
Mahtja, Kaloga, Vungi, Ala-Tilga, Resto, Leoski, Palujüri, Tummelka,
Vänni, Hanija, Plaksi, Kilomani, Piipsemäe, Luutsniku, Puspuri,
Hämkoti, Simula, Vorstimäe, Miilimäe, Kuura, Kõomäe, Söödi, Plaani,
Vakari, Peedo, Tuuka, Pundi, Kotka
>>> len(haanja.children)
84
>>> print(haanja.children[77].name)
Söödi
>>> print(haanja.children[6].name)
Soodi

>>> harju = eesti.children[0]
>>> tallinn = harju.children[0]
>>> print tallinn.name
Tallinn
>>> print(', '.join([x.name for x in tallinn.children]))
...  #doctest: +NORMALIZE_WHITESPACE
Haabersti, Kesklinn, Kristiine, Lasnamäe, Mustamäe, Nõmme, Pirita, Põhja-Tallinn
