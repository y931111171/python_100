from pywebio.utils import pyinstaller_datas

block_cipher = None
a = Analysis(['minimal.py'],
         pathex=['/Developer/PItests/minimal'],
         binaries=None,
         datas=None,
         hiddenimports=[],
         hookspath=None,
         runtime_hooks=None,
         excludes=None,
         cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
         cipher=block_cipher)
exe = EXE(pyz,... )
coll = COLLECT(...)