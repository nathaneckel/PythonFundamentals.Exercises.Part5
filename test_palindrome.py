import unittest
import palindrome


class PalindromeTest(unittest.TestCase):

    def test_is_palindrome(self):
        test_cases = [
            ("redivider", True),
            ("deified", True),
            ("civic", True),
            ("radar", True),
            ("level", True),
            ("Mr Owl ate my metal worm", True),
            ("Do geese see God", True),
            ("Was it a car or a cat I saw", True),
            ("Murder for a jar of red rum", True),
            ("palindrome", False),
            ("Python", False)
        ]
        for str_in, expected in test_cases:
            with self.subTest(f"{str_in} -> {expected}"):
                self.assertEqual(expected, palindrome.is_palindrome(str_in))

