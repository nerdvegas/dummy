name = "dummy"

version = "1.0.0"

authors = [
    "ajohns"
]

description = \
    """
    Python-based hello world example package.
    """

requires = [
    "python"
]

uuid = "dfgdfgdgdfgdfgdgdfg"

def commands():
    env.PYTHONPATH.append("{root}/python")
