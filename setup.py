from cx_Freeze import setup, Executable

base = None

executables = [Executable('clip.py', base=base)]

packages = ['idna']

options = {
    'build_exe': {
        'packages': packages
    }
}

setup(
    name = 'Clippy',
    options = options,
    version = '1.0.0',
    description = 'A stack-based clipboard',
    executables = executables
)
