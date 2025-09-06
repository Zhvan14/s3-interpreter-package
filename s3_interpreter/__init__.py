from .interpreter import S3Interpreter

def interpret(code_line):
    """
    Creates a new interpreter instance and runs a single line of S-language code.
    """
    interpreter = S3Interpreter()
    interpreter.interpret(code_line)

def multiline(code_lines):
    """
    Creates a new interpreter instance and runs multiple lines of S-language code.
    """
    interpreter = S3Interpreter()
    interpreter.multiline(*code_lines)

# The list of public items in your module
__all__ = ['S3Interpreter', 'interpret', 'multiline']
