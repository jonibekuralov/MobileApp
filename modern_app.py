from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.card import MDCard
from kivymd.uix.gridlayout import MDGridLayout
from kivy.core.window import Window

# Set window size for mobile-like experience
Window.size = (360, 640)

# KV Language for UI
KV = '''
MDScreen:
    MDBoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 20
        
        # App Header
        MDTopAppBar:
            title: "Smart Calculator"
            elevation: 4
            pos_hint: {"top": 1}
        
        # Display Card
        MDCard:
            orientation: 'vertical'
            padding: 15
            spacing: 10
            elevation: 3
            radius: [15, 15, 15, 15]
            
            MDLabel:
                text: "Result"
                theme_text_color: "Secondary"
                font_style: "Caption"
                halign: "center"
            
            MDTextField:
                id: display
                text: "0"
                font_style: "H4"
                halign: "center"
                readonly: True
                input_filter: "float"
        
        # Button Grid
        MDGridLayout:
            cols: 4
            spacing: 10
            padding: 10
            
            # Row 1
            MDRaisedButton:
                text: "C"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: app.theme_cls.error_color
                on_press: app.clear()
            
            MDRaisedButton:
                text: "⌫"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: app.theme_cls.primary_dark
                on_press: app.delete()
            
            MDRaisedButton:
                text: "%"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: app.theme_cls.primary_dark
                on_press: app.operator_press("%")
            
            MDRaisedButton:
                text: "÷"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: app.theme_cls.primary_dark
                on_press: app.operator_press("÷")
            
            # Row 2
            MDRaisedButton:
                text: "7"
                on_press: app.number_press("7")
            
            MDRaisedButton:
                text: "8"
                on_press: app.number_press("8")
            
            MDRaisedButton:
                text: "9"
                on_press: app.number_press("9")
            
            MDRaisedButton:
                text: "×"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: app.theme_cls.primary_dark
                on_press: app.operator_press("×")
            
            # Row 3
            MDRaisedButton:
                text: "4"
                on_press: app.number_press("4")
            
            MDRaisedButton:
                text: "5"
                on_press: app.number_press("5")
            
            MDRaisedButton:
                text: "6"
                on_press: app.number_press("6")
            
            MDRaisedButton:
                text: "−"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: app.theme_cls.primary_dark
                on_press: app.operator_press("−")
            
            # Row 4
            MDRaisedButton:
                text: "1"
                on_press: app.number_press("1")
            
            MDRaisedButton:
                text: "2"
                on_press: app.number_press("2")
            
            MDRaisedButton:
                text: "3"
                on_press: app.number_press("3")
            
            MDRaisedButton:
                text: "+"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: app.theme_cls.primary_dark
                on_press: app.operator_press("+")
            
            # Row 5
            MDRaisedButton:
                text: "0"
                on_press: app.number_press("0")
            
            MDRaisedButton:
                text: "."
                on_press: app.decimal_press()
            
            MDRaisedButton:
                text: "="
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                md_bg_color: app.theme_cls.success_color
                on_press: app.calculate()
'''

class ModernCalculatorApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)
    
    def get_display(self):
        return self.root.ids.display
    
    def number_press(self, number):
        display = self.get_display()
        current = display.text
        if current == "0":
            display.text = number
        else:
            display.text = current + number
    
    def operator_press(self, operator):
        display = self.get_display()
        current = display.text
        if current and current[-1] not in '+−×÷%':
            display.text = current + operator
    
    def decimal_press(self):
        display = self.get_display()
        current = display.text
        if '.' not in current:
            display.text = current + '.'
    
    def clear(self):
        self.get_display().text = "0"
    
    def delete(self):
        display = self.get_display()
        current = display.text
        if len(current) > 1:
            display.text = current[:-1]
        else:
            display.text = "0"
    
    def calculate(self):
        display = self.get_display()
        try:
            expression = display.text
            # Replace symbols with Python operators
            expression = expression.replace('×', '*').replace('÷', '/').replace('−', '-')
            
            # Evaluate the expression
            result = eval(expression)
            
            # Format result
            if result == int(result):
                display.text = str(int(result))
            else:
                display.text = str(result)
        except:
            display.text = "Error"

if __name__ == '__main__':
    ModernCalculatorApp().run()
