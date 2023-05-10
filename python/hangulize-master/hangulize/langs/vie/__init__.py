# -*- coding: utf-8 -*-
from hangulize import *


class Vietnamese(Language):
    """For transcribing Vietnamese."""

    __iso639__ = {1: 'vi', 2: 'vie', 3: 'vie'}
    __tmp__ = 'X'

    vowels = 'aAeEioOuUy'
    notation = Notation([
        (u'ă',         'A'),
        (u'â',         'O'),
        (u'đ',         'D'),
        (u'ê',         'E'),
        (u'ơ',         'O'),
        (u'ư',         'U'),
        ('ch',         'C'),
        ('c',          'k'),
        ('j',          'd'),
        ('kh{@}',      'K'),
        ('ngh{e|E|i}', 'N'),
        ('ng',         'N'),
        ('nh{@}',      'nY'),
        ('anh',        'ain'),
        ('nh',         'n'),
        ('gi',         'd'),
        ('gh',         'g'),
        ('ph{@}',      'f'),
        ('qua',        'kWa'),
        ('q',          'k'),
        ('th{@}',      'T'),
        ('tr',         'C'),
        ('dz{@}',      'd'),
        ('z{@}',       'd'),
        ('ia',         'iO'),
        ('ya',         'yO'),
        ('ua',         'uO'),
        ('Ua',         'UO'),
        ('A',          'a'),
        ('y{@}',       'Y'),
        ('y',          'i'), # bl, br, bn, dr, kl, kr, pl, pr, hr rc, 
        ('C{@}',       'XC'),
        ('{@}C',       'CX'),
        ('^k',         'Xk'),
        ('k{@|l|r|W}', 'Xk'),
        ('{@}k',       'kX'),
        ('m{@}',       'Xm'),
        ('{@}m',       'mX'),
        ('n{@|Y}',     'Xn'),
        ('{@}n',       'nX'),
        ('N',          'NX'),
        ('^p',         'Xp'),
        ('p{@|l|r}',   'Xp'),
        ('{@}p',       'pX'),
        ('^t',         'Xt'),
        ('t{@|l}',     'Xt'),
        ('{@}t',       'tX'),
        ('^l',         Choseong(L)),
        ('{X}l{@}',    Choseong(L)),
        ('l{@}',       Jongseong(L), Choseong(L)),
        ('l',          Jongseong(L)),
        ('b',          Choseong(B)),
        ('XC',         Choseong(JJ)),
        ('CX',         Jongseong(G)),
        ('C',          Choseong(JJ)),
        ('d',          Choseong(J)),
        ('D',          Choseong(D)),
        ('f',          Choseong(P)),
        ('g',          Choseong(G)),
        ('h{@}',       Choseong(H)),
        ('Xk',         Choseong(GG)),
        ('kX',         Jongseong(G)),
        ('k',          Choseong(GG)),
        ('K',          Choseong(K)),
        ('Xm',         Choseong(M)),
        ('mX',         Jongseong(M)),
        ('Xn',         Choseong(N)),
        ('nX',         Jongseong(N)),
        ('NX',         Jongseong(NG)),
        ('Xp',         Choseong(BB)),
        ('pX',         Jongseong(B)),
        ('p',          Choseong(BB)),
        ('r',          Choseong(L)),
        ('s',          Choseong(S)),
        ('Xt',         Choseong(DD)),
        ('tX',         Jongseong(S)),
        ('t',          Choseong(DD)),
        ('T',          Choseong(T)),
        ('v',          Choseong(B)),
        ('x',          Choseong(SS)),
        ('z',          Choseong(K)),
        ('Wa',         Jungseong(WA)),
        ('Ya',         Jungseong(YA)),
        ('Ye',         Jungseong(YAE)),
        ('YE',         Jungseong(YE)),
        ('Yi',         Jungseong(I)),
        ('Yo',         Jungseong(YO)),
        ('YO',         Jungseong(YEO)),
        ('Yu',         Jungseong(YU)),
        ('YU',         Jungseong(YU)),
        ('a',          Jungseong(A)),
        ('e',          Jungseong(AE)),
        ('E',          Jungseong(E)),
        ('i',          Jungseong(I)),
        ('o',          Jungseong(O)),
        ('O',          Jungseong(EO)),
        ('u',          Jungseong(U)),
        ('U',          Jungseong(EU)),
    ])

    def normalize(self, string):
        return normalize_roman(string, {
            u'Ă': u'ă', u'Ằ': u'ă', u'ằ': u'ă', u'Ẳ': u'ă', u'ẳ': u'ă',
            u'Ẵ': u'ă', u'ẵ': u'ă', u'Ắ': u'ă', u'ắ': u'ă', u'Ặ': u'ă',
            u'ặ': u'ă', u'Â': u'â', u'Ầ': u'â', u'ầ': u'â', u'Ẩ': u'â',
            u'ẩ': u'â', u'Ẫ': u'â', u'ẫ': u'â', u'Ấ': u'â', u'ấ': u'â',
            u'Ậ': u'â', u'ậ': u'â', u'Đ': u'đ', u'Ê': u'ê', u'Ề': u'ê',
            u'ề': u'ê', u'Ể': u'ê', u'ể': u'ê', u'Ễ': u'ê', u'ễ': u'ê',
            u'Ế': u'ê', u'ế': u'ê', u'Ệ': u'ê', u'ệ': u'ê', u'Ơ': u'ơ',
            u'Ờ': u'ơ', u'ờ': u'ơ', u'Ở': u'ơ', u'ở': u'ơ', u'Ỡ': u'ơ',
            u'ỡ': u'ơ', u'Ớ': u'ơ', u'ớ': u'ơ', u'Ợ': u'ơ', u'ợ': u'ơ',
            u'Ư': u'ư', u'Ừ': u'ư', u'ừ': u'ư', u'Ử': u'ư', u'ử': u'ư',
            u'Ữ': u'ư', u'ữ': u'ư', u'Ứ': u'ư', u'ứ': u'ư', u'Ự': u'ư',
            u'ự': u'ư'
        })


__lang__ = Vietnamese
