from tkinter import *

class Calc:
    def __init__(self):

        self.window = Tk()
        self.window.title("Calc")
        self.window.resizable(0,0) #sua aplicação vai ter o tamanho dos widgtes que estiverem dentro dela e não pode ser escalonada manualmente.
         #podemos escolher uma cor personalizada no "pickcolor" no google e copie o HEX

        self.screen_numbers = Entry(self.window, font="arial 25 bold", bg="#fcb103", fg="#9c6794", width=15) #o entry permite que você digite em determinado campo e ele guarda para a gnt.
        self.screen_numbers.pack() #o pack pega o local que queremo colocar a função acima e coloca centralizado no topo na janela, a menos que passemos um local.

        self.frame = Frame(self.window) #bg = backgroud, fg = para mudar a cor da fonte,  bd= borda
        self.frame.pack()

        self.button_1 = Button(self.frame, bg="#67729c", bd=0, text="1", font="arial 20 bold", fg="white",
                               width=3, height=2, command= lambda: self.touch("1"))

        self.button_2 = Button(self.frame, bg="#67729c", bd=0, text="2", font="arial 20 bold", fg="white",
                               width=3, height=2, command= lambda: self.touch("2"))

        self.button_3 = Button(self.frame, bg="#67729c", bd=0, text="3", font="arial 20 bold", fg="white",
                               width=3, height=2, command= lambda: self.touch("3"))

        self.button_4 = Button(self.frame, bg="#67729c", bd=0, text="4", font="arial 20 bold", fg="white",
                               width=3, height=2, command= lambda: self.touch("4"))

        self.button_5 = Button(self.frame, bg="#67729c", bd=0, text="5", font="arial 20 bold", fg="white",
                               width=3, height=2, command= lambda: self.touch("5"))

        self.button_6 = Button(self.frame, bg="#67729c", bd=0, text="6", font="arial 20 bold", fg="white",
                               width=3, height=2, command= lambda: self.touch("6"))

        self.button_7 = Button(self.frame, bg="#67729c", bd=0, text="7", font="arial 20 bold", fg="white",
                               width=3, height=2, command= lambda: self.touch("7"))

        self.button_8 = Button(self.frame, bg="#67729c", bd=0, text="8", font="arial 20 bold", fg="white",
                               width=3, height=2, command= lambda: self.touch("8"))

        self.button_9 = Button(self.frame, bg="#67729c", bd=0, text="9", font="arial 20 bold", fg="white",
                               width=3, height=2, command= lambda: self.touch("9"))

        self.button_0 = Button(self.frame, bg="#67729c", bd=0, text="0", font="arial 20 bold", fg="white",
                               width=3, height=2, command= lambda: self.touch("0"))

        self.button_increase = Button(self.frame, bg="#67729c", bd=0, text="+", font="arial 20 bold", fg="white",
                               width=3, height=2, command= lambda: self.touch("+"))

        self.button_unincrease = Button(self.frame, bg="#67729c", bd=0, text="-", font="arial 20 bold", fg="white",
                                  width=3, height=2, command= lambda: self.touch("-"))

        self.button_division = Button(self.frame, bg="#67729c", bd=0, text="/", font="arial 20 bold", fg="white",
                                        width=3, height=2, command= lambda: self.touch("/"))

        self.button_multi = Button(self.frame, bg="#67729c", bd=0, text="*", font="arial 20 bold", fg="white",
                                        width=3, height=2, command= lambda: self.touch("*"))

        self.button_equal = Button(self.frame, bg="#67729c", bd=0, text="=", font="arial 20 bold", fg="white",
                                   width=3, height=2, command= self.total)

        self.button_clean = Button(self.frame, bg="#67729c", bd=0, text="C", font="arial 20 bold", fg="white",
                                   width=3, height=2, command=self.Clean)


        self.button_1.grid(row=0, column=0) #o grid consegue alinhar os objetos como se fosse uma grade perfeita
        self.button_2.grid(row=0, column=1)
        self.button_3.grid(row=0, column=2)
        self.button_division.grid(row=0, column=3)
        self.button_4.grid(row=1, column=0)
        self.button_5.grid(row=1, column=1)
        self.button_6.grid(row=1, column=2)
        self.button_multi.grid(row=1, column=3)
        self.button_7.grid(row=2, column=0)
        self.button_8.grid(row=2, column=1)
        self.button_9.grid(row=2, column=2)
        self.button_unincrease.grid(row=2, column=3)
        self.button_0.grid(row=3, column=0)
        self.button_increase.grid(row=3, column=1)
        self.button_clean.grid(row=3, column=2)
        self.button_equal.grid(row=3, column=3)



        self.window.mainloop()


    def touch(self, num):
        self.screen_numbers.insert(END, num)

    def Clean(self):
        self.screen_numbers.delete(0, END)

    def total(self):
        t = eval(self.screen_numbers.get()) # o eval retona para gnt uma expressão matemática
        self.screen_numbers.delete(0, END)
        self.screen_numbers.insert(0, str(t))

Calc()