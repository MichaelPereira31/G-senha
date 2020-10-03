from tkinter import *
import random 
import smtplib
import webbrowser

class Aplication: 
    def __init__(self,master=None):

        self.segundoContainer = Frame(master)
        self.segundoContainer['pady'] = 10
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer['padx'] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer['padx'] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer['padx'] = 20
        self.quintoContainer.pack()

        self.sextoContainer = Frame(master)
        self.sextoContainer['pady'] = 20
        self.sextoContainer.pack()

        self.setimoContainer = Frame(master)
        self.setimoContainer['pady'] = 0
        self.setimoContainer.pack()

        '''menubar = 
        self.config = Menu(self.primeiroContainer, tearoff=0)
        self.config.add_command(label="Configurações", command=turnbuttononoff)
        self.config.add_command(label="Configurações", command=turnbuttononoff)
        self.config.add_separator()
        self.config.pack(side=LEFT)'''

        self.titulo = Label(self.segundoContainer,text="Dados do Cliente")
        self.titulo.pack()


        self.empresaLabel = Label(self.terceiroContainer,text="Empresa: ",width=12)
        self.empresaLabel.pack(side=LEFT)

        self.empresa = Entry(self.terceiroContainer)
        self.empresa.pack(side=LEFT)

        self.emailLabel = Label(self.quartoContainer,text="E-mail Cliente: ")
        self.emailLabel.pack(side=LEFT)

        self.email = Entry(self.quartoContainer)
        self.email.pack(side=LEFT)

        self.gerarSenhaBtn = Button(self.quintoContainer,text="Gerar Senha")
        self.gerarSenhaBtn["command"] = self.password
        self.gerarSenhaBtn.pack(side=LEFT)

        self.gerarSenha = Entry(self.quintoContainer)
        self.gerarSenha.delete(0,END)
        self.gerarSenha.insert(0,str('********'))
        self.gerarSenha.pack(side=LEFT)

        self.enviar = Button(self.sextoContainer,text="Enviar")
        self.enviar['command'] = self.submit
        self.enviar.pack(side=LEFT)

        self.configBtn = Button(self.sextoContainer,text='Criar E-mail')
        self.configBtn['command'] = self.config
        self.configBtn.pack(side=LEFT)

        self.mensagem = Label(self.setimoContainer,text='')
        self.mensagem.pack()
    
    #Gerar senha
    def password(self):
        s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*'
        tamanho = 8
        senha = ''.join(random.sample(s,tamanho))
        self.gerarSenha.delete(0,END)
        self.gerarSenha.insert(0,senha)


    #Enviar e-mail
    def submit(self):

        email_from = "michaelpereira31082000@gmail.com"
        #senha_from = "******************"

        email_to = str(self.email.get())
        empresa = str(self.empresa.get())
        senha_to = str(self.gerarSenha.get())

        smtp = "smtp.gmail.com"

        server = smtplib.SMTP(smtp, 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(email_from, open('senha.txt').read().strip())

        #msg = 'Empresa: %s \nE-mail: %s \nSenha: %s'%(empresa,email_to,senha_to)
        emp = 'Empresa: '+empresa
        sen = 'Senha: '+senha_to
        ema = 'E-mail: '+email_to
        
        #msg = [emp,sen,ema]
        #print(msg)
        msg = senha_to
        if(server.sendmail(email_from, email_to, msg)):
            server.quit()
            self.email.delete(0,END)
            self.empresa.delete(0,END)
            self.gerarSenha.delete(0,END)

            self.mensagem['text'] = 'Senha Enviado com Sucesso!'
        else:  
            self.mensagem['text'] = 'Erro'

    def config(self):

        top = Toplevel()
        Conta(top)
        top.mainloop()
    
    def criarEmail(self):
        webbrowser.open('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')

class Conta: 
    def __init__(self,master=None):
        self.umContainer = Frame(master) 
        self.umContainer['pady'] = 10
        self.umContainer.pack()

        self.doisContainer = Frame(master)
        self.doisContainer['pady'] = 10
        self.doisContainer.pack()
        
        btnGoogle = Button(self.umContainer,text="Criar conta Google")
        btnGoogle['width'] = 20
        btnGoogle['command'] = self.contaGoogle
        btnGoogle.pack(side=LEFT)

        btnMicrosoft = Button(self.doisContainer,text="Criar conta Microsoft")
        btnMicrosoft['width'] = 20
        btnMicrosoft['command'] = self.contaMicrosoft
        btnMicrosoft.pack(side=LEFT)

        '''
    
        
        self.tresContainer = Frame(master)
        self.tresContainer['pady'] = 10
        self.tresContainer.pack()

        self.quatroContainer = Frame(master)
        self.quatroContainer['pady'] = 10
        self.quatroContainer.pack()

        self.cincoContainer = Frame(master)
        self.cincoContainer['pady'] = 10
        self.cincoContainer.pack()

        self.seisContainer = Frame(master)
        self.seisContainer['pady'] = 10
        self.seisContainer.pack()

        self.emailLabel = Label(self.umContainer,text='E-mail: ')
        self.emailLabel.pack(side=LEFT)

        self.email = Entry(self.umContainer)
        self.email.pack(side=LEFT)

        self.senhaLabel = Label(self.doisContainer,text='Senha: ')
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.doisContainer)
        self.senha.pack(side=LEFT)

        self.confimarSenhaLabel = Label(self.tresContainer,text="Confirmar Senha: ")
        self.confimarSenhaLabel.pack(side=LEFT)

        self.confirmarSenha = Entry(self.tresContainer)
        self.confirmarSenha.pack(side=LEFT)

        self.confirmar = Button(self.quatroContainer,text='Confirmar')
        self.confirmar.pack(side=LEFT)

        self.sair = Button(self.quatroContainer,text='Sair')
        self.sair.pack(side=LEFT)

        self.mensagem = Label(self.cincoContainer,text='')
        self.mensagem.pack()'''
    
    def contaGoogle(self):
        webbrowser.open('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')
        self.umContainer.destroy()
        

    def contaMicrosoft(self):
        webbrowser.open('https://signup.live.com/signup?mkt=pt-BR&uaid=61b4da86be2f4f6d869b277a6af6248a&lic=1')
root = Tk()
Aplication(root)
root.mainloop()
