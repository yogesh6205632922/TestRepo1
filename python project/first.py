import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x600")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_display()
        self.create_buttons()

    def create_display(self):
        input_frame = tk.Frame(self.root)
        input_frame.pack(side=tk.TOP, pady=10)

        input_field = tk.Entry(input_frame, font=('arial', 20, 'bold'), textvariable=self.input_text, width=30, bd=5, relief=tk.RIDGE, justify='right')
        input_field.grid(row=0, column=0)
        input_field.pack()

    def btn_click(self, item):
        self.expression += str(item)
        self.input_text.set(self.expression)

    def btn_clear(self):
        self.expression = ""
        self.input_text.set("")

    def btn_equal(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except Exception:
            self.input_text.set("Error")
            self.expression = ""

    def scientific_function(self, func):
        try:
            value = float(self.expression)
            if func == 'sqrt':
                result = math.sqrt(value)
            elif func == 'log':
                result = math.log10(value)
            elif func == 'ln':
                result = math.log(value)
            elif func == 'sin':
                result = math.sin(math.radians(value))
            elif func == 'cos':
                result = math.cos(math.radians(value))
            elif func == 'tan':
                result = math.tan(math.radians(value))
            elif func == 'exp':
                result = math.exp(value)
            elif func == 'pi':
                result = math.pi
            elif func == 'e':
                result = math.e
            else:
                result = value
            self.input_text.set(str(result))
            self.expression = str(result)
        except Exception:
            self.input_text.set("Error")
            self.expression = ""

    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        # Button layout
        buttons = [
            ['7', '8', '9', '/', 'sqrt'],
            ['4', '5', '6', '*', 'log'],
            ['1', '2', '3', '-', 'ln'],
            ['0', '.', '=', '+', 'C'],
            ['sin', 'cos', 'tan', 'exp', 'pi']
        ]

        for row in buttons:
            row_frame = tk.Frame(button_frame)
            row_frame.pack(expand=True, fill='both')
            for btn in row:
                if btn == '=':
                    b = tk.Button(row_frame, text=btn, width=6, height=2, font=('arial', 14), command=self.btn_equal)
                elif btn == 'C':
                    b = tk.Button(row_frame, text=btn, width=6, height=2, font=('arial', 14), command=self.btn_clear)
                elif btn in ['sqrt', 'log', 'ln', 'sin', 'cos', 'tan', 'exp', 'pi', 'e']:
                    b = tk.Button(row_frame, text=btn, width=6, height=2, font=('arial', 14),
                                  command=lambda b=btn: self.scientific_function(b))
                else:
                    b = tk.Button(row_frame, text=btn, width=6, height=2, font=('arial', 14),
                                  command=lambda b=btn: self.btn_click(b))
                b.pack(side=tk.LEFT, expand=True, fill='both')


# Run the calculator
if __name__ == '__main__':
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()
