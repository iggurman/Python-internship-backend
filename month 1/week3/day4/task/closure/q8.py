def secret(msg):

    def reveal():
        print(msg)

    return reveal


show = secret("Python is Awesome")

show()