from tkinter import *
from tkinter import ttk
import sqlite3
from PIL import ImageTk, Image

class gd:
    def __init__(self):
        ''''''    
    def get_data(self,event):
        current = account_table.item(account_table.focus()) #current is reference of the clicked row on table
        row = current["values"]
        try:
            self.r=row[0]
        except:
            pass
        
    def delete(self):
        try:
            a=self.r
            conn = sqlite3.connect('account_database.db')
            c = conn.cursor()
            c.execute('DELETE FROM account WHERE identity = ?' ,(a,)) #r, comma is there because of bug in python
            conn.commit()
            conn.close()
            show_all()
        except:
            pass
        
def admin_page():

    global ap_cancel
    def ap_cancel():
        admin_frame.destroy()
        
    def view_all():
        #table_frame.place(x=70,y=70,width=1150,height=600)
        ap_cancel()
        table_frame.pack(fill=BOTH, expand=1)
        show_all()

    def table_frame_close():
        table_frame.pack_forget()
        admin_page()
        
    try:
        ul_cancel()
    except:
        pass
    
    admin_frame = Frame(master, bg="springgreen4", bd=7, relief=GROOVE)
    admin_frame.place(x=540, y=160, width=200, height=400)
    

    ViewAll= Button(admin_frame, text='View All', width=10, height=2, command =view_all)
    ViewAll.place(x=60, y=60)
    
    cancel = Button(admin_frame, text='x', width=2, height=1,bg='red', fg='white', command =admin_frame.destroy)
    cancel.place(x=165, y=0)

    l_total = Label(table_frame, text='TOTAL AMOUNT\n'+str(total), width=15, height=5)
    l_total.place(x=1007, y=10)    

    b_delete = Button(table_frame, text='Delete', width=7, height=2, command =g.delete)
    b_delete.place(x=1033, y=150)

    b_close = Button(table_frame, text="Close", width=7, height=2, command=table_frame_close)
    b_close.place(x=1033,y=200)
    
''' ---------------------------------------------------------------------------'''

'''login frame work'''

def user_login():
    '''Login window work'''
       
    def login_submit():
        '''get data after pressing submit'''
        a=e_id.get()
        x=e_pass.get()
            
        if a=='' or x=='': #checking if any entry is empty or not
            l_error = Label(login_frame, text='Please enter correctly', font=('Calibri',10,'bold'), fg='red', bg='springgreen4') 
            l_error.place(x=100, y=115)
        else:
            account_security()               #calling account frame after clicking submit
            
            
    #////////////////////////////////////////////////////////////////////////////////////////////////////////#
            
    def account_security():
        
        i=e_id.get()
        p=e_pass.get()
        
        k=False
        conn = sqlite3.connect('account_database.db')
        c = conn.cursor()
        c.execute("SELECT bal FROM account WHERE identity = ?", (i,))
        
        for r in c:
            k=True
            
        if i=="smit" and p == "0000" or i=="atharv" and p=="0407":
            admin_page()# error recieved.
            
        elif k==False:
            l_error = Label(login_frame, text='No account matches this ID', font=('Calibri',10,'bold'), fg='red', bg='springgreen4') 
            l_error.place(x=100, y=115)
            
        elif k==True:
            c.execute("SELECT password FROM account WHERE identity = ?", (i,))
            for r in c:
                ''''''
                
            if p==r[0]:
                account(i)
                conn.commit()
                conn.close()
                ul_cancel()#closing fram after clicking submit
            else:
                l_error = Label(login_frame, text='Wrong Password', font=('Calibri',10,'bold'), fg='red', bg='springgreen4') 
                l_error.place(x=100, y=115)
                
            
        
        
        
    #////////////////////////////////////////////////////////////////////////////////////////////////////////#    
            
    global ul_cancel  #global because im accessing this inother functions#'''user register frame destroy'''
    '''userlogin frame destroy'''   
    def ul_cancel():
        login_frame.destroy()
          
    try:            #'''will raise exception if account frame is not opened initially'''
        ac_cancel() #'''account options frame destroy'''
    except:
        pass
     
    try:            #'''will raise exception if reg frame is not opened initially'''
        ur_cancel() #'''user register frame destroy '''
    except:
        pass

    try:            #'''will raise exception if reg frame is not opened initially'''
        ap_cancel() #'''user register frame destroy '''
    except:
        pass

    '''Two different try cases because if one frame is not opened previously and
    then closed it will raise an exception and the command to close some other frame
    written after that will not execute as it will directly jump to except
    skipping the next commands in try block'''

    #////////////////////////////////////////////////////////////////////////////////////////////////////////#
    
    login_frame = Frame(master, bg="springgreen4", bd=4, relief=RIDGE)
    login_frame.place(x=440, y=260, width=400, height=200)
    
    l_id = Label(login_frame, text='User ID', font=('Calibri',10,'bold'),fg='black', bg='white')
    l_id.place(x=16, y=10)   
    e_id = Entry(login_frame, font=("Calibri",15))
    e_id.place(x=100, y=10)

    l_pass = Label(login_frame, text='Password', font=('Calibri',10,'bold'),fg='black', bg='white')
    l_pass.place(x=10, y=80)
    password = StringVar() #Password variable
    e_pass = Entry(login_frame, textvariable=password, show='*', font=("Calibri",15))
    e_pass.place(x=100, y=80)
    

    b_cancel = Button(login_frame, text="Quit", command=ul_cancel)
    b_cancel.place(x=200,y=150)

    b_sub = Button(login_frame, text="Submit", command = login_submit)
    b_sub.place(x=100,y=150)
    

''' ---------------------------------------------------------------------------'''  
       
'''Register frame work'''    
def user_register(*login_frame):
    '''get data after pressing submit'''
    def register_submit():
    
        f = e_fname.get()
        l = e_lname.get()
        i = e_id.get()
        p = e_password.get()
        k=False
        
        conn = sqlite3.connect('account_database.db')
        c = conn.cursor()
        c.execute("SELECT bal FROM account WHERE identity = ?", (i,))
        for r in c:
            k=True
        
        
        if f=='' or l=='' or i=='' or p=='':   #checking if any entry is empty or not
            l_error = Label(register_frame, text='Please enter correctly', font=('Calibri',10,'bold'),fg='red', bg='springgreen4') 
            l_error.place(x=100, y=400)
            
        elif k:
            l_error = Label(register_frame, text='Username already taken', font=('Calibri',10,'bold'),fg='red', bg='springgreen4') 
            l_error.place(x=100, y=400)
            
        else:
            e_fname.delete(0,END)   #delte entrie after lcicking submit
            e_lname.delete(0,END)
            e_id.delete(0,END)
            e_password.delete(0,END)

            conn = sqlite3.connect('account_database.db')
            c = conn.cursor()
            c.execute('INSERT INTO account VALUES (?, ?, ?, ?, ?, ?)' , (i, f, l, p, '0', ''))
            conn.commit()
            conn.close()
            ur_cancel()#closing fram after clicking submit
            show_all()
            
    #////////////////////////////////////////////////////////////////////////////////////////////////////////#
            
    global ur_cancel            #global because im accessing this inother functions#'''user register frame destroy'''
    def ur_cancel():
        register_frame.destroy()#'''user register frame destroy'''
        
    try:            #'''will raise exception if login frame is not opened initially'''
        ul_cancel()         #'''userlogin frame destroy'''
    except:
        pass

    try:            #'''will raise exception if account frame is not opened initially'''
        ac_cancel()  #'''account options frame destroy'''       
    except:
        pass

    try:            #'''will raise exception if reg frame is not opened initially'''
        ap_cancel() #'''user register frame destroy '''
    except:
        pass

    '''Two different try cases because if one frame is not opened previously and
    then closed it will raise an exception and the command to close some other frame
    written after that will not execute as it will directly jump to except
    skipping the next commands in try block'''

    #////////////////////////////////////////////////////////////////////////////////////////////////////////#
    
    register_frame = Frame(master, bg="springgreen4", bd=4, relief=RIDGE)
    register_frame.place(x=440, y=90, width=400, height=600)
    
    l_fname = Label(register_frame, text='First Name', font=('Calibri',10,'bold'),fg='black', bg='white')
    l_fname.place(x=16, y=10)   
    e_fname = Entry(register_frame, font=("Calibri",15))
    e_fname.place(x=100, y=10)

    l_lname = Label(register_frame, text='Last name', font=('Calibri',10,'bold'),fg='black', bg='white')
    l_lname.place(x=16, y=80)   
    e_lname = Entry(register_frame, font=("Calibri",15))
    e_lname.place(x=100, y=80)

    l_id = Label(register_frame, text='ID', font=('Calibri',10,'bold'),fg='black', bg='white')
    l_id.place(x=16, y=150)   
    e_id = Entry(register_frame, font=("Calibri",15))
    e_id.place(x=100, y=150)

    l_password = Label(register_frame, text='Password', font=('Calibri',10,'bold'),fg='black', bg='white')
    l_password.place(x=16, y=220)   
    password = StringVar() #Password variable
    e_password = Entry(register_frame, textvariable=password, show='*', font=("Calibri",15))
    e_password.place(x=100, y=220)
    
    b_sub = Button(register_frame, text="Submit", command = register_submit)
    b_sub.place(x=100,y=430)

    b_cancel = Button(register_frame, text="Quit", command=ur_cancel)
    b_cancel.place(x=200,y=430)

''' ---------------------------------------------------------------------------'''

def user_log():
    '''intermediate call function declared to destroy previously oppened same frame
    i.e. closing previous login frame before oppening a new one'''
    try:
        ul_cancel()
    except:
        pass
       
    user_login()


''' ---------------------------------------------------------------------------'''

    
def user_reg():
    '''intermediate call function declared to destroy previously oppened same frame
    i.e. closing previous register frame before oppening a new one'''
    try:
        ur_cancel()
    except:
        pass
       
    user_register() 

''' ---------------------------------------------------------------------------'''

def account(i):

    global ac_cancel    #global because im accessing this inother functions
    def ac_cancel():
        '''account frame destroy function'''
        account_frame.destroy()
        
        
    #////////////////////////////////////////////////////////////////////////////////////////////////////////#
    
    def check_balance():
        conn = sqlite3.connect('account_database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM account WHERE identity = ?", (i,))
        for r in c:
            ''''''
            
        balance_frame = Frame(master, bg="springgreen4", bd=4, relief=RIDGE)
        balance_frame.place(x=423, y=100, width=400, height=500)

        l = Label(balance_frame,bg ='springgreen4', fg='white', text='', width=2, height=1)
        l.pack(side=TOP, fill=X)
        
        l_cross = Button(balance_frame,bg ='red', fg='white', text='X', width=2, height=1,relief=GROOVE, command =balance_frame.destroy)
        l_cross.place(x=368, y=0)

        l_bal = Label(balance_frame, text="Balance\n"+r[4], font=("Calibri",15,"bold"), bg="White", fg="black", bd=7, relief=GROOVE)
        l_bal.pack(fill=X)

        conn.commit()
        conn.close()

    def transactions():

        conn = sqlite3.connect('account_database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM account WHERE identity = ?", (i,))
        for r in c:
            ''''''
        
        trans_frame = Frame(master, bg="springgreen4", bd=4, relief=RIDGE)
        trans_frame.place(x=423, y=100, width=400, height=500)

        l = Label(trans_frame,bg ='white', fg='black', text='Transactions', width=2, height=1)
        l.pack(side=TOP, fill=X)

        l_cross = Button(trans_frame,bg ='red', fg='white', text='X', width=2, height=1,relief=GROOVE, command =trans_frame.destroy)
        l_cross.place(x=368, y=0)

        l_bal = Label(trans_frame, text=r[5], font=("Calibri",15,"bold"), bg="White", fg="black", bd=7, relief=GROOVE)
        l_bal.pack(fill=Y)

        conn.commit()
        conn.close()
        
        
    def deposit():

        def deposit_submit():
            global total
            
            y = int(e_amount.get())
            x = str(y+ int(r[4]))
            c.execute('UPDATE account SET bal = ? WHERE identity = ?' , (x,i))
            total = total + y
            d=r[5]
            d=d+'Deposit: '+str(y)+'\n'
            c.execute('UPDATE account SET trans = ? WHERE identity = ?' , (d,i))
            
            
            deposit_frame.destroy()
            conn.commit()
            conn.close()  
            
        conn = sqlite3.connect('account_database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM account WHERE identity = ?", (i,))
        for r in c:
            ''''''
        
        deposit_frame = Frame(master, bg="springgreen4", bd=4, relief=RIDGE)
        deposit_frame.place(x=483, y=200, width=300, height=300)

        l = Label(deposit_frame,bg ='springgreen4', fg='white', text='', width=2, height=1)
        l.pack(side=TOP, fill=X)

        b_cross = Button(deposit_frame, bg ='red', fg='white', text='X', width=2, height=1,relief=GROOVE, command =deposit_frame.destroy)
        b_cross.place(x=268, y=0)

        l_amount = Label(deposit_frame, text='Amount', font=('Calibri',15,'bold'),fg='black', bg='white')
        l_amount.pack(side=TOP, fill=X)   
        e_amount = Entry(deposit_frame, font=("Calibri",15))
        e_amount.pack(fill=X)

        l = Label(deposit_frame,bg ='springgreen4', fg='white', text='', width=2, height=1)
        l.pack(side=TOP, fill=X)

        b_submit = Button(deposit_frame, bg ='white', fg='black', text='SUBMIT', width=15, height=1,relief=GROOVE, command =deposit_submit)
        b_submit.place(x=95, y=150)
                  
    def withdraw(*total):

        def withdraw_submit():
            global total
            y = int(e_amount.get())

            if y>=int(r[4]):
                l = Label(withdraw_frame,bg ='springgreen4', fg='red', text='Insufficient Balance', width=20, height=1)
                l.place(x=10, y=110)
                
            else:    
                x = str(int(r[4])-y)
                c.execute('UPDATE account SET bal = ? WHERE identity = ?' , (x,i))

                d=r[5]
                d=d+'Withdraw: '+str(y)+'\n'
                c.execute('UPDATE account SET trans = ? WHERE identity = ?' , (d,i))
                total = total - y
                withdraw_frame.destroy()
                conn.commit()
                conn.close()  
            
        conn = sqlite3.connect('account_database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM account WHERE identity = ?", (i,))
        for r in c:
            ''''''
        
        withdraw_frame = Frame(master, bg="springgreen4", bd=4, relief=RIDGE)
        withdraw_frame.place(x=483, y=200, width=300, height=300)

        l = Label(withdraw_frame,bg ='springgreen4', fg='white', text='', width=2, height=1)
        l.pack(side=TOP, fill=X)

        b_cross = Button(withdraw_frame, bg ='red', fg='white', text='X', width=2, height=1,relief=GROOVE, command =withdraw_frame.destroy)
        b_cross.place(x=268, y=0)

        l_amount = Label(withdraw_frame, text='Amount', font=('Calibri',15,'bold'),fg='black', bg='white')
        l_amount.pack(side=TOP, fill=X)   
        e_amount = Entry(withdraw_frame, font=("Calibri",15))
        e_amount.pack(fill=X)

        l = Label(withdraw_frame,bg ='springgreen4', fg='white', text='', width=2, height=1)
        l.pack(side=TOP, fill=X)

        b_submit = Button(withdraw_frame, bg ='white', fg='black', text='SUBMIT', width=15, height=1,relief=GROOVE, command =withdraw_submit)
        b_submit.place(x=95, y=150)      
                      
    account_frame = Frame(master, bg="springgreen4", bd=4, relief=RIDGE)
    account_frame.place(x=540, y=160, width=200, height=400)

    b_checkbalance = Button(account_frame, text='BALANCE', width=10, height=2, command =check_balance)
    b_checkbalance.place(x=60, y=60)

    b_transactions = Button(account_frame, text='TRANSACTIONS', width=12, height=2, command =transactions)
    b_transactions.place(x=54, y=130)

    b_withdraw = Button(account_frame, text='WITHDRAW', width=10, height=2, command =withdraw)
    b_withdraw.place(x=60, y=200)

    b_deposit = Button(account_frame, text='DEPOSIT', width=10, height=2, command =deposit)
    b_deposit.place(x=60, y=270)

    b_cross = Button(account_frame,bg ='red', fg='white', text='X', width=2, height=1,relief=GROOVE, command =account_frame.destroy)
    b_cross.place(x=170, y=0)
    
    
            
''' ---------------------------------------------------------------------------'''
global show_all
def show_all():
    a=[]
    b=()
    conn = sqlite3.connect('account_database.db')
    c = conn.cursor()
    c.execute('SELECT identity, fna,lna, password, bal, trans FROM account')
    account_table.delete(*account_table.get_children())
    for r in c:
        account_table.insert("", "end", values=(r[0],r[1],r[2],'Hidden',r[4],r[5]))
    conn.commit()
    conn.close()

'''-----------------------------------------------------------------------------------'''    

   
'''-----------------------------------------------------------------------------------'''    
total=50000
master = Tk()
master.title('Bank')
master.geometry('1280x720')

i1 = ImageTk.PhotoImage(Image.open("mane.jpg"));
img = Label(master, image=i1)
img.image = i1
img.place(x=0, y=0)

title = Label(master, text="Bank Database", font=("Calibri",30,"bold"), bg="springgreen4", fg="white", bd=7, relief=GROOVE)
title.pack(side=TOP, fill=X)

b_login = Button(master, text='Login', width=8, height=2, command =user_log)
b_login.place(x=1000, y=70)

b_register = Button(master, text='Register', width=8, height=2, command =user_reg)
b_register.place(x=1100, y=70)


table_frame = Frame(master, bg="springgreen4", bd=7, relief=RIDGE)


hs = Scrollbar(table_frame, orient=HORIZONTAL)
hs.pack(side=BOTTOM, fill=X)
vs = Scrollbar(table_frame, orient=VERTICAL)
vs.pack(side=RIGHT, fill=Y)
account_table = ttk.Treeview(table_frame, columns=("i", "f", "l", "p", "b", "t"), xscrollcommand=hs.set, yscrollcommand=vs.set)
hs.config(command=account_table.xview)
vs.config(command=account_table.yview)
account_table.heading("i", text="userid")
account_table.heading("f", text="FirstName")
account_table.heading("l", text="LastName")
account_table.heading("p", text="Password")
account_table.heading("b", text="Balance")
account_table.heading("t", text="Transactions")
#account_table.heading("squestion", text="security question")

account_table["show"] = "headings"
#shows only those columns in which headings are present, does not show the default index column.

account_table.place(x=0,y=0,width=1000,height=575)
#account_table.pack(fill=BOTH, expand=1)

account_table.column("i", width=100)
account_table.column("f", width=150)
account_table.column("l", width=150)
account_table.column("p", width=150)
account_table.column("b", width=150)
account_table.column("t", width=200)
#account_table.column("squestion", width=200)

g=gd()
account_table.bind("<ButtonRelease-1>",g.get_data)
try:
    conn = sqlite3.connect('account_database.db') # connect with database or to connect an existing database
    c = conn.cursor()
    c.execute('CREATE TABLE account (identity CHAR(3), fna VARCHAR(15), lna VARCHAR(15), password VARCHAR(15), bal CHAR(10), trans VARCHAR(30))')
    c.execute('INSERT INTO account VALUES (?, ?, ?, ?, ?, ?)' , ('smit', 'admin', '', '', '0', ''))
    c.execute('INSERT INTO account VALUES (?, ?, ?, ?, ?, ?)' , ('atharva', 'admin', '', '', '0', ''))
    conn.commit() #commit is called to reflect changes in database if comment not called then it is as good as command not executing
    conn.close()
except sqlite3.OperationalError:
    pass


n='smit'
m='atharva'
flag=False
conn = sqlite3.connect('account_database.db')
c = conn.cursor()
c.execute("SELECT * FROM account WHERE identity = ?",(n,))
for r in c:
    flag=True
if flag==False:    
    c.execute('INSERT INTO account VALUES (?, ?, ?, ?, ?, ?)' , ('smit', 'admin', '', '', '0', ''))
conn.commit() #commit is called to reflect changes in database if comment not called then it is as good as command not executing
conn.close()

flag=False
conn = sqlite3.connect('account_database.db')
c = conn.cursor()
c.execute("SELECT * FROM account WHERE identity = ?",(m,))
for r in c:
    flag=True
if flag==False:    
    c.execute('INSERT INTO account VALUES (?, ?, ?, ?, ?, ?)' , ('atharva', 'admin', '', '', '0', ''))  
conn.commit() #commit is called to reflect changes in database if comment not called then it is as good as command not executing
conn.close()

conn = sqlite3.connect('account_database.db')
c = conn.cursor()
c.execute("SELECT bal FROM account")

for r in c:
    ''''''
    
for i in range(0,len(r)):
    total = total +int(r[i])
conn.commit() #commit is called to reflect changes in database if comment not called then it is as good as command not executing
conn.close()

user_login()

master.mainloop()


