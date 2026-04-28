import customtkinter as ctk

# ===== ESTILO GLOBAL (VIEW) =====
BG_PRINCIPAL = "#1e1e1e"
BG_SECUNDARIO = "#2a2a2a"
COR_TEXTO = "#00bfa6"
COR_BOTAO = "#5d5bd0"
HOVER_BOTAO = "#4c4ab8"
BG_LEITURA = "#3F3F3F"


class MainView(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")

        self.title("Leitor de Livros")
        self.geometry("1000x700")
        self.configure(fg_color=BG_PRINCIPAL)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.criar_topo()
        self.criar_conteudo()

    def criar_topo(self):
        self.topo = ctk.CTkFrame(self, fg_color=BG_PRINCIPAL)
        self.topo.grid(row=0, column=0, sticky="ew")

        self.entry_busca = ctk.CTkEntry(
            self.topo,
            placeholder_text="Buscar...",
            text_color=COR_TEXTO
        )
        self.entry_busca.pack(fill="x", padx=10, pady=10)

        self.entry_busca.bind("<Return>", self._on_busca)

    def criar_conteudo(self):
        self.conteudo = ctk.CTkFrame(self, fg_color=BG_SECUNDARIO)
        self.conteudo.grid(row=1, column=0, sticky="nsew")

    def trocar_tela(self, frame_class, *args):
        for w in self.conteudo.winfo_children():
            w.destroy()

        self.tela_atual = frame_class(self.conteudo, *args)
        self.tela_atual.pack(fill="both", expand=True)

    def _on_busca(self, event):
        if hasattr(self, "on_busca"):
            self.on_busca(self.entry_busca.get())


class TelaInicial(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=BG_SECUNDARIO)

        for i, livro in enumerate(controller.livros):
            btn = ctk.CTkButton(
                self,
                text=livro.nome,
                fg_color='#2a9d8f',
                # hover_color=HOVER_BOTAO,
                text_color="white",
                corner_radius=8,
                command=lambda l=livro: controller.abrir_livro(l)
            )
            btn.grid(row=i // 6, column=i % 6, padx=5, pady=5, sticky="ew")



class TelaLivro(ctk.CTkFrame):
    def __init__(self, master, controller, livro):
        super().__init__(master, fg_color=BG_SECUNDARIO)

        self.controller = controller
        self.livro = livro
        self.capitulo_atual = 1

        # ===== GRID PRINCIPAL =====
        self.grid_rowconfigure(1, weight=3)  # leitura
        self.grid_rowconfigure(2, weight=1)  # anotação
        self.grid_columnconfigure(0, weight=1)

        # TOPO (VOLTA + CAPÍTULO)
        topo = ctk.CTkFrame(self, fg_color=BG_SECUNDARIO)
        topo.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 5))
        topo.grid_columnconfigure(1, weight=1)

        self.botao_voltar = ctk.CTkButton(
            topo,
            text="← Voltar",
            width=100,
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            command=self.voltar
        )
        self.botao_voltar.grid(row=0, column=0, sticky="w")

        self.label_cap = ctk.CTkLabel(
            topo,
            text="",
            text_color=COR_TEXTO,
            font=("Arial", 14, "bold")
        )
        self.label_cap.grid(row=0, column=1, sticky="e")

        # ÁREA DE LEITURA
        frame_texto = ctk.CTkFrame(self, fg_color="#252525", corner_radius=10)
        frame_texto.grid(row=1, column=0, sticky="nsew", padx=10, pady=(5, 5))
        frame_texto.grid_rowconfigure(1, weight=1)
        frame_texto.grid_columnconfigure(0, weight=1)

        label_texto = ctk.CTkLabel(
            frame_texto,
            text="Texto do Livro",
            text_color=COR_TEXTO,
            font=("Arial", 14, "bold")
        )
        label_texto.grid(row=0, column=0, sticky="w", padx=10, pady=(5, 0))

        self.texto = ctk.CTkTextbox(
            frame_texto,
            fg_color=BG_LEITURA,
            text_color=COR_TEXTO,
            font=("Arial", 16)
        )
        self.texto.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.texto.configure(
            spacing1=2,
            spacing2=6,
            spacing3=2)

        # ÁREA DE ANOTAÇÕES
        frame_anotacoes = ctk.CTkFrame(self, fg_color="#232323", corner_radius=10)
        frame_anotacoes.grid(row=2, column=0, sticky="nsew", padx=10, pady=(5, 10))
        frame_anotacoes.grid_rowconfigure(1, weight=1)
        frame_anotacoes.grid_columnconfigure(0, weight=1)

        label_anot = ctk.CTkLabel(
            frame_anotacoes,
            text="Anotações",
            text_color=COR_TEXTO,
            font=("Arial", 14, "bold")
        )
        label_anot.grid(row=0, column=0, sticky="w", padx=10, pady=(5, 0))

        self.anotacoes = ctk.CTkTextbox(
            frame_anotacoes,
            fg_color=BG_SECUNDARIO,
            text_color=COR_TEXTO
        )
        self.anotacoes.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.anotacoes.insert("0.0", livro.anotacoes)

        # NAVEGAÇÃO CAPÍTULOS
        nav = ctk.CTkFrame(frame_anotacoes, fg_color="transparent")
        nav.grid(row=2, column=0, pady=(0, 10))

        ctk.CTkButton(
            nav,
            text="Anterior",
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            command=self.prev_cap
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            nav,
            text="Próximo",
            fg_color=COR_BOTAO,
            hover_color=HOVER_BOTAO,
            command=self.next_cap
        ).pack(side="right", padx=10)

        # INICIALIZA
        self.mostrar_capitulo()

    # EXIBIÇÃO
    def mostrar_capitulo(self):
        cap = self.livro.get_capitulo(self.capitulo_atual)
        if not cap:
            return

        texto = ""
        for v in cap.versiculos:
            texto += f"{v.numero} {v.texto}\n"

        self.texto.configure(state="normal")
        self.texto.delete("0.0", "end")
        self.texto.insert("0.0", texto)
        self.texto.configure(state="disabled")

        self.label_cap.configure(text=f"Capítulo {self.capitulo_atual}")

    #  NAVEGAÇÃO
    def next_cap(self):
        if self.capitulo_atual < len(self.livro.capitulos):
            self.capitulo_atual += 1
            self.mostrar_capitulo()

    def prev_cap(self):
        if self.capitulo_atual > 1:
            self.capitulo_atual -= 1
            self.mostrar_capitulo()

    # SALVAR
    def salvar(self):
        texto = self.anotacoes.get("0.0", "end").strip()
        self.controller.salvar_anotacoes(self.livro, texto)

    #  DESTAQUE
    def destacar(self, termo):
        self.texto.configure(state="normal")

        self.texto.tag_remove("highlight", "0.0", "end")

        start = "0.0"
        while True:
            pos = self.texto.search(termo, start, stopindex="end", nocase=True)
            if not pos:
                break

            end = f"{pos}+{len(termo)}c"
            self.texto.tag_add("highlight", pos, end)
            start = end

        self.texto.tag_config("highlight", background="yellow")

        self.texto.configure(state="disabled")

    # VOLTAR
    def voltar(self):
        self.controller.voltar_inicio()