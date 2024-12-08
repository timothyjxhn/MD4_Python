"""
MD4 Hash Function Test Cases
Minimum Python Version: 3.8

To run the test cases, run the following command:
$ python md4_test.py

All test case results were verified against the following online tool:
https://gchq.github.io/CyberChef/
"""
from md4 import md4
import unittest

class TestMD4(unittest.TestCase):
    def test_empty_string(self):
        string = ""
        self.assertEqual(md4(string, "string"), "31d6cfe0d16ae931b73c59d7e0c089c0")

    def test_a(self):
        string = "hello world"
        self.assertEqual(md4(string, "string"), "aa010fbc1d14c795d86ef98c95479d17")

    def test_abc(self):
        string = "The quick brown fox jumps over the lazy dog"
        self.assertEqual(md4(string, "string"), "1bee69a46ba811185c194762abaeae90")

    def test_message_digest(self):
        string = "message digest"
        self.assertEqual(md4(string, "string"), "d9130a8164549fe818874806e1c7014b")

    def test_alphabet(self):
        string = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(md4(string, "string"), "d79e1c308aa5bbcdeea8ed63df412da9")

    def test_alphanumeric(self):
        string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        self.assertEqual(md4(string, "string"), "043f8582f241db351ce627e153e7f0e4")

    def test_long_numbers(self):
        string = "12345678901234567890123456789012345678901234567890123456789012345678901234567890"
        self.assertEqual(md4(string, "string"), "e33b4ddc9c38f2199c3e7b164fcc0536")


if __name__ == "__main__":
    unittest.main()
