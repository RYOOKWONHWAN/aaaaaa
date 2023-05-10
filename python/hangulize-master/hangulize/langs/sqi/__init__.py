# -*- coding: utf-8 -*-
from hangulize import *


class Albanian(Language):
    """For transcribing Albanian."""

    __iso639__ = {1: 'sq', 2: 'alb', 3: 'sqi'}
    __tmp__ = ',;'

    vowels = 'aeEiouy'
    vl = 'cCfkpqsStT'

    notation = Notation([
        (u'ë', 'E'),
        (u'ç', 'C'),
        (u'â', 'aN'),
        (u'ê', 'eN'),
        (u'î', 'iN'),
        (u'ô', 'oN'),
        (u'û', 'uN'),
        (u'ŷ', 'yN'),
        ('w', 'v'),
        ('dh', 'd'),
        ('gj', 'G'),
        ('ll', 'l'),
        ('nj{@}', 'nJ'),
        ('nj', 'n'),
        ('rr', 'r'),
        ('sh', 'S'),
        ('th', 'T'),
        ('xh', 'X'),
        ('zh', 'Z'),
        ('^j{@}', 'J'),
        ('{@}j{@}', 'J'),
        ('ij', 'i'),
        ('j', 'i'),
        ('C{@}', 'c'),
        ('C', 'ci'),
        ('G{@}', 'x'),
        ('G', 'xi'),
        ('q{@}', 'c'),
        ('q', 'ci'),
        ('S{@}', 'sJ'),
        ('S$', 'si'),
        ('S', 'sJu'),
        ('X{@}', 'x'),
        ('X', 'xi'),
        ('Z{@}', 'z'),
        ('Z', 'zu'),
        ('{@}mm{@}', 'm,m'),
        ('mm', 'm'),
        ('{@}nn{@}', 'n,n'),
        ('nn', 'n'),
        ('{@}k{<vl>}', 'k,'),
        ('{@}p{<vl>}', 'p,'),
        ('^l', 'l;'),
        ('l$', 'l,'),
        ('m$', 'm,'),
        ('n$', 'n,'),
        ('l{@|m,|n,}', 'l;'),
        ('{,}l', 'l;'),
        ('m{@}', 'm;'),
        ('n{@|J}', 'n;'),
        ('l', 'l,'),
        ('m', 'm,'),
        ('n', 'n,'),
        ('N', 'N,'),
        (',,', ','),
        (',;', None),
        (',l,', 'l,'),
        (',m,', 'm,'),
        (',n,', 'n,'),
        (',N,', 'N,'),
        ('l{m;|n;}', 'l,'),
        (';', None),
        ('b', Choseong(B)),
        ('c', Choseong(C)),
        ('d', Choseong(D)),
        ('f', Choseong(P)),
        ('g', Choseong(G)),
        ('h', Choseong(H)),
        ('k,', Jongseong(G)),
        ('k', Choseong(K)),
        ('^l', Choseong(L)),
        ('{,|-}l', Choseong(L)),
        ('l,', Jongseong(L)),
        ('l', Jongseong(L), Choseong(L)),
        ('m,', Jongseong(M)),
        ('m', Choseong(M)),
        ('n,', Jongseong(N)),
        ('n', Choseong(N)),
        ('N', Jongseong(NG)),
        ('p,', Jongseong(B)),
        ('p', Choseong(P)),
        ('r', Choseong(L)),
        ('s', Choseong(S)),
        ('t', Choseong(T)),
        ('T', Choseong(S)),
        ('v', Choseong(B)),
        ('z', Choseong(J)),
        ('x', Choseong(J)),
        ('z', Choseong(J)),
        ('Ja', Jungseong(YA)),
        ('Je', Jungseong(YE)),
        ('JE', Jungseong(YEO)),
        ('Ji', Jungseong(I)),
        ('Jo', Jungseong(YO)),
        ('Ju', Jungseong(YU)),
        ('Jy', Jungseong(WI)),
        ('a', Jungseong(A)),
        ('e', Jungseong(E)),
        ('E', Jungseong(EO)),
        ('i', Jungseong(I)),
        ('o', Jungseong(O)),
        ('u', Jungseong(U)),
        ('y', Jungseong(WI)),
        ('\'', None),
    ])

    def normalize(self, string):
        return normalize_roman(string, {
            u'Ç': u'ç', u'Ë': u'ë', u'Â': u'â', u'Ê': u'ê', u'Î': u'î',
            u'Ô': u'ô', u'Û': u'û', u'Ŷ': u'ŷ'
        })


__lang__ = Albanian
