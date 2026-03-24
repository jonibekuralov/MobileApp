from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.clock import Clock

# Set window size for mobile-like experience
Window.size = (360, 640)
Window.clearcolor = (0.95, 0.95, 0.98, 1)

class StyledButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = 24
        self.color = (1, 1, 1, 1)
        
    def on_press(self):
        self.background_color = (0.7, 0.7, 0.7, 1)
        
    def on_release(self):
        self.background_color = self.original_color

class BeautyCalculatorApp(App):
    def build(self):
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Title
        title = Label(
            text='📱 Smart Calculator',
            font_size=28,
            size_hint=(1, 0.08),
            color=(0.2, 0.4, 0.8, 1),
            bold=True
        )
        main_layout.add_widget(title)
        
        # Display Card
        display_layout = BoxLayout(
            orientation='vertical', 
            size_hint=(1, 0.15),
            padding=15,
            spacing=5
        )
        
        result_label = Label(
            text='Natija',
            font_size=14,
            color=(0.5, 0.5, 0.5, 1),
            size_hint=(1, 0.3)
        )
        display_layout.add_widget(result_label)
        
        self.display = TextInput(
            text='0',
            font_size=36,
            size_hint=(1, 0.7),
            halign='right',
            readonly=True,
            background_color=(1, 1, 1, 1),
            foreground_color=(0.1, 0.1, 0.1, 1),
            cursor_color=(0, 0, 0, 0),
            border=(20, 20, 20, 20)
        )
        display_layout.add_widget(self.display)
        main_layout.add_widget(display_layout)
        
        # Button layout
        button_layout = BoxLayout(orientation='vertical', spacing=8)
        
        # Row 1: Clear, Delete, Percent, Divide
        row1 = BoxLayout(spacing=8)
        row1.add_widget(self.create_styled_button('C', (0.9, 0.3, 0.3, 1), self.clear))
        row1.add_widget(self.create_styled_button('⌫', (0.6, 0.6, 0.6, 1), self.delete))
        row1.add_widget(self.create_styled_button('%', (0.6, 0.6, 0.6, 1), lambda x: self.operator_press('%')))
        row1.add_widget(self.create_styled_button('÷', (0.6, 0.6, 0.6, 1), lambda x: self.operator_press('÷')))
        
        # Row 2: 7, 8, 9, Multiply
        row2 = BoxLayout(spacing=8)
        row2.add_widget(self.create_styled_button('7', (0.9, 0.9, 0.9, 1), lambda x: self.number_press('7')))
        row2.add_widget(self.create_styled_button('8', (0.9, 0.9, 0.9, 1), lambda x: self.number_press('8')))
        row2.add_widget(self.create_styled_button('9', (0.9, 0.9, 0.9, 1), lambda x: self.number_press('9')))
        row2.add_widget(self.create_styled_button('×', (0.6, 0.6, 0.6, 1), lambda x: self.operator_press('×')))
        
        # Row 3: 4, 5, 6, Subtract
        row3 = BoxLayout(spacing=8)
        row3.add_widget(self.create_styled_button('4', (0.9, 0.9, 0.9, 1), lambda x: self.number_press('4')))
        row3.add_widget(self.create_styled_button('5', (0.9, 0.9, 0.9, 1), lambda x: self.number_press('5')))
        row3.add_widget(self.create_styled_button('6', (0.9, 0.9, 0.9, 1), lambda x: self.number_press('6')))
        row3.add_widget(self.create_styled_button('−', (0.6, 0.6, 0.6, 1), lambda x: self.operator_press('−')))
        
        # Row 4: 1, 2, 3, Add
        row4 = BoxLayout(spacing=8)
        row4.add_widget(self.create_styled_button('1', (0.9, 0.9, 0.9, 1), lambda x: self.number_press('1')))
        row4.add_widget(self.create_styled_button('2', (0.9, 0.9, 0.9, 1), lambda x: self.number_press('2')))
        row4.add_widget(self.create_styled_button('3', (0.9, 0.9, 0.9, 1), lambda x: self.number_press('3')))
        row4.add_widget(self.create_styled_button('+', (0.6, 0.6, 0.6, 1), lambda x: self.operator_press('+')))
        
        # Row 5: 0, Decimal, Equals
        row5 = BoxLayout(spacing=8)
        row5.add_widget(self.create_styled_button('0', (0.9, 0.9, 0.9, 1), lambda x: self.number_press('0')))
        row5.add_widget(self.create_styled_button('.', (0.9, 0.9, 0.9, 1), self.decimal_press))
        row5.add_widget(self.create_styled_button('=', (0.3, 0.8, 0.3, 1), self.calculate))
        
        button_layout.add_widget(row1)
        button_layout.add_widget(row2)
        button_layout.add_widget(row3)
        button_layout.add_widget(row4)
        button_layout.add_widget(row5)
        
        main_layout.add_widget(button_layout)
        
        # Footer
        footer = Label(
            text='Made with ❤️ in Python',
            font_size=12,
            size_hint=(1, 0.05),
            color=(0.5, 0.5, 0.5, 1)
        )
        main_layout.add_widget(footer)
        
        return main_layout
    
    def create_styled_button(self, text, bg_color, on_press_func):
        button = Button(
            text=text,
            font_size=24,
            background_color=bg_color,
            color=(0.1, 0.1, 0.1, 1) if bg_color[0] > 0.7 else (1, 1, 1, 1),
            size_hint=(1, 1)
        )
        button.original_color = bg_color
        button.bind(on_press=on_press_func)
        return button
    
    def number_press(self, number):
        current = self.display.text
        if current == '0':
            self.display.text = number
        else:
            self.display.text = current + number
    
    def operator_press(self, operator):
        current = self.display.text
        if current and current[-1] not in '+−×÷%':
            self.display.text = current + operator
    
    def decimal_press(self, instance):
        current = self.display.text
        if '.' not in current:
            self.display.text = current + '.'
    
    def clear(self, instance):
        self.display.text = '0'
    
    def delete(self, instance):
        current = self.display.text
        if len(current) > 1:
            self.display.text = current[:-1]
        else:
            self.display.text = '0'
    
    def calculate(self, instance):
        try:
            expression = self.display.text
            # Replace symbols with Python operators
            expression = expression.replace('×', '*').replace('÷', '/').replace('−', '-')
            
            # Evaluate the expression
            result = eval(expression)
            
            # Format result
            if result == int(result):
                self.display.text = str(int(result))
            else:
                self.display.text = str(result)
        except:
            self.display.text = 'Xatolik'

if __name__ == '__main__':
    BeautyCalculatorApp().run()
