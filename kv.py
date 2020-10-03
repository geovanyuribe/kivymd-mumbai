words_kv ="""
MDTextField:
    hint_text:"Introduzca la frase"
    helper_text: "Porfis escriba todo en mayúsculas (La amo muchito <3)"
    helper_text_mode:"persistent"
    pos_hint: {'center_x': .5, 'center_y': .82}
    size_hint_x: None
    width:300
    color_mode: 'custom'
    line_color_focus: 0, 0.01176, 0.68039, 0.8
"""

input_lineas_kv ="""
MDTextField:
    hint_text:"Introduzca el número de líneas"
    helper_text: "Porfis escriba un número entero (La amo kilitos C:)"
    helper_text_mode:"persistent"
    pos_hint: {'center_x': .5, 'center_y': .65}
    size_hint_x: None
    width:300
    color_mode: 'custom'
    line_color_focus: 0, 0.01176, 0.68039, 0.8
"""

toolbar_kv ="""
BoxLayout:
    orientation:'vertical'
    MDToolbar:
        title: "Lilo Cajitas Mumbai"
        md_bg_color: 0, 0.01176, 0.48039, 0.8

    MDLabel:
        halign: "center"
"""