from tkinter import*
from PyDictionary import PyDictionary
p=PyDictionary()

class Dictionary:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("Dictionary |developed by MS coproration")
        self.root.resizable(False,False)

        title=Label(self.root,text="                         Dictionary",font=("times new roman",40),bg='#053746',fg='white',anchor='w').place(x=0,y=0,relwidth=1)
        word=Label(self.root,text="Enter the word ",font=("goudy old style",20),bg='#053746',fg='white').place(x=200,y=100,width=200,height=50)
        self.word_text=Entry(self.root,font=("timesnew roman",15,'bold'),bg='lightyellow')
        self.word_text.place(x=500,y=100,width=200,height=50)
        self.Meaning_text=Label(self.root,text="Meaning:",font=("goudy old style",10),bg='#053746',fg='white')
        self.Meaning_text.place(x=0,y=175,relwidth=1,height=70)
        self.Antonym_text=Label(self.root,text="Antonym:",font=("goudy old style",10),bg='#053746',fg='white')
        self.Antonym_text.place(x=0,y=225,relwidth=1,height=70)
        self.Synonym_text=Label(self.root,text="Synonym:",font=("goudy old style",10),bg='#053746',fg='white')
        self.Synonym_text.place(x=0,y=275,relwidth=1,height=70)
        btn_Submit=Button(self.root,text="Submit",command=self.dict,font=("times new roman",15,'bold'),bg='blue',fg='white').place(x=400,y=350,width=200,height=50)
    def dict(self):
       
       self.Meaning_text.config(text=p.meaning(self.word_text.get())['Noun'][0])
       self.Antonym_text.config(text=p.antonym(self.word_text.get()))
       self.Synonym_text.config(text=p.synonym(self.word_text.get()))
       
        
     
root=Tk()
obj=Dictionary(root)
root.mainloop()
