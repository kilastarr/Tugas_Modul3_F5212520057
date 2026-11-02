from controllers.auth_controller import AuthController

if __name__ == "__main__":
    app = AuthController()
    app.show_login()  # Diubah dari app.run() menjadi app.show_login()