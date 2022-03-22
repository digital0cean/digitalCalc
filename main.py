# =================================================================

from fontTools.ttLib import TTFont
import matplotlib.pyplot as plot
from tkinter import *
from numpy import *
from misc import *
import pyperclip
import math

# =================================================================

class ButtonsCoordinates(object):
    x = 10
    y = 62

class Main(Frame):
    def __init__(self, app):
        super(Main, self).__init__(app)
        self.builder()

    def builder(self):
        try:
            font = TTFont('misc/Notewroty.otf')
            font.save()
        except:
            print("Шрифт уже загружен")

        self.frame = Frame(width = 490, height = 52, bg = Colors.white).place(x = 5, y = 5)
        self.frame = Frame(width = 470, height = 306, bg = Colors.shad).place(x = 15, y = 390); self.frame = Frame(width = 480, height = 306, bg = Colors.dark_yellow).place(x = 10, y = 380)
        self.frame = Frame(width = 470, height = 310, bg = Colors.shad).place(x = 15, y = 65); self.frame = Frame(width = 490, height = 310, bg = Colors.plotcalc).place(x = 5, y = 55)

        self.eq = "0"
        self.label = Label(text = self.eq, font = ("Noteworthy", 20, "bold"), bg = Colors.white, fg = Colors.black)
        self.label.place(x = 10, y = 8)

        self.text1 = Label(text = "Напиши функцию f(x), чтобы нарисовать её график!", bg = Colors.dark_yellow, fg = Colors.black, font = ("Noteworthy", 18, "bold"))
        self.text1.place(x = 13, y = 380)
        self.text2 = Label(text = "Начало", bg = Colors.dark_yellow, fg = Colors.black, font = ("Noteworthy", 12, "bold"))
        self.text2.place(x = 25, y = 520)
        self.text3 = Label(text = "Конец", bg = Colors.dark_yellow, fg = Colors.black, font = ("Noteworthy", 12, "bold"))
        self.text3.place(x = 120, y = 520)
        self.text4 = Label(text = "Шаг", bg = Colors.dark_yellow, fg = Colors.black, font = ("Noteworthy", 12, "bold"))
        self.text4.place(x = 246, y = 520)

        self.fx = StringVar(value = "sin(x)")
        self.input = Entry(width = 20, bd = 4, justify = LEFT, selectforeground = Colors.darknest_yellow, selectbackground = Colors.black, textvariable = str(self.fx), bg = Colors.dark_yellow, fg = Colors.black, font = ("Noteworthy", 18, "bold"))
        self.input.place(x = 13, y = 420)

        fx_com = lambda commanda = self.fx: self.fx_logic(commanda)
        self.fx_button = Button(width = 11, height = 2, text = "Нарисовать", bd = 0, highlightthickness = 0, highlightbackground = Colors.yellow, font = ("Noteworthy", 11, "bold"), fg = Colors.black, command = fx_com)
        self.fx_button.place(x = 350, y = 422)

        self.fx_start = StringVar(value = "-4")
        self.input_start = Entry(width = 4, bd = 4, justify = LEFT, selectforeground = Colors.darknest_yellow, selectbackground = Colors.black, textvariable = str(self.fx_start), bg = Colors.dark_yellow, fg = Colors.black, font = ("Noteworthy", 18, "bold"))
        self.input_start.place(x = 13, y = 480)

        self.fx_end = StringVar(value = "4")
        self.input_end = Entry(width = 4, bd = 4, justify = LEFT, selectforeground = Colors.darknest_yellow, selectbackground = Colors.black, textvariable = str(self.fx_end), bg = Colors.dark_yellow, fg = Colors.black, font = ("Noteworthy", 18, "bold"))
        self.input_end.place(x = 103, y = 480)

        self.fx_step = StringVar(value = "0.0001")
        self.input_step = Entry(width = 8, bd = 4, justify = LEFT, selectforeground = Colors.darknest_yellow, selectbackground = Colors.black, textvariable = str(self.fx_step), bg = Colors.dark_yellow, fg = Colors.black, font = ("Noteworthy", 18, "bold"))
        self.input_step.place(x = 193, y = 480)

        self.fx_grid = IntVar(value = 1)
        self.c_grid = Checkbutton(text = "Сетка", bg = Colors.dark_yellow, variable = self.fx_grid, fg = Colors.black, font = ("Noteworthy", 12, "bold"), onvalue = 1, selectcolor = Colors.darknest_yellow)
        self.c_grid.place(x = 350, y = 470)

        buttons = [
        "Очист.", "sin(x)", "cos(x)", "tan(x)", "cot(x)", "sec(x)", "csc(x)",
        "7", "8", "9", "*", "/", "+", "-",
        "4", "5", "6", "log₂(x)", "lg(x)", "ln(x)", "abs(x)",
        "1", "2", "3", "=", "√", "x ²", "!",
        "0", "asin(x)", "acos(x)", "atan(x)", "acot(x)", "asec(x)", "acsc(x)",
        "π", "e", "%", "‰", "(", ")", ","
        ]

        for button in buttons:
            com = lambda cmd = button: self.logic(cmd)
            Button(text = button, bd = 0, highlightthickness = 2, highlightbackground = Colors.gray, font = ("Noteworthy", 16, "bold"), fg = Colors.black, command = com).place(x = ButtonsCoordinates.x, y = ButtonsCoordinates.y, width = 60, height = 40)
            ButtonsCoordinates.x += 70
            if ButtonsCoordinates.x > 450:
                ButtonsCoordinates.x = 10
                ButtonsCoordinates.y += 50

        self.ctrlc = Button(text = "Скопировать", width = 5, height = 1, highlightthickness = 0, bd = 2, highlightbackground = Colors.light_gray, font = ("Noteworthy", 12, "bold"), fg = Colors.black, command = self.clip).place(x = 405, y = 13)

    def clip(self):
        pyperclip.copy(self.eq)
        self.eq = "Результат скопирован!"
        self.upd()

    def logic(self, com):
        if com == "Очист.":
            self.eq = ""
    # =================================================================
        elif com == ",":
            self.eq += "."
    # =================================================================
        elif com == "%":
            self.eq = str((eval(self.eq))/10)
    # =================================================================
        elif com == "‰":
            self.eq = str((eval(self.eq))/100)
    # =================================================================
        elif com == "π":
            self.eq = str(round(math.pi, 6))
    # =================================================================
        elif com == "e":
            self.eq = str(round(math.e, 6))
    # =================================================================
        elif com == "sin(x)":
            self.eq = str(math.sin(eval(self.eq)))
    # =================================================================
        elif com == "cos(x)":
            self.eq = str(math.cos(eval(self.eq)))
    # =================================================================
        elif com == "tan(x)":
            try:
                self.eq = str(math.tan(eval(self.eq)))
            except:
                self.eq = "Ошибка!"
    # =================================================================
        elif com == "cot(x)":
            try:
                self.eq = str(1/math.tan(eval(self.eq)))
            except:
                self.eq = "Ошибка!"
    # =================================================================
        elif com == "sec(x)":
            try:
                self.eq = str(1/math.cos(eval(self.eq)))
            except:
                self.eq = "Ошибка!"
    # =================================================================
        elif com == "csc(x)":
            try:
                self.eq = str(1/math.sin(eval(self.eq)))
            except:
                self.eq = "Ошибка!"
    # =================================================================
        elif com == "!":
            try:
                self.eq = str(math.factorial(eval(self.eq)))
            except:
                self.eq = "Ошибка!"
    # =================================================================
        elif com == "x ²":
            try:
                self.eq = str(math.pow(2, eval(self.eq)))
            except:
                self.eq = "Ошибка!"
    # =================================================================
        elif com == "√":
            try:
                self.eq = str(math.sqrt(eval(self.eq)))
            except:
                self.eq = "Ошибка!"
    # =================================================================
        elif com == "log₂(x)":
            try:
                self.eq = str(math.log(2, eval(self.eq)))
            except:
                self.eq = "Ошибка!"
    # =================================================================
        elif com == "ln(x)":
            try:
                self.eq = str(math.log(math.e, eval(self.eq)))
            except:
                self.eq = "Ошибка!"
    # =================================================================
        elif com == "lg(x)":
            try:
                self.eq = str(math.log(10, eval(self.eq)))
            except:
                self.eq = "Ошибка!"
    # =================================================================
        elif com == "abs(x)":
            try:
                self.eq = str(abs(eval(self.eq)))
            except:
                self.eq = "Ошибка!"
    # =================================================================
        elif com == "asin(x)":
            try:
                self.eq = str(arcsin(eval(self.eq)))
                if self.eq == "nan":
                    self.eq = "Не существует"
            except:
                self.eq = "Ошибка!"
    # =================================================================
        elif com == "acos(x)":
            try:
                self.eq = str(arccos(eval(self.eq)))
                if self.eq == "nan":
                    self.eq = "Не существует"
            except:
                self.eq = "Ошибка!"
    # =================================================================
        elif com == "atan(x)":
            try:
                self.eq = str(arctan(eval(self.eq)))
                if self.eq == "nan":
                    self.eq = "Не существует"
            except:
                self.eq = "Ошибка!"
    # =================================================================
        elif com == "acot(x)":
            try:
                self.eq = str(arctan(1/(eval(self.eq))))
                if self.eq == "nan":
                    self.eq = "Не существует"
            except:
                self.eq = "Ошибка!"
    # =================================================================
        elif com == "asec(x)":
            try:
                self.eq = str(arccos(1/(eval(self.eq))))
                if self.eq == "nan":
                    self.eq = "Не существует"
            except:
                self.eq = "Ошибка!"
    # =================================================================
        elif com == "acsc(x)":
            try:
                self.eq = str(arcsin(1/(eval(self.eq))))
                if self.eq == "nan":
                    self.eq = "Не существует"
            except:
                self.eq = "Ошибка!"
    # =================================================================
        elif com ==  "=":
            try:
                self.eq = str(eval(self.eq))
            except:
                self.eq = "Ошибка!"
    # =================================================================
        else:
            if self.eq == "0":
                self.eq = ""
            if self.eq == "Ошибка!":
                self.eq = ""
            if self.eq == "Результат скопирован!":
                self.eq = ""
            if self.eq == "*":
                self.eq = ""
            if self.eq == "/":
                self.eq = ""
            if self.eq == "+":
                self.eq = ""
            self.eq += com
        self.upd()

    def upd(self):
        if len(self.eq) > 25:
            self.eq = "Ошибка!"
        if self.eq == "":
            self.eq = "0"
        self.label.configure(text = self.eq)

    def fx_logic(self, fx_com):
            fx_com = self.fx.get()
            fx_start = self.fx_start.get()
            fx_end = self.fx_end.get()
            fx_step = self.fx_step.get()
            fx_grid = self.fx_grid.get()

            if fx_grid == 1:
                fx_grid = 0.1
            else:
                fx_grid = 0

            if fx_start == '':
                fx_start = -1
            if fx_end == '':
                fx_end = 1
            if fx_step == '':
                fx_step = 0.1

            x = arange(float(fx_start), float(fx_end), float(fx_step))
            plot.figure(figsize = (6, 6), frameon = True,  clear = True, facecolor = Colors.yellow, edgecolor = Colors.dark_yellow)
            plot.plot(x, eval(fx_com));
            plot.xlabel(r'$x$')
            plot.ylabel(r'$y$')
            plot.title(rf'$f_1(x)=${str(fx_com)}')
            plot.plot(x, eval(fx_com), label = f'{fx_com}')
            plot.legend(loc = 'upper right', fontsize = 12)
            plot.grid(visible = False, color = Colors.black, linewidth = fx_grid)
            plot.savefig("graph.png")
            plot.show()

# =================================================================

if __name__ == "__main__":
    do = Tk()
    do["bg"] = Colors.bg
    do.geometry("500x700")
    do.title("Камень")
    do.resizable(False, False)
    application = Main(do)
    application.pack()
    do.mainloop()