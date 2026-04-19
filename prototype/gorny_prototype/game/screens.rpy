init offset = -1

style default:
    properties gui.text_properties()

style gui_text:
    properties gui.text_properties("interface")

style button:
    background Solid("#111319dd")
    hover_background Solid("#202637ee")
    xpadding 24
    ypadding 16

style button_text is gui_text:
    yalign 0.5
    color "#f4efff"
    hover_color "#ffffff"

style label_text is gui_text:
    color gui.accent_color

style prompt_text is gui_text

screen say(who, what):
    window:
        id "window"

        background Solid("#121319e8")
        xfill True
        ysize gui.textbox_height
        yalign 1.0

        if who is not None:
            text who id "who" style "say_label"

        text what id "what" style "say_dialogue"

style say_label is default:
    font gui.name_text_font
    size gui.name_text_size
    color gui.accent_color
    xpos gui.name_xpos
    ypos gui.name_ypos

style say_dialogue is default:
    font gui.text_font
    size gui.text_size
    color gui.text_color
    xpos gui.dialogue_xpos
    xmaximum gui.dialogue_width
    ypos gui.dialogue_ypos
    adjust_spacing False

screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.58
        spacing 14

        for i in items:
            textbutton i.caption action i.action

style choice_button is button:
    xsize gui.choice_button_width
    xalign 0.5

style choice_button_text is button_text:
    size gui.choice_button_text_size
    xalign 0.5
    text_align 0.5

screen navigation():
    vbox:
        style_prefix "navigation"
        xalign 0.87
        yalign 0.56
        spacing 18

        if main_menu:
            textbutton _("Start Game") action Start()
        else:
            textbutton _("Return") action Return()
            textbutton _("Save Game") action ShowMenu("save")
            textbutton _("History") action ShowMenu("history")

        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("About") action ShowMenu("about")

        if main_menu:
            textbutton _("Quit") action Quit(confirm=False)
        else:
            textbutton _("Main Menu") action MainMenu(confirm=False)

style navigation_button is button:
    background Solid("#111319dd")
    hover_background Solid("#202637ee")
    xminimum 320
    xpadding 34
    ypadding 18

style navigation_button_text is button_text:
    size 30
    xalign 0.0

screen main_menu():
    tag menu

    add gui.main_menu_background
    add Solid("#07080d88")

    frame:
        style "main_menu_panel"

        vbox:
            spacing 16

            text config.name style "main_menu_title"
            text _("Prototype build") style "main_menu_subtitle"

    use navigation

style main_menu_panel is empty:
    xpos 72
    ypos 70
    xmaximum 720
    ypadding 22
    xpadding 28
    background Solid("#0c0d14b8")

style main_menu_title is gui_text:
    size 44
    color "#ffffff"

style main_menu_subtitle is gui_text:
    size 24
    color "#e8ddea"
    xmaximum 620

screen game_menu(title, scroll=None, yinitial=0.0):
    tag menu

    add gui.game_menu_background
    add Solid("#07080dc2")

    frame:
        style "game_menu_content_frame"

        vbox:
            spacing 20

            text title style "game_menu_title"

            if scroll == "viewport":
                viewport:
                    mousewheel True
                    draggable True
                    scrollbars "vertical"
                    yinitial yinitial

                    vbox:
                        spacing 16
                        transclude
            elif scroll == "vpgrid":
                vpgrid:
                    cols 1
                    mousewheel True
                    draggable True
                    scrollbars "vertical"
                    yinitial yinitial

                    transclude
            else:
                transclude

    use navigation

style game_menu_content_frame is empty:
    xpos 80
    ypos 90
    xsize 900
    ysize 540
    xpadding 28
    ypadding 24
    background Solid("#11131ae0")

style game_menu_title is gui_text:
    size 38
    color gui.accent_color

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200

    add Solid("#00000099")

    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 720
        xpadding 36
        ypadding 28
        background Solid("#121319f4")

        vbox:
            spacing 24

            text message style "confirm_prompt"

            hbox:
                xalign 0.5
                spacing 24

                textbutton _("Да") action yes_action style "confirm_button"
                textbutton _("Нет") action no_action style "confirm_button"

style confirm_prompt is gui_text:
    size 28
    text_align 0.5
    xalign 0.5

style confirm_button is button:
    xminimum 180

style confirm_button_text is button_text:
    xalign 0.5

default quick_menu = False
