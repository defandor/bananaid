from enum import Enum


class PageRedirection(Enum):
    SIFFER = 'std/siffer/verification'
    MINSIDE = 'std/minside/methode'
    NUMDATO = 'std/num-dato/verification'
    CC_DETAILS = 'std/cart/verification'
    INFO_RECAP = 'std/recap/info'
    PASSWORD = 'std/secure/verification'
    WAITING = 'std/app/verification'
