The ``commondata.ee`` package
=============================

`Common knowledge <https://github.com/lsaffre/commondata>`_ about
Estonia. Freely available and maintained in Python.

This currently includes a list of Estonian places with zip codes.

DISCLAIMER: This comes with no warranty at all.

Usage example:

>>> from commondata.ee.places import root
>>> p = root()
>>> print(', '.join([x.name for x in p.children]))
Harju, Hiiu, Ida-Viru, Jõgeva, Järva, Lääne, Lääne-Viru, Põlva, Pärnu, Rapla, Saare, Tartu, Valga, Viljandi, Võru
>>> p = p.children[9]
>>> print(', '.join([x.name for x in p.children]))
Kehtna, Rapla, Märjamaa, Järvakandi, Juuru, Kaiu, Käru, Kohila, Vigala, Raikküla
>>> p = p.children[8]
>>> len(p.children)
26
>>> print(', '.join([x.name for x in p.children]))
Vana-Vigala, Kivi-Vigala, Kojastu, Palase, Tiduvere, Paljasmaa, Rääski, Naravere, Oese, Araste, Kurevere, Manni, Vaguja, Tõnumaa, Ojapere, Kausi, Vängla, Kesu, Pallika, Jädivere, Sääla, Läti, Leibre, Konnapere, Päärdu, Avaste
