# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.win32.versioninfo import VSVersionInfo

a = Analysis(
    ['UI.py'],
    pathex=[],
    binaries=[],
    datas=[]
    imports=['csaps', 'matplotlib', 'numpy', 'pandas', 'scikit_fda', 'scipy', 'sklearn', 'joblib', 'multimethod', 'findiff', 'rdata', 'fdasrsf', 'dcor', 'numdifftools', 'customtkinter', 'openpyxl'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Vgram UI',
    version="version.txt",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico',
)
