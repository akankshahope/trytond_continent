#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
from .continent import *


def register():
    Pool.register(
        Continent,
        module='continent', type_='model')
