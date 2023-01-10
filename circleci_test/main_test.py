# sys.path.append("")
import os
import sys
from circleci_python.main import Add

sys.path.append(os.path.join("/home/circleci/circleci-demo"))
def TestAdd():
    assert Add(2, 3) == 5
    print("Add Function works correctly")


if __name__ == '__main__':
    TestAdd()
    # print(sys.path)