from logging import getLogger
from typing import Any
from maya import cmds, mel
from textwrap import dedent

logger = getLogger(__name__)

from core.module_handler import reload_module

VERSION = "v.1.0.0"

def build_enviroment():
    # type: () -> None
    mel.eval('source "artAttrCreateMenuItems.mel";')
    build_menu()

def reload(*args):
    # type: (Any) -> None
    reload_module("repos", True)
    cmds.evalDeferred(
        dedent(
            """
            from core.startup import build_menu
            build_menu()
            """
        ),
        lp=True,
    )

def build_menu():
    # type: () -> None

    logger.info("Building Menu")

    MENU_NAME = "utils_menu"
    MENU_ITEMS = [
        {
            "name": "create_cube",
            "command": "from maya import cmds;cmds.polyCube()",
            "label": "Create Cube",
        },
        {
            "name": "reload_toolkit",
            "command": reload,
            "label": "Reload Toolkit",
        },
        {
            "name": "seperator_01",
            "divider": True,
        },
        {
            "name": "version_info",
            "command": "pass",
            "label": "Version: {}".format(VERSION)
        }
    ]

    if cmds.menu(MENU_NAME, query=True, exists=True):
        cmds.menu(MENU_NAME, edit=True, deleteAllItems=True)
    else:
        cmds.menu(MENU_NAME, label="Utils Menu", parent="MayaWindow", tearOff=False)

    for data in MENU_ITEMS:
        name = data.pop("name")
        cmds.menuItem(name, parent=MENU_NAME, **data)