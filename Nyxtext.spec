# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['.\\editor\\scripts\\main.py'],
             pathex=['.\\.venv\\Lib\\site-packages\\'],
             binaries=[],
             datas=[
                 ('.\\.venv\\Lib\\site-packages\\customtkinter', 'customtkinter'),
                 ('.\\.venv\\Lib\\site-packages\\tkterm\\src', 'src'),
                 ('.\\.venv\\Lib\\site-packages\\tkterm\\version.py', '.'),
                 ('.\\.venv\\Lib\\site-packages\\tkterm\\backend', 'backend'),
                 ('.\\editor\\scripts\\color_Themes', 'color_Themes'),
                 ('.\\editor\\scripts\\misc', 'misc'),
                 ('.\\.venv\\Lib\\site-packages\\tkterm\\img', 'img'),
                 ('.\\.venv\\Lib\\site-packages\\chlorophyll', 'chlorophyll'),
                 ('.\\.venv\\Lib\\site-packages\\CTkMenuBar', 'CTkMenuBar'),
                 ('.\\.venv\\Lib\\site-packages\\pywinstyles','pywinstyles'),
                 ('.\\.venv\\Lib\\site-packages\\hPyT','hPyT'),
             ],
             hiddenimports=['trace'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='NyxText',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          icon='.\\editor\\scripts\\misc\\icons\\icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='NyxText')
