init python:
    def relationship_callback(event, interact=True, **kwargs):
        character = kwargs.get("character")

        if character is None:
            return

        character = getattr(store, character)
        relationship_girls = getattr(store, "relationship_girls")

        if character not in relationship_girls:
            relationship_girls.append(character)
            setattr(store, "relationship_girls", relationship_girls)

# Declare characters used by this game. The color argument colorizes the name of the character.
define character.narrator = Character (None, what_outlines=[ (2, "#000") ])
define character.u = Character("[name]", who_color="#53d769", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ju = Character("Джулия", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.car = Character("Автомобиль", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ca = Character("Кэмерон", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ma = Character("Мэйсон", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.aut = Character("Отем", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.em = Character("Эмили", who_color="#fc3d39", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.an = Character("Миссис Андерсон", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ch = Character("Крис", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.no = Character("Нора", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ry = Character("Райн", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ro = Character("Мисс Роуз", who_color="#fc3d39", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.la = Character("Лорен", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ri = Character("Райли", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.el = Character("Элай", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.imre = Character("Имре", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.au = Character("Обри", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.sam = Character("Сэм", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.karen = Character("Карен", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.jo = Character("Джош", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.courtney = Character("Кортни", who_color="#fc3d39", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.jeremy = Character("Джереми", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.katy = Character("Кэти", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.sarah = Character("Сара", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.gr = Character("Грэйсон", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.cl = Character("Хлоя", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.tom = Character("Том", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.tut = Character("Обучение", who_color="#53d769", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.lee = Character("Мистер Ли", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ben = Character("Бенджамин", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ehr = Character("Доктор Эрмантраут", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.pe = Character("Пенелопа", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ev = Character("Эвелин", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.aa = Character("Аарон", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.sec = Character("Охранник", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.li = Character("Линдси", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.unknown = Character("Неизвестный человек", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.uber = Character("Водитель Uber", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.clerk = Character("Продавец Магазина", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.am = Character("Эмбер", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ki = Character("Ким", who_color="#fc3d39", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ad = Character("Адам", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.co = Character("Советница", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 6.0
define character.waiter = Character("Официант", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.host = Character("Хозяин", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.poet1 = Character("Лиза", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.poet2 = Character("Мартин", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.sa = Character("Саманта", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.guya = Character("Питер", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.guyb = Character("Гарри", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.finn = Character("Финн", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.guyd = Character("Перри", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.se = Character("Себастьян", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.guyc = Character("Маркус", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.matt = Character("Мэтт", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 7.0
define character.cal = Character("Калеб", who_color="#83d81c", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ]) # Ape pledge
define character.coop = Character("Купер", who_color="#11af68", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ]) # Ape pledge
define character.kai = Character("Кай", who_color="#1caedb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ]) # Ape pledge
define character.wes = Character("Уэсли", who_color="#db6f1c", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ]) # Ape
define character.par = Character("Паркер", who_color="#a815f2", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ]) # Ape
define character.rg1 = Character("Анжелика", who_color="#db6f1c", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.rg2 = Character("Элиза", who_color="#a815f2", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.nerd = Character("Зануда", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.xav = Character("Хавьер", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.jax = Character("Джексон", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.teach = Character("Учитель", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.class1 = Character("Класс", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 8.0
define character.de = Character("Декан", who_color="#fc3d39", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.je = Character("Джо", who_color="#53d769", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ann = Character("Объявление спикера", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.empl = Character("Сотрудник", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 9.0
define character.unkfem = Character("Женский голос", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 10.0
define character.jen = Character("Дженни", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.mrr = Character("Мистер Роуз", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.be = Character("Бен", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.jer = Character("Джерри", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.dg1 = Character("Рэйчел", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.dg2 = Character("Элеонора", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.dg3 = Character("Карен", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.dg4 = Character("Ребекка", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 11.0
define character.art = Character("Художественный руководитель", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.air = Character("Airport Host", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ran = Character("Фермер", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.hor = Character("Лошадь", who_color="#a815f2", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.dun = Character("Дункан", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.bartender = Character("Бармен", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.foxy = Character("Фокси", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ericka = Character("Эрика", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.jane = Character("Джейн", who_color="#fc3d39", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.candy = Character("Кэнди", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.mana = Character("Менеджер", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.driver = Character("Водитель", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.sus = Character("Сьюзан", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.jud = Character("Судья", who_color="#db6f1c", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.charli = Character("Чарли", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.csa = Character("Торговый представитель", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.dennis = Character("Деннис", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.bank = Character("Банковский служащий", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 12.0
define character.robber = Character("Грабитель", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.fwait = Character("Французская официантка", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.na = Character("Наоми", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.pg = Character("Фотограф", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.lmass = Character("Леди Массажистка", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.mmass = Character("Мужчина массажист", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.clady = Character("Сумасшедшая", who_color="#ff8afb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.escman = Character("Менеджер", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.bishop = Character("Епископ", who_color="#800080", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.nurse = Character("Медсестра", who_color="#dbfffe", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.barber = Character("Парикмахер", who_color="#fecb2e", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.greeter = Character("Хостес", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.tattoo = Character("Мастер татуировок", who_color="#ff1694", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 13.0
define character.ary = Character("Арисса", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.ash = Character("Эштон", who_color="#fd9426", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.barh = Character("Хозяин", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.clipps = Character("Клиппс", who_color="#cccccc", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.emmy = Character("Эмми", who_color="#fc3158", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.gary = Character("Гэри", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.gitw = Character("Неизвестный", who_color="#0055ff", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.kourt = Character("Кортни", who_color="#ff8afb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.luuk = Character("Луук", who_color="#ff1694", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.polly = Character("Полли", who_color="#8b0000", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.random_guy = Character("Бармен", who_color="#5fc9f8", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])

# 14.0
define character.ngam = Character("Night Gambler", who_color="#ff1694", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.emerald = Character("Emerald", who_color="#046307", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.madame = Character("Madame", who_color="#800080", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.satin = Character("Satin", who_color="#ecd9c9", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.wtrain = Character("Woman", who_color="#ff1694", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.rub = Character("Rubee", who_color="#8b0000", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
define character.trainer = Character("Trainer", who_color="#147efb", who_outlines=[ (2, "#000") ], what_outlines=[ (2, "#000") ])
