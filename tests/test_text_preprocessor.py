import unittest
from modules.text_preprocessor import Preprocessor

class TestPreprocessor(unittest.TestCase):

    def setUp(self):
        self.text = """
        ## Example Title

        Hello, **World!**  
        Visit [OpenAI](https://openai.com) or email us at test@example.com.
        This is a sample text with numbers 123 and punctuation!!!
        """

    def test_lowercase(self):
        p = Preprocessor(to_lowercase=True)
        result = p.preprocess("HeLLo WoRLd")
        self.assertEqual(result, "hello world")

    def test_remove_html_tags(self):
        p = Preprocessor(remove_html_tags=True)
        text = "<p>Hello <b>World</b></p>"
        result = p.preprocess(text)
        self.assertEqual(result.strip(), "Hello World")

    def test_remove_md_tags(self):
        p = Preprocessor(remove_md_tags=True)
        text = "Hello, **World!** [OpenAI](https://openai.com)"
        result = p.preprocess(text)
        self.assertNotIn("**", result)
        self.assertNotIn("(", result)

    def test_remove_urls(self):
        p = Preprocessor(remove_urls=True)
        text = "Visit https://example.com now!"
        result = p.preprocess(text)
        self.assertNotIn("https://example.com", result)

    def test_remove_emails(self):
        p = Preprocessor(remove_emails=True)
        text = "Contact me at test@example.com"
        result = p.preprocess(text)
        self.assertNotIn("test@example.com", result)

    def test_remove_numbers(self):
        p = Preprocessor(remove_numbers=True)
        text = "Version 2.0 released in 2025"
        result = p.preprocess(text)
        self.assertNotRegex(result, r"\d")

    def test_remove_punctuation(self):
        p = Preprocessor(remove_punctuation=True)
        text = "Hello, world!"
        result = p.preprocess(text)
        self.assertEqual(result, "Hello world")

    def test_remove_special_chars(self):
        p = Preprocessor(remove_special_chars=True)
        text = "Hello @world #python!"
        result = p.preprocess(text)
        self.assertNotIn("@", result)
        self.assertNotIn("#", result)

    def test_remove_whitespace(self):
        p = Preprocessor(remove_whitespace=True)
        text = "   Hello   world   "
        result = p.preprocess(text)
        self.assertEqual(result, "Hello world")

    def test_stemming(self):
        p = Preprocessor(stem=True)
        text = "running played tested"
        result = p.preprocess(text)
        # PorterStemmer reduces to base forms
        self.assertIn("run", result)
        self.assertIn("play", result)
        self.assertIn("test", result)

    def test_lemmatization(self):
        p = Preprocessor(lemmatize=True)
        text = "cars feet running"
        result = p.preprocess(text)
        # WordNetLemmatizer should lemmatize to singular/base
        self.assertIn("car", result)
        self.assertIn("foot", result)

    def test_combined_operations(self):
        p = Preprocessor(
            to_lowercase=True,
            remove_html_tags=True,
            remove_md_tags=True,
            remove_urls=True,
            remove_emails=True,
            remove_punctuation=True,
            remove_numbers=True,
            remove_whitespace=True,
            remove_special_chars=True,
        )
        result = p.preprocess(self.text)
        self.assertNotIn("**", result)
        self.assertNotIn("https://", result)
        self.assertNotIn("@", result)
        self.assertTrue(result.islower())

if __name__ == "__main__":
    unittest.main()
