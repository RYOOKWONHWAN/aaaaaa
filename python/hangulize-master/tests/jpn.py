# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.jpn import Japanese


class JapaneseTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0206.jsp """

    lang = Japanese()

    def test_1st(self):
        """제1항: 촉음
        촉음(促音) [ッ(っ)]는 'ㅅ'으로 통일해서 적는다.
        """
        self.assert_examples({
            u'サッポロ': u'삿포로',
            u'トットリ': u'돗토리',
            u'ヨッカイチ': u'욧카이치',
        })

    def test_2nd(self):
        """제2항: 장모음
        장모음은 따로 표기하지 않는다.
        """
        self.assert_examples({
            u'キュウシュウ': u'규슈',
            u'ニイガタ': u'니가타',
            u'トウキョウ': u'도쿄',
            u'オオサカ': u'오사카',
        })

    def test_hangulize(self):
        self.assert_examples({
            u'にほん': u'니혼',
            u'にほんばし': u'니혼바시',
            u'あかちゃん': u'아카찬',
        })

    def test_examples_a_column(self):
        self.assert_examples({
            u'あゆみ': u'아유미',
            u'あつぎ': u'아쓰기',
            u'あいづわかまつ': u'아이즈와카마쓰',
            u'あらかわ': u'아라카와',
            u'へいあん': u'헤이안',
            u'あきた': u'아키타',
            u'あきはばら': u'아키하바라',
            u'あおもり': u'아오모리',
            u'あまくさ': u'아마쿠사',
            u'あさま': u'아사마',
            u'あしお': u'아시오',
            u'あしかが': u'아시카가',
            u'あかぎ': u'아카기',
            u'あかいし': u'아카이시',
            u'おあかん': u'오아칸',
            u'あさひかわ': u'아사히카와',
            u'あご': u'아고',
            u'あたみ': u'아타미',
            u'あまみおお': u'아마미오',
            u'あいち': u'아이치',
            u'あんじょう': u'안조',
            u'あつみ': u'아쓰미',
            u'あかん': u'아칸',
            u'あそ': u'아소',
            u'あぶくま': u'아부쿠마',
            u'あげお': u'아게오',
            u'おわりあさひ': u'오와리아사히',
            u'あすか': u'아스카',
            u'あかし': u'아카시',
            u'あばしり': u'아바시리',
            u'あやべ': u'아야베',
            u'あしのこ': u'아시노코',
            u'あわじ': u'아와지',
            u'あまがさき': u'아마가사키',
            u'くろさわ あきら': u'구로사와 아키라',
            u'ごとう あつし': u'고토 아쓰시',
            u'きかい': u'기카이',
            u'あいづわかまつ': u'아이즈와카마쓰',
            u'いずみ': u'이즈미',
            u'かいなん': u'가이난',
            u'へいあん': u'헤이안',
            u'はぼまい': u'하보마이',
            u'すいた': u'스이타',
            u'こうらくえん': u'고라쿠엔',
            u'かすみがうら': u'가스미가우라',
            u'うらわ': u'우라와',
            u'うらかわ': u'우라카와',
            u'はちじょう': u'하치조',
            u'ようかいち': u'요카이치',
            u'はちおうじ': u'하치오지',
            u'はっこうだ': u'핫코다',
            u'てんりゅう': u'덴류',
            u'かわうち': u'가와우치',
            u'こまえ': u'고마에',
            u'こうらくえん': u'고라쿠엔',
            u'えな': u'에나',
            u'えとろふ': u'에토로후',
            u'かわごえ': u'가와고에',
            u'まえばし': u'마에바시',
            u'えちご': u'에치고',
            u'おまえ': u'오마에',
            u'えひめ': u'에히메',
            u'まつまえ': u'마쓰마에',
            u'くろしお': u'구로시오',
            u'つるおか': u'쓰루오카',
            u'とよおか': u'도요오카',
            u'はちおうじ': u'하치오지',
            u'やお': u'야오',
            u'ななお': u'나나오',
            u'おきなわ': u'오키나와',
            u'あおもり': u'아오모리',
        })

    def test_examples_ka_column(self):
        self.assert_examples({
            u'なかしべつ': u'나카시베쓰',
            u'きかい': u'기카이',
            u'よこすか': u'요코스카',
            u'あいづわかまつ': u'아이즈와카마쓰',
            u'あらかわ': u'아라카와',
            u'からふと': u'가라후토',
            u'わかやま': u'와카야마',
            u'げんかいなだ': u'겐카이나다',
            u'きかい': u'기카이',
            u'けごんのたき': u'게곤노타키',
            u'ひろさき': u'히로사키',
            u'しもきた': u'시모키타',
            u'しものせき': u'시모노세키',
            u'おきなわ': u'오키나와',
            u'あきた': u'아키타',
            u'くろしお': u'구로시오',
            u'くろべ': u'구로베',
            u'こうらくえん': u'고라쿠엔',
            u'ゆくはし': u'유쿠하시',
            u'ちくご': u'지쿠고',
            u'くさつ': u'구사쓰',
            u'せんかく': u'센카쿠',
            u'あまくさ': u'아마쿠사',
            u'くしろ': u'구시로',
            u'くらしき': u'구라시키',
            u'けごんのたき': u'게곤노타키',
            u'はっけん': u'핫켄',
            u'やりがたけ': u'야리가타케',
            u'いけだ': u'이케다',
            u'おんたけ': u'온타케',
            u'みやけ': u'미야케',
            u'きただけ': u'기타다케',
            u'ほっくわん': u'홋쿠완',
            u'おおたけ': u'오타케',
            u'なら けん': u'나라 겐',
            u'こまえ': u'고마에',
            u'こうらくえん': u'고라쿠엔',
            u'よこすか': u'요코스카',
            u'よこて': u'요코테',
            u'よこはま': u'요코하마',
            u'はこだて': u'하코다테',
            u'はっこうだ': u'핫코다',
            # u'しれとこ': u'시레토고',
            # => 시레토코
            u'とまこまい': u'도마코마이',
            u'にっこう': u'닛코',
        })

    def test_examples_ga_column(self):
        self.assert_examples({
            u'かながわ': u'가나가와',
            u'かすみがうら': u'가스미가우라',
            u'もがみ': u'모가미',
            u'やりがたけ': u'야리가타케',
            u'つがる': u'쓰가루',
            u'するが': u'스루가',
            u'さが': u'사가',
            u'たねが': u'다네가',
            u'あつぎ': u'아쓰기',
            u'とちぎ': u'도치기',
            u'はぎ': u'하기',
            u'あかぎ': u'아카기',
            u'ぎの': u'기노',
            u'ぎんざ': u'긴자',
            u'むぎ': u'무기',
            u'ぎふ': u'기후',
            u'みやぎ': u'미야기',
            u'けいひん': u'게이힌',
            u'かわぐち': u'가와구치',
            u'よなぐに': u'요나구니',
            u'もりぐち': u'모리구치',
            u'やまぐち': u'야마구치',
            u'ぐんま': u'군마',
            u'さかぐち きんいちろう': u'사카구치 긴이치로',
            u'ひぐち けいこ': u'히구치 게이코',
            u'ひぐち たかやす': u'히구치 다카야스',
            u'さとう めぐむ': u'사토 메구무',
            u'げんかいなだ': u'겐카이나다',
            u'あげお': u'아게오',
            u'くればやし しげお': u'구레바야시 시게오',
            u'むらかみ しげとし': u'무라카미 시게토시',
            u'しげみつ まもる': u'시게미쓰 마모루',
            u'さいとう しげよし': u'사이토 시게요시',
            u'まちだ しげる': u'마치다 시게루',
            u'まえお しげさぶろう': u'마에오 시게사부로',
            u'ながしま しげお': u'나가시마 시게오',
            u'けごんのたき': u'게곤노타키',
            u'ぶんご': u'분고',
            u'ちくご': u'지쿠고',
            u'かわごえ': u'가와고에',
            u'ちゅうごく': u'주고쿠',
            u'えちご': u'에치고',
            u'ごとう': u'고토',
            u'あご': u'아고',
            u'こごた': u'고고타',
            u'ひょうご': u'효고',
        })

        
    def test_examples_misc(self):
        self.assert_examples({
            u'オノ・ヨーコ': u'오노 요코',
        })
