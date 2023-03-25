class StringFormatter:
    def __init__(self, string):
        self.string = string

    def remove_short_words(self, n):
        words = self.string.split()
        words = [word for word in words if len(word) >= n]
        self.string = ' '.join(words)
        return self

    def replace_digits(self):
        self.string = ''.join(['*' if char.isdigit() else char for char in self.string])
        return self

    def insert_spaces(self):
        self.string = ' '.join(self.string)
        return self

    def sort_by_size(self):
        words = self.string.split()
        words.sort(key=len)
        self.string = ' '.join(words)
        return self

    def sort_lexicographically(self):
        words = self.string.split()
        words.sort()
        self.string = ' '.join(words)
        return self

    def __str__(self):
        return self.string