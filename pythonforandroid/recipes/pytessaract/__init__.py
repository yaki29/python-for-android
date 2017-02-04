from pythonforandroid.toolchain import PythonRecipe

class PytessaractRecipe(PythonRecipe):
    version = '0.1'
    url = 'https://pypi.python.org/packages/62/e3/84698f88eb404c6c6f8d185830543ba857fd68c4bc5c991c960cd59dde9a/pytesseract-{version}.tar.gz'
    depends = [('python2', 'python3crystax')]
    site_packages_name = 'pytessaract'
    call_hostpython_via_targetpython = True

recipe = PytessaractRecipe()
