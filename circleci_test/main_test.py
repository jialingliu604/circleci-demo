# sys.path.append("")
from ..circleci_python.main import Add



def TestAdd():
    assert Add(2, 3) == 5
    print("Add Function works correctly")


if __name__ == '__main__':
    TestAdd()
    # print(sys.path)