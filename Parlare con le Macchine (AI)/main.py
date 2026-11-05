import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from PIL import Image, ImageTk, ImageDraw, ImageOps
from io import BytesIO
import hashlib
import hmac
import os
import re
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


DB_CONFIG = {
    "host": "192.168.6.123",
    "port": 3306,
    "database": "ales_commerce",
    "user": "ales_user",
    "password": "12345678"
}

TABLE_NAME = "articoli"
CATEGORIES_TABLE = "categorie"

# Se il collegamento in `articoli` ha un nome particolare, aggiungilo qui.
ARTICLE_CATEGORY_FIELDS = (
    "id_categoria", "categoria_id", "id_categorie", "categorie_id",
    "categoria", "categorie", "id_cat", "cat_id", "category_id",
    "fk_categoria", "categoria_fk", "categoria_ids"
)
ARTICLE_ID_FIELDS = (
    "id_articolo", "articolo_id", "id_articoli", "articoli_id",
    "id_prodotto", "prodotto_id", "product_id", "id_product"
)
# Eventuali tabelle ponte articolo/categoria; lette solo se esistono.
CATEGORY_LINK_TABLES = (
    "articoli_categorie", "articoli_categoria", "articolo_categoria",
    "articolo_categorie", "categorie_articoli", "categoria_articoli",
    "categorie_articolo", "categoria_articolo", "art_cat"
)
USERS_TABLE = "utenti"  # id AUTO_INCREMENT, email, password VARCHAR(255), in_enabled
PASSWORD_ITERATIONS = 260_000


def crea_hash_password(password):
    """Hash PBKDF2 con sale casuale: la password non viene salvata in chiaro."""
    salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, PASSWORD_ITERATIONS
    )
    return f"pbkdf2_sha256${PASSWORD_ITERATIONS}${salt.hex()}${digest.hex()}"


def verifica_hash_password(password, encoded):
    """Confronto costante nel tempo, senza memorizzare la password."""
    try:
        algoritmo, n, salt_hex, digest_hex = str(encoded).split("$")
        if algoritmo != "pbkdf2_sha256":
            return False
        iterazioni = int(n)
        if not 100_000 <= iterazioni <= 1_000_000:
            return False
        salt = bytes.fromhex(salt_hex)
        expected = bytes.fromhex(digest_hex)
        if len(salt) != 16 or len(expected) != 32:
            return False
        actual = hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), salt, iterazioni
        )
        return hmac.compare_digest(actual, expected)
    except (ValueError, TypeError):
        return False


def email_valida(email):
    return bool(re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email)) and len(email) <= 254

def verifica_password_database(password_inserita, password_salvata):
    """Verifica sia hash PBKDF2 sia vecchie password memorizzate in chiaro.

    I nuovi account salvano SEMPRE un hash nel campo `password`.
    La compatibilità con i record esistenti non richiede modifiche ai dati.
    """
    if password_salvata is None:
        return False
    if isinstance(password_salvata, bytes):
        password_salvata = password_salvata.decode("utf-8", errors="replace")
    password_salvata = str(password_salvata)
    if password_salvata.startswith("pbkdf2_sha256$"):
        return verifica_hash_password(password_inserita, password_salvata)
    # Compatibilità con gli account già presenti nel database.
    return hmac.compare_digest(password_inserita, password_salvata)



def importo_decimale(valore):
    """Legge un importo MySQL DECIMAL senza trasformarlo in float."""
    return Decimal(str(valore if valore is not None else 0))


def formatta_prezzo(valore):
    """Formato italiano: 1234567.89 -> 1.234.567,89 €."""
    try:
        numero = importo_decimale(valore).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        # Python usa 1,234.56; scambiamo separatore migliaia e decimali.
        return f"{numero:,.2f}".replace(",", "~").replace(".", ",").replace("~", ".") + " €"
    except (InvalidOperation, ValueError, TypeError):
        return str(valore) if valore is not None else ""


def leggi_prezzo_filtro(testo):
    """Accetta 1234,56, 1.234,56 e 1234.56 nei campi di filtro."""
    testo = testo.strip().replace("€", "").replace(" ", "")
    if not testo:
        return None
    if "," in testo and "." in testo:
        if testo.rfind(",") > testo.rfind("."):
            testo = testo.replace(".", "").replace(",", ".")
        else:
            testo = testo.replace(",", "")
    elif "," in testo:
        testo = testo.replace(",", ".")
    elif re.fullmatch(r"\d{1,3}(?:\.\d{3})+", testo):
        testo = testo.replace(".", "")
    valore = Decimal(testo)
    if not valore.is_finite() or valore < 0:
        raise ValueError("Prezzo non valido")
    return valore


BLU = "#131921"
BLU_CHIARO = "#232f3e"
GIALLO = "#febd69"
SFONDO = "#ffffff"
TESTO = "#0f1111"
GRIGIO = "#dddddd"


class AmazonButton(tk.Canvas):
    """Pulsante stile Amazon: altezza 30px, carattere ~14px,
    testo centrato e bordi a pillola. Non richiede librerie esterne.
    """

    STYLES = {
        "primary": ("#ffd814", "#f7ca00", "#fcd200", "#0f1111"),
        "secondary": ("#ffffff", "#f7fafa", "#888c8c", "#0f1111"),
        "subtle": ("#f0f2f2", "#e3e6e6", "#adb1b8", "#0f1111"),
        "danger": ("#b12704", "#951f03", "#891c03", "#ffffff"),
    }

    def __init__(self, master, text, command=None, variant="secondary",
                 width=282, height=30, state="normal"):
        try:
            parent_bg = master.cget("bg")
        except tk.TclError:
            parent_bg = "#ffffff"
        super().__init__(
            master, width=width, height=height, bg=parent_bg,
            highlightthickness=0, bd=0, relief="flat",
            cursor="hand2" if state == "normal" else "arrow",
            takefocus=True
        )
        self._text = text
        self._command = command
        self._variant = variant
        self._state = state
        self._hover = False
        self.bind("<Configure>", self._draw)
        self.bind("<Enter>", self._enter)
        self.bind("<Leave>", self._leave)
        self.bind("<ButtonRelease-1>", self._activate)
        self.bind("<Return>", self._activate)
        self.bind("<space>", self._activate)
        self._draw()

    def _enter(self, event):
        self._hover = True
        self._draw()

    def _leave(self, event):
        self._hover = False
        self._draw()

    def _activate(self, event):
        if self._state == "normal" and self._command:
            if getattr(event, "keysym", None) in ("Return", "space") or (
                0 <= event.x < self.winfo_width() and
                0 <= event.y < self.winfo_height()
            ):
                self._command()

    def _pill(self, x0, y0, x1, y1, color):
        r = min((y1 - y0) / 2, (x1 - x0) / 2)
        if r <= 0:
            return
        self.create_oval(x0, y0, x0 + 2*r, y1, fill=color, outline=color)
        self.create_oval(x1 - 2*r, y0, x1, y1, fill=color, outline=color)
        if x1-x0 > 2*r:
            self.create_rectangle(x0+r, y0, x1-r, y1, fill=color, outline=color)

    def _draw(self, event=None):
        self.delete("all")
        w = max(10, self.winfo_width())
        h = max(10, self.winfo_height())
        base, hover, border, fg = self.STYLES[self._variant]
        if self._state != "normal":
            base, hover, border, fg = "#f0f2f2", "#f0f2f2", "#d5d9d9", "#727575"
        self._pill(1, 1, w-1, h-1, border)
        self._pill(2, 2, w-2, h-2, hover if self._hover else base)
        self.create_text(
            w/2, h/2, text=self._text, fill=fg,
            font=("Arial", 10), anchor="center",
            width=max(10, w-22), justify="center"
        )
        if self.focus_get() == self:
            self.create_rectangle(1, 1, w-2, h-2, outline="#007185", width=1)


class NegozioApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Ales Commerce - Ricerca prodotti")
        self.root.geometry("1350x850")
        self.root.minsize(950, 600)
        self.root.configure(bg=SFONDO)

        self.products = []
        self.categories = []
        self.category_by_id = {}
        self.category_id_by_name = {}
        self.product_category_ids = {}
        self.category_label_to_id = {}
        self.category_id_to_label = {}
        self.uncategorized_id = "__senza_categoria__"
        self.category_link_detected = False
        self.cart = {}
        self.images = []
        self.visible_products = []
        self._last_render_width = 0
        self._home_resize_job = None

        self.saved_for_later = {}
        self.gift_var = tk.BooleanVar(value=False)
        self.cart_images = []

        # Sessione: ID recuperato dalla tabella utenti dopo il login.
        # L'ID rimane disponibile finché il programma resta aperto.
        self.user_id = None
        self.user_email = None
        self.account_text = tk.StringVar(value="Ciao, accedi\nAccount e liste")
        self.login_window = None
        self._login_redirect_to_cart = False
        self.cart_windows = set()

        self.search_var = tk.StringVar()
        self.category_var = tk.StringVar(value="Tutte le categorie")
        self.brand_var = tk.StringVar(value="Tutte le marche")
        self.rating_var = tk.StringVar(value="Tutte le valutazioni")
        self.min_price_var = tk.StringVar()
        self.max_price_var = tk.StringVar()

        self.cart_text = tk.StringVar(value="Carrello (0)")
        self.results_text = tk.StringVar(value="Caricamento prodotti...")
        self.results_heading = tk.StringVar(value="Scopri le categorie")

        self.build_header()
        self.build_navigation()
        self.build_main_area()
        # Evita callback di ridimensionamento rimaste in coda alla chiusura.
        self.root.bind("<Destroy>", self._on_main_window_destroy, add="+")
        # Stampa gli account appena si avvia l'app, prima di caricare i prodotti.
        # La diagnostica non deve impedire il funzionamento del negozio.
        self.stampa_tutti_utenti("avvio del programma")
        self.load_products()

    # --------------------------------------------------
    # INTESTAZIONE
    # --------------------------------------------------

    def build_header(self):
        # La barra segue il layout Amazon fornito: campo flessibile,
        # altezza 60 px, angoli da 4 px, testo da ~14 px.
        header = tk.Frame(self.root, bg=BLU, height=82)
        header.pack(fill="x")
        header.pack_propagate(False)

        logo = tk.Label(
            header, text="ales", font=("Arial", 25, "bold"),
            fg="white", bg=BLU
        )
        logo.pack(side="left", padx=(20, 3))

        tk.Label(
            header, text=".commerce", font=("Arial", 13, "bold"),
            fg=GIALLO, bg=BLU
        ).pack(side="left", padx=(0, 18), pady=(12, 0))

        # Contenitore della ricerca largo quanto lo spazio disponibile.
        # Il Canvas consente angoli arrotondati anche in Tkinter classico.
        search_box = tk.Canvas(
            header, bg=BLU, height=60,
            bd=0, highlightthickness=0, relief="flat"
        )
        search_box.pack(
            side="left", fill="x", expand=True,
            padx=10, pady=10
        )

        self.search_entry = tk.Entry(
            search_box,
            textvariable=self.search_var,
            font=("Arial", 11),  # ~14px, come il CSS allegato
            fg="#0f1111", bg="#ffffff",
            insertbackground="#0f1111",
            bd=0, relief="flat", highlightthickness=0
        )
        search_entry_window = search_box.create_window(
            15, 30, window=self.search_entry, anchor="w", height=38
        )

        search_button = tk.Button(
            search_box,
            text="⌕",
            font=("Arial", 22, "bold"),
            bg="#febd69", fg="#0f1111",
            activebackground="#f3a847", activeforeground="#0f1111",
            bd=0, relief="flat", cursor="hand2",
            command=self.apply_filters, takefocus=True
        )
        search_button_window = search_box.create_window(
            0, 4, window=search_button, anchor="nw", height=52
        )

        def rounded_rect(canvas, x1, y1, x2, y2, r, **kw):
            # Tracciato arrotondato con raggio simile a border-radius: 4px.
            return canvas.create_polygon(
                x1+r, y1, x2-r, y1, x2, y1, x2, y1+r,
                x2, y2-r, x2, y2, x2-r, y2, x1+r, y2,
                x1, y2, x1, y2-r, x1, y1+r, x1, y1,
                smooth=True, splinesteps=12, **kw
            )

        def aggiorna_ricerca(event=None):
            larghezza = search_box.winfo_width()
            if larghezza < 95:
                return
            search_box.delete("search_bg")
            focused = self.search_entry.focus_get() is self.search_entry
            bordo = "#ff9900" if focused else "#ffffff"
            rounded_rect(
                search_box, 2, 2, larghezza - 2, 58, 4,
                fill="#ffffff", outline=bordo,
                width=3 if focused else 1, tags="search_bg"
            )
            search_box.tag_lower("search_bg")
            # Lascia 60px al pulsante di ricerca.
            search_box.coords(search_entry_window, 15, 30)
            search_box.itemconfigure(
                search_entry_window, width=max(10, larghezza - 86)
            )
            search_box.coords(search_button_window, larghezza - 60, 4)
            search_box.itemconfigure(search_button_window, width=56)

        search_box.bind("<Configure>", aggiorna_ricerca)
        self.search_entry.bind("<FocusIn>", aggiorna_ricerca)
        self.search_entry.bind("<FocusOut>", aggiorna_ricerca)
        self.search_entry.bind(
            "<Return>", lambda event: self.apply_filters()
        )
        # Un clic sulla cornice porta il cursore dentro il campo di ricerca.
        search_box.bind(
            "<Button-1>", lambda event: self.search_entry.focus_set()
        )

        tk.Button(
            header,
            textvariable=self.account_text,
            font=("Arial", 10, "bold"),
            fg="white", bg=BLU,
            activebackground=BLU_CHIARO,
            bd=0, cursor="hand2", command=self.show_account
        ).pack(side="left", padx=10)

        tk.Button(
            header,
            textvariable=self.cart_text,
            font=("Arial", 11, "bold"),
            fg="white", bg=BLU,
            activebackground=BLU_CHIARO,
            bd=0, cursor="hand2", command=self.show_cart
        ).pack(side="right", padx=18)

    def build_navigation(self):
        nav = tk.Frame(self.root, bg=BLU_CHIARO, height=38)
        nav.pack(fill="x")
        nav.pack_propagate(False)

        for testo, azione in (
            ("☰ Tutte le categorie", self.clear_filters),
            ("Offerte", lambda: self.navigation_click("Offerte")),
        ):
            tk.Button(
                nav, text=testo, font=("Arial", 10, "bold"),
                fg="white", bg=BLU_CHIARO,
                activebackground="#37475a", activeforeground="white",
                bd=0, cursor="hand2", command=azione
            ).pack(side="left", padx=12, pady=5)

        # Questo menu è riempito con i nomi effettivi di SELECT * FROM categorie.
        self.category_nav_menu = tk.Menu(nav, tearoff=False)
        tk.Menubutton(
            nav, text="Categorie ▾", menu=self.category_nav_menu,
            font=("Arial", 10, "bold"), fg="white", bg=BLU_CHIARO,
            activebackground="#37475a", activeforeground="white",
            bd=0, cursor="hand2", padx=12
        ).pack(side="left", pady=5)

        tk.Button(
            nav, text="I tuoi articoli", font=("Arial", 10, "bold"),
            fg="white", bg=BLU_CHIARO,
            activebackground="#37475a", activeforeground="white",
            bd=0, cursor="hand2", command=self.show_cart
        ).pack(side="left", padx=12, pady=5)

    def update_category_navigation(self):
        self.category_nav_menu.delete(0, "end")
        self.category_nav_menu.add_command(
            label="Tutte le categorie", command=self.clear_filters
        )
        if self.categories:
            self.category_nav_menu.add_separator()
        for categoria in self.categories:
            category_id = categoria["id"]
            self.category_nav_menu.add_command(
                label=categoria["nome"],
                command=lambda cid=category_id: self.select_category(cid)
            )

    def select_category(self, category_id):
        """Apri i prodotti della categoria scelta, senza alterare i dati."""
        category_id = self._chiave_categoria(category_id)
        self.search_var.set("")
        self.brand_var.set("Tutte le marche")
        self.rating_var.set("Tutte le valutazioni")
        self.min_price_var.set("")
        self.max_price_var.set("")
        self.sort_var.set("Consigliati")
        self.category_var.set(
            self.category_id_to_label.get(category_id, "Tutte le categorie")
        )
        self.apply_filters()
        self.canvas.yview_moveto(0)

    # --------------------------------------------------
    # AREA PRINCIPALE E FILTRI
    # --------------------------------------------------

    def build_main_area(self):
        self.main = tk.Frame(self.root, bg=SFONDO)
        self.main.pack(fill="both", expand=True)

        # Barra laterale sinistra
        self.sidebar = tk.Frame(
            self.main,
            bg=SFONDO,
            width=225,
            padx=17,
            pady=14
        )
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        tk.Label(
            self.sidebar,
            text="Filtri",
            font=("Arial", 16, "bold"),
            bg=SFONDO,
            fg=TESTO
        ).pack(anchor="w", pady=(0, 15))

        self.filter_section("Categoria")

        self.category_combo = ttk.Combobox(
            self.sidebar, textvariable=self.category_var,
            state="readonly", values=["Tutte le categorie"]
        )
        self.category_combo.pack(fill="x", pady=(0, 15))
        self.category_combo.bind(
            "<<ComboboxSelected>>", lambda event: self.apply_filters()
        )

        self.filter_section("Marca")

        self.brand_combo = ttk.Combobox(
            self.sidebar,
            textvariable=self.brand_var,
            state="readonly"
        )
        self.brand_combo.pack(fill="x", pady=(0, 15))
        self.brand_combo.bind(
            "<<ComboboxSelected>>",
            lambda event: self.apply_filters()
        )

        self.filter_section("Valutazione clienti")

        self.rating_combo = ttk.Combobox(
            self.sidebar,
            textvariable=self.rating_var,
            state="readonly",
            values=[
                "Tutte le valutazioni",
                "4 stelle e più",
                "3 stelle e più",
                "2 stelle e più"
            ]
        )
        self.rating_combo.pack(fill="x", pady=(0, 15))
        self.rating_combo.bind(
            "<<ComboboxSelected>>",
            lambda event: self.apply_filters()
        )

        self.filter_section("Prezzo")

        tk.Label(
            self.sidebar,
            text="Prezzo minimo (€)",
            bg=SFONDO,
            fg=TESTO
        ).pack(anchor="w")

        self.min_entry = ttk.Entry(
            self.sidebar,
            textvariable=self.min_price_var
        )
        self.min_entry.pack(fill="x", pady=(3, 8))

        tk.Label(
            self.sidebar,
            text="Prezzo massimo (€)",
            bg=SFONDO,
            fg=TESTO
        ).pack(anchor="w")

        self.max_entry = ttk.Entry(
            self.sidebar,
            textvariable=self.max_price_var
        )
        self.max_entry.pack(fill="x", pady=(3, 10))

        self.min_entry.bind(
            "<Return>",
            lambda event: self.apply_filters()
        )
        self.max_entry.bind(
            "<Return>",
            lambda event: self.apply_filters()
        )

        AmazonButton(
            self.sidebar, text="Applica filtri",
            command=self.apply_filters, variant="secondary"
        ).pack(fill="x", pady=(0, 8))

        AmazonButton(
            self.sidebar, text="Cancella filtri",
            command=self.clear_filters, variant="secondary"
        ).pack(fill="x", pady=(0, 15))

        ttk.Separator(self.sidebar).pack(fill="x", pady=8)

        AmazonButton(
            self.sidebar, text="Aggiorna dal database",
            command=self.load_products, variant="subtle"
        ).pack(fill="x", pady=5)

        # Area risultati
        self.results_area = tk.Frame(self.main, bg=SFONDO)
        self.results_area.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.results_header = tk.Frame(
            self.results_area,
            bg=SFONDO,
            padx=15,
            pady=12
        )
        self.results_header.pack(fill="x")

        tk.Label(
            self.results_header,
            textvariable=self.results_heading,
            font=("Arial", 17, "bold"),
            bg=SFONDO,
            fg=TESTO
        ).pack(anchor="w")

        tk.Label(
            self.results_header,
            textvariable=self.results_text,
            font=("Arial", 10),
            bg=SFONDO,
            fg="#565959"
        ).pack(anchor="w", pady=(4, 0))

        # Ordinamento
        sort_frame = tk.Frame(
            self.results_area,
            bg="#f3f3f3",
            padx=12,
            pady=7
        )
        sort_frame.pack(fill="x", padx=10)

        tk.Label(
            sort_frame,
            text="Ordina per:",
            bg="#f3f3f3"
        ).pack(side="left")

        self.sort_var = tk.StringVar(value="Consigliati")

        self.sort_combo = ttk.Combobox(
            sort_frame,
            textvariable=self.sort_var,
            state="readonly",
            values=[
                "Consigliati",
                "Prezzo crescente",
                "Prezzo decrescente",
                "Valutazione"
            ],
            width=23
        )
        self.sort_combo.pack(side="left", padx=8)
        self.sort_combo.bind(
            "<<ComboboxSelected>>",
            lambda event: self.apply_filters()
        )

        # Canvas scorrevole per la griglia
        self.canvas = tk.Canvas(
            self.results_area,
            bg=SFONDO,
            highlightthickness=0
        )

        self.scrollbar = ttk.Scrollbar(
            self.results_area,
            orient="vertical",
            command=self.canvas.yview
        )

        self.grid_frame = tk.Frame(
            self.canvas,
            bg=SFONDO
        )

        self.grid_window = self.canvas.create_window(
            (0, 0),
            window=self.grid_frame,
            anchor="nw"
        )

        self.canvas.configure(
            yscrollcommand=self.scrollbar.set
        )

        self.canvas.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(8, 0)
        )
        self.scrollbar.pack(side="right", fill="y")

        self.grid_frame.bind(
            "<Configure>",
            self.update_scroll_region
        )

        self.canvas.bind("<Configure>", self.update_grid_width)
        self.canvas.bind("<Enter>", self.bind_mousewheel)
        self.canvas.bind("<Leave>", self.unbind_mousewheel)

    def filter_section(self, title):
        tk.Label(
            self.sidebar,
            text=title,
            font=("Arial", 11, "bold"),
            bg=SFONDO,
            fg=TESTO
        ).pack(anchor="w", pady=(0, 7))

    # --------------------------------------------------
    # CARICAMENTO DATABASE
    # --------------------------------------------------

    @staticmethod
    def _campo_esistente(riga, nomi):
        """Trova una colonna ignorando maiuscole/minuscole."""
        chiavi = {str(k).lower(): k for k in riga}
        for nome in nomi:
            if nome.lower() in chiavi:
                return chiavi[nome.lower()]
        return None

    @staticmethod
    def _chiave_categoria(valore):
        """Uniforma gli identificativi SQL per confrontarli senza ambiguità."""
        if valore is None:
            return None
        valore = str(valore).strip()
        if not valore:
            return None
        try:
            decimale = Decimal(valore)
            if decimale == decimale.to_integral_value():
                return str(int(decimale))
        except (InvalidOperation, ValueError, OverflowError):
            pass
        return valore

    @staticmethod
    def _colore_esadecimale(valore):
        """Converte il colore SQL in un codice Tk #RRGGBB valido.

        Se il campo è vuoto o malformato, usa un bordo neutro.
        """
        if valore is None:
            return "#d5d9d9"
        colore = str(valore).strip()
        if colore.lower().startswith("0x"):
            colore = colore[2:]
        colore = colore.lstrip("#")
        if re.fullmatch(r"[0-9A-Fa-f]{3}", colore):
            colore = "".join(c * 2 for c in colore)
        if re.fullmatch(r"[0-9A-Fa-f]{6}", colore):
            return "#" + colore.upper()
        return "#d5d9d9"

    def _prepara_categorie(self, righe):
        """Usa ID e nome esattamente come arrivano dalla tabella categorie."""
        categorie = []
        mappa = {}
        nomi = {}
        for riga in righe:
            campo_id = self._campo_esistente(
                riga, ("id", "id_categoria", "categoria_id", "id_categorie")
            )
            campo_nome = self._campo_esistente(
                riga, ("nome", "nome_categoria", "categoria", "label", "name")
            )
            if campo_id is None or campo_nome is None:
                raise ValueError(
                    "La tabella categorie deve contenere l'ID e il nome "
                    "(ad esempio le colonne 'id' e 'nome')."
                )
            id_categoria = self._chiave_categoria(riga[campo_id])
            nome_categoria = str(riga[campo_nome] or "").strip()
            if id_categoria is None or not nome_categoria:
                continue
            campo_immagine = self._campo_esistente(riga, ("immagine",))
            campo_colore = self._campo_esistente(riga, ("colore",))
            categorie.append({
                "id": id_categoria,
                "nome": nome_categoria,
                "immagine": riga.get(campo_immagine) if campo_immagine else None,
                "colore": self._colore_esadecimale(
                    riga.get(campo_colore) if campo_colore else None
                )
            })
            mappa[id_categoria] = nome_categoria
            nomi[nome_categoria.casefold()] = id_categoria
        self.categories = categorie
        self.category_by_id = mappa
        self.category_id_by_name = nomi

    def _risolvi_categorie(self, valore):
        """Supporta FK numeriche e nomi testuali di categoria."""
        if valore is None:
            return set()
        parti = re.split(r"[,;|]", str(valore))
        risultato = set()
        for parte in parti:
            parte = parte.strip()
            if not parte:
                continue
            chiave = self._chiave_categoria(parte)
            if chiave in self.category_by_id:
                risultato.add(chiave)
            elif parte.casefold() in self.category_id_by_name:
                risultato.add(self.category_id_by_name[parte.casefold()])
        return risultato

    def _collega_prodotti_categorie(self, cursor, righe_categorie):
        """Associa i prodotti tramite FK in articoli o tabella ponte esistente."""
        self.product_category_ids = {
            p["id"]: set() for p in self.products
        }
        self.category_link_detected = False
        if not self.products or not self.categories:
            return

        # Caso comune: articoli.id_categoria -> categorie.id.
        campo = self._campo_esistente(self.products[0], ARTICLE_CATEGORY_FIELDS)
        if campo is not None:
            self.category_link_detected = True
            for prodotto in self.products:
                self.product_category_ids[prodotto["id"]].update(
                    self._risolvi_categorie(prodotto.get(campo))
                )

        # Supporto anche a categorie.id_articolo (categorie associate ai prodotti).
        if righe_categorie:
            campo_articolo = self._campo_esistente(
                righe_categorie[0], ARTICLE_ID_FIELDS
            )
            if campo_articolo is not None:
                self.category_link_detected = True
                for categoria, raw in zip(self.categories, righe_categorie):
                    article_id = self._chiave_categoria(raw.get(campo_articolo))
                    for id_articolo in self.product_category_ids:
                        if self._chiave_categoria(id_articolo) == article_id:
                            self.product_category_ids[id_articolo].add(categoria["id"])

        # Supporto opzionale per una relazione molti-a-molti in tabella ponte.
        try:
            cursor.execute("SHOW TABLES")
            tavole = cursor.fetchall()
            nomi_tabelle = {
                str(next(iter(riga.values()))).lower(): str(next(iter(riga.values())))
                for riga in tavole if riga
            }
            for nome_candidato in CATEGORY_LINK_TABLES:
                nome_tabella = nomi_tabelle.get(nome_candidato)
                if not nome_tabella or not re.fullmatch(r"[A-Za-z0-9_]+", nome_tabella):
                    continue
                cursor.execute(f"SELECT * FROM `{nome_tabella}`")
                associazioni = cursor.fetchall()
                if not associazioni:
                    continue
                id_articolo = self._campo_esistente(associazioni[0], ARTICLE_ID_FIELDS)
                id_categoria = self._campo_esistente(associazioni[0], ARTICLE_CATEGORY_FIELDS)
                if id_articolo is None or id_categoria is None:
                    continue
                self.category_link_detected = True
                products_by_id = {
                    self._chiave_categoria(p["id"]): p["id"] for p in self.products
                }
                for riga in associazioni:
                    product_id = products_by_id.get(
                        self._chiave_categoria(riga.get(id_articolo))
                    )
                    if product_id is not None:
                        self.product_category_ids[product_id].update(
                            self._risolvi_categorie(riga.get(id_categoria))
                        )
        except mysql.connector.Error:
            # In alcuni server SHOW TABLES non è autorizzato: i collegamenti
            # diretti letti da articoli rimangono utilizzabili.
            pass

    def _aggiorna_controlli_categorie(self):
        etichette = ["Tutte le categorie"]
        self.category_label_to_id = {}
        self.category_id_to_label = {}
        nomi_duplicati = {
            c["nome"] for c in self.categories
            if sum(1 for x in self.categories if x["nome"] == c["nome"]) > 1
        }
        for categoria in self.categories:
            etichetta = categoria["nome"]
            if etichetta in nomi_duplicati:
                etichetta += f" (ID {categoria['id']})"
            etichette.append(etichetta)
            self.category_label_to_id[etichetta] = categoria["id"]
            self.category_id_to_label[categoria["id"]] = etichetta
        if any(
            not self.product_category_ids.get(p["id"], set())
            for p in self.products
        ):
            etichetta_senza = "Senza categoria"
            if etichetta_senza in self.category_label_to_id:
                etichetta_senza = "Senza categoria (non associati)"
            etichette.append(etichetta_senza)
            self.category_label_to_id[etichetta_senza] = self.uncategorized_id
            self.category_id_to_label[self.uncategorized_id] = etichetta_senza

        self.category_combo["values"] = etichette
        if self.category_var.get() not in etichette:
            self.category_var.set("Tutte le categorie")
        self.update_category_navigation()

    def load_products(self):
        connection = None
        cursor = None
        try:
            self.results_text.set("Caricamento articoli e categorie...")
            connection = mysql.connector.connect(**DB_CONFIG)
            cursor = connection.cursor(dictionary=True)

            # Categoria: esattamente la query richiesta.
            cursor.execute("SELECT * FROM categorie")
            righe_categorie = cursor.fetchall()
            self._prepara_categorie(righe_categorie)

            # SELECT * include la colonna FK anche se è stata aggiunta
            # dopo la prima versione dell'applicazione.
            cursor.execute(f"SELECT * FROM `{TABLE_NAME}` ORDER BY id")
            self.products = cursor.fetchall()
            self._collega_prodotti_categorie(cursor, righe_categorie)
            self._aggiorna_controlli_categorie()

            marche = sorted({
                str(p.get("marca") or "").strip()
                for p in self.products if str(p.get("marca") or "").strip()
            }, key=str.lower)
            self.brand_combo["values"] = ["Tutte le marche"] + marche
            if self.brand_var.get() not in self.brand_combo["values"]:
                self.brand_var.set("Tutte le marche")
            self.apply_filters()
            if self.categories and self.products and not self.category_link_detected:
                self.results_text.set(
                    "Categorie caricate, ma non ho trovato la colonna che "
                    "collega gli articoli alle categorie (es. id_categoria)."
                )

        except (mysql.connector.Error, ValueError) as error:
            self.results_text.set("Impossibile caricare articoli e categorie.")
            messagebox.showerror(
                "Errore catalogo MySQL",
                f"Non riesco a caricare o associare articoli e categorie.\n\n{error}"
            )
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None and connection.is_connected():
                connection.close()

    # --------------------------------------------------
    # RICERCA, FILTRI E ORDINAMENTO
    # --------------------------------------------------

    def apply_filters(self):
        testo = self.search_var.get().strip().lower()
        marca = self.brand_var.get()
        categoria_selezionata = self.category_label_to_id.get(
            self.category_var.get()
        )
        valutazione = self.rating_var.get()

        try:
            prezzo_min = leggi_prezzo_filtro(self.min_price_var.get())
            prezzo_max = leggi_prezzo_filtro(self.max_price_var.get())

        except (ValueError, InvalidOperation):
            messagebox.showwarning(
                "Prezzo non valido",
                "Inserisci un numero valido nei campi del prezzo."
            )
            return

        risultati = []

        for p in self.products:
            campi = [
                p.get("label", ""),
                p.get("descrizione", ""),
                p.get("marca", ""),
                p.get("tag", ""),
                " ".join(
                    self.category_by_id.get(cid, "")
                    for cid in self.product_category_ids.get(p["id"], set())
                ),
                str(p.get("id", ""))
            ]

            testo_prodotto = " ".join(
                str(campo or "") for campo in campi
            ).lower()

            if testo and testo not in testo_prodotto:
                continue

            if marca != "Tutte le marche":
                if str(p.get("marca") or "").strip() != marca:
                    continue

            ids_prodotto = self.product_category_ids.get(p["id"], set())
            if categoria_selezionata == self.uncategorized_id:
                if ids_prodotto:
                    continue
            elif (categoria_selezionata is not None and
                    categoria_selezionata not in ids_prodotto):
                continue

            try:
                prezzo = importo_decimale(p.get("prezzo_cat") or 0)
            except (TypeError, ValueError):
                prezzo = Decimal("0")

            try:
                stelle = float(p.get("stelline") or 0)
            except (TypeError, ValueError):
                stelle = 0

            if prezzo_min is not None and prezzo < prezzo_min:
                continue

            if prezzo_max is not None and prezzo > prezzo_max:
                continue

            if valutazione == "4 stelle e più" and stelle < 4:
                continue

            if valutazione == "3 stelle e più" and stelle < 3:
                continue

            if valutazione == "2 stelle e più" and stelle < 2:
                continue

            risultati.append(p)

        ordinamento = self.sort_var.get()

        if ordinamento == "Prezzo crescente":
            risultati.sort(
                key=lambda p: importo_decimale(p.get("prezzo_cat") or 0)
            )

        elif ordinamento == "Prezzo decrescente":
            risultati.sort(
                key=lambda p: importo_decimale(p.get("prezzo_cat") or 0),
                reverse=True
            )

        elif ordinamento == "Valutazione":
            risultati.sort(
                key=lambda p: float(p.get("stelline") or 0),
                reverse=True
            )

        self.show_products(risultati)

        if self._mostra_panorama_categorie():
            self.results_heading.set("Scopri le categorie")
            self.results_text.set(
                f"{len(self.categories)} categorie e {len(self.products)} "
                "articoli disponibili nel catalogo."
            )
        elif categoria_selezionata is not None:
            self.results_heading.set(
                self.category_id_to_label.get(
                    categoria_selezionata, "Articoli della categoria"
                )
            )
            self.results_text.set(f"{len(risultati)} articoli in questa categoria.")
        else:
            self.results_heading.set("Risultati della ricerca")
            self.results_text.set(
                f"Visualizzati {len(risultati)} risultati su "
                f"{len(self.products)} articoli disponibili."
            )

    def clear_filters(self):
        self.search_var.set("")
        self.category_var.set("Tutte le categorie")
        self.brand_var.set("Tutte le marche")
        self.rating_var.set("Tutte le valutazioni")
        self.min_price_var.set("")
        self.max_price_var.set("")
        self.sort_var.set("Consigliati")
        self.apply_filters()

    # --------------------------------------------------
    # GRIGLIA PRODOTTI
    # --------------------------------------------------

    def show_products(self, products):
        """Mostra i risultati su una griglia che usa tutta la larghezza."""
        self.visible_products = list(products)
        self._render_home_products()

    def _mostra_panorama_categorie(self):
        """La home iniziale presenta le categorie; la ricerca mostra i prodotti."""
        return (
            bool(self.categories)
            and self.category_var.get() == "Tutte le categorie"
            and self.brand_var.get() == "Tutte le marche"
            and self.rating_var.get() == "Tutte le valutazioni"
            and not self.search_var.get().strip()
            and not self.min_price_var.get().strip()
            and not self.max_price_var.get().strip()
            and self.sort_var.get() == "Consigliati"
        )

    @staticmethod
    def _cornice_arrotondata(canvas, width, height, colore_bordo="#d5d9d9"):
        """Disegna il box col bordo esadecimale letto da categorie.colore."""
        canvas.delete("cornice")
        r = 17
        canvas.create_polygon(
            r, 2, width-r, 2, width-2, r, width-2, height-r,
            width-r, height-2, r, height-2, 2, height-r, 2, r,
            fill="#ffffff", outline=colore_bordo, width=2,
            smooth=True, splinesteps=12, tags="cornice"
        )
        canvas.tag_lower("cornice")

    def _foto_box_categoria(self, blob, larghezza, altezza):
        """Legge categorie.immagine (BLOB JPG/PNG/WEBP), senza ritagliarla."""
        if not blob:
            return None
        try:
            with Image.open(BytesIO(bytes(blob))) as originale:
                originale.load()
                originale = originale.convert("RGBA")
                originale.thumbnail(
                    (max(1, larghezza - 10), max(1, altezza - 10)),
                    Image.Resampling.LANCZOS
                )
                sfondo = Image.new("RGBA", (larghezza, altezza), "white")
                sinistra = (larghezza - originale.width) // 2
                alto = (altezza - originale.height) // 2
                sfondo.alpha_composite(originale, (sinistra, alto))
                maschera = Image.new("L", (larghezza, altezza), 0)
                ImageDraw.Draw(maschera).rounded_rectangle(
                    (0, 0, larghezza - 1, altezza - 1), radius=12, fill=255
                )
                sfondo.putalpha(maschera)
                foto = ImageTk.PhotoImage(sfondo)
                self.images.append(foto)
                return foto
        except (OSError, ValueError, TypeError):
            return None

    def _foto_categoria(self, blob, dimensione, colore):
        """Anteprima quadrata con angoli arrotondati, da img del database."""
        if not blob:
            return None
        try:
            with Image.open(BytesIO(bytes(blob))) as originale:
                originale.load()
                originale = originale.convert("RGBA")
                originale.thumbnail(
                    (dimensione-8, dimensione-8), Image.Resampling.LANCZOS
                )
                anteprima = Image.new(
                    "RGBA", (dimensione, dimensione), colore
                )
                x = (dimensione - originale.width) // 2
                y = (dimensione - originale.height) // 2
                anteprima.alpha_composite(originale, (x, y))
                maschera = Image.new("L", (dimensione, dimensione), 0)
                ImageDraw.Draw(maschera).rounded_rectangle(
                    (0, 0, dimensione-1, dimensione-1),
                    radius=12, fill=255
                )
                anteprima.putalpha(maschera)
                foto = ImageTk.PhotoImage(anteprima)
                self.images.append(foto)
                return foto
        except (OSError, ValueError, TypeError):
            return None

    def _render_category_overview(self, larghezza):
        """Griglia di riquadri 2×2: usa SOLO categorie e prodotti del database."""
        colonne = (4 if larghezza >= 1000 else
                   3 if larghezza >= 780 else 2)
        for c in range(5):
            self.grid_frame.grid_columnconfigure(
                c,
                weight=1 if c < colonne else 0,
                uniform="overview" if c < colonne else "",
                minsize=0
            )

        # Nessun prodotto inventato: si mostrano solo quelli già associati.
        categorie_con_prodotti = []
        assegnati = set()
        for categoria in self.categories:
            cid = categoria["id"]
            articoli = [
                p for p in self.products
                if cid in self.product_category_ids.get(p["id"], set())
            ]
            categorie_con_prodotti.append((
                cid, categoria["nome"], articoli,
                categoria.get("immagine"), categoria.get("colore", "#d5d9d9")
            ))
            assegnati.update(p["id"] for p in articoli)

        senza_categoria = [
            p for p in self.products if p["id"] not in assegnati
        ]
        if senza_categoria:
            categorie_con_prodotti.append((
                self.uncategorized_id,
                self.category_id_to_label.get(self.uncategorized_id, "Senza categoria"),
                senza_categoria,
                None, "#d5d9d9"
            ))

        larghezza_card = max(210, int(larghezza / colonne) - 13)
        dimensione_immagine = max(76, (larghezza_card - 46) // 2)
        altezza_card = 2 * (dimensione_immagine + 48) + 69
        # Colori delle anteprime prodotti (solo per categorie senza immagine).
        colori_sfondo = ("#e1efe6", "#e6f2f8", "#f4f0ec", "#e0eff5")

        for indice, (cid, nome, articoli, immagine_categoria, colore_bordo) in enumerate(categorie_con_prodotti):
            riga, colonna = divmod(indice, colonne)
            colore = colori_sfondo[indice % len(colori_sfondo)]
            contenitore = tk.Canvas(
                self.grid_frame,
                bg=SFONDO, bd=0, highlightthickness=0,
                height=altezza_card
            )
            contenitore.grid(
                row=riga, column=colonna, sticky="nsew",
                padx=4, pady=5
            )
            interno = tk.Frame(contenitore, bg="white", padx=11, pady=10)
            id_interno = contenitore.create_window(
                4, 4, window=interno, anchor="nw"
            )

            def ridimensiona(event, area=contenitore, elemento=id_interno, bordo=colore_bordo):
                area.itemconfigure(
                    elemento, width=max(1, event.width - 8),
                    height=max(1, event.height - 8)
                )
                self._cornice_arrotondata(
                    area, event.width, event.height, bordo
                )

            contenitore.bind("<Configure>", ridimensiona)

            intestazione = tk.Frame(interno, bg="white")
            intestazione.pack(fill="x", pady=(0, 7))
            titolo = tk.Label(
                intestazione,
                text=nome,
                bg="white", fg=TESTO,
                font=("Arial", 12, "bold"),
                anchor="w", justify="left",
                wraplength=max(130, larghezza_card-67),
                cursor="hand2"
            )
            titolo.pack(side="left", fill="x", expand=True)
            freccia = tk.Label(
                intestazione, text="›",
                font=("Arial", 23), fg=TESTO,
                bg="white", cursor="hand2"
            )
            freccia.pack(side="right", padx=(3, 0))
            for widget in (titolo, freccia, intestazione):
                widget.bind(
                    "<Button-1>", lambda event, category=cid:
                        self.select_category(category)
                )

            # L'immagine assegnata a categorie.immagine è l'elemento
            # principale del box. La vecchia griglia 2×2 rimane come fallback
            # se non è stato inserito un BLOB immagine valido.
            foto_box = self._foto_box_categoria(
                immagine_categoria,
                max(80, larghezza_card - 36),
                max(100, altezza_card - 115)
            )
            if foto_box is not None:
                foto_categoria = tk.Label(
                    interno, bg="white", image=foto_box,
                    cursor="hand2", bd=0
                )
                foto_categoria.image = foto_box
                foto_categoria.pack(fill="both", expand=True, pady=(0, 8))
                foto_categoria.bind(
                    "<Button-1>", lambda event, category=cid:
                        self.select_category(category)
                )
                tk.Label(
                    interno,
                    text=f"{len(articoli)} articoli" if len(articoli) != 1 else "1 articolo",
                    bg="white", fg="#565959", font=("Arial", 9)
                ).pack(anchor="w")
                continue

            mosaico = tk.Frame(interno, bg="white")
            mosaico.pack(fill="both", expand=True)
            mosaico.grid_columnconfigure(0, weight=1, uniform="tiles")
            mosaico.grid_columnconfigure(1, weight=1, uniform="tiles")

            if not articoli:
                tk.Label(
                    mosaico, text="Nessun articolo associato",
                    font=("Arial", 10), fg="#565959",
                    bg="white", anchor="center"
                ).grid(row=0, column=0, columnspan=2, pady=24, sticky="ew")
                continue

            for posizione, prodotto in enumerate(articoli[:4]):
                r, c = divmod(posizione, 2)
                tassello = tk.Frame(mosaico, bg="white", cursor="hand2")
                tassello.grid(
                    row=r, column=c, sticky="new", padx=3, pady=(1, 8)
                )
                immagine = tk.Frame(
                    tassello, bg=colore,
                    width=dimensione_immagine,
                    height=dimensione_immagine,
                    cursor="hand2"
                )
                immagine.pack(fill="x")
                immagine.pack_propagate(False)
                foto = self._foto_categoria(
                    prodotto.get("img"), dimensione_immagine, colore
                )
                etichetta_img = tk.Label(
                    immagine, bg=colore,
                    image=foto if foto is not None else "",
                    text="" if foto is not None else "Immagine\nnon disponibile",
                    fg="#667575", font=("Arial", 9),
                    cursor="hand2"
                )
                etichetta_img.pack(expand=True)
                etichetta_nome = tk.Label(
                    tassello,
                    text=str(prodotto.get("label") or ""),
                    font=("Arial", 9), fg=TESTO, bg="white",
                    wraplength=max(70, dimensione_immagine),
                    justify="left", anchor="nw",
                    height=2, cursor="hand2"
                )
                etichetta_nome.pack(fill="x", pady=(5, 0))
                for widget in (tassello, immagine, etichetta_img, etichetta_nome):
                    widget.bind(
                        "<Button-1>", lambda event, category=cid:
                            self.select_category(category)
                    )

    def _render_home_products(self):
        prodotti = self.visible_products
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
        self.images = []

        larghezza = self.canvas.winfo_width()
        if larghezza < 100:
            larghezza = max(700, int(self.root.geometry().split("x")[0]) - 245)
        self._last_render_width = larghezza

        if self._mostra_panorama_categorie():
            self._render_category_overview(larghezza)
            return

        colonne = max(2, min(5, (larghezza - 16) // 320))
        larghezza_scheda = max(220, (larghezza - 22) // colonne - 12)
        larghezza_testo = max(190, larghezza_scheda - 42)
        for indice in range(5):
            self.grid_frame.grid_columnconfigure(
                indice,
                weight=1 if indice < colonne else 0,
                uniform="schede_home" if indice < colonne else "",
                minsize=0
            )

        if not prodotti:
            tk.Label(
                self.grid_frame,
                text="Nessun articolo corrisponde alla ricerca o alla categoria.",
                font=("Arial", 13), bg=SFONDO, fg=TESTO,
                padx=24, pady=35
            ).grid(row=0, column=0, sticky="w", columnspan=colonne)
            return

        # Gli articoli con più categorie appaiono in ciascuna categoria.
        gruppi = {categoria["id"]: [] for categoria in self.categories}
        senza_categoria = []
        for prodotto in prodotti:
            ids = self.product_category_ids.get(prodotto["id"], set())
            ids_validi = [cid for cid in ids if cid in gruppi]
            if not ids_validi:
                senza_categoria.append(prodotto)
            for cid in ids_validi:
                gruppi[cid].append(prodotto)

        if senza_categoria:
            gruppi[None] = senza_categoria

        riga_corrente = 0
        for cid, prodotti_categoria in gruppi.items():
            if not prodotti_categoria:
                continue
            nome_categoria = self.category_by_id.get(cid, "Senza categoria")
            barra_sezione = tk.Frame(self.grid_frame, bg="#f3f5f5", padx=14, pady=12)
            barra_sezione.grid(
                row=riga_corrente, column=0, columnspan=colonne,
                sticky="ew", padx=6, pady=(15 if riga_corrente else 5, 8)
            )
            tk.Label(
                barra_sezione, text=nome_categoria,
                font=("Arial", 17, "bold"), bg="#f3f5f5", fg=TESTO
            ).pack(side="left")
            tk.Label(
                barra_sezione,
                text=f"{len(prodotti_categoria)} articoli",
                font=("Arial", 10), bg="#f3f5f5", fg="#565959"
            ).pack(side="right")
            riga_corrente += 1

            for index, prodotto in enumerate(prodotti_categoria):
                riga, colonna = divmod(index, colonne)
                card = tk.Frame(
                    self.grid_frame, bg="white",
                    highlightbackground="#d5d9d9", highlightthickness=1,
                    padx=13, pady=14
                )
                card.grid(
                    row=riga_corrente + riga, column=colonna,
                    sticky="nsew", padx=6, pady=6
                )
                self.create_product_card(card, prodotto, larghezza_testo)
            riga_corrente += (len(prodotti_categoria) + colonne - 1) // colonne

    def create_product_card(self, card, product, larghezza_testo=280):
        """Scheda prodotto con immagine grande, testi leggibili e tasto in basso."""
        zona_immagine = tk.Frame(card, bg="white", height=235)
        zona_immagine.pack(fill="x", pady=(0, 12))
        zona_immagine.pack_propagate(False)

        image_label = tk.Label(
            zona_immagine,
            text="Immagine non disponibile",
            bg="white", fg="#666666",
            wraplength=larghezza_testo
        )
        image_label.pack(expand=True)

        image_data = product.get("img")
        if image_data:
            try:
                image = Image.open(BytesIO(bytes(image_data)))
                image.thumbnail(
                    (min(285, larghezza_testo), 225),
                    Image.Resampling.LANCZOS
                )
                photo = ImageTk.PhotoImage(image)
                image_label.configure(image=photo, text="")
                image_label.image = photo
                self.images.append(photo)
            except (OSError, ValueError, TypeError):
                pass

        tk.Label(
            card, text=str(product.get("label") or ""),
            font=("Arial", 12, "bold"),
            bg="white", fg="#007185",
            wraplength=larghezza_testo,
            justify="left", anchor="w"
        ).pack(fill="x", anchor="w", pady=(0, 8))

        try:
            stelle = float(product.get("stelline") or 0)
        except (TypeError, ValueError):
            stelle = 0
        piene = max(0, min(5, round(stelle)))
        tk.Label(
            card,
            text=f"{'★' * piene}{'☆' * (5 - piene)}   {stelle:.1f}/5",
            font=("Arial", 11), bg="white", fg="#c45500"
        ).pack(anchor="w", pady=(0, 5))

        categorie_prodotto = [
            cat["nome"] for cat in self.categories
            if cat["id"] in self.product_category_ids.get(product["id"], set())
        ]
        tk.Label(
            card,
            text="Categoria: " + (", ".join(categorie_prodotto) if categorie_prodotto else "Senza categoria"),
            font=("Arial", 9), bg="white", fg="#565959",
            wraplength=larghezza_testo, justify="left", anchor="w"
        ).pack(fill="x", anchor="w", pady=(0, 5))

        prezzo = formatta_prezzo(product.get("prezzo_cat"))
        tk.Label(
            card, text=prezzo,
            font=("Arial", 21), bg="white", fg=TESTO
        ).pack(anchor="w", pady=(0, 7))

        tk.Label(
            card, text=f"Marca: {product.get('marca') or ''}",
            font=("Arial", 10), bg="white", fg="#565959",
            wraplength=larghezza_testo, justify="left"
        ).pack(anchor="w", pady=(0, 4))

        try:
            disponibile = int(product.get("qta_mag") or 0)
        except (TypeError, ValueError):
            disponibile = 0
        tk.Label(
            card,
            text=f"Disponibilità: {disponibile}" if disponibile > 0 else "Non disponibile",
            font=("Arial", 10), bg="white",
            fg="#067d62" if disponibile > 0 else "#b12704"
        ).pack(anchor="w", pady=(0, 8))

        # I testi restano completi, senza tagli o puntini sospensivi.
        tk.Label(
            card, text=str(product.get("descrizione") or ""),
            font=("Arial", 10), bg="white", fg=TESTO,
            wraplength=larghezza_testo,
            justify="left", anchor="nw"
        ).pack(fill="x", anchor="w", pady=(0, 8))

        tk.Label(
            card, text=f"Tag: {product.get('tag') or ''}",
            font=("Arial", 9), bg="white", fg="#565959",
            wraplength=larghezza_testo,
            justify="left", anchor="w"
        ).pack(fill="x", anchor="w", pady=(0, 10))

        AmazonButton(
            card,
            text="Aggiungi al carrello" if disponibile else "Non disponibile",
            variant="primary", height=30,
            state="normal" if disponibile > 0 else "disabled",
            command=lambda p=product: self.add_to_cart(p)
        ).pack(side="bottom", fill="x", pady=(4, 0))

    # --------------------------------------------------
    # NAVIGAZIONE
    # --------------------------------------------------

    def navigation_click(self, voce):
        if voce == "Tutte le categorie":
            self.clear_filters()

        elif voce == "Offerte":
            self.clear_filters()
            messagebox.showinfo(
                "Offerte",
                "Puoi consultare tutti gli articoli del database."
            )

        elif voce == "I tuoi articoli":
            self.show_cart()

    # --------------------------------------------------
    # LOGIN E ACCOUNT UTENTE (MySQL)
    # --------------------------------------------------

    def show_account(self):
        """Il pulsante Account apre il login o i dati dell'utente connesso."""
        if self.user_id is None:
            self.show_login()
            return
        if not self._account_ancora_abilitato():
            return

        finestra = tk.Toplevel(self.root)
        finestra.title("Il tuo account - Ales Commerce")
        finestra.geometry("440x335")
        finestra.resizable(False, False)
        finestra.configure(bg="white")
        finestra.transient(self.root)

        tk.Label(
            finestra, text="Il tuo account", bg="white", fg=TESTO,
            font=("Arial", 19, "bold")
        ).pack(anchor="w", padx=28, pady=(25, 17))
        tk.Label(
            finestra, text=f"Email: {self.user_email}",
            bg="white", fg=TESTO, font=("Arial", 11)
        ).pack(anchor="w", padx=28, pady=4)
        tk.Label(
            finestra, text=f"ID utente: {self.user_id}",
            bg="white", fg="#067d62", font=("Arial", 11, "bold")
        ).pack(anchor="w", padx=28, pady=(4, 22))
        AmazonButton(
            finestra, text="Esci dall'account", variant="secondary", width=380,
            command=lambda: self.logout(finestra)
        ).pack(padx=28, fill="x", pady=(0, 12))

        AmazonButton(
            finestra, text="Disattiva il mio account", variant="danger", width=380,
            command=lambda: self.disattiva_account(finestra)
        ).pack(padx=28, fill="x")

    def disattiva_account(self, finestra):
        """Disattiva l'account attualmente autenticato, solo dopo conferma."""
        if self.user_id is None:
            messagebox.showwarning(
                "Accesso richiesto", "Effettua il login per gestire il tuo account.",
                parent=finestra
            )
            return

        confermato = messagebox.askyesno(
            "Conferma disattivazione",
            "Vuoi davvero disattivare il tuo account?\n\n"
            "Non potrai più effettuare il login finché un amministratore "
            "non riattiverà il tuo account.",
            icon="warning", parent=finestra
        )
        if not confermato:
            return

        self.stampa_tutti_utenti("prima della disattivazione")
        conn = None
        cursor = None
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            # L'ID deriva dalla sessione autenticata, non da un campo libero.
            cursor.execute(
                f"UPDATE {USERS_TABLE} SET in_enabled = 0 "
                "WHERE id = %s AND in_enabled <> 0",
                (self.user_id,)
            )
            aggiornati = cursor.rowcount
            conn.commit()
            self.stampa_tutti_utenti("dopo la disattivazione")
        except mysql.connector.Error as error:
            if conn is not None:
                conn.rollback()
            messagebox.showerror(
                "Errore disattivazione",
                f"Non è stato possibile disattivare l'account.\n{error}",
                parent=finestra
            )
            return
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                conn.close()

        if aggiornati == 0:
            messagebox.showwarning(
                "Account non modificato",
                "L'account risulta già disabilitato oppure non è più presente.",
                parent=finestra
            )
            self.logout(finestra)
            return

        self.logout(finestra)
        messagebox.showinfo(
            "Account disattivato",
            "Il tuo account è stato disattivato. Non potrai più accedere "
            "finché un amministratore non lo riattiverà.",
            parent=self.root
        )

    def _finestra_accesso(self, title, size="455x430"):
        """Costruisce una pagina di accesso indipendente dalla home."""
        if self.login_window is not None and self.login_window.winfo_exists():
            self.login_window.destroy()
        finestra = tk.Toplevel(self.root)
        self.login_window = finestra
        finestra.title(title)
        finestra.geometry(size)
        finestra.resizable(False, False)
        finestra.configure(bg="#ffffff")
        finestra.transient(self.root)
        finestra.grab_set()
        def chiudi_accesso():
            self._login_redirect_to_cart = False
            self.login_window = None
            finestra.destroy()

        finestra.protocol("WM_DELETE_WINDOW", chiudi_accesso)
        return finestra

    def _campo_accesso(self, parent, label, variable, password=False):
        tk.Label(
            parent, text=label, bg="white", fg=TESTO,
            font=("Arial", 10, "bold")
        ).pack(anchor="w", pady=(13, 5))
        entry = tk.Entry(
            parent, textvariable=variable, font=("Arial", 12),
            relief="solid", bd=1, show="●" if password else ""
        )
        entry.pack(fill="x", ipady=6)
        return entry

    def show_login(self, open_cart_after=False):
        """Apri l'accesso; se richiesto dal carrello, aprilo dopo il login."""
        if self.user_id is not None:
            if open_cart_after:
                self.show_cart()
            else:
                self.show_account()
            return

        self._login_redirect_to_cart = bool(open_cart_after)
        finestra = self._finestra_accesso("Accedi - Ales Commerce", "455x400")
        area = tk.Frame(finestra, bg="white", padx=35, pady=20)
        area.pack(fill="both", expand=True)
        tk.Label(
            area, text="Accedi", bg="white", fg=TESTO,
            font=("Arial", 22, "bold")
        ).pack(anchor="w")

        email = tk.StringVar()
        password = tk.StringVar()
        email_entry = self._campo_accesso(area, "Indirizzo email", email)
        password_entry = self._campo_accesso(area, "Password", password, True)

        mostra = tk.BooleanVar(value=False)
        tk.Checkbutton(
            area, text="Mostra password", variable=mostra,
            bg="white", activebackground="white", anchor="w",
            command=lambda: password_entry.config(show="" if mostra.get() else "●")
        ).pack(anchor="w", pady=(5, 10))

        def entra(event=None):
            indirizzo = email.get().strip().lower()
            segreto = password.get()
            password.set("")
            self._esegui_login(indirizzo, segreto, finestra)

        AmazonButton(
            area, text="Accedi", variant="primary", width=370,
            command=entra
        ).pack(fill="x", pady=(4, 15))
        password_entry.bind("<Return>", entra)
        email_entry.bind("<Return>", lambda event: password_entry.focus_set())

        tk.Label(
            area, text="Non hai ancora un account?", bg="white", fg="#565959",
            font=("Arial", 10)
        ).pack(anchor="center")
        AmazonButton(
            area, text="Crea un account", variant="secondary", width=370,
            command=self.show_registration
        ).pack(fill="x", pady=(8, 0))
        email_entry.focus_set()

    def _esegui_login(self, email, password, finestra):
        if not email_valida(email) or not password:
            self.stampa_tutti_utenti("tentativo di login con dati incompleti")
            messagebox.showwarning(
                "Dati mancanti", "Inserisci un'email valida e la password.",
                parent=finestra
            )
            return

        conn = None
        cursor = None
        esito_login = "login non riuscito"
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor(dictionary=True)
            cursor.execute(
                f"SELECT id, email, password, in_enabled FROM {USERS_TABLE} "
                "WHERE email = %s LIMIT 1", (email,)
            )
            utente = cursor.fetchone()
            if not utente or not verifica_password_database(
                password, utente.get("password")
            ):
                messagebox.showerror(
                    "Accesso non riuscito", "Email o password non corretti.",
                    parent=finestra
                )
                return

            # Un account disabilitato non può accedere né aprire il carrello.
            if int(utente.get("in_enabled") or 0) == 0:
                esito_login = "login negato: account disabilitato"
                messagebox.showerror(
                    "Account disabilitato", "L'utente è stato disabilitato.",
                    parent=finestra
                )
                return

            # L'ID vero è preso dal server, non inserito dall'utente.
            self.user_id = int(utente["id"])
            self.user_email = utente["email"]
            esito_login = f"login riuscito (ID {self.user_id})"
            self.account_text.set(f"Ciao, {self.user_email.split('@')[0]}\nIl tuo account")
            finestra.destroy()
            apri_carrello = self._login_redirect_to_cart
            self._login_redirect_to_cart = False
            if apri_carrello:
                self.show_cart()
            else:
                messagebox.showinfo(
                    "Accesso effettuato", f"Accesso riuscito! ID utente: {self.user_id}",
                    parent=self.root
                )
        except mysql.connector.Error as error:
            if getattr(error, "errno", None) == 1146:
                dettaglio = (
                    "La tabella 'utenti' non esiste sul server. "
                    "Contatta l'amministratore: la registrazione "
                    "è temporaneamente disabilitata."
                )
            else:
                dettaglio = f"Impossibile verificare l'accesso sul server MySQL.\n{error}"
            messagebox.showerror("Errore database", dettaglio, parent=finestra)
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                conn.close()
            self.stampa_tutti_utenti(esito_login)

    def show_registration(self):
        finestra = self._finestra_accesso("Crea account - Ales Commerce", "455x470")
        area = tk.Frame(finestra, bg="white", padx=35, pady=20)
        area.pack(fill="both", expand=True)
        tk.Label(
            area, text="Crea account", bg="white", fg=TESTO,
            font=("Arial", 21, "bold")
        ).pack(anchor="w")

        email = tk.StringVar()
        password = tk.StringVar()
        conferma = tk.StringVar()
        email_entry = self._campo_accesso(area, "Indirizzo email", email)
        self._campo_accesso(area, "Password (minimo 8 caratteri)", password, True)
        self._campo_accesso(area, "Conferma password", conferma, True)

        def registra():
            indirizzo = email.get().strip().lower()
            segreto = password.get()
            conferma_segreto = conferma.get()
            password.set("")
            conferma.set("")
            self._registra_utente(indirizzo, segreto, conferma_segreto, finestra)

        AmazonButton(
            area, text="Crea account", variant="primary", width=370,
            command=registra
        ).pack(fill="x", pady=(25, 12))
        AmazonButton(
            area, text="Torna al login", variant="secondary", width=370,
            command=lambda: self.show_login(
                open_cart_after=self._login_redirect_to_cart
            )
        ).pack(fill="x")
        email_entry.focus_set()

    def stampa_account_database(self, cursor, momento):
        """Stampa gli utenti e il valore del campo password così com’è nel database."""
        cursor.execute(
            f"SELECT id, email, password, in_enabled FROM {USERS_TABLE} ORDER BY id"
        )
        account = cursor.fetchall()
        utenti = []
        for riga in account:
            if isinstance(riga, dict):
                id_utente = riga.get("id")
                email = riga.get("email")
                password = riga.get("password")
                abilitato = riga.get("in_enabled")
            else:
                id_utente, email, password, abilitato = riga

            # Il contenuto del campo password è riportato senza mascheratura.
            # Se contiene un hash PBKDF2 viene mostrato l'hash, non la password originaria.
            if password is None:
                password_visibile = "(NULL)"
            elif isinstance(password, (bytes, bytearray)):
                password_visibile = password.decode("utf-8", errors="replace")
            else:
                password_visibile = str(password)

            try:
                stato = "Abilitato" if int(abilitato) != 0 else "Disabilitato"
            except (ValueError, TypeError):
                stato = "Sconosciuto"
            utenti.append((
                str(id_utente), str(email), password_visibile,
                str(abilitato), stato
            ))

        larghezza_email = min(80, max([20] + [len(r[1]) for r in utenti]))
        larghezza_password = max(15, max((len(r[2]) for r in utenti), default=0))
        larghezze = (6, larghezza_email, larghezza_password, 12, 13)
        separatore = "+" + "+".join("-" * (n + 2) for n in larghezze) + "+"
        print(f"\nACCOUNT DATABASE - {momento.upper()} ({len(utenti)} utenti)", flush=True)
        print(separatore, flush=True)
        print(
            f"| {'ID':<6} | {'Email':<{larghezza_email}} | "
            f"{'Password':<{larghezza_password}} | {'in_enabled':<12} | {'Stato':<13} |",
            flush=True
        )
        print(separatore, flush=True)
        for identita, email, password_visibile, enabled, stato in utenti:
            print(
                f"| {identita:<6} | {email[:larghezza_email]:<{larghezza_email}} | "
                f"{password_visibile:<{larghezza_password}} | {enabled:<12} | {stato:<13} |",
                flush=True
            )
        print(separatore, flush=True)
        if not utenti:
            print("Nessun account presente nel database.", flush=True)
        print("(Valori del campo password come memorizzati nel database.)\n", flush=True)

    def stampa_tutti_utenti(self, momento):
        """Legge e stampa tutti gli utenti; errori di log non bloccano l'app."""
        conn = None
        cursor = None
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            self.stampa_account_database(cursor, momento)
        except mysql.connector.Error as error:
            print(
                f"\n[UTENTI] Impossibile stampare la tabella ({momento}): {error}\n",
                flush=True
            )
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                conn.close()

    def _registra_utente(self, email, password, conferma, finestra):
        """Crea l'account nella tabella utenti e assegna l'ID via AUTO_INCREMENT."""
        email = email.strip().lower()
        if not email_valida(email):
            messagebox.showwarning(
                "Email non valida", "Inserisci un indirizzo email valido.",
                parent=finestra
            )
            return
        if len(password) < 8 or len(password) > 128:
            messagebox.showwarning(
                "Password non valida", "La password deve contenere da 8 a 128 caratteri.",
                parent=finestra
            )
            return
        if password != conferma:
            messagebox.showwarning(
                "Password diverse", "Le due password non coincidono.",
                parent=finestra
            )
            return

        self.stampa_tutti_utenti("prima della registrazione")
        conn = None
        cursor = None
        registrato = False
        nuovo_id = None
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()

            cursor.execute(
                f"SELECT id FROM {USERS_TABLE} WHERE email = %s LIMIT 1",
                (email,)
            )
            if cursor.fetchone() is not None:
                messagebox.showwarning(
                    "Email già registrata",
                    "Esiste già un account con questo indirizzo email. Effettua il login.",
                    parent=finestra
                )
                return

            # PBKDF2 con salt casuale, usando il campo `password` già esistente.
            password_hash = crea_hash_password(password)
            cursor.execute(
                f"INSERT INTO {USERS_TABLE} (email, password, in_enabled) "
                "VALUES (%s, %s, %s)",
                (email, password_hash, 1)
            )
            nuovo_id = cursor.lastrowid
            conn.commit()
            registrato = True
            # Query indipendente dopo il COMMIT: mostra l'account creato.
            self.stampa_tutti_utenti("dopo la registrazione")

        except mysql.connector.IntegrityError as error:
            if conn is not None:
                conn.rollback()
            if getattr(error, "errno", None) == 1062:
                messagebox.showwarning(
                    "Email già registrata",
                    "Esiste già un account con questo indirizzo email.",
                    parent=finestra
                )
            else:
                messagebox.showerror(
                    "Registrazione fallita",
                    "Impossibile creare l'account. Verifica i dati con l'amministratore.",
                    parent=finestra
                )
        except mysql.connector.Error as error:
            if conn is not None:
                conn.rollback()
            messagebox.showerror(
                "Errore database",
                f"Registrazione non riuscita sul server MySQL.\n{error}",
                parent=finestra
            )
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                conn.close()

        if registrato:
            messagebox.showinfo(
                "Account creato",
                f"Registrazione completata! Il tuo ID utente è {nuovo_id}.\n"
                "Ora puoi effettuare l'accesso.",
                parent=finestra
            )
            # Se l'utente proveniva dal carrello, conserva il reindirizzamento.
            self.show_login(open_cart_after=self._login_redirect_to_cart)

    def _account_ancora_abilitato(self):
        """Ricontrolla l'abilitazione sul server per le sessioni già aperte."""
        if self.user_id is None:
            return False

        conn = None
        cursor = None
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor(dictionary=True)
            cursor.execute(
                f"SELECT in_enabled FROM {USERS_TABLE} WHERE id = %s LIMIT 1",
                (self.user_id,)
            )
            utente = cursor.fetchone()
            if utente is None:
                self.logout()
                messagebox.showerror(
                    "Account non trovato", "L'account non esiste più.",
                    parent=self.root
                )
                return False

            if int(utente.get("in_enabled") or 0) == 0:
                self.logout()
                messagebox.showerror(
                    "Account disabilitato", "L'utente è stato disabilitato.",
                    parent=self.root
                )
                return False
            return True
        except mysql.connector.Error as error:
            messagebox.showerror(
                "Verifica account",
                f"Impossibile verificare se l'utente è abilitato.\n{error}",
                parent=self.root
            )
            return False
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                conn.close()

    def logout(self, finestra=None):
        # Nessun carrello già aperto deve restare visibile dopo il logout.
        for cart_window in list(self.cart_windows):
            if cart_window.winfo_exists():
                cart_window.destroy()
        self.cart_windows.clear()
        # Il carrello appartiene alla sessione: non mostrarlo a un altro account.
        self.cart.clear()
        self.saved_for_later.clear()
        self.gift_var.set(False)
        self.update_cart_counter()
        self.user_id = None
        self.user_email = None
        self._login_redirect_to_cart = False
        self.account_text.set("Ciao, accedi\nAccount e liste")
        if finestra is not None and finestra.winfo_exists():
            finestra.destroy()
        self.stampa_tutti_utenti("logout")

    # --------------------------------------------------
    # SCORRIMENTO
    # --------------------------------------------------

    def update_scroll_region(self, event=None):
        self.canvas.configure(
            scrollregion=self.canvas.bbox("all")
        )

    def update_grid_width(self, event):
        # La finestra interna deve avere la stessa larghezza del Canvas:
        # questo impedisce alla griglia di restare stretta a sinistra.
        self.canvas.itemconfigure(self.grid_window, width=event.width)

        if ((self.visible_products or self.categories) and
                abs(event.width - self._last_render_width) >= 45):
            if self._home_resize_job is not None:
                self.root.after_cancel(self._home_resize_job)
            self._home_resize_job = self.root.after(120, self._refresh_home_layout)

    def _on_main_window_destroy(self, event):
        if event.widget is self.root and self._home_resize_job is not None:
            try:
                self.root.after_cancel(self._home_resize_job)
            except tk.TclError:
                pass
            self._home_resize_job = None

    def _refresh_home_layout(self):
        self._home_resize_job = None
        posizione = self.canvas.yview()[0]
        self._render_home_products()
        self.root.after_idle(lambda: self.canvas.yview_moveto(posizione))

    def bind_mousewheel(self, event):
        self.canvas.bind_all(
            "<MouseWheel>",
            self.mousewheel
        )

    def unbind_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")

    def mousewheel(self, event):
        self.canvas.yview_scroll(
            int(-event.delta / 120),
            "units"
        )

    
    # --------------------------------------------------
    # CARRELLO STILE AMAZON
    # --------------------------------------------------

    def add_to_cart(self, product):
        product_id = product["id"]

        try:
            disponibile = int(product.get("qta_mag") or 0)
        except (TypeError, ValueError):
            disponibile = 0

        quantita = self.cart.get(product_id, {}).get("quantita", 0)

        if quantita >= disponibile:
            messagebox.showwarning(
                "Quantità non disponibile",
                "Hai raggiunto la quantità disponibile in magazzino."
            )
            return

        if product_id not in self.cart:
            self.cart[product_id] = {
                "prodotto": product,
                "quantita": 0
            }

        self.cart[product_id]["quantita"] += 1

        # Se era salvato per dopo, lo rimuove da quella lista
        self.saved_for_later.pop(product_id, None)

        self.update_cart_counter()
        self.results_text.set(
            f"Aggiunto al carrello: {product.get('label', '')}"
        )

    def update_cart_counter(self):
        totale = sum(
            item["quantita"] for item in self.cart.values()
        )
        self.cart_text.set(f"Carrello ({totale})")

    def show_cart(self, scroll_fraction=None, jump_to_saved=False, existing_window=None):
        # Il carrello è accessibile esclusivamente agli utenti autenticati.
        if self.user_id is None:
            self.show_login(open_cart_after=True)
            return
        if not self._account_ancora_abilitato():
            return

        if existing_window is not None and existing_window.winfo_exists():
            # Riusiamo LA STESSA finestra: niente salto sul desktop dopo + / -.
            finestra = existing_window
            for widget in finestra.winfo_children():
                widget.destroy()
        else:
            finestra = tk.Toplevel(self.root)
            self.cart_windows.add(finestra)
            finestra.bind(
                "<Destroy>",
                lambda event, window=finestra: self.cart_windows.discard(window)
                if event.widget is window else None
            )
            finestra.title("Carrello")
            finestra.geometry("1250x750")
            finestra.minsize(900, 550)
            finestra.configure(bg="#eaeded")

        # Conserva le immagini finché la finestra è aperta
        finestra.cart_images = []

        # ---------------- INTESTAZIONE ----------------

        header = tk.Frame(finestra, bg="#131921", height=55)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="ales",
            font=("Arial", 23, "bold"),
            bg="#131921",
            fg="white"
        ).pack(side="left", padx=20)

        tk.Label(
            header,
            text=".commerce  |  Carrello",
            font=("Arial", 12),
            bg="#131921",
            fg="white"
        ).pack(side="left")

        # ---------------- CORPO ----------------

        body = tk.Frame(finestra, bg="#eaeded")
        body.pack(fill="both", expand=True, padx=18, pady=15)

        body.grid_columnconfigure(0, weight=4)
        body.grid_columnconfigure(1, weight=1)
        body.grid_rowconfigure(0, weight=1)

        
        # AREA SINISTRA SCORREVOLE
        contenitore_sinistro = tk.Frame(body, bg="#eaeded")
        contenitore_sinistro.grid(
            row=0, column=0,
            sticky="nsew",
            padx=(0, 15)
        )

        canvas_sinistro = tk.Canvas(
            contenitore_sinistro,
            bg="#eaeded",
            highlightthickness=0
        )

        scrollbar_sinistra = ttk.Scrollbar(
            contenitore_sinistro,
            orient="vertical",
            command=canvas_sinistro.yview
        )

        canvas_sinistro.configure(
            yscrollcommand=scrollbar_sinistra.set
        )

        scrollbar_sinistra.pack(side="right", fill="y")
        canvas_sinistro.pack(side="left", fill="both", expand=True)

        # Tutto il contenuto del carrello va qui
        sinistra = tk.Frame(canvas_sinistro, bg="#eaeded")

        finestra_sinistra = canvas_sinistro.create_window(
            (0, 0),
            window=sinistra,
            anchor="nw"
        )

        def aggiorna_scroll(event=None):
            canvas_sinistro.configure(
                scrollregion=canvas_sinistro.bbox("all")
            )

        def aggiorna_larghezza(event):
            canvas_sinistro.itemconfigure(
                finestra_sinistra,
                width=event.width
            )

        sinistra.bind("<Configure>", aggiorna_scroll)
        canvas_sinistro.bind("<Configure>", aggiorna_larghezza)

        # Lo scorrimento riguarda tutta la colonna sinistra (carrello + salvati).
        # Il binding sulla finestra raggiunge anche immagini, pulsanti e descrizioni,
        # senza interferire con il canvas dei prodotti nella finestra principale.
        finestra.cart_canvas = canvas_sinistro

        def scorrimento_mouse(event):
            if getattr(event, "num", None) == 4:  # Linux: rotella in su
                spostamento = -3
            elif getattr(event, "num", None) == 5:  # Linux: rotella in giù
                spostamento = 3
            elif getattr(event, "delta", 0):
                spostamento = -int(event.delta / 120)
                if spostamento == 0:
                    spostamento = -1 if event.delta > 0 else 1
            else:
                return
            canvas_sinistro.yview_scroll(spostamento, "units")
            return "break"

        finestra.bind("<MouseWheel>", scorrimento_mouse)
        finestra.bind("<Button-4>", scorrimento_mouse)
        finestra.bind("<Button-5>", scorrimento_mouse)

        destra = tk.Frame(body, bg="#eaeded", width=260)
        destra.grid(row=0, column=1, sticky="new")
        destra.grid_propagate(False)

        # ---------------- RIEPILOGO ORDINE ----------------

        riepilogo = tk.Frame(
            destra,
            bg="white",
            padx=16,
            pady=16
        )
        riepilogo.pack(fill="x", pady=(0, 15))

        tk.Label(
            riepilogo,
            text="Riepilogo ordine",
            font=("Arial", 15, "bold"),
            bg="white",
            fg="#0f1111"
        ).pack(anchor="w", pady=(0, 12))

        tk.Label(
            riepilogo,
            text="✓ Spedizione gratuita dove prevista",
            font=("Arial", 9),
            bg="white",
            fg="#067d62",
            wraplength=220,
            justify="left"
        ).pack(anchor="w", pady=(0, 12))

        totale = sum(
            (importo_decimale(item["prodotto"].get("prezzo_cat") or 0)
             * item["quantita"])
            for item in self.cart.values()
        )

        numero_articoli = sum(
            item["quantita"] for item in self.cart.values()
        )

        totale_label = tk.Label(
            riepilogo,
            text=f"Totale provvisorio ({numero_articoli} articoli): "
                 f"{formatta_prezzo(totale)}",
            font=("Arial", 13, "bold"),
            bg="white",
            fg="#0f1111",
            wraplength=225,
            justify="left"
        )
        totale_label.pack(anchor="w", pady=(0, 10))

        regalo_check = tk.Checkbutton(
            riepilogo,
            text="Questo ordine contiene un regalo",
            variable=self.gift_var,
            bg="white",
            activebackground="white",
            wraplength=220,
            justify="left"
        )
        regalo_check.pack(anchor="w", pady=(0, 12))

        AmazonButton(
            riepilogo, text="Procedi all'ordine",
            variant="primary",
            command=lambda: self.proceed_checkout(finestra)
        ).pack(fill="x")

        tk.Label(
            riepilogo,
            text="Nessun pagamento verrà effettuato da questa demo.",
            font=("Arial", 8),
            bg="white",
            fg="#565959",
            wraplength=220,
            justify="left"
        ).pack(anchor="w", pady=(10, 0))

        # ---------------- PANNELLO ARTICOLI ----------------

        prodotti_box = tk.Frame(sinistra, bg="white", padx=18, pady=15)
        prodotti_box.pack(fill="both", expand=True)

        tk.Label(
            prodotti_box,
            text="Carrello",
            font=("Arial", 21),
            bg="white",
            fg="#0f1111"
        ).pack(anchor="w", pady=(0, 10))

        tk.Label(
            prodotti_box,
            text="Prezzo",
            font=("Arial", 9),
            bg="white",
            fg="#565959"
        ).pack(anchor="e")

        ttk.Separator(prodotti_box).pack(fill="x", pady=5)

        lista = tk.Frame(prodotti_box, bg="white")
        lista.pack(fill="x", expand=True)

        # ---------------- ARTICOLI NEL CARRELLO ----------------

        if not self.cart:
            tk.Label(
                lista,
                text="Il carrello è vuoto.",
                font=("Arial", 13),
                bg="white"
            ).pack(anchor="w", pady=20)

        for product_id, item in list(self.cart.items()):
            product = item["prodotto"]
            quantita = item["quantita"]

            prezzo = importo_decimale(product.get("prezzo_cat") or 0)
            subtotale = prezzo * quantita

            riga = tk.Frame(lista, bg="white", pady=12)
            riga.pack(fill="x")

            # Immagine
            image_label = tk.Label(
                riga,
                text="Immagine\nnon disponibile",
                bg="white",
                width=18,
                height=8
            )
            image_label.pack(side="left", padx=(0, 15), anchor="n")

            image_data = product.get("img")

            if image_data:
                try:
                    image = Image.open(BytesIO(image_data))
                    image.thumbnail((150, 155))
                    photo = ImageTk.PhotoImage(image)

                    image_label.configure(image=photo, text="")
                    image_label.image = photo
                    finestra.cart_images.append(photo)

                except Exception:
                    pass

            # Informazioni
            info = tk.Frame(riga, bg="white")
            info.pack(side="left", fill="both", expand=True)

            tk.Label(
                info,
                text=product.get("label", ""),
                font=("Arial", 12, "bold"),
                bg="white",
                fg="#007185",
                wraplength=450,
                justify="left",
                anchor="w"
            ).pack(anchor="w", fill="x")

            tk.Label(
                info,
                text=f"Marca: {product.get('marca', '')}",
                font=("Arial", 9),
                bg="white",
                fg="#565959"
            ).pack(anchor="w", pady=(5, 0))

            tk.Label(
                info,
                text=f"Disponibilità immediata: {product.get('qta_mag', 0)}",
                font=("Arial", 9),
                bg="white",
                fg="#067d62"
            ).pack(anchor="w", pady=3)

            tk.Label(
                info,
                text=product.get("descrizione", ""),
                font=("Arial", 9),
                bg="white",
                fg="#0f1111",
                wraplength=450,
                justify="left",
                anchor="w"
            ).pack(anchor="w", fill="x", pady=(3, 8))

            # Pulsanti quantità e azioni
            azioni = tk.Frame(info, bg="white")
            azioni.pack(anchor="w", pady=(5, 0))

            quantita_frame = tk.Frame(
                azioni,
                bg="white",
                highlightthickness=0
            )
            quantita_frame.pack(side="left", padx=(0, 10))

            AmazonButton(
                quantita_frame, text="−", width=34,
                variant="secondary",
                command=lambda pid=product_id, win=finestra:
                    self.change_cart_quantity(pid, -1, win)
            ).pack(side="left")

            tk.Label(
                quantita_frame,
                text=str(quantita),
                width=3,
                bg="white",
                font=("Arial", 10, "bold")
            ).pack(side="left")

            AmazonButton(
                quantita_frame, text="+", width=34,
                variant="secondary",
                command=lambda pid=product_id, win=finestra:
                    self.change_cart_quantity(pid, 1, win)
            ).pack(side="left")

            AmazonButton(
                azioni, text="Rimuovi", width=90, variant="secondary",
                command=lambda pid=product_id, win=finestra:
                    self.remove_from_cart(pid, win)
            ).pack(side="left", padx=3)

            AmazonButton(
                azioni, text="Salva per dopo", width=122, variant="secondary",
                command=lambda pid=product_id, win=finestra:
                    self.save_for_later(pid, win)
            ).pack(side="left", padx=3)

            AmazonButton(
                azioni, text="Condividi", width=95, variant="secondary",
                command=lambda p=product: self.share_product(p)
            ).pack(side="left", padx=3)

            # Prezzo a destra
            tk.Label(
                riga,
                text=formatta_prezzo(subtotale),
                font=("Arial", 12, "bold"),
                bg="white",
                fg="#0f1111"
            ).pack(side="right", padx=(10, 0), anchor="n")

            ttk.Separator(lista).pack(fill="x", pady=5)

        # ---------------- SALVATI PER DOPO ----------------

        if self.saved_for_later:
            tk.Label(
                sinistra,
                text="Articoli salvati per dopo",
                font=("Arial", 18),
                bg="#eaeded",
                fg="#0f1111"
            ).pack(anchor="w", pady=(18, 10))

            salvati_box = tk.Frame(
                sinistra,
                bg="white",
                padx=18,
                pady=15
            )
            salvati_box.pack(fill="x")

            tk.Label(
                salvati_box,
                text="Prezzo",
                font=("Arial", 9),
                bg="white",
                fg="#565959"
            ).pack(anchor="e")

            ttk.Separator(salvati_box).pack(fill="x", pady=7)

            for product_id, product in list(self.saved_for_later.items()):
                scheda = tk.Frame(
                    salvati_box,
                    bg="white",
                    highlightbackground="#dddddd",
                    highlightthickness=1,
                    padx=12,
                    pady=12
                )
                scheda.pack(fill="x", pady=5)

                # Immagine del prodotto
                image_label = tk.Label(
                    scheda,
                    text="Immagine non disponibile",
                    bg="white",
                    width=20,
                    height=10
                )
                image_label.pack(side="left", padx=(0, 18), anchor="n")

                image_data = product.get("img")

                if image_data:
                    try:
                        image = Image.open(BytesIO(image_data))
                        image.thumbnail((190, 190))

                        photo = ImageTk.PhotoImage(image)
                        image_label.configure(image=photo, text="")
                        image_label.image = photo

                        # Mantiene l'immagine visibile
                        finestra.cart_images.append(photo)

                    except Exception:
                        pass

                # Informazioni prodotto
                info = tk.Frame(scheda, bg="white")
                info.pack(side="left", fill="both", expand=True)

                tk.Label(
                    info,
                    text=product.get("label", ""),
                    font=("Arial", 12),
                    bg="white",
                    fg="#007185",
                    wraplength=280,
                    justify="left",
                    anchor="w"
                ).pack(anchor="w", fill="x", pady=(0, 6))

                prezzo_testo = formatta_prezzo(product.get("prezzo_cat"))

                tk.Label(
                    info,
                    text=prezzo_testo,
                    font=("Arial", 17, "bold"),
                    bg="white",
                    fg="#0f1111"
                ).pack(anchor="w", pady=(0, 7))

                tk.Label(
                    info,
                    text=("Disponibilità immediata" if int(product.get("qta_mag") or 0) > 0
                          else "Attualmente non disponibile"),
                    font=("Arial", 9),
                    bg="white",
                    fg=("#067d62" if int(product.get("qta_mag") or 0) > 0
                        else "#b12704")
                ).pack(anchor="w", pady=2)

                tk.Label(
                    info,
                    text=f"Marca: {product.get('marca', '')}",
                    font=("Arial", 9),
                    bg="white",
                    fg="#0f1111"
                ).pack(anchor="w", pady=2)

                tk.Label(
                    info,
                    text=f"Quantità disponibile: {product.get('qta_mag', 0)}",
                    font=("Arial", 9),
                    bg="white",
                    fg="#0f1111"
                ).pack(anchor="w", pady=2)

                tk.Label(
                    info,
                    text=product.get("descrizione", ""),
                    font=("Arial", 9),
                    bg="white",
                    fg="#0f1111",
                    wraplength=280,
                    justify="left",
                    anchor="w"
                ).pack(anchor="w", fill="x", pady=(6, 10))

                # Pulsanti azione
                AmazonButton(
                    info, text="Sposta nel carrello", variant="secondary",
                    command=lambda pid=product_id, win=finestra:
                        self.move_back_to_cart(pid, win)
                ).pack(fill="x", pady=(3, 6))

                AmazonButton(
                    info, text="Rimuovi", variant="secondary", width=110,
                    command=lambda pid=product_id, win=finestra:
                        self.remove_saved_product(pid, win)
                ).pack(anchor="w")

        # Scorri fino ai salvati se un prodotto è appena stato spostato;
        # altrimenti mantieni la posizione dopo modifiche/rimozioni.
        def ripristina_posizione():
            if not canvas_sinistro.winfo_exists():
                return
            canvas_sinistro.update_idletasks()
            aggiorna_scroll()
            if jump_to_saved and self.saved_for_later:
                altezza = max(1, sinistra.winfo_reqheight())
                posizione = salvati_box.winfo_y() / altezza
                canvas_sinistro.yview_moveto(posizione)
            elif scroll_fraction is not None:
                canvas_sinistro.yview_moveto(scroll_fraction)

        finestra.after_idle(ripristina_posizione)

        # Riferimento alle immagini
        self.cart_images = finestra.cart_images

    def refresh_cart_window(self, finestra, jump_to_saved=False):
        if not finestra.winfo_exists():
            return
        posizione = 0.0
        if hasattr(finestra, "cart_canvas") and finestra.cart_canvas.winfo_exists():
            posizione = finestra.cart_canvas.yview()[0]
        # Non distruggiamo il Toplevel: resta nella medesima posizione/dimensione.
        self.show_cart(
            scroll_fraction=posizione,
            jump_to_saved=jump_to_saved,
            existing_window=finestra
        )

    def remove_saved_product(self, product_id, finestra):
        self.saved_for_later.pop(product_id, None)
        self.refresh_cart_window(finestra)

    # --------------------------------------------------
    # MODIFICA QUANTITÀ
    # --------------------------------------------------

    def change_cart_quantity(self, product_id, variazione, finestra):
        if product_id not in self.cart:
            return

        item = self.cart[product_id]
        nuova_quantita = item["quantita"] + variazione

        if nuova_quantita <= 0:
            del self.cart[product_id]

        else:
            try:
                disponibile = int(
                    item["prodotto"].get("qta_mag") or 0
                )
            except (TypeError, ValueError):
                disponibile = 0

            if nuova_quantita > disponibile:
                messagebox.showwarning(
                    "Quantità non disponibile",
                    f"Sono disponibili solo {disponibile} unità."
                )
                return

            item["quantita"] = nuova_quantita

        self.update_cart_counter()
        self.refresh_cart_window(finestra)

    # --------------------------------------------------
    # RIMUOVI
    # --------------------------------------------------

    def remove_from_cart(self, product_id, finestra):
        self.cart.pop(product_id, None)
        self.update_cart_counter()

        self.refresh_cart_window(finestra)

    # --------------------------------------------------
    # SALVA PER DOPO
    # --------------------------------------------------

    def save_for_later(self, product_id, finestra):
        if product_id in self.cart:
            item = self.cart.pop(product_id)
            self.saved_for_later[product_id] = item["prodotto"]

        self.update_cart_counter()
        self.refresh_cart_window(finestra, jump_to_saved=True)

    def move_back_to_cart(self, product_id, finestra):
        if product_id not in self.saved_for_later:
            return

        product = self.saved_for_later[product_id]

        try:
            disponibile = int(product.get("qta_mag") or 0)
        except (TypeError, ValueError):
            disponibile = 0

        if disponibile <= 0:
            messagebox.showwarning(
                "Non disponibile",
                "Questo prodotto non è disponibile in magazzino."
            )
            return

        self.cart[product_id] = {
            "prodotto": product,
            "quantita": 1
        }

        del self.saved_for_later[product_id]

        self.update_cart_counter()
        self.refresh_cart_window(finestra)

    # --------------------------------------------------
    # CONDIVIDI PRODOTTO
    # --------------------------------------------------

    def share_product(self, product):
        testo = (
            f"{product.get('label', '')}\n"
            f"Marca: {product.get('marca', '')}\n"
            f"Prezzo: {formatta_prezzo(product.get('prezzo_cat'))}\n"
            f"Descrizione: {product.get('descrizione', '')}"
        )

        self.root.clipboard_clear()
        self.root.clipboard_append(testo)
        self.root.update()

        messagebox.showinfo(
            "Condividi",
            "Dettagli del prodotto copiati negli appunti. "
            "Ora puoi incollarli in un messaggio."
        )

    # --------------------------------------------------
    # ACQUISTO CON AGGIORNAMENTO MAGAZZINO MYSQL
    # --------------------------------------------------

    def proceed_checkout(self, finestra):
        if not self.cart:
            messagebox.showwarning(
                "Carrello vuoto", "Aggiungi almeno un articolo prima di procedere.",
                parent=finestra
            )
            return
        if self.user_id is None or not self._account_ancora_abilitato():
            return

        righe = []
        for product_id, item in self.cart.items():
            try:
                quantita = int(item["quantita"])
                articolo_id = int(product_id)
            except (TypeError, ValueError):
                messagebox.showerror("Errore", "Articolo o quantità non validi.", parent=finestra)
                return
            if quantita <= 0 or articolo_id <= 0:
                messagebox.showerror("Errore", "Articolo o quantità non validi.", parent=finestra)
                return
            righe.append((articolo_id, quantita))

        totale = sum(
            importo_decimale(item["prodotto"].get("prezzo_cat") or 0)
            * item["quantita"]
            for item in self.cart.values()
        )
        regalo = "Sì" if self.gift_var.get() else "No"
        numero = sum(q for _, q in righe)
        confermato = messagebox.askyesno(
            "Conferma acquisto",
            f"Articoli: {numero}\n"
            f"Totale indicativo: {formatta_prezzo(totale)}\n"
            f"Regalo: {regalo}\n\n"
            "Confermi l'acquisto e la diminuzione delle quantità disponibili?\n"
            "Attenzione: questa versione non gestisce pagamenti online.",
            parent=finestra
        )
        if not confermato:
            return

        conn = None
        cursor = None
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            conn.start_transaction()
            cursor = conn.cursor(dictionary=True)

            # Verifica lo stato dell'utente nella stessa transazione.
            cursor.execute(
                f"SELECT in_enabled FROM {USERS_TABLE} WHERE id = %s FOR UPDATE",
                (self.user_id,)
            )
            utente = cursor.fetchone()
            if utente is None or int(utente.get("in_enabled") or 0) != 1:
                raise ValueError("L'utente è stato disabilitato o non esiste più.")

            # UPDATE condizionale: anche con acquisti simultanei le quantità
            # non vanno sotto zero. Tutti gli articoli vengono trattati insieme.
            # Ordinare gli ID riduce il rischio di deadlock tra acquisti concorrenti.
            for articolo_id, quantita in sorted(righe):
                cursor.execute(
                    f"UPDATE `{TABLE_NAME}` "
                    "SET qta_mag = qta_mag - %s "
                    "WHERE id = %s AND qta_mag >= %s",
                    (quantita, articolo_id, quantita)
                )
                if cursor.rowcount != 1:
                    raise ValueError(
                        f"Disponibilità insufficiente o articolo {articolo_id} non trovato. "
                        "L'acquisto è stato annullato: nessuna quantità modificata."
                    )

            conn.commit()

        except (mysql.connector.Error, ValueError) as error:
            if conn is not None:
                conn.rollback()
            messagebox.showerror("Acquisto non completato", str(error), parent=finestra)
            return
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                conn.close()

        # Solo dopo COMMIT riuscito aggiorniamo i dati locali e il carrello.
        quantita_acquistate = dict(righe)
        for prodotto in self.products:
            prodotto_id = prodotto.get("id")
            if prodotto_id in quantita_acquistate:
                prodotto["qta_mag"] = max(
                    0, int(prodotto.get("qta_mag") or 0)
                    - quantita_acquistate[prodotto_id]
                )
        self.cart.clear()
        self.gift_var.set(False)
        self.update_cart_counter()
        self.apply_filters()
        if finestra.winfo_exists():
            self.refresh_cart_window(finestra)
        messagebox.showinfo(
            "Acquisto confermato",
            "Acquisto registrato: le quantità nel database MySQL sono state aggiornate.\n"
            "Il carrello è stato svuotato. Nessun pagamento è stato elaborato.",
            parent=finestra if finestra.winfo_exists() else self.root
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = NegozioApp(root)
    root.mainloop()
