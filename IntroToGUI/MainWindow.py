import tkinter


class MainWindow:
    def __init__(self, parent):
        self.parent = parent
        self.fileName = None
        self.dirty = False  # True = changes were made to data that have not been saved
        self.data = {} # Key = bookmark names, Value = urls

        menubar = tkinter.Menu(self.parent)
        self.parent["menu"] = menubar

        fileMenu = tkinter.Menu(menubar)

        for label, command, shortcut_text, shortcut in (
            ("New...", self.fileNew, "Ctrl+N", "<Control-n>"),
            ("Open...", self.fileOpen, "Ctrl + O", "<Control - n>"),
            ("Save", self.fileSave, "Ctrl + S", "<Control-s>"),
            (None, None, None, None),
            ("Quit", self.fileQuit, "Ctrl + Q", "<Control - q>")
        ):
            if label is None:
                fileMenu.add_separator()
            else:
                fileMenu.add_command(label=label, underline=0, command=command, accelerator=shortcut_text)
                self.parent.bind(shortcut, command)
        menubar.add_cascade(label = "File", menu = fileMenu, underline=0)


