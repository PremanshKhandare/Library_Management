from tkinter import*
from tkinter import ttk
import mysql.connector

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")
        
        # Variable
        
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.finalprice_var=StringVar()
        
        
        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="orange",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="yellow")
        frame.place(x=0,y=130,width=1530,height=400)
        
        # Data Frame Left
        
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="cyan",fg="green",bd=15,relief=RIDGE,font=("times new roman",15,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)
        
        lblMember=Label(DataFrameLeft,bg="cyan",text="Member Type",font=("times new roman",15,"bold"),textvariable=self.member_var,padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)
        
        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1)
        
        lblPRN_No=Label(DataFrameLeft,bg="cyan",text="PRN No",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.prn_var,width=29)
        txtPRN_NO.grid(row=1,column=1)
        
        lblTitle=Label(DataFrameLeft,bg="cyan",text="ID No",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.id_var,width=29)
        txtTitle.grid(row=2,column=1)
        
        lblFirstName=Label(DataFrameLeft,bg="cyan",text="FirstName",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)
        
        lblLastName=Label(DataFrameLeft,bg="cyan",text="LastName",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)
        
        lblAddress1=Label(DataFrameLeft,bg="cyan",text="Address1",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)
        
        lblAddress2=Label(DataFrameLeft,bg="cyan",text="Address2",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)
        
        lblPostCode=Label(DataFrameLeft,bg="cyan",text="PostCode",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.postcode_var,width=29)
        txtPostCode.grid(row=7,column=1)
        
        lblMobile=Label(DataFrameLeft,bg="cyan",text="Mobile",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMobile.grid(row=0,column=2,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=0,column=3)
        
        lblTitle=Label(DataFrameLeft,bg="cyan",text="Book Title",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblTitle.grid(row=1,column=2,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.booktitle_var,width=29)
        txtTitle.grid(row=1,column=3)
        
        lblAuthor=Label(DataFrameLeft,bg="cyan",text="Author Name",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.author_var,width=29)
        txtAuthor.grid(row=2,column=3)
        
        lblBookId=Label(DataFrameLeft,bg="cyan",text="BookId",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblBookId.grid(row=3,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.bookid_var,width=29)
        txtBookId.grid(row=3,column=3)
        
        lblDateBorrowed=Label(DataFrameLeft,bg="cyan",text="Date Borrowed",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=4,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDateBorrowed.grid(row=4,column=3)
        
        lblDateDue=Label(DataFrameLeft,bg="cyan",text="Date Due",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=5,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.datedue_var,width=29)
        txtDateDue.grid(row=5,column=3)
        
        lblLateReturnFine=Label(DataFrameLeft,bg="cyan",text="Late Return Fine",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.latereturnfine_var,width=29)
        txtLateReturnFine.grid(row=6,column=3)
        
        lblActualPrice=Label(DataFrameLeft,bg="cyan",text="Actual Price",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=7,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.finalprice_var,width=29)
        txtActualPrice.grid(row=7,column=3)
        
        # Data Frame Right
        
        DataFrameRight=LabelFrame(frame,text="Book Details",bg="cyan",fg="green",bd=15,relief=RIDGE,font=("times new roman",15,"bold"))
        DataFrameRight.place(x=910,y=5,width=575,height=350)
        
        self.txtBox=Text(DataFrameRight,font=("times new roman",15,"bold"),width=32,height=13,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)
        
        ListScrollbar=Scrollbar(DataFrameRight)
        ListScrollbar.grid(row=0,column=1,sticky="ns")
        
        listBooks=['Head First Book','Learn Python The Hard Way','Python Programming','Python CookBook','Rich Dad Poor Dad','Jungle Book','Machine Techno','Clueless','Wonderland','Zoolandia','Wonderland','Human Evolution','Star Wars','Kings Favour','Geronimo Stilton','Wakanda Forever','The Great Wall']
        
        listBox=Listbox(DataFrameRight,font=("times new roman",15,"bold"),width=20,height=13)
        listBox.grid(row=0,column=0,padx=4)
        ListScrollbar.config(command=listBox.yview)
        
        for item in listBooks:
            listBox.insert(END,item)
        
        # Button Frame
        
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="yellow")
        Framebutton.place(x=0,y=530,width=1530,height=70)
        
        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("times new roman",15,"bold"),width=19,bg="green",fg="white")
        btnAddData.grid(row=0,column=0)
        
        btnAddData=Button(Framebutton,text="Show Data",font=("times new roman",15,"bold"),width=19,bg="green",fg="white")
        btnAddData.grid(row=0,column=1)
        
        btnAddData=Button(Framebutton,text="Update",font=("times new roman",15,"bold"),width=19,bg="green",fg="white")
        btnAddData.grid(row=0,column=2)
        
        btnAddData=Button(Framebutton,text="Delete",font=("times new roman",15,"bold"),width=19,bg="green",fg="white")
        btnAddData.grid(row=0,column=3)
        
        btnAddData=Button(Framebutton,text="Reset",font=("times new roman",15,"bold"),width=19,bg="green",fg="white")
        btnAddData.grid(row=0,column=4)
        
        btnAddData=Button(Framebutton,text="Exit",font=("times new roman",15,"bold"),width=19,bg="green",fg="white")
        btnAddData.grid(row=0,column=5)
        
        # Information Frame
        
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="yellow")
        FrameDetails.place(x=0,y=600,width=1530,height=195)
        
        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="yellow")
        Table_frame.place(x=0,y=2,width=1460,height=190)
        
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        
        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","address1","address2","postid","mobile","bookid","booktitle","author","dateborrowed","datedue","latereturnfine","finalprice"),xscrollcommand=xscroll.set)
        
        xscroll.pack(side=BOTTOM)
        
        xscroll.config(command=self.library_table.xview)
        
        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="FirstName")
        self.library_table.heading("lastname",text="LastName")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="Date Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("finalprice",text="Final Price")
        
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        
        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("finalprice",width=100)
        
        self.fetch_data()
        
        
    def add_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Merry@9old",
                database="mydata"
            )
        
            my_cursor = conn.cursor()
        
            query = """
            INSERT INTO library 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
        
            values = (
                self.member_var.get(),
                self.prn_var.get(),
                self.id_var.get(),
                self.firstname_var.get(),
                self.lastname_var.get(),
                self.address1_var.get(),
                self.address2_var.get(),
                self.postcode_var.get(),
                self.mobile_var.get(),
                self.bookid_var.get(),
                self.booktitle_var.get(),
                self.author_var.get(),
                self.dateborrowed_var.get(),
                self.datedue_var.get(),
                self.latereturnfine_var.get(),
                self.finalprice_var.get()
            )
        
            my_cursor.execute(query, values)
        
            conn.commit()
            self.fetch_data()

        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if conn.is_connected():
                conn.close()  
        
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Merry@9old",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library") 
        rows=my_cursor.fetchall()   
        
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()        

if __name__ == "__main__":
     root=Tk()
     obj=LibraryManagementSystem(root)
     root.mainloop()   
          