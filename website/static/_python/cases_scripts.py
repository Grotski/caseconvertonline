import re
import json


with open("minor_words_for_title_case.json") as json_file:
    file_content = json_file.read()
    conjuctions_words = json.loads(file_content)


def to_title_case(text):
    text = text.lower()
    def capitalize_word(match):
        word = match.group(0)

        for value in conjuctions_words.values():
            if match.start() == 0 or text[match.start() - 1] in ['\n', '.', '. ', '!', '?']:
                return word.capitalize()
            elif word not in value:
                return word.capitalize()
        return word
    sentence_pattern = re.compile(r"(\b\w+\b)", re.MULTILINE)
    text_lines = [sentence_pattern.sub(capitalize_word, line) for line in text.splitlines()]
    return "\n".join(text_lines)


def to_sentence_case(text):
    text = text.lower()
    def capitalize(match):
        return match.group(1) + match.group(2).upper()
    
    sentence_pattern = re.compile(r'(^|[.!?]\s+|\.\s*\“|\.\s*\”|\.\s*\"|\s*\"|\s*\“|;-)([a-zа-і-я])', re.MULTILINE)
    
    quoted_sentence_pattern = re.compile(r'(\“[a-z])')
    
    text = sentence_pattern.sub(capitalize, text)
    
    text = quoted_sentence_pattern.sub(lambda m: m.group(1).upper(), text)
    
    return text


def to_capitalize_case(text):
    text = text.lower()
    return re.sub(
        r"[A-Za-z]+('[A-Za-z]+)?|[А-Яа-і-я]+('[А-Яа-я]+)?",
        lambda word: word.group(0).capitalize(),
        text)
