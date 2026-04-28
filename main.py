from tela import MainView
from controller import Controller

if __name__ == "__main__":
    app = MainView()
    Controller(app)
    app.mainloop()