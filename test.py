import unittest
from application import Storage

class TestSuite(unittest.TestCase):
  def test(self):
    storage = Storage()
    storage.populate()
    score = storage.score()
    self.failIf(score != 12345)

def main():
  unittest.main()

if __name__ == "__main__":
  main()
