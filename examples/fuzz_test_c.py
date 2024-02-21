from boofuzz import *

def main():
    session = Session(target=Target(connection=SocketConnection("127.0.0.1", 26001, proto='tcp')))

    s_initialize(name="Input")
    s_string("FUZZ")

    session.connect(s_get("Input"))
    session.fuzz()

if __name__ == "__main__":
    main()

