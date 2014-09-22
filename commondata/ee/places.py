# -*- coding: UTF-8 -*-
# Copyright 2014 Luc Saffre
# License: BSD (see file COPYING for details)

from __future__ import unicode_literals
from __future__ import print_function

from commondata.utils import Place, PlaceGenerator


class PlaceInEstonia(Place):

    def __unicode__(self):
        return self.name


class Country(PlaceInEstonia):
    value = 0


class County(PlaceInEstonia):
    value = 1
    # maakond


class Municipality(PlaceInEstonia):
    value = 2
    # vald


class Town(Municipality):
    pass
    # linn


class Township(Town):
    value = 3
    # linnaosa


class Village(PlaceInEstonia):
    value = 5
    # küla


class SmallBorough(Village):
    pass
    # alevik


class Borough(SmallBorough):
    pass
    # alev


def root():

    p = PlaceGenerator()
    p.install(Country, County, Town, Township, Municipality, Borough,
              SmallBorough, Village)
    p.set_args('name zip_code')

    eesti = p.country("Eesti")

    from .harju import populate ; populate(p)
    from .hiiu import populate ; populate(p)
    from .idaviru import populate ; populate(p)
    from .j6geva import populate ; populate(p)
    from .jarva import populate ; populate(p)
    from .laane import populate ; populate(p)
    from .laaneviru import populate ; populate(p)
    from .p6lva import populate ; populate(p)
    from .parnu import populate ; populate(p)
    from .rapla import populate ; populate(p)
    from .saare import populate ; populate(p)
    from .tartu import populate ; populate(p)
    from .valga import populate ; populate(p)
    from .viljandi import populate ; populate(p)
    from .v6ru import populate ; populate(p)
    
    return eesti
