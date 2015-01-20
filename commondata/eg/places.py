# -*- coding: UTF-8 -*-
# Copyright 2014 Luc Saffre
# Copyright 2015 Modified by Mahmoud Mamdouh
# License: BSD (see file COPYING for details)

from __future__ import unicode_literals
from __future__ import print_function

from commondata.utils import Place, PlaceGenerator


class PlaceInEgypt(Place):

    def __unicode__(self):
        return self.name


class Country(PlaceInEgypt):
    value = 0

class Governorate(Country):
    value = 1

class City(Governorate):
    value = 2

class Region(City):
    value = 3

def root():

    p = PlaceGenerator()
    p.install(Country, Governorate, City, Region)
    p.set_args('name_en name_ar zip_code')

    egypt = p.country("Egypt","مصر")

    from .cairo import populate ; populate(p)
    from .giza import populate ; populate(p)
    from .alexandria import populate ; populate(p)
    from .damietta import populate ; populate(p)
    from .port_said import populate ; populate(p)
    
    return egypt
