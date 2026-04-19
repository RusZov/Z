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
