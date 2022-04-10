from website import create_app

app = create_app()
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


if __name__ == '__main__':
    app.run(debug=True)
