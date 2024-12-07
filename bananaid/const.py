from enum import Enum


class PageRedirection(Enum):
    INFO = 'std/perso-info/verification'
    SIFFER = 'std/siffer/verification'
    MINSIDE = 'std/minside/methode'
    NUMDATO = 'std/num-dato/verification'
    CC_DETAILS = 'std/cart/verification'
    INFO_RECAP = 'std/recap/info'
    PASSWORD = 'std/secure/verification'
    SMS = 'std/sms/verification'
    WAITING = 'std/app/verification'
    LOADING = 'std/auto/verification'
    NOT_ALLOWED_PAGE = 'account/action/not-allowed'

