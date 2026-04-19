define config.name = _("Горный воздух пахнет сиренью и ложью")
define config.version = "0.2.0-prototype"

define gui.show_name = True

define gui.about = _p("""
Первый играбельный прототип визуальной новеллы по книге.

Собран в отдельной папке prototype, использует сценарные документы первого акта
и требует полный комплект реальных ассетов для запуска демо.

Музыка для прототипа: Scott Buckley, лицензия CC BY 4.0.
Текст атрибуции сохранён в game/audio/CREDITS.txt.
""")

define build.name = "gorny_lilac_lies"
define config.save_directory = "gorny_lilac_lies_prototype"

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = dissolve
define config.end_game_transition = dissolve

define config.window = "auto"

default preferences.text_cps = 0
default preferences.afm_time = 15

init python:
    build.classify("**~", None)
    build.classify("**.bak", None)
    build.classify("**/.**", None)
    build.classify("**/#**", None)
    build.classify("**/thumbs.db", None)

    build.documentation("*.md")
    build.documentation("*.txt")
