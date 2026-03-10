from abc import ABC, abstractmethod

class TextFormatter:
    @abstractmethod
    def format_text(self, text):
        pass
    def publish(self, text):
        return f"***\n{text}\n***"
class LoudFormatter(TextFormatter):
    def format_text(self, text):
        return text.upper()
    
class MarkdownFormatter(TextFormatter):
    def format_text(self, text):
        return f"**{text}**"
    
def generate_output(formatter, text):
    text = formatter.format_text(text)
    print(formatter.publish(text))

loud = LoudFormatter()
md = MarkdownFormatter()

generate_output(loud, "Warning")
generate_output(md, "Bold statement")