import os
def Add(a, b):
    return a + b


def SayHello():
    print("Hello World!")


if __name__ == '__main__':
    SayHello()
    print(os.environ['GCP_CREDENTIALS'])
