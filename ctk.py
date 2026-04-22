import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

def centralizar_janela(app, largura, altura):
    tela_larg = app.winfo_screenwidth()
    tela_alt  = app.winfo_screenheight()
    x = (tela_larg // 2) - (largura // 2)
    y = (tela_alt  // 2) - (altura  // 2)
    app.geometry(f'{largura}x{altura}+{x}+{y}')

label = ctk.CTkLabel(
    app,
    text='Olá, mundo!',
    font=('Arial', 18, 'bold'),   # (família, tamanho, estilo)
    text_color='blue',           # Cor do texto
    fg_color='transparent',       # Cor de fundo ('transparent' = sem fundo)
    bg_color='white',
    anchor='center',                   # Alinhamento: 'w','e','n','s','center'
    justify='left',               # Alinhamento multi-linha
    corner_radius=8,              # Arredondamento (com fg_color)
)

textbox = ctk.CTkTextbox(
    app,
    width=400,
    height=200,
    font=('Arial', 13),
    text_color='teal', 
    wrap='word',          # Quebra de linha: 'word', 'char', 'none'
    state='normal',       # 'normal' ou 'disabled'
    activate_scrollbars=True,
)

def altera_texto(app, texto):
    app.configure(state="normal")
    app.delete("0.0", "end")
    app.insert("0.0", texto)
    app.configure(state="disabled")


label.pack(fill = 'y', anchor = 'center')
textbox.insert('end', 'Linha 1\nLinha 2\n')
textbox.pack(pady=10)



centralizar_janela(app, 800, 600)
app.mainloop()