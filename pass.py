import tkinter as tk
from tkinter import messagebox
from random import choice,shuffle

class passGenerator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("550x400")
        self.title("PASSWORD GENERATOR")
        self.config(padx=50,pady=20,bg="yellow")
        self.create_widgets()
        
    def create_widgets(self):
        self.head_label=tk.Label(text="PASSWORD GENERATOR",pady=40,font=("bold"),bg="yellow")
        self.head_label.grid(row=0,column=1)
        
        self.pass_label=tk.Label(text="Pass Length:",bg="yellow",font=("slant",10))
        self.pass_label.grid(row=1,column=0,pady=20)
        
        self.pass_length=tk.Entry(self,width=40)
        self.pass_length.grid(row=1,column=1,pady=20)
        
        self.pass_gen_label=tk.Label(text="Generated Password:",bg="yellow",font=("slant",10))
        self.pass_gen_label.grid(row=2,column=0,pady=20)
        
        self.pass_gen=tk.Entry(self,width=40)
        self.pass_gen.grid(row=2,column=1,pady=20)
        
        self.gen_button=tk.Button(self,text="generate pass",command=self.pass_generate,fg="white",bg="black")
        self.gen_button.grid(row=3,column=1,pady=20,padx=0)
        
    def pass_generate(self):
        #checking whether the length is entered
        l=self.pass_length.get()
        if len(l)==0:
            messagebox.showwarning(title="oops",message="enter the length")
        else:
            l=int(l)
            
            #checking already present password for deletion
            
            gen_entry=self.pass_gen.get()
            if len(gen_entry)>0:
                self.pass_gen.delete(0,tk.END)
            
            
            #checking whether the password length is lesser
            
            if l<8:
                messagebox.showwarning(title="oops",message="length greater than 7")
            elif l>30:
                messagebox.showwarning(title="oops",message="length lesser than 31")
            else:
                letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                numbers=['0','1','2','3','4','5','6','7','8','9']
                symbols=['!', '#', '$', '%', '&', '(', ')', '*', '+','/',';','[',']','|','?']
                
                if l==8:
                    pass_letters=[choice(letters) for _ in range(5)]
                    pass_numbers=[choice(numbers) for _ in range(2)]
                    pass_symbols=[choice(symbols) for _ in range(1)]
                elif l>8 and l<=15:
                    num=3
                    sym=2
                    alp=l-num-sym
                    pass_letters=[choice(letters) for _ in range(alp)]
                    pass_numbers=[choice(numbers) for _ in range(num)]
                    pass_symbols=[choice(symbols) for _ in range(sym)]
                else:
                    num=4
                    sym=4
                    alp=l-num-sym
                    pass_letters=[choice(letters) for _ in range(alp)]
                    pass_numbers=[choice(numbers) for _ in range(num)]
                    pass_symbols=[choice(symbols) for _ in range(sym)]
                    
                pw= pass_letters + pass_numbers + pass_symbols
                shuffle(pw)
                
                password="".join(pw)
                self.pass_gen.insert(0,password)
                    
app=passGenerator()
app.mainloop()

            