from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDIconButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.toolbar import MDToolbar
from kivy.lang import Builder
from kv import words_kv, toolbar_kv, input_lineas_kv
import re

color_mumbai = [0/255, 3/255, 97/255, 0.8]

dict_medidas={
    'A':3.5,
    'B':3.5,
    'C':3.5,
    'D':3,
    'E':2.5,
    'F':2.5,
    'G':3,
    'H':3.5,
    'I':1.5,
    'J':1.5,
    'K':4,
    'L':2.5,
    'M':6,
    'N':3.5,
    'Ñ':3.5,
    'O':3,
    'P':3,
    'Q':3,
    'R':3,
    'S':3,
    'T':3.5,
    'U':3.5,
    'V':4,
    'W':6,
    'X':3.5,
    'Y':3.5,
    'Z':2.5,
    ' ':0.7
    }

# listToStr = ' '.join([str(elem) for elem in LISTA])

class Mumbai(MDApp):
    def build(self):
        
        screen_1 = Screen()

        self.toolbar = Builder.load_string(toolbar_kv)
        screen_1.add_widget(self.toolbar)

        btn_flat = MDIconButton(
            icon="./assets/icono.png",
            pos_hint= {"center_x": .5, "center_y": .3},
            user_font_size= "200sp",
            on_release=self.calculate
            )
        screen_1.add_widget(btn_flat)
        
        self.words = Builder.load_string(words_kv)
        screen_1.add_widget(self.words)

        self.input_lineas = Builder.load_string(input_lineas_kv)
        screen_1.add_widget(self.input_lineas)
        
        return screen_1
    
    def calculate(self, obj):
        if self.words.text=="" and self.input_lineas.text=="":
            close_btn = MDFlatButton(text="Cerrar", on_release=self.close_dialog)
            self.dialog = MDDialog(
                text="Si hunde el botón sin llenar ningún campo, 3 vaquitas y 3 perritos se ponen tristes :C",
                title='Le hundió sin llenar nungún campo :C:C:C:C:C',
                size_hint=(0.7, 1),
                buttons=[close_btn]
                )
            self.dialog.open()
        if self.words.text=="" and self.input_lineas.text!="":
            close_btn = MDFlatButton(text="Cerrar", on_release=self.close_dialog)
            self.dialog = MDDialog(
                text="Si hunde el botón sin poner una frase, 3 vaquitas se ponen tristes :C",
                title='Le hundió sin poner la frase :C:C:C:C:C',
                size_hint=(0.7, 1),
                buttons=[close_btn]
                )
            self.dialog.open()
        if self.words.text!="" and self.input_lineas.text=="":
            close_btn = MDFlatButton(text="Cerrar", on_release=self.close_dialog)
            self.dialog = MDDialog(
                text="Si hunde el botón sin llenar el número de líneas, 3 perritos se ponen tristes :C",
                title='Le hundió sin poner el número de líneas :C:C:C:C:C',
                size_hint=(0.7, 1),
                buttons=[close_btn]
                )
            self.dialog.open()
        if self.words.text!="" and self.input_lineas.text!="":
            try:
                frase=self.words.text
                lineas_deseadas = int(self.input_lineas.text)
                try:
                    ######################
                    palabras_lista = frase.split(' ')
                    palabras_dict={}

                    for palabra in palabras_lista:
                        longitud_letras_palabra= []
                        for letra in palabra:
                            longitud_letras_palabra.append(dict_medidas[letra])
                        espacio_entre_letras = (len(palabra)-1)*0.3
                        longitud_palabra = sum(longitud_letras_palabra)+espacio_entre_letras
                        palabras_dict.update({palabra:longitud_palabra})

                    lineas = {}
                    longitudes_linea = {}
                    for linea in range(lineas_deseadas):
                        lineas.update({f'linea_{linea+1}':[]})
                        longitudes_linea.update({f'linea_{linea+1}':[]})

                    longitud_total = sum(palabras_dict.values())
                    longitud_optima = longitud_total/lineas_deseadas
                    palabras_optimas = len(palabras_dict)/lineas_deseadas

                    linea_actual=1

                    for palabra in palabras_dict:
                        lineas[f'linea_{linea_actual}'].append(palabra)
                        longitud_actual_frase = []
                        for i in lineas[f'linea_{linea_actual}']:
                            longitud_actual_frase.append(palabras_dict[i])
                        longitud_actual_frase=sum(longitud_actual_frase)
                        if len(lineas[f'linea_{linea_actual}']) >= palabras_optimas or longitud_actual_frase >= longitud_optima:
                            linea_actual+=1

                    for linea in lineas.keys():
                        longitud_frase = []
                        for i in lineas[linea]:
                            longitud_frase.append(palabras_dict[i])
                        longitud_frase=sum(longitud_frase)+0.7*(len(lineas[linea])-1)
                        longitudes_linea.update({linea:longitud_frase})

                    horizontal = round(max(longitudes_linea.values())+3, 1)
                    vertical = round(6*len(lineas)+(1*(len(lineas)-1))+3, 1)
                    altura = 3
                    ######################
                    medidas="HORIZONTAL: "+str(horizontal)+" cm \n"+"VERTICAL: "+str(vertical)+" cm \n"+"ALTURA: "+str(altura)+" cm"
                    descripcion = ''
                    for i in lineas.values():
                        for j in i:
                            descripcion=descripcion+j+' '
                        descripcion=descripcion+'\n--------------------------------------------\n'
                    close_btn = MDFlatButton(text="Cerrar", on_release=self.close_dialog)
                    self.dialog = MDDialog(
                        text=medidas+'\n'+'*************************\n*************************\n'+descripcion,
                        title='MEDIDAS PARA:\n'+'"'+frase+'"'+' en '+str(lineas_deseadas)+' líneas.',
                        size_hint=(0.7, 1),
                        buttons=[close_btn]
                        )
                    self.dialog.open()
                except Exception as e:
                    print("hubo error", e)
            except:
                close_btn = MDFlatButton(text="Cerrar", on_release=self.close_dialog)
                self.dialog = MDDialog(
                    text="Si hunde el botón y el número de líneas no es un entero, 3 cabritas se ponen tristes :C",
                    title='Puso un número de líneas que no es un número entero :C:C:C:C:C',
                    size_hint=(0.7, 1),
                    buttons=[close_btn]
                    )
                self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

Mumbai().run()