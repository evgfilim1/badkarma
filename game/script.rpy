# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define captain = Character("Капитан", color="#29ec29")  # Цвета генерировал случайно, но вы можете выбрать любой.
define geran = Character("Геран", color="#adf320")
define landa = Character("Ланда", color="#fc047a", image="landa")
define bam = Character("Бам", color="#f2f20a")
define buk = Character("Бук", color="#0a77f2")
define sam = Character("Сэм", color="#789abc", image="sam")
define aspara = Character("Аспара", color="#e3256b", image="aspara")  # цвет суеты рулит
define dub = Character("Дуб", color="#228b22", image="dub")
define people = Character("Жители", color="#861718")

# Фоновые изображения
image bg tree:
    "bg-tree.jpg"
    zoom 1.5
image bg forest:
    "bg-forest.png"
    zoom 1.5
image bg hanging:
    "hanging.png"
    zoom 2.5
image bg village:
    "bg-village.png"
    zoom 2.0
image bg kitchen:
    "bg-kitchen.png"
    zoom 2.25
image bg night:
    "bg-night.png"
    zoom 1.5
image bg meme first:
    "meme0.png"
    zoom 1.5
image bg meme second:
    "meme1.png"
    zoom 1.5
image bg meme third:
    "meme2.png"
    zoom 1.5
image bg campfire:
    "bg-campfire.png"
    zoom 1.75
image bg campfire people:
    "bg-campfire-people.png"
    zoom 2.25
image bg home:
    "bg-home.jpg"
    zoom 0.5
image bg home out:
    "bg-home-out.png"
    zoom 1.5
image bg lake:
    "bg-lake.png"
    zoom 1.75
image bg village out:
    "bg-village-out.png"
    zoom 1.25
image bg river:
    "bg-river.png"
    zoom 1.25

# Изображения героев
image landa happy:
    "landa-happy.png"
    zoom 0.5
image sam neutral:
    "sam-neutral.png"
    zoom 0.5
image aspara neutral:
    "aspara-neutral.png"
    zoom 0.5
image dub neutral:
    "dub-neutral.png"
    zoom 0.5

define timeskip = Fade(0.5, 1.0, 0.5, color="#000000")

# Игра начинается здесь:
label start:
    scene black

    # Предисловие/пролог/етс.
    # Вывод текста на экран от лица рассказчика.
    "Ветер, блуждая меж крон деревьев, подхватывал в небо лепечущих птиц. Лес вновь воспевает
        творения жизни и вновь затихает под шелест ветвей."
    "Вечный покой нарушает {b}Не Вечный{/b}, вновь заявляя свое право на жизнь."

    scene bg tree with dissolve
    "Под лучами весеннего солнца в песню жизни и леса как в дерево вклинивались звуки работы
        молота и топора."
    "Стоя на куполе из переплетения громадных корней, толщина каждого из которых могла достигать
        до десятка полных обхватов, а длинной в сотни метров, группа людей занималась рубкой
        гигантских артерий деревьев."

    "Высокая женщина крепкого телосложения отдавала приказы между ударами тяжелого топора и столь
        же тяжелыми вздохами."
    "В её карих глазах читался железный характер, способный бросить вызов этому лесу."

    # Вывод текста на экран от лица персонажа.
    captain "Натягивайте канаты! Вбивайте крепления! Крутите узел!"

    # Здесь стоит добавить картинку с персонажем/-ами.

    # Здесь стоит добавить немного описания персонажа/-ей, но идей пока нет.
    geran "Ланда, может уже сделаем перерыв, топор начинает тупиться?.."

    show landa happy at left with dissolve
    landa "Или же тебе надоело делать свое дело, Геран? Не ленись, первый корень всегда самый
        тяжелый, дальше будет проще."
    landa "Бам, Бук, крепежи готовы?"
    "В ожидании ответа Ланда дала себе несколько секунд на передышку и стирание капель пота
        со лба."
    hide landa with dissolve

    "Из-за ближайшего переплета корней и верёвок, словно пытаясь перекричать друг друга, по очереди
        стали раздаваться два звонких голоса: женский и мужской."
    bam "Да."
    buk "Готово!"
    bam "Подвинься!"
    buk "Сам не мешай!"
    bam "У меня узел важнее!"
    buk "Эй, это моя {i}нога{/i}, не надо её привязывать!!!"
    bam "Хи-хи-хи!"
    landa "{i}Эти двое опять за свое? Уже как три зимы не дети, а всё ещё ведут себя, как
        маленькие.{/i}"

    "Выпрямившись и приподнявшись из разруба, Ланда нашла глазами последнего члена группы
        корнерубов."
    show landa happy at left with dissolve
    landa "Как успехи с противовесом, Сэм?"
    landa "Для противовеса надо тщательно выбирать камень, иначе либо он упадет без отрубленного
        корня, либо же ты вместе с ним. Помнишь, что случилось с тобой в прошлом году?"
    show sam neutral at right with dissolve
    sam "Сейчас закреплю..."
    sam "{i}Тяжело найти хороший противовес здесь наверху. Хотя... корни каждый год ползут наверх
        и тащат за собой груды камней, так что...{/i}"
    sam "Я нашёл! Вроде подходит."
    hide sam
    hide landa
    with dissolve

    "Стоило мне это сказать, как твёрдая поверхность стала ускользать из-под моих ног. С тяжёлым
        хрустом и напряжением, шестиметровый отросток дерева стал обваливаться под собственным
        весом вниз."
    scene black with dissolve
    menu:
        "Схватиться за что-нибудь":
            pass

        "Ничего не делать":
            scene bg meme first
            play music "audio/directed-by.webm"
            pause 3.5
            scene bg meme second
            pause 3.5
            scene bg meme third
            pause 1.0
            return
    "Cам того не осознавая, я вцепился руками в куски камня, выпирающие с поверхности валуна.
        Вжавшись пальцами в камень, я лишь пытался не открыть глаза."
    "Спустя несколько секунд треска дерева и шквального ветра, снизу послышался хлопок,
        ознаменовавший приземление тяжеленного отростка на землю."
    "Я ещё сильней вжался в спасительный камень, который, скорее всего, висел над дырой в куполе
        из корней."

    landa "Сэм, держись! Не отпускай, мы сейчас тебя вытащим!"
    "Это было первое, что я услышал, поняв, что не лечу вниз вместе с куском дерева."

    menu:
        "Открыть глаза":
            pass
    scene bg tree with dissolve
    "Я открыл глаза, и было уж хотел найти взглядом страховочную веревку, как прямо на меня
        из камня, будто насквозь, стали сверлить два каменных глаза."
    "По всему телу пробежали мурашки, меня сразу бросило в холодный пот, а к горлу подступил ком."
    "Каменная фигура с девичьими чертами лица застыла в кричащей гримасе и, будто беззвучно
        кричала, но не она, не её голос звучал в сейчас наперекор ветру. Я почувствовал что-то
        тёплое в своей руке."
    "Что-то, что было тёплым, как живое..."  # https://www.youtube.com/watch?v=BIlkYNYWWGc
    sam "А-А-А-А-А-А-А-А!!!" with hpunch
    "Я отдернул руки от камня и, потеряв равновесие, вдруг стал ощущать свободное падение."
    scene bg hanging
    "Несколько раз веревка развернула меня в воздухе, прежде чем резко натянуться и остановить
        меня примерно в двадцати метрах над землёй." with vpunch
    "Я посмотрел на свои руки. Одна их них была сильно окровавлена, капли срывались с кончиков
        пальцев, устремляясь вниз, где и находилась наша деревня."

    "Откуда-то снизу, из деревни прозвучал счастливый детский возглас."
    "Девочка" "Мама!!! Мама!!! Смотри, небосвет! У них получилось!!!"
    "Это — малышка Рамма, ей три года, и это второй раз когда она видела, как через почти
        непроглядный купол из корней гигантских деревьев, что укрывал деревню каждую зиму, мы
        пробиваем первую дыру."
    "Мы называем его \"семя света\", которому корнерубы дают упасть на землю в первые дни
        \"Зеленой листвы\", чтобы наша небольшая деревушка смогла вновь греться в лучах небосвета
        и его тепла."

    "Оглянувшись на деревню, в душе снова стало теплее."
    "Столб света, спускаясь с небосвода, падал прямо в водяной пруд, на дне которого располагались
        огромные камни с ярко-белыми кристаллами."
    "Свет от них отражался во все стороны, освещая пространство вокруг, а также деревянные домики,
        что расположились на корнях и опушках около пруда."
    "В куполе корней, освещённом только светоплесенью и огненными грибами, жизнь шла медленно
        и неуверенно, но сейчас, когда свет фонтанировал во все стороны, люди в деревне будто
        пробудились от белого сна."
    "Люди с улыбками смотрели на семя света и на то, как одинокую фигуру затаскивали на верёвке
        обратно наверх к куполу из корней."

    scene bg forest with timeskip
    show landa happy at left with dissolve
    landa "Ну вот и всё. Заживёт само через какое-то время."
    "Ланда затянула на мне повязку из сплетений лозы листодрева."
    landa "С такой раной тебе не стоит пока находиться наверху, да и похоже ты перегрелся, раз
        начал видеть людей из камня. Мы осмотрели тот валун и никакой каменной девушки не нашли."
    show sam neutral at right with dissolve
    sam "Честно тебе говорю, я держал её за руку и смотрел прямо в лицо! Думаешь я вру?"
    landa "Я думаю, что у тебя разыгралась фантазия со страха и стала мерещится девчонка из камня."
    "Ланда выпрямилась в полный рост и посмотрела в вырубленное в потолке отверстие."
    landa "Мы хорошо потрудились, в этот раз управились всего за шесть часов. Иди отдыхай, мы
        соберём инструменты и спустимся как раз к тому моменту, как старикашка начнёт рассказывать
        свои байки мелюзге у большого костра."
    sam "То, что у его дерева колец больше, чем наших с тобой вместе взятых, ещё не делает его
        старикашкой. Он нам двоим фору даст и одной рукой топором махать будет."
    sam "Когда-то он был наверху, и так же, как и мы сейчас, рубил эти корни, чтобы деревня могла
        жить дальше."
    landa "Не пойми неправильно, я его уважаю, но нас становится всё больше и нам надо искать
        больше еды, а его легенды и сказки не дают нам уйти дальше корней."
    sam "Ты же сама была наверху уже много раз и видела, как велик лес. Это лишь вопрос времени,
        когда нам станет тесно жить у пруда и придётся выйти наружу."
    landa "Да-да-да, гласят, что в лесу одному не выжить, и что там водятся гигантские животные,
        и синие люди живут на деревьях."
    "Она сказала это с заметной усмешкой."
    sam "Я лично не хочу рисковать своей жизнью ради того, чтобы узнать, что там может меня съесть.
        Я понимаю, что староста — твой отец, но будь поаккуратней, за неуважение к легендам могут
        и наказать."
    landa "Да знаю я, но ты же меня не сдашь?"
    "Приподняв одну бровь, она встала с корточек и протянула мне руку."
    sam "Лес — это когда деревья в нём живут вместе."
    "Я схватил её руку и поднялся с холодного камня."
    landa "А листья в нём вечно зелены. Отдыхай."
    "Она улыбнулась и, подхватив рюкзак, направилась в сторону подъёма на купол из корней."
    hide landa with dissolve
    sam "Спасибо..."
    "Я же в свою очередь направился в сторону деревни."
    hide sam
    scene bg village
    with dissolve

    "Рука потихоньку переставала болеть, а я уже приближался к деревне, откуда уже тянуло запахом
        жареных грибов и жуков. В желудке невольно пробурчало, а ноги понесли в сторону кухни."
    "Кто-то готовил, кто-то развешивал украшения в виде цветов и узоров, вырезанных на листьях
        больших кустарников, а кто-то обустраивал сцену под вечерний сбор деревни. Холода в этом
        году были долгими, и люди радовались теплу и солнцу."
    "Я подошёл к открытой кухне, из-под крыльца которой густым столбом шёл пар и дым от готовки,
        которая не прекращалась с самого утра."

    scene bg kitchen
    show aspara neutral at left
    with dissolve
    aspara "Сэ-э-эм!!!"
    "Этот голос мне больно знаком."
    aspara "С днём семясвета тебя! Вы уже закончили и спустились? В этот раз как-то быстро."
    "Это была милая, среднего возраста женщина, которая несла в руках корзину с живыми жуками,
        которые то и дело пытались выбраться на волю и сбежать."
    show sam neutral at right with dissolve
    sam "И тебя с праздником, Аспара. Нет, ребята всё ещё собирают инструменты и проверяют,
        чтобы ничего больше не рухнуло сверху, а меня отправили отдыхать, я сейчас не сильно им
        смогу помочь."
    "Сказал я, помахивая перебинтованной и красной от крови рукой."

    menu:
        # Эта строка будет показана игроку, когда он будет выбирать, что делать.
        aspara "Храни тебя кора, это ж как ты умудрился???"

        # Вариант ответа заканчивается ":"
        "Да так, порезался о камень...":
            # Эта строка будет показана игроку, когда он выберет этот вариант.
            sam "Да порезался об острый камень. Так, царапина, поболит и перестанет."
            "Я решил умолчать о последующем падении, а то пришлось бы слушать много нотаций."

        "Меня укусила Бам":
            sam "Да меня Бам укусила."
            aspara "Опять эта негодница за своё, вернётся, я ей таких лопухов навешаю!!!"
            sam "Ладно-ладно, шучу, я просто порезался об острый камень."

    aspara "Эх, помню, как твой отец тоже лазил наверх, а потом рассказывал нам маленьким о том,
        что он видел наверху... Жаль они не пережили те холода."
    aspara "Ты наверно жутко голодный, а я тут, хозяйка, рот голодный словами затыкаю. Садись
        за стол, сейчас я тебе всё принесу."
    "Видно, Аспара поймала себя на какой-то мысли, что сменила тему."

    "Я схватил столовые приборы и сел за большой деревянный стол, за которым могло поместиться
        с десяток человек, но все давно пообедали и уже занимаются своими делами."
    "Её слова, конечно, не могли оставить мои мысли в покое, но я плохо помнил своего отца,
        а тем более мать."
    "Они умерли, когда мне было пара лет, и, можно сказать, для меня вся деревня — это семья,
        наверно даже роднее Ланды и старосты у меня никого нет."
    "От мыслей меня отвлек гулкий удар тарелки по столу."
    aspara "Приятного аппетита! А я пошла готовить дальше."
    aspara "Сегодня большой день, а нам ещё столько нужно сделать до вечера."

    menu:
        aspara "Не хочешь помочь мне на кухне, а то мне не хватает свободных рук и рта, который бы
            всё пробовал?"

        "\"Да, конечно, я помогу.\"":
            pass  # = ничего не делать, сюжет просто продолжается

        "\"Ты опять хочешь приготовить что-то новое и скормить это мне?\"":
            sam "Ты опять хочешь приготовить что-то новое и скормить это мне?"
            aspara "Нет, ну что ты. Меня попросили в этом году не экспериментировать с праздничной
                едой..."
            "Она отвела глаза в сторону и провела пальцем по столу."
            aspara "Но я собрала парочку грибов с крайней опушки, и мне очень хочется их
                приготовить. Но честно-честно они не ядовитые!"

    sam "Ладно, я всё равно сейчас сильно не помощник, не сидеть же мне без дела до вечера."
    "Сказал я и принялся набивать желудок грибным супом."
    aspara "Вот и славненько. Ешь пока, а я поставлю огонь для Барканов, мне надо будет, чтобы ты
        нарезал потом их, а то в прошлый раз один из них меня укусил."
    hide aspara
    hide sam
    with dissolve
    "Доев обед, я встал за стол для разделки, и следующие несколько часов превратились в активную
        борьбу за целостность моей второй руки от жвал Барканов."
    "Ближе к вечеру последний гриб был очищен и подготовлен, и шашлыки из Барканов и Браминов были
        зажарены. Свет, проходящий через дыру в куполе, потихоньку терял силу, и время подходило
        к закату."

    scene bg night with timeskip
    "После яркого дня, светосемя, мох на стенках купола, набрал в себя большое количество света,
        поэтому в первую ночь весь купол озарился разноцветными вставками и жилками светящихся
        растений и кристаллов."
    "Пока вся деревня собиралась у дома старосты, и люди усаживались за большие столы вокруг
        большого костра, в основании которого лежал срубленный ещё утром корень, я отнёс
        последнюю тарелку с едой на стол."
    "После чего сразу уселся на свободное место рядом с жареным мясом Брамина."
    "Люди болтали между собой, медленно поднимался общий гул."

    "После того как последний стул был занят, на небольшую сцену перед всеми, прихрамывая, вышел
        человек средних лет."
    "Но даже для своего небольшого возраста он выглядел слишком молодо, хотя мудрости было иной
        раз больше, чем у опытного старца. Тут же все замолчали."
    "Мужчина, хоть и в возрасте, но виду не подавал, вскинул руки вверх и не для своего вида низким
        и внушительным голосом заговорил."
    show dub neutral with dissolve
    dub "Поздравляю вас с Новым Годом! Ещё одни холода позади, это были тяжелые времена для нас
        всех. Мы перенесли тяготы и лишения, преодолели преграды и невзгоды."
    dub "Я горжусь вами, как гордились бы и те, кого с нами больше нет."
    dub "Холод не был столь суров к нам в этом году, на то наше счастье. Но мы чтим память тех, кто
        был с нами и будет в наших сердцах долгие годы, пока не перерождаются в новых семенах жизни
        вокруг нас."
    dub "Возложим же имена тех, чей огонь горит в наших сердцах к великому пламени новой жизни!"

    scene bg campfire with dissolve
    "Некоторые люди стали подниматься со своих мест, держа в руках деревянные таблички с выбитыми
        на них надписями. Это имена тех, чью память они хотят почтить."
    "Родители, братья и сестры, дети... Люди гибнут почти каждый год по тем или иным причинам,
        кто-то от болезни, кто-то от голода."
    "Но они не уходят от нас навсегда, природа всегда находится в балансе, отнимая жизнь, она даёт
        жизнь чему-то новому."

    "Ко мне со спины подошла Ланда, протянула две деревянные таблички и прошептала на ухо."
    landa "Я понимаю, что ты не помнишь своих родителей, но всё же стоит почтить и их память..."
    show landa happy with dissolve
    menu:
        "Я обернулся и увидел глаза, смотрящие прямо в душу с надеждой и ожиданием."

        "Взять таблички":
            pass
    "После тяжелого смиренного вздоха, я взял деревяшки и уже под одобрительный взгляд вышел из-за
        стола."
    hide landa with dissolve
    "Я помнил их имена не как приятные воспоминания, а как традицию. Каждый в деревне должен был
        назвать своего ребенка по имени одного из своих родителей."
    "Это напоминало всем о цикличности жизни, а также о том что надо хранить память своих предков."

    "Я взглянул на таблички. \"Элодей\" и \"Роза\": так звали моих родителей и так же будут звать
        моих детей."
    "Склонившись перед сложенным кострищем, я положил деревяшки у основания и не заметил, как
        остался последним из тех, кто хотел почтить память."
    show dub neutral with dissolve
    dub "Сэм, семя Элодея и Розы. Тебе предоставлена честь возжечь пламя новой жизни."
    "Я недовольно посмотрел на Ланду, а та явно пыталась сказать \"Я тут не при чём\"."

    "Мужчина достал что-то из кармана и провёл по посоху, на конце которого вдруг вспыхнул огонь,
        который быстро охватил наконечник посоха."
    dub "Зажги же огонь, что укажет нашим предкам путь домой!"
    "Я уже хотел взяться за посох, как вдруг он схватил меня за больную руку, и при свете огня
        начал пристально всматриваться в место пореза на руке, где давно уже запеклась кровь."
    "Староста нахмурился и вложил в руку горящий посох, вновь вскинув руки вверх."
    menu:
        dub "Я, Дуб, тринадцатый от своего имени, объявляю о начале Нового Года!!!"

        "Зажечь огонь":
            pass
    "Я понял, что после его слов надо было разжечь костер, что я, собственно, и сделал, бросив
        посох в середину сложенных дров. Дрова, залитые соком огнегрибов, моментально вспыхнули,
        и огонь озарил собой всю деревню."
    scene bg campfire people with dissolve
    dub "Лес — это когда деревья в нём живут вместе."
    people "А листья в нём вечно зелены!"

    hide dub with dissolve
    "Заиграла музыка и началось всеобщее пиршество."
    "Люди гудели, пели, танцевали вокруг огня и не только. Все праздновали главный праздник года."
    "Я был слишком уставшим для празднества и танцев, так что ноги сами понесли меня в кровать."

    scene bg home out with dissolve
    menu:
        "Проходя по пустым улочкам, я добрался до небольшого деревянного домика."

        "Зайти в дом":
            pass
    scene bg home with dissolve
    "Я вошёл в свою хижину, где валялось много разного хлама в пыли и листьях, что, как обычно,
        встречали меня."
    "Больше всего как я, так и меня, была рада видеть мягкая соломенная кровать."
    "Стянув с себя грязную одежду, я бухнулся спать."

    scene bg home with timeskip
    "Я открыл глаза от шума, созданного дверью, а точнее Ландой, вбежавшей в комнату с сумкой
        и топором за спиной."
    show landa happy at left with dissolve
    landa "Сэм, ты должен уходить, немедленно!"
    "Вполголоса выкрикнула она встормашивая полусонного меня на кровати."
    landa "Мой отец, Дуб, хочет тебя убить из-за какой-то каменной розы."
    landa "Я подслушала его разговор после праздника, он сейчас собирает старших, чтобы убить тебя!"
    show sam neutral at right with dissolve
    sam "Что, почему?.."
    "Пробормотал я, вставая с кровати."
    landa "Я рассказала ему про девушку из камня, которую ты якобы видел. Он так же, как и я,
        подумал о том, что тебе показалось, но когда я рассказала про порез, то он ушел из деревни
        и не возвращался до выступления."
    menu:
        landa "Я хотела с ним поговорить, но подслушала, как они хотят убить тебя, пока ты
            не навредил всей деревне! Они говорили серьёзно, так что я думаю, они уже идут сюда.
            Давай быстрее!"

        "Спросить про \"каменную розу\"":
            sam "Что за каменная роза?"
            "Вскакивая с кровати всё же решил спросить я."
            landa "Не знаю, какая-то хворь, они говорили что о ней забыли десятки лет назад. Я сразу
                побежала к тебе, схватив что попалось по пути."

        "Промолчать":
            pass

    landa "Тут сумка и немного еды, я прихватила твой топор из кладовой."
    "Я тут же поднес руку поближе к лицу, чтобы рассмотреть её в полумраке."
    "На месте, где ещё утром была кровоточащая рана, уже находилось серое пятно с трещинами, будто
        сухая земля."
    "Я сжал кулак и дотронулся пальцами до серого пятна."
    sam "К..к..камень?"
    "С ужасом прошептал я, раз за разом прикасаясь к окаменевшей части ладони."
    "Ланда какое-то время наблюдала за мной, а потом впихнула мне в руки сумку с припасами и,
        приказывая, сказала."
    landa "Тебе надо бежать! Сейчас!"
    "Она выталкивала меня за дверь с каждым словом, не давая мне взять свои вещи или поговорить."

    scene black with dissolve
    "Мы вышли из дома, и Ланда схватила меня за руку, уволакивая за собой в темноту."
    "Уходя, я слышал нарастающий гул и видел множество факелов и теней, прыгающих по стенам
        деревянных домов."
    "Стража" "Подоприте дверь и окна, не дайте ему выйти!"
    "Последнее что мы услышали, удаляясь от домов."
    "Самая важная ночь в году и самая страшная для меня. Один день, способный изменить всю жизнь,
        я надеялся что он никогда не наступит, но, похоже, судьба решила за меня."
    "Я бежал за Ландой, боясь не за свою жизнь, а что это последний раз, когда я вижу деревню,
        пруд, дорогих мне людей и спокойную жизнь."

    scene bg lake
    show sam neutral at left
    with dissolve
    sam "Как мы выйдем из корней? Вы же убрали крюки и веревки по которым мы поднимались по корням."
    show landa happy at right with dissolve
    landa "Я знаю ещё один выход, только, возможно, он тебе не понравится."
    sam "Веди."
    "Ланда кивнула в ответ и схватила меня за руку."

    scene bg village out with dissolve
    "Несколько минут мы бежали вдоль озера, а после углубились в заросли."
    "Она размахивала длинным ножом расчищая нам путь и через лозы и громадные листья."
    show sam neutral at left with dissolve
    sam "Куда мы всё же идем?"
    "Уже сомневаясь во всей задумке, я все же решился спросить, а Ланда все продолжала размахивать
        инструментом и, запыхаясь, ответила."
    show landa happy at right with dissolve
    landa "Озеро много лет не меняет своей формы, вода откуда-то приходит и куда-то уходит."
    "Она нашла выход, не над землей а под ней?"
    landa "Сегодня я его видела, плохо, но видела, он проходит под корнями."
    sam "Кто он?"
    landa "Поток воды."
    "Как нельзя кстати, с её словами деревья, наконец, разошлись, и мы подошли к основанию купола
        из корней."

    scene bg river with dissolve
    "Сквозь заросли и почву, в полом корне бурно струился поток воды, уходящий под купол."
    show sam neutral at left with dissolve
    sam "А оно точно не течет под землю? Ты уверена?"
    show landa happy at right with dissolve
    landa "Да, недалеко, на востоке, течет река, мы выплывем прямо у её начала."
    hide landa with dissolve
    pause 0.5
    show landa happy at right with dissolve
    "Пока я смотрел на бурлящий поток воды и взвешивал все за и против, Ланда так же незаметно
        появилась, как и исчезла. Но что-то изменилось, за её спиной висела сумка, старая медная
        кастрюля и всякая всячина."
    sam "Что это значит?"
    landa "Это значит, нас ждут приключения!"
    show landa happy at center with move
    "С усмешкой вскрикнула она и, сделав резкий шаг, чмокнула меня в губы."
    show landa happy at right with move
    "Я оторопел от происходящего, но тут же она толкнула меня от себя."
    landa "Увидимся на той стороне, Сэм!"
    "И только через пару мгновений я понял, что она толкнула меня в воду..."

    scene black with dissolve
    "{i}Продолжение следует...{/i}"
    scene black with dissolve
