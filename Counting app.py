import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class main(GridLayout):
    
    def __init__(self, **kwargs):
        super(main, self).__init__(**kwargs)

        self.running = 0
        self.true = 0
        self.decks = 0
        self.units = 0
        self.count = 0
        self.started = False
        self.minimum = 0
        
        self.cols = 2        

        self.betLbl = Label(text="Bet: ", font_size=32)
        self.add_widget(self.betLbl)

        self.startBtn = Button(text="Start", font_size=32)
        self.startBtn.bind(on_press=self.startStop)
        self.add_widget(self.startBtn)

        self.plusBtn = Button(text="2,3,4,5,6", font_size=32)
        self.plusBtn.bind(on_press=self.plus)
        self.add_widget(self.plusBtn)

        self.minusBtn = Button(text="10,J,Q,K,A", font_size=32)
        self.minusBtn.bind(on_press=self.minus)
        self.add_widget(self.minusBtn)

        self.unitsIn = TextInput(multiline=False,text="Units")
        self.add_widget(self.unitsIn)

        self.decksIn = TextInput(multiline=False,text="Decks")
        self.add_widget(self.decksIn)

    def plus(self, instance):
        if self.started:
            self.running += 1
            self.count += 1
            if self.count == 26:
                self.decks -= 1
                self.count = 0
            self.true = self.running/self.decks
            if self.true < -2:
                bet = 0
            elif self.true < 1:
                bet = self.units
            elif self.true > 5:
                bet = self.units * 5
            else:
                bet = self.true * self.units
            
            self.betLbl.text = "Bet: " + str(int(bet))

    def minus(self, instance):
        if self.started:
            self.running -= 1
            self.count -= 1
            if self.count == 26:
                self.decks -= 1
                self.count = 0
            self.true = self.running/self.decks
            if self.true < -2:
                bet = 0
            elif self.true < 1:
                bet = self.units
            elif self.true > 5:
                bet = self.units * 5
            else:
                bet = self.true * self.units
            
            self.betLbl.text = "Bet: " + str(int(bet))
    
    def startStop(self, instance):
        if self.startBtn.text == "Start":
            try:
                self.decks = float(self.decksIn.text)
                self.units = int(self.unitsIn.text)
                #make sure these aren't 0
                x = 1/self.decks
                x = 1/self.units
                self.minimum = 0.5*self.decks - 5
                self.started = True
                self.betLbl.text = "Bet: " + str(self.units)                
                self.startBtn.text = "Stop"
            except Exception as e:
                print(e)
            
        elif self.startBtn.text == "Stop":
            self.running = 0
            self.true = 0
            self.started = False
            self.startBtn.text = "Start"
           

class cardApp(App):
    def build(self):
        return main()
    
cardApp().run()
