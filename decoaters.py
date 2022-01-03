def announce(f):
    def wrapper():
        print("About to run function.")
        f()
        print("Done with the Function.")
    return wrapper

@announce
def hello():
    print("Hello! World")


hello()