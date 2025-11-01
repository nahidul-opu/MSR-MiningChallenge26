import re

class TextClassifier:
    def __init__(self, *, case_sensitive=False):
        self.case_sensitive = case_sensitive

    def classify(self, text):
        raise NotImplementedError("Subclasses must implement classify method")
    
    def get_matches(self):
        raise NotImplementedError("Subclasses must implement get_matches method")

class RegexClassifier(TextClassifier):
    def __init__(self, keywords, *, case_sensitive=False):
        self.keywords = keywords
        super().__init__(case_sensitive=case_sensitive)

    def classify(self, text):
        pattern = r"\b(?:{})\w*".format("|".join(map(re.escape, self.keywords)))
        flags = 0 if self.case_sensitive else re.IGNORECASE

        self. matches = re.findall(pattern, text, flags)
        
        return bool(self.matches)
    
    def get_matches(self):
        return self.matches
    

class SimpleSubstringClassifier(TextClassifier):
    def __init__(self, keywords, *, case_sensitive=False):
        self.keywords = keywords
        super().__init__(case_sensitive=case_sensitive)

    def classify(self, text):
        if not self.case_sensitive:
            text = text.lower()
            keywords = {w.lower() for w in self.keywords}
        else:
            keywords = self.keywords

        self.matches = [keyword for keyword in keywords if keyword in text]
        
        return bool(self.matches)
    
    def get_matches(self):
        return self.matches
    

class LLMClassifier(TextClassifier):
    def __init__(self,prompt_template, llm_model="gpt-oss-20b"):
        super().__init__(case_sensitive=False)
        self.prompt_template = prompt_template
        self.llm_model = llm_model

    def classify(self, text):
        # Placeholder implementation
        # In a real scenario, this would involve calling the LLM with the text and keywords
        self.matches = []  # Assume no matches found
        return bool(self.matches)
    
    def get_matches(self):
        raise ModuleNotFoundError("This function is not available for LLMClassifier")
    

class EmbeddingClassifier(TextClassifier):
    def __init__(self, base_text, embedding_model="all-MiniLM-L6-v2", similarity_threshold=0.7):
        super().__init__(case_sensitive=False)
        self.base_text = base_text
        self.embedding_model = embedding_model
        self.similarity_threshold = similarity_threshold

    def classify(self, text):
        # Placeholder implementation
        # In a real scenario, this would involve computing embeddings and checking similarity
        self.matches = []  # Assume no matches found
        return bool(self.matches)
    
    def get_matches(self):
        raise ModuleNotFoundError("This function is not available for EmbeddingClassifier")