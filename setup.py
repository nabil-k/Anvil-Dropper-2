import cx_Freeze
import os
os.environ['TCL_LIBRARY'] = "C:\\Program Files\\Python36\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Program Files\\Python36\\tcl\\tk8.6"

executables = [cx_Freeze.Executable("game.py")]
cx_Freeze.setup(
    version="22.99",
    name="Anvil Dropper",
    options ={
        "build_exe":{
            "packages":["pygame"],
            "include_files":[
                "Anton-Regular.ttf",
                "anvil.png",
                "blue.png",
                "Balloon-Game.mp3",
                "gameBg.png",
                "menuWallpaper.png"
                ]
        }
    },
    executables = executables
)