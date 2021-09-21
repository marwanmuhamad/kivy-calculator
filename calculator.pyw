from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window 


#Set the app size:
Window.size = (300, 500)

Builder.load_file('calculator.kv')

class MyLayout(Widget):

    # my_value = ""
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.val = ""
            
    # create functions:
    def percent(self):
        if self.val == "0":
            self.val = "" 
        self.val += "%"
        self.ids.calc_input.text = self.val

    def delete(self):
        try:
            self.val = list(self.val) 
            self.val.pop()
            myStr = "" 
            for i in self.val:
                myStr += str(i)
            self.val = myStr 
            self.ids.calc_input.text = self.val
        except Exception as e:
            # print(e)
            self.val = "0"
            self.ids.calc_input.text = self.val
    def clear(self):
        self.val = "0"
        self.ids.calc_input.text = self.val

    def devide(self):
        self.val += "/"
        self.ids.calc_input.text = self.val
    
    def seven(self):
        if self.val == "0":
            self.val = "" 
        self.val += "7"
        self.ids.calc_input.text = self.val
    
    def eight(self):
        if self.val == "0":
            self.val = ""  
        self.val += "8"
        self.ids.calc_input.text = self.val
    
    def nine(self):
        if self.val == "0":
            self.val = "" 
        self.val += "9"
        self.ids.calc_input.text = self.val
    
    def multiply(self):
        self.val += "*"
        self.ids.calc_input.text = self.val
    
    def four(self):
        if self.val == "0":
            self.val = "" 
        self.val += "4"
        self.ids.calc_input.text = self.val
    
    def five(self):
        if self.val == "0":
            self.val = "" 
        self.val += "5"
        self.ids.calc_input.text = self.val
    
    def six(self):
        if self.val == "0":
            self.val = "" 
        self.val += "6"
        self.ids.calc_input.text = self.val
    
    def minus(self):
        self.val += "-"
        self.ids.calc_input.text = self.val
    
    def one(self):
        if self.val == "0":
            self.val = "" 
        self.val += "1"
        self.ids.calc_input.text = self.val
    
    def two(self):
        if self.val == "0":
            self.val = "" 
        self.val += "2"
        self.ids.calc_input.text = self.val
    
    def three(self):
        if self.val == "0":
            self.val = "" 
        self.val += "3"
        self.ids.calc_input.text = self.val
    
    def plus(self):
        self.val += "+"
        self.ids.calc_input.text = self.val
    
    def sign(self):
        if self.val.startswith("-"):
            self.val = self.val.lstrip("-")
        elif not self.val.startswith("-"):
            self.val = "-" + self.val
        
        self.ids.calc_input.text = self.val

    def zero(self):
        if self.val == "0":
            self.val = "" 
        self.val += "0"
        self.ids.calc_input.text = self.val
    
    def dot(self):
        self.val += "."
        self.ids.calc_input.text = self.val
    
    def equal(self):
        try:
            if self.val.endswith("%"):
                self.val = self.val.rstrip("%")
                self.val += "/100"
            elif self.val.startswith("%"):
                self.val = self.val.lstrip("%")
            
            self.val = eval(self.val)
            self.val = str(self.val)
            self.ids.calc_input.text = self.val
        except:
            return None
    
    def __del__(self):
        self.val = ""


class Calculator(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    Calculator().run()