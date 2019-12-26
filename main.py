import tkinter as tk 
import tkinter.ttk as ttk
import sqlite3
import function as f 

def main_gui():

    def voice_button():
        root.destroy()
        main_gui()

    def input_button():
        root.destroy()
        input_gui()

    def list_button():
        root.destroy()
        table_gui()

    def quit_button():
        root.destroy()

    def openweb_button():
        voice = f.rec()
        print(voice)
        print("voice rec OK")
        labelow=tk.Label(root,text=voice,font=("",12),height=2)
        labelow.pack(fill="x")
        sql = """
        select word,url from webpage where word = '{}'
        """.format(voice)
        for r in c.execute(sql):
            f.openweb(r[1])
        

    dbname = "database.db"
    c = sqlite3.connect(dbname)

    try:
        ddl = """
        create table webpage
        (
            word varchar(50) primary key,
            title varchar(50) not null,
            url varchar(100) not null,
        )"""
        c.execute(ddl)
        c.execute("insert into webpage values('YouTube','YouTube','https://www.youtube.com/')") ##初期
        c.execute("insert into webpage values('Amazon','Amazon | 本, ファッション, 家電から食品まで | アマゾン','https://www.amazon.co.jp/py')")
        c.execute("commit")
    except:
        pass

    root = tk.Tk()
    root.title("VOICE OPENS WEB")
    root.geometry("300x280")


    frame = tk.Frame(root,bd=2,relief="ridge") 
    frame.pack(fill="x")
    button1=tk.Button(frame,text="声",command=voice_button)
    button1.pack(side="left")
    button2=tk.Button(frame,text="登録",command=input_button)
    button2.pack(side="left")
    button3=tk.Button(frame,text="リスト",command=list_button)
    button3.pack(side="left")
    button4=tk.Button(frame,text="終了",command=quit_button)
    button4.pack(side="right")

    label1=tk.Label(root,text="声で入力してください",font=("",16),height=2)
    label1.pack(fill="x")


    button5=tk.Button(root,text="入力",font=("",16),width=10,bg="gray",command=openweb_button)
    button5.pack()

    root.mainloop()

def table_gui():

    def voice_button():
        root.destroy()
        main_gui()
    
    def input_button():
        root.destroy()
        input_gui()

    def quit_button():
        root.destroy()

    c=sqlite3.connect("database.db")

    root=tk.Tk()
    root.title("VOICE OPENS WEB")
    root.geometry("500x300")

    frame=tk.Frame(root,bd=2,relief="ridge")
    frame.pack(fill="x")
    button1=tk.Button(frame,text="声",command=voice_button)
    button1.pack(side="left")
    button2=tk.Button(frame,text="登録",command=input_button)
    button2.pack(side="left")
    button3=tk.Button(frame,text="リスト")
    button3.pack(side="left")
    button4=tk.Button(frame,text="終了",command=quit_button)
    button4.pack(side="right")

    label1=tk.Label(root,text="登録リスト",font=("",16),height=2)
    label1.pack(fill="x")

    tree = ttk.Treeview(root,padding=10)
    tree["columns"]=(1,2)
    tree["show"]="headings"
    tree.column(1,width=50)
    tree.column(2,width=100)
    tree.heading(1,text="ことば")
    tree.heading(2,text="ウェブページ")

    ttk.Style().configure("TreeView",font=("",12))
    ttk.Style().configure("Treeview.Heading",font=("",14,"bold"))

    sql = """
    select word,title 
    from webpage
    """

    i=0
    for r in c.execute(sql):
        r = (r[0],r[1])
        tree.insert("","end",tags=i,values=r)
        i+=1

    tree.pack(fill="x",padx=20,pady=20)
    
    root.mainloop()

def input_gui():

    def voice_button():
        root.destroy()
        main_gui()

    def input_button():
        root.destroy()
        input_gui() 

    def list_button():
        root.destroy()
        table_gui()

    def quit_button():
        root.destroy()

    def add_button():
        word=entry_i1.get()
        url=entry_i2.get()
        title=f.titleget(url)
        try:
            ddl="""
            insert into webpage values('{}','{}','{}')
            """.format(word,title,url)
            c.execute(ddl)
            c.execute("commit")
            print("登録できました")
        except:
            print("登録できませんでした")

    c=sqlite3.connect("database.db")

    root=tk.Tk()
    root.title("VOICE OPENS WEB")
    root.geometry("300x280")

    frame=tk.Frame(root,bd=2,relief="ridge")
    frame.pack(fill="x")
    button1=tk.Button(frame,text="声",command=voice_button)
    button1.pack(side="left")
    button2=tk.Button(frame,text="登録",command=input_button)
    button2.pack(side="left")
    button3=tk.Button(frame,text="リスト",command=list_button)
    button3.pack(side="left")
    button4=tk.Button(frame,text="終了",command=quit_button)
    button4.pack(side="right")  

    label1=tk.Label(root,text="登録画面",font=("",16),height=2)
    label1.pack(fill="x")

    frame_i1=tk.Frame(root,pady=10)
    frame_i1.pack()
    label_i1=tk.Label(frame_i1,font=("",14),text="ことば")
    label_i1.pack(side="left")
    entry_i1=tk.Entry(frame_i1,font=("",14),justify="center",width=15)
    entry_i1.pack(side="left")

    frame_i2=tk.Frame(root,pady=10)
    frame_i2.pack()
    label_i2=tk.Label(frame_i2,font=("",14),text="URL")
    label_i2.pack(side="left")
    entry_i2=tk.Entry(frame_i2,font=("",14),justify="center",width=25)
    entry_i2.pack(side="left")

    button5=tk.Button(root,text="登録",font=("",16),width=10,bg="gray",command=add_button)
    button5.pack()



main_gui()




