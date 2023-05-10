# -*- coding: utf-8 -*-
from hangulize import *


class Ukrainian(Language):
    """For transcribing Ukrainian."""

    __iso639__ = {1: 'uk', 2: 'ukr', 3: 'ukr'}
    __tmp__ = ',;'

    vowels = u'аеєиіїйоOуьюя'
    cs = u'бвгґджзклмнпрстфхцчшщ'
    vl = u'кпстфхцчшщ'
    notation = Notation([
        ('-', '/'),
        (u'{ж|з|ц|ч|ш|щ}ь{@}', None),
        (u'ьа', u'я'),
        (u'йа', u'я'),
        (u'ье', u'є'),
        (u'йе', u'є'),
        (u'ьи', u'ї'),
        (u'йи', u'ї'),
        (u'ьі', u'ї'),
        (u'йі', u'ї'),
        (u'ьо', u'O'),
        (u'йо', u'O'),
        (u'ьу', u'ю'),
        (u'йу', u'ю'),
        (u'^ль', u'лі'),
        (u'^мь', u'мі'),
        (u'^нь', u'ні'),
        (u'{л|м|н}ь{є|ю|я|O}', u'і'),
        (u'{л|м|н}ь{ї|й}', None),
        (u'{л|м|н}ь$', None),
        (u'{л|м|н}ь{<cs>}', None),
        (u'{<cs>}\'{є|ї|й|ю|я|O}', u'і'),
        (u'бб', u'б'),
        (u'гг', u'г'),
        (u'ґґ', u'ґ'),
        (u'дд', u'д'),
        (u'дс', u'дз'),
        (u'жж', u'ж'),
        (u'зз', u'з'),
        (u'кк', u'к'),
        (u'лл', u'л'),
        (u'{@}мм{@}', u'м,м'),
        (u'мм', u'м'),
        (u'{@}нн{@}', u'н,н'),
        (u'нн', u'н'),
        (u'пп', u'п'),
        (u'рр', u'р'),
        (u'сс', u'с'),
        (u'тт', u'т'),
        (u'тц', u'ц'),
        (u'тч', u'ч'),
        (u'фф', u'ф'),
        (u'хх', u'х'),
        (u'цц', u'ц'),
        (u'чч', u'ч'),
        (u'шш', u'ш'),
        (u'щщ', u'щ'),
        (u'{з|с|ц}ь', None),
        (u'{и|і|ї}й', None),
        (u'{@}ь', None),
        (u'тс', u'ц'),
        (u'дз', u'з'),
        (u'тз', u'з'),
        (u'нкт', u'Nт'),
        (u'^в{<cs>}', u'у'),
        (u'{@}в{<cs>}', u'у'),
        (u'{@}в$', u'у'),
        (u'{@}к{<vl>}', u'к,'),
        (u'{@}п{<vl>}', u'п,'),
        (u'{@}т{<vl>}', u'т,'),
        (u'{ж|з|ц|ч}O', u'о'),
        (u'{ж|з|ц|ч}ю', u'у'),
        (u'{ж|з|ц|ч}я', u'а'),
        (u'щ', u'ш'),
        (u'{<cs>}є', u'е'),
        (u'ша', u'ся'),
        (u'ше', u'сє'),
        (u'шо', u'сO'),
        (u'шу', u'сю'),
        (u'ш{и|і|ї|й|ь}', u'с'),
        (u'ш$', u'сі'),
        (u'ш', u'сю'),
        (u'дж{@}', u'з'),
        (u'дж', u'зі'),
        (u'ж{@}', u'з'),
        (u'ж', u'зу'),
        (u'ч{@}', u'ц'),
        (u'ч', u'чі'),
        (u'^л', u'л;'),
        (u'^м', u'м;'),
        (u'^н', u'н;'),
        (u'л$', u'л,'),
        (u'м$', u'м,'),
        (u'н$', u'н,'),
        (u'л{@|м,|н,|N}', u'л;'),
        (u'м{@}', u'м;'),
        (u'н{@}', u'н;'),
        (u'л', u'л,'),
        (u'м', u'м,'),
        (u'н', u'н,'),
        (u',,', u','),
        (u',;', None),
        (u',л,', u'л,'),
        (u',м,', u'м,'),
        (u',н,', u'н,'),
        (u'л{м;|н;}', u'л,'),
        (u';', None),
        (u'б', Choseong(B)),
        (u'в', Choseong(B)),
        (u'г', Choseong(H)),
        (u'ґ', Choseong(G)),
        (u'д', Choseong(D)),
        (u'ж', Choseong(J)),
        (u'з', Choseong(J)),
        (u'ж', Choseong(J)),
        (u'к,', Jongseong(G)),
        (u'к', Choseong(K)),
        (u'^л', Choseong(L)),
        (u'л,', Jongseong(L)),
        (u'л', Jongseong(L), Choseong(L)),
        (u'м,', Jongseong(M)),
        (u'м', Choseong(M)),
        (u'н,', Jongseong(N)),
        (u'н', Choseong(N)),
        (u'N', Jongseong(NG)),
        (u'п,', Jongseong(B)),
        (u'п', Choseong(P)),
        (u'р', Choseong(L)),
        (u'с', Choseong(S)),
        (u'т,', Jongseong(S)),
        (u'т', Choseong(T)),
        (u'ф', Choseong(P)),
        (u'х', Choseong(H)),
        (u'ц', Choseong(C)),
        (u'ч', Choseong(C)),
        (u'а', Jungseong(A)),
        (u'е', Jungseong(E)),
        (u'є', Jungseong(YE)),
        (u'O', Jungseong(YO)),
        (u'и', Jungseong(I)),
        (u'і', Jungseong(I)),
        (u'ї', Jungseong(I)),
        (u'й', Jungseong(I)),
        (u'о', Jungseong(O)),
        (u'у', Jungseong(U)),
        (u'ь', Jungseong(I)),
        (u'ю', Jungseong(YU)),
        (u'я', Jungseong(YA)),
    ])

    def normalize(self, string):
        return normalize_roman(string, {
            u'А': u'а', u'Б': u'б', u'В': u'в', u'Г': u'г', u'Ґ': u'ґ',
            u'Д': u'д', u'Е': u'е', u'Є': u'є', u'Ж': u'ж', u'З': u'з',
            u'И': u'и', u'І': u'і', u'Ї': u'ї', u'Й': u'й', u'К': u'к',
            u'Л': u'л', u'М': u'м', u'Н': u'н', u'О': u'о', u'П': u'п',
            u'Р': u'р', u'С': u'с', u'Т': u'т', u'У': u'у', u'Ф': u'ф',
            u'Х': u'х', u'Ц': u'ц', u'Ч': u'ч', u'Ш': u'ш', u'Щ': u'щ',
            u'Ь': u'ь', u'Ю': u'ю', u'Я': u'я'
        })


__lang__ = Ukrainian
