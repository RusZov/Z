define r = Character("Рома", color="#d9c29c")
define n = Character("Никита", color="#b9ead7")

default act2_phone_hunt_confirmed = False
default act2_marina_partial_confession = False
default act2_school_cover_ready = False
default act2_roma_scene_done = False
default act2_nikita_contact_ready = False
default act2_nikita_contacted = False
default act2_entry_variant = "direct"

init 1 python:
    BASE_FLAGS.update({
        "act2_phone_hunt_confirmed": False,
        "act2_marina_partial_confession": False,
        "act2_school_cover_ready": False,
        "act2_roma_scene_done": False,
        "act2_nikita_contact_ready": False,
        "act2_nikita_contacted": False,
        "act2_entry_variant": "direct",
    })

init python:
    def act2_entry_summary():
        if getattr(store, "ending_code", None) == "A":
            return "После сумеречного союза стало ясно: передышка была не наградой, а отсрочкой."
        if getattr(store, "ending_code", None) == "D":
            return "После школьной победы оказалось, что слухи умеют защищать только днём."
        if getattr(store, "ending_code", None) == "C":
            return "После слежки ночь в Горном стала теснее, чем любая комната."
        if getattr(store, "ending_code", None) == "E":
            return "После сорванной маски каждый шорох звучал как продолжение той же ошибки."
        return "После финала демо у Дианы остался телефон, слишком мало сна и слишком много людей, которым он был нужен."


label act2_start:
    $ act2_entry_variant = ending_code or "direct"
    $ play_prototype_bgm("suspense")

    scene expression prototype_scene("diana_room_night")
    with fade
    show expression prototype_character("diana", "phone") as diana_sprite at sprite_left
    show expression prototype_character("marina", "bag") as marina_sprite at sprite_right
    with dissolve

    th "[act2_entry_summary()]"
    th "Телефон лежал между мной и стеной, как отдельный жилец. Я уже почти уснула, когда он вспыхнул без звука."
    th "На экране мелькнуло: «Где вещь из сарая? Утром заберём. Адрес подтвердили»."

    $ act2_phone_hunt_confirmed = True
    $ shift_stat("criminal_heat", 1)
    $ shift_stat("resolve", 1)

    m "Покажи."
    d "Ты говорила, что до утра нас никто не тронет."
    m "Я говорила, что надеюсь. Это не одно и то же."

    menu:
        "Спрятать телефон глубже и требовать ответов":
            $ phone_hidden_success = True
            $ shift_stat("trust_marina", 1)
            $ shift_stat("legend_integrity", -1)
            d "Тогда без пауз. Кто именно его ищет?"
        "Оставить телефон в руке и сразу считать угрозу":
            $ phone_photos_saved = True
            $ shift_stat("evidence_strength", 1)
            $ shift_stat("ai_dependency", 1)
            d "Утром уже поздно. Мне нужно понимать, куда они придут сначала."

    m "Не участковый. Те, кто выше него. Им нужен не ты, а то, что может открыть этот телефон."
    th "Значит, телефон искали не как улику. Его искали как ключ."

    jump act2_home_partial_confession


label act2_home_partial_confession:
    $ play_prototype_bgm("home_tension")

    scene expression prototype_scene("diana_room_night")
    with dissolve
    show expression prototype_character("diana", "folded") as diana_sprite at sprite_left
    show expression prototype_character("marina", "stop") as marina_sprite at sprite_right
    with dissolve

    th "Марина села на край кровати так, будто собиралась признаться во всём. Но даже в темноте было видно: признается только в той части, которую сможет пережить."

    menu:
        "Давить прямо: про долг, переезд и сумку":
            $ act2_marina_partial_confession = True
            $ mother_warned_partial = True
            $ shift_stat("trust_marina", -1)
            $ shift_stat("resolve", 1)
            d "Хватит нарезать правду ломтиками. Долг. Переезд. Сумка. Начни хоть с одного."
            m "Долг был ещё до Горного. Переездом я покупала нам время. А сумку меня попросили довезти и молчать."
        "Говорить тише и дать ей выбрать, с чего начать":
            $ act2_marina_partial_confession = True
            $ mother_warned_partial = True
            $ marina_trusts_diana_plan = True
            $ shift_stat("trust_marina", 1)
            d "Скажи ту часть, на которой ты не сломаешься."
            m "Хорошо. Есть долг, который я не вытянула бы одна. Мы приехали сюда не случайно. И в сумке было не то, о чём мне сказали сначала."

    m "Имена я пока не дам. Если ты их услышишь сейчас, назад дороги уже не будет."
    d "Назад у нас и так нет."
    m "Есть хотя бы видимость нормальности. Её надо дотянуть до школы."

    $ shift_stat("school_heat", 1)

    jump act2_school_cover_vika


label act2_school_cover_vika:
    $ play_prototype_bgm("school_day")

    scene expression prototype_scene("school_corridor")
    with dissolve
    show expression prototype_character("diana", "folded") as diana_sprite at sprite_left
    show expression prototype_character("vika", "dominant") as vika_sprite at sprite_right
    with dissolve

    th "Утром школа выглядела как декорация для чужой стабильности. Вика заметила мой недосып раньше, чем я успела придумать выражение лица."
    v "Ты или влюбилась, или влипла. Для Горного второе вероятнее."
    d "Мне нужен шум. Красивый, бессмысленный и достаточно громкий."
    show expression prototype_character("vika", "smirk") as vika_sprite at sprite_right
    with dissolve
    v "То есть я."

    menu:
        "Попросить Вику разогнать слух о новой школьной драме":
            $ vika_social_shield = True
            $ act2_school_cover_ready = True
            $ shift_stat("trust_vika", 2)
            $ shift_stat("school_heat", -1)
            $ shift_stat("legend_integrity", 1)
            v "Сделаем тебе образ девочки, у которой проблемы только романтические. Это самая надёжная маскировка."
        "Сделать Вику точкой доступа к журналам и кабинетам":
            $ vika_social_shield = True
            $ act2_school_cover_ready = True
            $ shift_stat("trust_vika", 1)
            $ shift_stat("evidence_strength", 1)
            $ shift_stat("school_heat", 1)
            v "Хорошо. Я отвлеку тех, кто любит смотреть в списки и чужие рюкзаки. Но ты потом расскажешь, зачем тебе это было."

    $ vika_feels_chosen = True
    $ met_vika = True

    th "Школа стала не убежищем, а полем прикрытия. Но в Горном это уже почти одно и то же."

    jump act2_roma_at_well


label act2_roma_at_well:
    $ play_prototype_bgm("investigation")
    $ roma_informant_open = True
    $ act2_roma_scene_done = True

    scene expression prototype_scene("alley_well_night")
    with dissolve
    show expression prototype_character("diana", "phone") as diana_sprite at sprite_left
    with dissolve

    th "К колодцу я пришла затемно. Это место уже умело хранить чужие голоса глубже воды."
    r "Марина всё-таки не удержала тебя дома."
    d "Значит, ты следил не за ней."
    r "Я следил за теми, кто спрашивал про телефон. Сегодня спрашивали слишком уверенно."

    menu:
        "Прижать Рому и потребовать имя":
            $ diana_used_roma_ruthlessly = True
            $ shift_stat("criminal_heat", 1)
            $ shift_stat("trust_marina", -1)
            d "Мне нужен не туман, а имя."
            r "Никита. Но не произноси его рядом с теми, кто носит форму."
        "Оставить Роме возможность отступить":
            $ diana_protected_roma = True
            $ shift_stat("trust_misha", 1)
            $ shift_stat("evidence_strength", 1)
            d "Скажи только то, после чего тебя не закопают за сараями."
            r "Тогда слушай. Ищут выход на Никиту. Он держится отдельно, но его уже тоже поджимают."

    $ nikita_lead_open = True
    $ act2_nikita_contact_ready = True

    r "У колодца его не жди. Иди через складскую остановку, через старый номер на бумажке. Он отвечает только на чужую осторожность."
    th "Рома не выглядел героем. В Горном это было лучшей рекомендацией."

    jump act2_nikita_lead


label act2_nikita_lead:
    $ play_prototype_bgm("finale")

    scene expression prototype_scene("misha_porch_evening")
    with dissolve
    show expression prototype_character("diana", "phone") as diana_sprite at sprite_left
    with dissolve

    th "Я переписала номер с влажной бумажки и трижды проверила, не дрожат ли пальцы. Дрожали, но не настолько, чтобы отступить."

    menu:
        "Написать Никите сразу и без легенды":
            $ act2_nikita_contacted = True
            $ shift_stat("resolve", 1)
            $ shift_stat("legend_integrity", -1)
            d "Мне нужен выход из Горного раньше, чем здесь начнут выбивать двери."
        "Сначала отправить короткий сигнал и ждать ответа":
            $ act2_nikita_contacted = True
            $ anonymous_tip_sent = True
            $ shift_stat("evidence_strength", 1)
            $ shift_stat("ai_dependency", 1)
            d "Я отправила только фото экрана, время и одну фразу: «Телефон уже ищут. Мне сказали, что ты не из них»."

    n "Если телефон у тебя, не неси его домой завтра."
    n "В школе тебя прикроют только до обеда."
    n "Если готова услышать полную цену долга Марины, приходи одна."

    $ criminal_heat = max(criminal_heat, 2)
    $ act2_nikita_contact_ready = False

    th "Выход на Никиту нашёлся не как спасение, а как следующий узкий коридор."
    th "Заготовка акта 2 собрана: телефон уже ищут, легенда держится на Вике, Рома дал проход наружу, а Никита назначил условия."

    return


label smoke_act2:
    $ reset_prototype_state()
    $ route_focus = "dima"
    $ met_dima = True
    $ met_vika = True
    $ phone_found = True
    $ phone_hidden_success = True
    $ phone_photos_saved = True
    $ dima_confession_unlocked = True
    $ nikita_lead_open = True
    $ final_choice = "dima"
    $ ending_code = "A"
    $ ending_title = "Союз в сумерках"
    $ trust_dima = 4
    $ trust_vika = 2
    $ trust_marina = 2
    $ evidence_strength = 3
    $ resolve = 3
    jump act2_start
