import regex as re


def generate_pattern_from_template(template: str):
    escaped = re.escape(template)
    spaced_escape = re.sub(r'\\\s+', "\\\s+", escaped)
    return "^" + spaced_escape.replace(r"<\*>", r"(.*?)") + "$"