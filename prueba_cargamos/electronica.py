from sitioweb import deploy_app

app = deploy_app()

if __name__ == '__main__':
    app.run(debug= True)
    