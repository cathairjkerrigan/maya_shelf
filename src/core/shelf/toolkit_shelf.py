from textwrap import dedent

from .shelf import Shelf

class ToolkitShelf(Shelf):

    def __init__(self):
        # type: () -> None
        Shelf.__init__(self, name="Utils_Shelf")

    def build(self):
        
        self.addButton(
            label="Sample Button",
            tooltip="Sample Button.",
            command=dedent(
                """
                print("sample button 01")
                """
            )
        )

        self.addSeperator()

        self.addButton(
            label="Print Selection",
            tooltip="Print Selection.",
            command=dedent(
                """
                from maya import cmds
                print(cmds.ls(sl=1))
                """
            )
        )

