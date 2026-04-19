define d = Character("Диана", color="#dfe9ff")
define dm = Character("Дима", color="#cad6ff")
define mi = Character("Миша", color="#d6d6d6")
define v = Character("Вика", color="#ffd7f3")
define m = Character("Марина", color="#ffe6c6")
define ai = Character("ИИ", color="#d7c4ff")
define th = Character(None, what_prefix="{i}", what_suffix="{/i}")

default route_focus = "none"
default current_scene_key = "arrival_train"
default current_music_key = None
default final_choice = None
default ending_code = None
default ending_title = ""

default trust_dima = 0
default trust_misha = 0
default trust_vika = 0
default trust_marina = 1
default legend_integrity = 2
default school_heat = 1
default criminal_heat = 0
default evidence_strength = 0
default ai_dependency = 0
default resolve = 2

default met_vika = False
default met_misha = False
default met_dima = False
default roma_informant_open = False
default phone_found = False
default phone_photos_saved = False
default phone_hidden_success = False
default mother_warned_partial = False
default mother_warned_full = False
default mother_gun_known = False
default anonymous_tip_sent = False
default police_corruption_confirmed = False
default dima_book_route = False
default milana_topic_triggered = False
default dima_confession_unlocked = False
default misha_warning_received = False
default nikita_lead_open = False
default vika_social_shield = False
default diana_played_sincere = False
default diana_played_cold = False
default diana_used_roma_ruthlessly = False
default diana_protected_roma = False
default dima_saw_truth = False
default vika_feels_chosen = False
default misha_feels_exposed = False
default marina_trusts_diana_plan = False

init python:
    import store

    BASE_NUMBERS = {
        "trust_dima": 0,
        "trust_misha": 0,
        "trust_vika": 0,
        "trust_marina": 1,
        "legend_integrity": 2,
        "school_heat": 1,
        "criminal_heat": 0,
        "evidence_strength": 0,
        "ai_dependency": 0,
        "resolve": 2,
    }

    BASE_FLAGS = {
        "route_focus": "none",
        "current_scene_key": "arrival_train",
        "current_music_key": None,
        "final_choice": None,
        "ending_code": None,
        "ending_title": "",
        "met_vika": False,
        "met_misha": False,
        "met_dima": False,
        "roma_informant_open": False,
        "phone_found": False,
        "phone_photos_saved": False,
        "phone_hidden_success": False,
        "mother_warned_partial": False,
        "mother_warned_full": False,
        "mother_gun_known": False,
        "anonymous_tip_sent": False,
        "police_corruption_confirmed": False,
        "dima_book_route": False,
        "milana_topic_triggered": False,
        "dima_confession_unlocked": False,
        "misha_warning_received": False,
        "nikita_lead_open": False,
        "vika_social_shield": False,
        "diana_played_sincere": False,
        "diana_played_cold": False,
        "diana_used_roma_ruthlessly": False,
        "diana_protected_roma": False,
        "dima_saw_truth": False,
        "vika_feels_chosen": False,
        "misha_feels_exposed": False,
        "marina_trusts_diana_plan": False,
    }

    def shift_stat(name, amount):
        value = getattr(store, name, 0) + amount
        value = max(0, min(5, value))
        setattr(store, name, value)
        return value

    def reset_prototype_state():
        for key, value in BASE_NUMBERS.items():
            setattr(store, key, value)

        for key, value in BASE_FLAGS.items():
            setattr(store, key, value)

    def current_values():
        values = {}

        for key in BASE_NUMBERS:
            values[key] = getattr(store, key)

        for key in BASE_FLAGS:
            values[key] = getattr(store, key)

        return values

transform sprite_left:
    xalign 0.18
    yalign 1.0
    yoffset -8
    ysize 700
    fit "contain"

transform sprite_center:
    xalign 0.5
    yalign 1.0
    yoffset -8
    ysize 720
    fit "contain"

transform sprite_right:
    xalign 0.82
    yalign 1.0
    yoffset -8
    ysize 700
    fit "contain"

screen prototype_hud():
    zorder 150

    if not _menu:
        frame:
            xalign 0.015
            yalign 0.02
            xpadding 18
            ypadding 12
            background Solid("#111111bb")

            vbox:
                spacing 4

                text "Прототип: [prototype_route_title(route_focus)]" size 24 color "#ffffff"
                text "Дима [trust_dima] | Миша [trust_misha] | Вика [trust_vika] | Марина [trust_marina]" size 18 color "#d9d4cb"
                text "Легенда [legend_integrity] | Школа [school_heat] | Криминал [criminal_heat]" size 18 color "#d9d4cb"
                text "Улики [evidence_strength] | ИИ [ai_dependency] | Решимость [resolve]" size 18 color "#d9d4cb"

label start:
    $ reset_prototype_state()
    $ prototype_assert_assets_ready()
    $ play_prototype_bgm("school_day")

    scene expression prototype_scene("arrival_train")
    with fade
    show expression prototype_character("diana", "phone") as diana_sprite at sprite_left
    show expression prototype_character("marina", "bag") as marina_sprite at sprite_right
    with dissolve

    th "За окном был идеальный апрель: горы, красные крыши, сирень и слишком яркое солнце."
    th "Если смотреть достаточно долго, можно поверить, что новая жизнь и правда начинается с открытки."
    m "Подъезжаем. Телефон не выпускай."
    d "Я и не собиралась."
    th "Марина устала ещё до того, как мы вышли из вагона. Сумка на её плече тянула вниз сильнее, чем дорога."

    scene expression prototype_scene("gorny_village_day")
    with dissolve

    th "Горный оказался красивее, чем должен был быть безопасный городок."
    th "А значит, где-то под этой красотой уже лежала ложь."

    scene expression prototype_scene("school_exterior")
    with dissolve
    show expression prototype_character("diana", "folded") as diana_sprite at sprite_left
    with dissolve

    th "Первый день в школе всегда начинается одинаково: вход, чужие лица и секунда, когда решается, кому ты позволишь назвать тебя своей."

    menu:
        "Сесть рядом с Димой":
            jump school_choice_dima
        "Пойти за Мишей во двор":
            jump school_choice_misha
        "Принять покровительство Вики":
            jump school_choice_vika

label school_choice_dima:
    $ route_focus = "dima"
    $ met_dima = True
    $ dima_book_route = True
    $ shift_stat("trust_dima", 2)
    $ shift_stat("school_heat", 1)
    $ shift_stat("legend_integrity", -1)

    scene expression prototype_scene("classroom_literature")
    with dissolve
    show expression prototype_character("diana", "folded") as diana_sprite at sprite_left
    show expression prototype_character("dima", "thinking") as dima_sprite at sprite_right
    with dissolve

    th "Он сидел у окна так, будто урок уже давно проиграл ему спор."
    d "Можно?"
    dm "Если тебя не пугают люди, которые читают на перемене."
    show expression prototype_character("dima", "crossed") as dima_sprite at sprite_right
    with dissolve
    d "Меня больше пугают люди, которые делают вид, что им ничего не интересно."
    th "Уголок его рта дёрнулся. Для Горного этого уже было почти рукопожатием."

    jump phone_discovery

label school_choice_misha:
    $ route_focus = "misha"
    $ met_misha = True
    $ shift_stat("trust_misha", 1)
    $ shift_stat("legend_integrity", 1)

    scene expression prototype_scene("school_corridor")
    with dissolve
    show expression prototype_character("diana", "folded") as diana_sprite at sprite_left
    show expression prototype_character("misha", "closed") as misha_sprite at sprite_right
    with dissolve

    th "Миша сорвался с урока первым и ушёл туда, где коридор превращался в лестницу к двору."
    d "Ты всегда так исчезаешь?"
    mi "Когда вокруг слишком много людей."
    th "Ответ был честнее, чем полагалось первому разговору."
    d "Тогда мы уже в чём-то похожи."
    show expression prototype_character("misha", "stop") as misha_sprite at sprite_right
    with dissolve
    mi "Не спеши так думать."

    jump phone_discovery

label school_choice_vika:
    $ route_focus = "vika"
    $ met_vika = True
    $ shift_stat("trust_vika", 2)
    $ shift_stat("legend_integrity", 1)

    scene expression prototype_scene("school_corridor")
    with dissolve
    show expression prototype_character("diana", "folded") as diana_sprite at sprite_left
    show expression prototype_character("vika", "dominant") as vika_sprite at sprite_right
    with dissolve

    th "Вика заметила меня раньше, чем я успела прикинуться мебелью."
    v "Новенькая, не стой одна. Здесь одиночек сначала жалеют, потом едят."
    d "Щедрое предложение."
    show expression prototype_character("vika", "smirk") as vika_sprite at sprite_right
    with dissolve
    v "Это не щедрость. Это инвестиция."
    th "Я улыбнулась ровно настолько, чтобы её не обидеть и не обнадёжить."

    jump phone_discovery

label phone_discovery:
    $ play_prototype_bgm("home_tension")
    scene expression prototype_scene("diana_room_night")
    with fade
    show expression prototype_character("diana", "phone") as diana_sprite at sprite_center
    with dissolve

    th "К вечеру дом затих, но тишина в Горном ничего не значила."
    th "Она только делала шаги слышнее."

    $ play_prototype_bgm("suspense")
    scene expression prototype_scene("shed_night")
    with dissolve
    show expression prototype_character("diana", "shocked") as diana_sprite at sprite_center
    with dissolve

    th "В сарае под брезентом я нашла телефон. Чёрный, грязный, всё ещё живой."
    th "В переписке мелькали 'кассирша', инициалы 'В.С.' и слишком спокойные угрозы."
    $ phone_found = True

    menu:
        "Сказать матери всю правду":
            $ mother_warned_full = True
            $ marina_trusts_diana_plan = True
            $ shift_stat("trust_marina", 2)
            $ shift_stat("criminal_heat", 1)
            $ shift_stat("evidence_strength", 1)
            $ shift_stat("legend_integrity", -1)
            $ play_prototype_bgm("home_tension")
            scene expression prototype_scene("diana_room_night")
            with dissolve
            show expression prototype_character("diana", "shocked") as diana_sprite at sprite_left
            show expression prototype_character("marina", "stop") as marina_sprite at sprite_right
            with dissolve
            d "Мам, это уже не просто слухи."
            m "Покажи."
            th "Она побледнела, но не отвела взгляд. Это было хуже паники."
        "Спрятать телефон и копать самой":
            $ phone_hidden_success = True
            $ phone_photos_saved = True
            $ diana_played_cold = True
            $ shift_stat("evidence_strength", 2)
            $ shift_stat("ai_dependency", 1)
            $ shift_stat("resolve", 1)
            th "Сначала дубли. Потом тайник. Потом правда."
            th "И только если выбора совсем не останется."
        "Открыть часть правды":
            $ mother_warned_partial = True
            $ phone_photos_saved = True
            $ shift_stat("trust_marina", 1)
            $ shift_stat("evidence_strength", 2)
            d "Мам, у нас тут неуютная находка. Но я ещё не всё понимаю."
            m "Скажешь, когда поймёшь. Только не одна."
        "Разобрать находку вместе с ИИ":
            $ phone_photos_saved = True
            $ diana_played_cold = True
            $ shift_stat("ai_dependency", 2)
            $ shift_stat("evidence_strength", 1)
            $ play_prototype_bgm("home_tension")
            scene expression prototype_scene("diana_room_night")
            with dissolve
            show expression prototype_character("diana", "phone") as diana_sprite at sprite_left
            with dissolve
            ai "Похоже на координацию угроз и финансового давления."
            d "То есть это уже сеть?"
            ai "С высокой вероятностью."
            th "Машина отвечала быстро. Слишком быстро, чтобы мне стало легче."

    jump misha_pressure_scene

label misha_pressure_scene:
    $ met_misha = True

    $ play_prototype_bgm("investigation")
    scene expression prototype_scene("misha_porch_evening")
    with dissolve
    show expression prototype_character("diana", "folded") as diana_sprite at sprite_left
    show expression prototype_character("misha", "closed") as misha_sprite at sprite_right
    with dissolve

    th "На соседском крыльце Миша курил так, будто дым мог заменить ему стены."
    mi "Тебе сюда нельзя."
    d "Значит, я на правильной тропе."

    menu:
        "Говорить мягко":
            $ shift_stat("trust_misha", 2 if route_focus == "misha" else 1)
            $ shift_stat("resolve", 1)
            show expression prototype_character("misha", "stop") as misha_sprite at sprite_right
            with dissolve
            d "Я не пришла тебя ломать. Я пришла понять, кто из нас ещё может вовремя остановиться."
            mi "Тогда не называй это пониманием. Называй шансом."
        "Давить вопросами":
            $ misha_warning_received = True
            $ misha_feels_exposed = True
            $ shift_stat("trust_misha", -1)
            $ shift_stat("criminal_heat", 2)
            $ shift_stat("school_heat", 1)
            show expression prototype_character("misha", "warning") as misha_sprite at sprite_right
            with dissolve
            d "Твой отец ездит не за продуктами. И ты это знаешь."
            mi "Ещё слово — и за тобой начнут смотреть не только в школе."
        "Держать дистанцию":
            $ misha_warning_received = True
            $ shift_stat("ai_dependency", 1)
            show expression prototype_character("misha", "warning") as misha_sprite at sprite_right
            with dissolve
            mi "Если хочешь дожить до лета, забудь мой двор."
            th "Я кивнула. Иногда отступление звучит убедительнее угроз."

    jump dima_confession_scene

label dima_confession_scene:
    $ met_dima = True
    $ milana_topic_triggered = True

    $ play_prototype_bgm("finale")
    scene expression prototype_scene("stadium_sunset")
    with dissolve
    show expression prototype_character("diana", "folded") as diana_sprite at sprite_left
    show expression prototype_character("dima", "guarded") as dima_sprite at sprite_right
    with dissolve

    th "На трибунах солнце было похоже на пожар, который никак не решится стать настоящим."
    dm "В Горном все думают, что тайна защищает. На деле она только продлевает приговор."
    d "А твоя?"
    dm "У меня была сестра. Теперь у меня есть только привычка говорить о ней в прошедшем времени."

    menu:
        "Ответить искренне":
            $ dima_confession_unlocked = True
            $ diana_played_sincere = True
            $ dima_saw_truth = True
            $ shift_stat("trust_dima", 2)
            if evidence_strength >= 2:
                $ nikita_lead_open = True
            show expression prototype_character("dima", "thinking") as dima_sprite at sprite_right
            with dissolve
            d "Я устала быть умной вместо живой. Если ты правда хочешь помочь, я перестану делать вид, что всё под контролем."
            dm "Тогда слушай. Никита не просто уборщик на складах. Через него можно выйти наружу."
        "Использовать эмпатию как рычаг":
            $ dima_confession_unlocked = True
            $ diana_played_cold = True
            $ shift_stat("trust_dima", -1)
            $ shift_stat("ai_dependency", 1)
            show expression prototype_character("dima", "crossed") as dima_sprite at sprite_right
            with dissolve
            d "Мне жаль тебя. И именно поэтому нам лучше сразу стать союзниками."
            dm "Это была почти правильная фраза. Почти."
        "Испугаться и отступить":
            $ shift_stat("ai_dependency", 1)
            show expression prototype_character("dima", "guarded") as dima_sprite at sprite_right
            with dissolve
            d "Я не готова сейчас это нести."
            dm "Тогда не делай вид, что несёшь."
        "Свести всё к общему врагу":
            $ dima_confession_unlocked = True
            $ police_corruption_confirmed = True
            $ shift_stat("trust_dima", 1)
            $ shift_stat("ai_dependency", 1)
            if evidence_strength >= 3:
                $ nikita_lead_open = True
            show expression prototype_character("dima", "thinking") as dima_sprite at sprite_right
            with dissolve
            d "Личное потом. Сначала разберёмся, кто держит посёлок на страхе."
            dm "Участковый у них в связке. Никита — единственный нормальный выход наружу."

    if route_focus == "vika":
        $ shift_stat("trust_vika", 1)
        hide dima_sprite
        show expression prototype_character("vika", "pointing") as vika_sprite at sprite_right
        with dissolve
        th "Когда я вернулась к школе, Вика уже знала, что я где-то пропадала."
        v "Если решишь играть жёстко, делай это так, чтобы слухи работали на тебя."

    jump final_choice_scene

label final_choice_scene:
    $ play_prototype_bgm("suspense")
    scene expression prototype_scene("alley_well_night")
    with dissolve
    show expression prototype_character("diana", "phone") as diana_sprite at sprite_center
    with dissolve

    th "К финалу акта у меня были улики, чужие секреты и слишком мало права на ошибку."
    th "Оставалось решить, кто войдёт во тьму вместе со мной."

    menu:
        "Выйти на Никиту через Диму":
            $ final_choice = "dima"
            $ anonymous_tip_sent = True
            $ nikita_lead_open = True
            $ shift_stat("trust_dima", 1)
            $ shift_stat("evidence_strength", 1)
            show expression prototype_character("dima", "guarded") as dima_sprite at sprite_right
            with dissolve
            dm "Если пойдём этим путём, назад уже не отыграем."
            d "Мне не нужен назад."
        "Никому не доверять":
            $ final_choice = "alone"
            $ shift_stat("ai_dependency", 2)
            $ shift_stat("resolve", 1)
            th "Иногда одиночество не выбор, а форма дисциплины."
        "Сделать Вику социальным щитом":
            $ final_choice = "vika"
            $ vika_social_shield = True
            $ vika_feels_chosen = True
            $ shift_stat("trust_vika", 2)
            $ shift_stat("legend_integrity", 1)
            $ shift_stat("school_heat", -1)
            show expression prototype_character("vika", "pointing") as vika_sprite at sprite_right
            with dissolve
            v "Хорошо. Пока они смотрят на меня, ты ходишь под шум."
        "Держать всех в полутонах":
            $ final_choice = "mixed"
            $ shift_stat("trust_dima", 1)
            $ shift_stat("trust_misha", 1)
            $ shift_stat("criminal_heat", 1)
            $ shift_stat("school_heat", 1)
            show expression prototype_character("misha", "warning") as misha_sprite at sprite_right
            with dissolve
            th "Полутона выглядят взросло, пока не оказывается, что именно в них удобнее целиться."

    jump act_end

label act_end:
    $ ending_code = determine_act_ending(current_values())

    if ending_code == "A":
        jump ending_alliance
    elif ending_code == "B":
        jump ending_isolation
    elif ending_code == "C":
        jump ending_surveillance
    elif ending_code == "D":
        jump ending_social
    else:
        jump ending_mask

label ending_alliance:
    $ ending_title = "Союз в сумерках"
    $ play_prototype_bgm("finale")

    scene expression prototype_scene("stadium_sunset")
    with fade
    show expression prototype_character("diana", "folded") as diana_sprite at sprite_left
    show expression prototype_character("dima", "thinking") as dima_sprite at sprite_right
    with dissolve

    th "Дима не обещал спасение. Только присутствие. Для Горного это уже звучало как клятва."
    dm "До Никиты доберёмся тихо. Если повезёт, второй акт начнётся не с похорон."
    th "Впервые за долгое время чужая рука рядом не казалась ловушкой."

    jump final_summary

label ending_isolation:
    $ ending_title = "Один на один с тишиной"
    $ play_prototype_bgm("home_tension")

    scene expression prototype_scene("diana_room_night")
    with fade
    show expression prototype_character("diana", "shocked") as diana_sprite at sprite_center
    with dissolve

    th "Я оставила людей за дверью и забрала себе только факты."
    ai "Вероятность успешного выживания растёт при минимизации социальных рисков."
    th "Наверное. Но комната всё равно стала меньше."

    jump final_summary

label ending_surveillance:
    $ ending_title = "Под колпаком"
    $ play_prototype_bgm("investigation")

    scene expression prototype_scene("alley_well_night")
    with fade
    show expression prototype_character("diana", "phone") as diana_sprite at sprite_left
    show expression prototype_character("misha", "warning") as misha_sprite at sprite_right
    with dissolve

    th "Чьи-то шаги начали совпадать с нашими слишком часто."
    mi "Я предупреждал."
    th "Теперь Горный смотрел на наш дом как охотник, который уже выбрал сторону ветра."

    jump final_summary

label ending_social:
    $ ending_title = "Королева чужих секретов"
    $ play_prototype_bgm("school_day")

    scene expression prototype_scene("school_corridor")
    with fade
    show expression prototype_character("diana", "folded") as diana_sprite at sprite_left
    show expression prototype_character("vika", "pointing") as vika_sprite at sprite_right
    with dissolve

    v "Пока они обсуждают, с кем ты сидишь и кому улыбаешься, никто не заметит, что ты таскаешь улики."
    th "Вика дала мне власть. Только пахла она не свободой, а дорогим ядом."

    jump final_summary

label ending_mask:
    $ ending_title = "Слишком рано сорвана маска"
    $ play_prototype_bgm("suspense")

    scene expression prototype_scene("shed_night")
    with fade
    show expression prototype_character("diana", "shocked") as diana_sprite at sprite_left
    show expression prototype_character("marina", "stop") as marina_sprite at sprite_right
    with dissolve

    th "Правда выскочила раньше, чем я успела построить для неё коридор отхода."
    m "Диана..."
    th "В сарае снова что-то щёлкнуло. На этот раз звук уже был не от телефона."

    jump final_summary

label smoke_alliance:
    $ reset_prototype_state()
    $ route_focus = "dima"
    $ met_dima = True
    $ met_misha = True
    $ dima_book_route = True
    $ phone_found = True
    $ phone_hidden_success = True
    $ phone_photos_saved = True
    $ milana_topic_triggered = True
    $ dima_confession_unlocked = True
    $ dima_saw_truth = True
    $ nikita_lead_open = True
    $ final_choice = "dima"
    $ trust_dima = 5
    $ trust_misha = 2
    $ evidence_strength = 3
    $ resolve = 4
    jump act_end

label smoke_isolation:
    $ reset_prototype_state()
    $ route_focus = "misha"
    $ met_misha = True
    $ phone_found = True
    $ phone_photos_saved = True
    $ misha_warning_received = True
    $ final_choice = "alone"
    $ trust_misha = 1
    $ ai_dependency = 5
    $ evidence_strength = 2
    $ resolve = 3
    jump act_end

label smoke_social:
    $ reset_prototype_state()
    $ route_focus = "vika"
    $ met_vika = True
    $ phone_found = True
    $ mother_warned_partial = True
    $ final_choice = "vika"
    $ vika_social_shield = True
    $ vika_feels_chosen = True
    $ trust_vika = 4
    $ legend_integrity = 4
    $ school_heat = 1
    $ evidence_strength = 2
    jump act_end

label final_summary:
    $ assets_present, assets_total = prototype_asset_counts()
    $ play_prototype_bgm(None)

    centered "[ending_title]"

    th "Фокус акта: [prototype_route_title(route_focus)]."
    th "Дима [trust_dima], Миша [trust_misha], Вика [trust_vika], Марина [trust_marina]."
    th "Улики [evidence_strength], школа [school_heat], криминал [criminal_heat], ИИ [ai_dependency]."

    th "Ассеты проверены: [assets_present] из [assets_total] сцен закрыты реальными фонами, музыка и спрайты подключены без заглушек."

    th "Конец первого акта прототипа."

    return
