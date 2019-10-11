name = "qt"

version = "5.6.1"

authors = [
    "The Qt Company"
]

description = \
    """
    Qt is a free and open-source widget toolkit for creating graphical user interfaces as well as cross-platform
    applications that run on various software and hardware platforms such as Linux, Windows, macOS, Android or
    embedded systems with little or no change in the underlying codebase while still being a native application
    with native capabilities and speed.
    """

requires = [
    "cmake-3+",
    "gcc-6+"
]

variants = [
    ["platform-linux"]
]

tools = [
    "assistant",
    "canbusutil",
    "designer",
    "lconvert",
    "linguist",
    "lrelease",
    "lupdate",
    "moc",
    "pixeltool",
    "qcollectiongenerator",
    "qdbus",
    "qdbuscpp2xml",
    "qdbusviewer",
    "qdbusxml2cpp",
    "qdoc",
    "qgltf",
    "qhelpconverterv",
    "qhelpgenerator",
    "qlalr",
    "qmake",
    "qml",
    "qmleasing",
    "qmlimportscanner",
    "qmllint",
    "qmlmin",
    "qmlplugindump",
    "qmlprofiler",
    "qmlscene",
    "qmltestrunner",
    "qtdiag",
    "qtpaths",
    "qtplugininfo",
    "qtwaylandscanner",
    "rcc",
    "uic",
    "xmlpatterns",
    "xmlpatternsvalidator",
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "qt-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")

    # Helper environment variables.
    env.QT_BINARY_PATH.set("{root}/bin")
    env.QT_INCLUDE_PATH.set("{root}/include")
    env.QT_LIBRARY_PATH.set("{root}/lib")