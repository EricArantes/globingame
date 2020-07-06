# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\Eric\\PycharmProjects\\roguelikeproject'],
             binaries=[],
             datas=[('data/assets/creaturespritsheet.png', 'data/assets'),('data/assets/itemspritesheet.png', 'data/assets'), ('data/assets/BG.jpg', 'data/assets'),('data/assets/joystix monospace.ttf', 'data/assets'), ('data/audio/music/gameloop1.wav', 'data/audio/music'),('data/audio/music/menu music.wav', 'data/audio/music'), ('data/audio/sfx/Hit_1.wav', 'data/audio/sfx'), ('data/audio/sfx/Hit_2.wav', 'data/audio/sfx'), ('data/audio/sfx/Hit_3.wav', 'data/audio/sfx'), ('data/audio/sfx/Hit_4.wav', 'data/audio/sfx'), ('data/audio/sfx/Hit_5.wav', 'data/audio/sfx'), ('data/audio/sfx/Miss_1.wav', 'data/audio/sfx'), ('data/audio/sfx/Miss_2.wav', 'data/audio/sfx'), ('data/audio/sfx/Miss_3.wav', 'data/audio/sfx'), ('data/audio/sfx/Miss_4.wav', 'data/audio/sfx'), ('data/audio/sfx/Miss_5.wav', 'data/audio/sfx'), ('data/audio/sfx/Crit_1.wav', 'data/audio/sfx'), ('data/audio/sfx/Crit_2.wav', 'data/audio/sfx'), ('data/audio/sfx/Crit_3.wav', 'data/audio/sfx'), ('data/audio/sfx/Crit_4.wav', 'data/audio/sfx')],
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
