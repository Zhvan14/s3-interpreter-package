from .interpreter import S3Interpreter

# Create a single instance of the interpreter when the module is imported
_interpreter = S3Interpreter()

# Define functions that use the single instance
def interpret(code_line):
    _interpreter.interpret(code_line)

def multiline(*code_lines):
    _interpreter.multiline(*code_lines)

# The list of public items in your module
__all__ = ['S3Interpreter', 'interpret', 'multiline']
