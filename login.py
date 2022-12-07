#bibliotecas
from customtkinter import *
from tkinter import messagebox,PhotoImage
import time

#Banco de dados
def bancoDados():
    user1 = l1.get()
    password2= l2.get()
    
    arquivo=open("bancodedados.txt","a")
    arquivo.write(f"User: {user1}\n")
    arquivo.write(f"Senha: {password2}\n")
    arquivo.close()
    
    arquivo=open('bancodedados.txt','r')
    for linha in arquivo:
        linha = linha.rstrip()
        print(linha)
    arquivo.close()

#Troca de Janela
def acessoPermitido():
    user = l1.get()
    password= l2.get()
    
    #Verificação de usuario admin
    if user == "admin" and password == "admin" or None:
        bancoDados()
        time.sleep(0.3)
        root.destroy()
        root2 = CTk()
        root2.geometry("280x320")
        root2.resizable(False,False)
        root2.iconbitmap("img/login.ico")
        root2.configure(background="#585757")
        root2.title("Login e Cadastro")
        lb = CTkLabel(text=f"Bem vindo {user}", text_color="#58A778",fg_color = "#585757", text_font="Arial 18 bold")
        f= CTkFrame(fg_color="#58A778", width=250, height=3)
        f2=CTkFrame(fg_color="#58A778", width=250)
        b= CTkButton(text="Logout", command = exit, fg_color="#A75858", text_color="white",text_font="Arial 12 bold", width=80, height=40, hover_color="#944040",bg_color="#58A778")
        im= CTkLabel(text="Muito obrigado por usar nosso Login.", text_font="Arial 8 bold",fg_color="#58A778", text_color="white")
        
        lb.pack(pady=0)
        f.pack(pady=0,ipady=1)
        im.place(x=35,y=60)
        f2.pack(pady=10,ipady=110)
        b.place(x=100,y=220)
        root2.mainloop()
        
    else:
        #Registro
        messagebox.showinfo("ERRO","Login ou senha inválidos, tente novamente ou crie uma conta!")
        bb= CTkButton(text="Registro", command=lambda:[abrir()],text_font="Arial 12 bold",fg_color="#E3A134",text_color="white",width=80, height=40, bg_color="#585757")
        bb.place(x=97,y=245)
        
        #Verificação de registro
        user = l1.get()
        def abrir():
            if l1.get() == "" and l2.get() == "":
                messagebox.showinfo("ERRO","CAMPOS EM BRANCO NÃO SÃO VALÍDOS!")
                
            elif l1.get() != "" and l2.get() != "":
                bancoDados()
                root.destroy()
                root2 = CTk()
                root2.geometry("280x320")
                root2.resizable(False,False)
                root2.iconbitmap("img/login.ico")
                root2.configure(background="#585757")
                root2.title("Login e Cadastro")
                lb = CTkLabel(text=f"Bem vindo {user}", text_color="#58A778",fg_color = "#585757", text_font="Arial 18 bold")
                f= CTkFrame(fg_color="#58A778", width=250, height=3)
                f2=CTkFrame(fg_color="#58A778", width=250)
                b= CTkButton(text="Logout", command = exit, fg_color="#A75858", text_color="white",text_font="Arial 12 bold", width=80, height=40, hover_color="#944040",bg_color="#58A778")
                im= CTkLabel(text="Muito obrigado por usar nosso Login.", text_font="Arial 8 bold",fg_color="#58A778", text_color="white")
                
                lb.pack(pady=0)
                f.pack(pady=0,ipady=1)
                im.place(x=35,y=60)
                f2.pack(pady=10,ipady=110)
                b.place(x=100,y=220)
                root2.mainloop()
             
#Tela
root = CTk()
root.geometry("280x320")
root.resizable(False,False)
root.iconbitmap("img/login.ico")
root.title("Login e Cadastro")
#imagens
imagem = PhotoImage(file="img/Tela.png")

#comandos
lb = CTkLabel(root,image=imagem)
bentrar= CTkButton(root,fg_color = "#58A778", command = acessoPermitido,text="Entrar", text_color="White", width=80, height=40,bg_color="#585757", text_font="Arial 12 bold", hover_color="#409461")
bsair = CTkButton(root,fg_color = "#A75858", command=exit, text="Sair", text_color="White", width=80, height=40,bg_color="#585757", text_font="Arial 12 bold", hover_color="#944040")
l1 = CTkEntry(root, width=245, text_font="arial 12 bold", bg_color="#585757", placeholder_text="admin")
l2 = CTkEntry(root, width=245, text_font="arial 12 bold",show="*", bg_color="#585757", placeholder_text="*****")

#places
lb.place(x=-54,y=0)
bentrar.place(x=180,y=245)
bsair.place(x=16,y=245)
l1.place(x=18,y=111,height=28)
l2.place(x=18,y=189,height=28)

root.mainloop() 
