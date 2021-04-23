import unittest
from pathlib import Path
from control_works.test_1.task_3.count_wordstats import count_top_10_words, count_sentences


class TestCountTopWords(unittest.TestCase):
    def test_one_word(self):
        self.assertEqual(count_top_10_words("abcd"), ["abcd"])

    def test_one_repeating_word(self):
        self.assertEqual(count_top_10_words("abcd abcd abcd abcd"), ["abcd"])

    def test_several_words(self):
        self.assertEqual(count_top_10_words("abcd, abcd, cdbs"), ["abcd", "cdbs"])

    def test_with_upper_lower_case(self):
        self.assertEqual(count_top_10_words("Abcd, abcd, Cdbs"), ["abcd", "cdbs"])

    def test_with_digits(self):
        self.assertEqual(count_top_10_words("abcd, ab2cd1, cdbs"), ["abcd", "ab", "cd", "cdbs"])
 
    def test_more_10_different_words(self):
        with open(Path() / "tests" / "test_1" / "task_3" / "resources" / "big_text_file.txt") as input_file:
            self.assertEqual(
                count_top_10_words(input_file.read()),
                ["is", "better", "than", "to", "the", "never", "be", "one", "it", "idea"],
            )


class TestCountSentences(unittest.TestCase):
    def test_one_sentence(self):
        self.assertEqual(count_sentences("Python is the best."), 1)

    def test_no_sentences(self):
        self.assertEqual(count_sentences("blabla"), 0)

    def test_big_text(self):
        with open(Path() / "tests" / "test_1" / "task_3" / "resources" / "big_text_file.txt") as input_file:
            self.assertEqual(count_sentences(input_file.read()), 19)
