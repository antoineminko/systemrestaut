from tkinter import *
from PIL import ImageTk, Image
from  tkinter import messagebox
import math, random, os

class facture:
    def __init__(self,root):
        self.root = root
        self.root.title("facture")
        self.root.geometry("1920x1080")
        #bande nom du restaurant
        title = Label(self.root,text="RESTAURANT DE L 'INPTIC  ",bd=10,relief=RAISED,font=("Algerian",30),bg="cyan",fg="black")
        title.place(x=400,y=0)
        #logo
        #self.logo = ImageTk.PhotoImage(Image.open("C:/Users/DR_ANTOINE/Desktop/gestion restaurant/image/download.jpg"))
        #self.logopo = Label(image=self.logo)
        #self.logopo.place(x=20,y=0 , width=100, height=50)

        #"################variable
        self.petitdj1 = IntVar()
        self.petitdj2 = IntVar()
        self.petitdj3 = IntVar()
        self.petitdj4 = IntVar()
        self.petitdj5 = IntVar()
        self.petitdj6 = IntVar()
        self.petitdj7 = IntVar()
        self.petitdj8 = IntVar()
        self.petitdj9 = IntVar()

        ###variable
        self.dj1 = IntVar()
        self.dj2 = IntVar()
        self.dj3 = IntVar()
        self.dj4 = IntVar()
        self.dj5 = IntVar()
        self.dj6 = IntVar()
        self.dj7 = IntVar()
        self.dj8 = IntVar()
        self.dj9 = IntVar()
        self.dj10 = IntVar()
        self.dj11 = IntVar()
        #dinier
        self.diner1 = IntVar()
        self.diner2 = IntVar()
        self.diner3 = IntVar()
        self.diner4 = IntVar()
        self.diner5 = IntVar()
        self.diner6 = IntVar()
        self.diner7 = IntVar()
        self.diner8= IntVar()
        self.diner9= IntVar()

        #somme apayer
        self.prix_total_petiDje = StringVar()
        self.prix_total_Dje = StringVar()
        self.prix_total_din = StringVar()

        self.taxe_petiDje =StringVar()
        self.taxe_Dje = StringVar()
        self.taxe_din =StringVar()

        #datails
        self.nom_client =StringVar()
        self.tel_client = StringVar()

        self.number_facture = StringVar()
        x = random.randint(1000,9999)
        self.number_facture.set(str(x))

        self.recherche_facture = StringVar()


        #separation de la bande
        Frame1=LabelFrame(self.root,text="DETAILS DU CLIENT", font=("times new roman",15,"bold"),fg="white",bg="gray")
        Frame1.place(x=0,y=110,relwidth=1)
        dnom = Label(Frame1,text="Nom du client",bg="gray",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=5,pady=5)
        dnom = Entry(Frame1,width=15,font=("times new roman",15), textvariable=self.nom_client, bd=2,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=5)
        dphone = Label(Frame1, text="Numero du telephone", bg="gray", font=("times new roman", 14, "bold")).grid(row=0,column=2,padx=5, pady=5)
        dphone = Entry(Frame1, width=15, font=("times new roman", 15), textvariable=self.tel_client, bd=2, relief=SUNKEN).grid(row=0, column=3, padx=5,pady=5)
        dfacture = Label(Frame1, text=" Numero de facture ", bg="gray", font=("times new roman", 14, "bold")).grid(row=0,column=4,padx=5,pady=5)
        dfacture = Entry(Frame1, width=15, font=("times new roman", 15), textvariable=self.recherche_facture, bd=2, relief=SUNKEN).grid(row=0, column=5, padx=5,pady=5)
        bill_btn = Button(Frame1,text="Recherche",command=self.recherche ,width=25,bd=7,relief=GROOVE,font=("times new roman",12,"bold")).grid(row=0,column=6,padx=100,pady=1)
        Frame2 = LabelFrame(self.root,text="PETIT DEJEUNER",bd=5,relief=GROOVE,font=("times new roman",12,"bold"),fg="lightgreen",bg="gray")
        Frame2.place(x=5 ,y=200,width=300,height=410)
#petit dejeuner
        pladejeu  = Label(Frame2,text="Buscuit & yaourt",font=("times new roman",12,"bold"),fg="cyan",bg="gray").grid(row=0,column=0,padx=1)
        pladejeu = Entry(Frame2,font=("times new roman",10,"bold"), textvariable=self.petitdj1, bd=2,relief=SUNKEN,justify=RIGHT).grid(row=0,column=1,padx=0,pady=4 )
        pladejeu2 = Label(Frame2, text="gateau & yaourt", font=("times new roman", 12, "bold"), fg="cyan",bg="gray").grid(row=1, column=0, padx=1,pady=10)
        pladejeu2_txt = Entry(Frame2, font=("times new roman", 10, "bold"),textvariable=self.petitdj2, bd=2, relief=SUNKEN, justify=RIGHT).grid(row=1, column=1,padx=0,  pady=10)
        pladejeu3 = Label(Frame2, text="creppe & yaourt", font=("times new roman", 12, "bold"), fg="cyan",bg="gray").grid(row=2, column=0, padx=1, pady=10)
        pladejeu3_txt = Entry(Frame2, font=("times new roman", 10, "bold"),textvariable=self.petitdj3, bd=2, relief=SUNKEN, justify=RIGHT).grid( row=2, column=1, padx=0, pady=10)
        pladejeu4 = Label(Frame2, text=" pain au poulet ", font=("times new roman", 12, "bold"), fg="cyan",  bg="gray").grid(row=3, column=0, padx=1, pady=10)
        pladejeu4_txt = Entry(Frame2, font=("times new roman", 10, "bold"),textvariable=self.petitdj4, bd=2, relief=SUNKEN, justify=RIGHT).grid(row=3, column=1, padx=0, pady=10)
        pladejeu5 = Label(Frame2, text=" pain de viande ", font=("times new roman", 12, "bold"), fg="cyan", bg="gray").grid(row=4, column=0, padx=1, pady=10)
        pladejeu5_txt = Entry(Frame2, font=("times new roman", 10, "bold"), bd=2,textvariable=self.petitdj5, relief=SUNKEN, justify=RIGHT).grid(row=4, column=1, padx=0, pady=10)
        pladejeu6 = Label(Frame2, text="pain au jambom ", font=("times new roman", 12, "bold"), fg="cyan", bg="gray").grid(row=5, column=0, padx=1, pady=10)
        pladejeu6_txt = Entry(Frame2, font=("times new roman", 10, "bold"), bd=2, relief=SUNKEN,textvariable=self.petitdj6, justify=RIGHT).grid(row=5, column=1, padx=0, pady=10)
        pladejeu7 = Label(Frame2, text="pain au rognon ", font=("times new roman", 12, "bold"), fg="cyan", bg="gray").grid(row=6, column=0, padx=1, pady=10)
        pladejeu7_txt = Entry(Frame2, font=("times new roman", 10, "bold"),textvariable=self.petitdj7, bd=2, relief=SUNKEN, justify=RIGHT).grid(row=6, column=1, padx=0, pady=10)
        pladejeu6 = Label(Frame2, text="pain a la rico", font=("times new roman", 12, "bold"), fg="cyan", bg="gray").grid( row=7, column=0, padx=1, pady=10)
        pladejeu6_txt = Entry(Frame2, font=("times new roman", 10, "bold"),textvariable=self.petitdj8, bd=2, relief=SUNKEN, justify=RIGHT).grid(row=7, column=1, padx=0, pady=10)
#dejeuner

        Frame3=LabelFrame(self.root,text="DEJEUNER",bd=3,relief=GROOVE,font=("times new roman",12,"bold"),fg="lightgreen",bg="gray")
        Frame3.place(x=300,y=200,width=380,height=410)

        dejeu = Label(Frame3,text="spaguetti viande ",font=("times new roman",12,"bold"),fg="cyan",bg="gray").grid(row=0,column=0,padx=10,pady=10)
        dejeu_txt = Entry(Frame3,width=15,textvariable=self.dj1,  font=("times new roman",12,"bold"),bd=2,relief=SUNKEN,justify=RIGHT).grid(row=0,column=1,padx=10,pady=10)
        dejeu1 = Label(Frame3, text="riz viande", font=("times new roman", 12, "bold"), fg="cyan", bg="gray").grid(row=1,column=0, padx=10, pady=10)
        dejeu1_txt = Entry(Frame3, width=15,textvariable=self.dj2, font=("times new roman", 12, "bold"), bd=2, relief=SUNKEN, justify=RIGHT).grid(row=1, column=1, padx=10, pady=10)
        dejeu2 = Label(Frame3, text="poisson riz ", font=("times new roman", 12, "bold"), fg="cyan", bg="gray").grid(row=2, column=0, padx=10, pady=10)
        dejeu2_txt = Entry(Frame3, width=15,textvariable=self.dj3, font=("times new roman", 12, "bold"), bd=2, relief=SUNKEN, justify=RIGHT).grid(row=2, column=1, padx=10, pady=10)
        dejeu3 = Label(Frame3, text="poulet riz", font=("times new roman", 12, "bold"), fg="cyan", bg="gray").grid(row=0,column=0, padx=10, pady=10)
        dejeu3_txt = Entry(Frame3, width=15,textvariable=self.dj4, font=("times new roman", 12, "bold"), bd=2, relief=SUNKEN, justify=RIGHT).grid(row=0, column=1, padx=10, pady=10)
        dejeu4 = Label(Frame3, text="banane poulet ", font=("times new roman", 12, "bold"), fg="cyan", bg="gray").grid(row=3, column=0, padx=10,pady=10)
        dejeu4_txt = Entry(Frame3, width=15,textvariable=self.dj5, font=("times new roman", 12, "bold"), bd=2, relief=SUNKEN, justify=RIGHT).grid(row=3, column=1, padx=10, pady=10)
        dejeu5 = Label(Frame3, text=" sans feuille ", font=("times new roman", 12, "bold"), fg="cyan", bg="gray").grid(row=4,column=0,padx=10,pady=10)
        dejeu5_txt = Entry(Frame3, width=15,textvariable=self.dj6, font=("times new roman", 12, "bold"), bd=2, relief=SUNKEN, justify=RIGHT).grid(row=4, column=1, padx=10, pady=10)
        dejeu6 = Label(Frame3, text="poulet banane petit pois", font=("times new roman", 12, "bold"), fg="cyan", bg="gray").grid(row=5,column=0, padx=10,pady=10)
        dejeu6_txt = Entry(Frame3, width=15,textvariable=self.dj7, font=("times new roman", 12, "bold"), bd=2, relief=SUNKEN, justify=RIGHT).grid(row=5, column=1, padx=10, pady=10)
        dejeu7 = Label(Frame3,text="ails braisé & riz & banane ", font=("times new roman", 12, "bold"), fg="cyan", bg="gray").grid(row=6,column=0,padx=10, pady=10)
        dejeu7_txt = Entry(Frame3, width=15,textvariable=self.dj8, font=("times new roman", 12, "bold"), bd=2, relief=SUNKEN, justify=RIGHT).grid(row=6, column=1, padx=10, pady=10)
        dejeu8 = Label(Frame3,text="rognon/banane/manioc/riz", font=("times new roman", 12, "bold"), fg="cyan", bg="gray").grid(row=6, column=0, padx=10,pady=10)
        dejeu8_txt = Entry(Frame3,width=15,textvariable=self.dj9, font=("times new roman", 12, "bold"), bd=2, relief=SUNKEN,   justify=RIGHT).grid(row=6, column=1, padx=10, pady=10)

        Frame4=LabelFrame(self.root,text="DINER",bd=3,relief=GROOVE,font=("times new roman",12,"bold"),fg="lightgreen",bg="gray")
        Frame4.place(x=680,y=200,width=350,height=410)

        dejeu = Label(Frame4, text=" manioc obergine triple ", font=("times new roman",12, "bold"), fg="cyan",   bg="gray").grid(row=0, column=0, padx=10, pady=10)
        dejeu_txt = Entry(Frame4,width=15, textvariable=self.diner1, font=("times new roman",12,"bold"),bd=2, relief=SUNKEN, justify=RIGHT).grid(row=0, column=1, padx=10, pady=10)
        dejeu1 = Label(Frame4,text=" sanguiller & manioc ", font=("times new roman", 12, "bold"), fg="cyan", bg="gray").grid(row=1, column=0, padx=10, pady=10)
        dejeu1_txt = Entry(Frame4,width=15, textvariable=self.diner2,font=("times new roman",12,"bold"),bd=2,relief=SUNKEN,justify=RIGHT).grid(row=1, column=1, padx=10, pady=10)
        dejeu3 = Label(Frame4,text="poulet  riz & banane", font=("times new roman", 12, "bold"), fg="cyan", bg="gray").grid(row=0, column=0, padx=10, pady=10)
        dejeu3_txt = Entry(Frame4,width=15, textvariable=self.diner3, font=("times new roman", 12, "bold"), bd=2, relief=SUNKEN,justify=RIGHT).grid(row=0, column=1, padx=10, pady=10)
        dejeu4 = Label(Frame4,text=" feuille de manioc banane ", font=("times new roman", 12, "bold"), fg="cyan", bg="gray").grid(row=4, column=0, padx=10, pady=10)
        dejeu4_txt = Entry(Frame4, width=15, textvariable=self.diner4, font=("times new roman", 12, "bold"), bd=2, relief=SUNKEN, justify=RIGHT).grid(row=4, column=1, padx=10, pady=10)
        dejeu5 = Label(Frame4, text="bouillon de carpe & manioc ", font=("times new roman", 12, "bold"), fg="cyan", bg="gray").grid( row=5, column=0, padx=10, pady=10)
        dejeu5_txt = Entry(Frame4, width=15, textvariable=self.diner5, font=("times new roman", 12, "bold"), bd=2, relief=SUNKEN,  justify=RIGHT).grid(row=5, column=1, padx=10, pady=10)
        dejeu6 = Label(Frame4, text=" coup de dind & riz & manioc  ", font=("times new roman", 12, "bold"), fg="cyan",    bg="gray").grid(row=6, column=0, padx=10, pady=10)
        dejeu6_txt = Entry(Frame4, width=15, textvariable=self.diner6, font=("times new roman", 12, "bold"), bd=2, relief=SUNKEN,   justify=RIGHT).grid(row=6, column=1, padx=10, pady=10)
        dejeu7 = Label(Frame4, text="poisson braisé & banane riz ", font=("times new roman", 12, "bold"), fg="cyan",   bg="gray").grid(row=7, column=0, padx=10, pady=10)
        dejeu7_txt = Entry(Frame4, textvariable=self.diner7, width=15, font=("times new roman", 12, "bold"), bd=2, relief=SUNKEN,    justify=RIGHT).grid(row=7, column=1, padx=10, pady=10)
        dejeu8 = Label(Frame4, text="viande de beuf & manioc/banane", font=("times new roman", 12, "bold"), fg="cyan", bg="gray").grid(row=8, column=0, padx=10, pady=10)
        dejeu8_txt = Entry(Frame4, textvariable=self.diner8, width=15, font=("times new roman", 12, "bold"), bd=2, relief=SUNKEN,  justify=RIGHT).grid(row=8, column=1, padx=10, pady=10)





        Frame5=LabelFrame(self.root,bd=3,relief=GROOVE,font=("times new roman",12,"bold"),fg="lightgreen",bg="#9CE2B2")
        Frame5.place(x=1035,y=200,width=320,height=410)
        facture_lbl=Label(Frame5,text=("facturation") , font=("arial",12,"bold"),bd=7,relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(Frame5,orient=VERTICAL)
        self.text = Text(Frame5,yscrollcommand=scroll_y)
        scroll_y.config(command=self.text.yview)
        self.text.pack(fill=BOTH,expand=1)

        Frame6=LabelFrame(self.root,text="somme a payer ",bd=5,relief=GROOVE,font=("times new roman",13,"bold"),fg="lightgreen",bg="gray")
        Frame6.place(x=0,y=600,relwidth=1,height=280)

        prixPDJ = Label(Frame6,text=" Prix de petit dejeuner total",font=("times new roman",13,"bold"),fg="cyan",bg="gray").grid(row=1,column=0,padx=5,pady=5,sticky="w")
        prixPDJ_txt = Entry(Frame6,width=15 ,textvariable=self.prix_total_petiDje, font=("times new roman",13,"bold"),relief=SUNKEN).grid(row=1,column=1,padx=5,pady=5)

        prixPDJ2 = Label(Frame6, text=" Prix dut dejeuner total", font=("times new roman", 13, "bold"), fg="cyan",  bg="gray").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        prixPDJ2_txt = Entry(Frame6, width=15, textvariable=self.prix_total_Dje, font=("times new roman", 13, "bold"), relief=SUNKEN).grid(row=2, column=1,padx=5,  pady=5)

        prixPDJ3 = Label(Frame6, text=" Prix du dinerr total", font=("times new roman", 13, "bold"), fg="cyan", bg="gray").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        prixPDJ3_txt = Entry(Frame6, width=15,textvariable=self.prix_total_din, font=("times new roman", 13, "bold"), relief=SUNKEN).grid(row=3, column=1,   padx=5,  pady=5)

    #taxe

        prixPDJ = Label(Frame6, text="  taxe Prix de petit dejeuner total", font=("times new roman", 13, "bold"), fg="cyan",bg="gray").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        prixPDJ_txt = Entry(Frame6, textvariable=self.taxe_petiDje, width=15, font=("times new roman", 13, "bold"), relief=SUNKEN).grid(row=1, column=3,  padx=5, pady=5)

        prixPDJ1 = Label(Frame6, text=" taxe Prix du dejeuner total", font=("times new roman", 13, "bold"), fg="cyan", bg="gray").grid(row=2, column=2, padx=5, pady=5, sticky="w")
        prixPDJ1_txt = Entry(Frame6, width=15,textvariable=self.taxe_Dje,  font=("times new roman", 13, "bold"), relief=SUNKEN).grid(row=2, column=3,padx=5, pady=5)

        prixPDJ1 = Label(Frame6, text=" taxe Prix du diner total", font=("times new roman", 13, "bold"), fg="cyan", bg="gray").grid(row=3, column=2, padx=5, pady=5, sticky="w")
        prixPDJ1_txt = Entry(Frame6, width=15,textvariable=self.taxe_din, font=("times new roman", 13, "bold"), relief=SUNKEN).grid(row=3,column=3,  padx=5, pady=5)

        ####boutton
        Frame7 = LabelFrame(Frame6,bd=5,relief=GROOVE)
        Frame7.place(x=880,width=735,height=180)
        total = Button(Frame7,text="Total",width=19,bd=7, command=self.total, relief=GROOVE,font=("times new roman",13,"bold"),bg="#9CE2B2").grid(row=1,column=0,padx=1,pady=10)
        facture = Button(Frame7, text="Généré la facture", command=self.generer_facture, width=19, bd=7, relief=GROOVE, font=("times new roman", 13, "bold"),bg="#9CE2B2").grid(row=1, column=2, padx=1, pady=10)
        reini = Button(Frame7, text=" Renitialisé la facture ", width=19, bd=7, relief=GROOVE, font=("times new roman", 13, "bold"), bg="#9CE2B2").grid(row=2, column=0, padx=1, pady=1)
        quitter = Button(Frame7, text="Quitter", width=19, bd=7, relief=GROOVE, font=("times new roman", 13, "bold"),bg="#9CE2B2").grid(row=2, column=2, padx=1, pady=1)
        self.afficher_facture()
    def total(self):
        self.pet1 = self.petitdj1.get() * 500
        self.pet2 = self.petitdj2.get() * 600
        self.pet3 = self.petitdj3.get() * 800
        self.pet4 = self.petitdj4.get() * 700
        self.pet5 = self.petitdj5.get() * 500
        self.pet6 = self.petitdj6.get() * 400
        self.pet7 = self.petitdj7.get() * 500
        self.pet8 = self.petitdj8.get() * 600

        self.total_petitDje = int(self.pet1 + self.pet2 + self.pet3 + self.pet4 + self.pet5 + self.pet6 + self.pet7 + self.pet8)
        self.prix_total_petiDje.set(str(self.total_petitDje))
        self.taxe_ptDj = round((self.total_petitDje * 0.05), 2)
        self.taxe_petiDje.set(str(self.taxe_ptDj))


        # dej
        self.de1 = self.dj1.get() * 1500
        self.de2 = self.dj2.get() * 1300
        self.de3 = self.dj3.get() * 2000
        self.de4 = self.dj4.get() * 2500
        self.de5 = self.dj5.get() * 1000
        self.de6 = self.dj6.get() * 1200
        self.de7 = self.dj7.get() * 1200
        self.de8 = self.dj8.get() * 1300

        self.total_Dje = int(self.de1 + self.de2 + self.de3 + self.de4 + self.de5 + self.de6 + self.de7 + self.de8)
        self.prix_total_Dje.set(str(self.total_Dje))
        self.taxe_Dje = round((self.total_Dje * 0.05), 2)
        self.taxe_Dj.set(str(self.taxe_Dje))

        ###Dje
        self.di1 = self.diner1.get() * 1000
        self.di2 = self.diner2.get() * 1000
        self.di3 = self.diner3.get() * 1000
        self.di4 = self.diner4.get() * 1000
        self.di5 = self.diner5.get() * 1000
        self.di6 = self.diner6.get() * 1000
        self.di7 = self.diner7.get() * 1000
        self.di8 = self.diner8.get() * 1000

        self.total_Din = int(self.di1 + self.di2 + self + self.di3 + self.di4 + self.di5 + self.di6 + self + self.di7 + self.di8)
        self.prix_total_din.set(str(self.total_Din))
        self.taxe_di = round((self.total_Din * 0.05), 2)
        self.taxe_din.set(str(self.taxe_di))
        self.Total_facture = float(self.total_petitDje + self.total_din + self.total_Dje+self.taxe_ptDj+self.taxe_Dje+self.taxe_di)

    def afficher_facture(self):
        self.text.delete("1.0",END)
        self.text.insert(END,"****BIENVENU AU RESTAURANT INPTIC*****")
        self.text.insert(END,"\n Numero Facture : "+self.number_facture.get())
        self.text.insert(END,"\n Nom Client:"+self.nom_client.get())
        self.text.insert(END,"\n Telephone:"+self.tel_client.get())
        self.text.insert(END,"\n**************************************")
        self.text.insert(END,"\n Produits \t\t Quantité  \t\t Prix ")
        self.text.insert(END,"*************************************")

    def generer_facture(self):
         if self.nom_client.get()=="" or self.tel_client.get()=="":
             messagebox.showerror("Erreur","Vous n'avez pas saisi le nom ou le numero du telephone")
         elif self.prix_total_petiDje.get() == "0" and self.prix_total_Dje.get() =="0" and self.prix_total_Dje.get() =="0":
             messagebox.showerror("erreur","Séléctionez vos plats")
         else:
             self.afficher_facture()
             #petit dejuner
             if self.d11.get()!=0:
                 self.text.insert(END,f"\n Buscuit & yaourt \t\t {self.petitdj1.get()} \t\t {self.pet1}")

             if self.petitdj2.get()!=0:
                 self.text.insert(END,f"\n gateau & yaourt \t\t {self.petitdj2.get()} \t\t {self.pet2}")

             if self.petitdj3.get()!=0:
                 self.text.insert(END,f"\n creppe & yaourt \t\t {self.petitdj3.get()} \t\t {self.pet3}")

             if self.petitdj4.get()!=0:
                 self.text.insert(END,f"\n pain au poulet  \t\t {self.petitdj4.get()} \t\t {self.pet4}")

             if self.petitdj5.get()!=0:
                 self.text.insert(END,f"\n pain de viande\t\t {self.petitdj5.get()} \t\t {self.pet5}")

             if self.petitdj6.get() != 0:
                 self.text.insert(END, f"\n pain au jambom \t\t {self.petitdj6.get()} \t\t {self.pet6}")

             if self.petitdj7.get()!=0:
                 self.text.insert(END,f"\n pain au rognon \t\t {self.petitdj7.get()} \t\t {self.pet7}")

             if self.petitdj8.get()!=0:
                 self.text.insert(END,f"\n pain a la rico \t\t {self.petitdj8.get()} \t\t {self.pet8}")
          #dejeuner
             if self.dj1.get()!=0:
                 self.text.insert(END,f"\n spaguetti viande  \t\t {self.dj1.get()} \t\t {self.de1}")

             if self.dj2.get()!=0:
                 self.text.insert(END,f"\n riz viande \t\t {self.dj2.get()} \t\t {self.de2}")

             if self.dj3.get()!=0:
                 self.text.insert(END,f"\n poisson riz \t\t {self.dj3.get()} \t\t {self.de3}")

             if self.dj4.get()!=0:
                 self.text.insert(END,f"\n poulet riz  \t\t {self.dj4.get()} \t\t {self.de4}")

             if self.dj5.get()!=0:
                 self.text.insert(END,f"\n banane poulet\t\t {self.dj5.get()} \t\t {self.de5}")

             if self.dj6.get() != 0:
                 self.text.insert(END, f"\n sans feuille \t\t {self.dj6.get()} \t\t {self.de6}")

             if self.dj7.get()!=0:
                 self.text.insert(END,f"\n poulet banane petit pois \t\t {self.dj7.get()} \t\t {self.de7}")

             if self.dj8.get()!=0:
                 self.text.insert(END,f"\n ails braisé & riz & banane \t\t {self.dj8.get()} \t\t {self.de8}")
            #diner

             if self.di1.get() != 0:
                 self.text.insert(END, f"\n manioc obergine triple \t\t {self.diner1.get()} \t\t {self.di1}")

             if self.di2.get() != 0:
                 self.text.insert(END, f"\n sanguiller & manioc \t\t {self.diner2.get()} \t\t {self.di2}")

             if self.di3.get() != 0:
                 self.text.insert(END, f"\n poulet  riz & banane \t\t {self.diner3.get()} \t\t {self.di3}")

             if self.di4.get() != 0:
                 self.text.insert(END, f"\n feuille de manioc banane  \t\t {self.diner4.get()} \t\t {self.di4}")

             if self.di5.get() != 0:
                 self.text.insert(END, f"\n bouillon de carpe & manioc\t\t {self.diner5.get()} \t\t {self.di5}")

             if self.di6.get() != 0:
                 self.text.insert(END, f"\n coup de dind & riz & manioc  \t\t {self.diner6.get()} \t\t {self.di6}")

             if self.di7.get() != 0:
                 self.text.insert(END, f"\n poisson braisé & banane riz \t\t {self.diner7.get()} \t\t {self.di7}")

             if self.di8.get() != 0:
                 self.text.insert(END, f"\n viande de beuf & manioc/banane \t\t {self.diner8.get()} \t\t {self.di8}")

             self.text.insert(END,"\n *****************************************")
             self.text.insert(END, f"\n\n Somme Total \t\t\t {self.Total_facture}")
             self.text.insert(END, "\n *****************************************")

             self.sauvegarder()

    def sauvegarder(self):
        op=messagebox.askyesno("sauvegarder ","Voulez vous sauvegarder la facture?")
        if op > 0:
            self.donneFacture=self.textarea.get(1.0,END)
            f1=open("C:/Users/DR_ANTOINE/Desktop/gestion restaurant/facture"+self.number_facture.get()+".txt","w")
            f1.write(self.donneFacture)
            messagebox.showinfo("sauvegarder",f"La facture numéro {self.number_facture.get()} a été enregistré  avec succès ")
            f1.close()
        else:
            return

    def recherche(self):
        present ="non"
        for i in os.listdir("C:/Users/DR_ANTOINE/Desktop/gestion restaurant/facture"):
            if i.split(",")[0]==self.recherche_facture.get():
                 f1 = open("C:/Users/DR_ANTOINE/Desktop/gestion restaurant/facture"+i,"r")
                 self.text.delete("1.0",END)
                 for d in f1:
                     self.text.insert(END,d)
                     f1.close()
                     present = "oui"
            if present =="non"  :
                messagebox.showerror("erreur","Numero Facture invalide")















root =Tk()
obj = facture(root)
root.mainloop()