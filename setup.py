import os

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext
from setuptools.command.sdist import sdist
from setuptools.command.build_py import build_py

class CustomSdist(sdist):
    def run(self):
        print("RUNNING sdist")
        super().run()
        breakpoint()

class CopyBinaryFile(build_py):
    def run(self):
        print("RUNNING build_py")
        super().run()
        binary = "D:/Projects/plugin-htmlkit/build/windows/x64/releasedbg/core.cp39-win_amd64.pyd"
        self.copy_file(binary, self.get_package_dir("nonebot_plugin_htmlkit"))

EXT_NAME = "nonebot_plugin_htmlkit.core"

class XmakeBuildExt(build_ext):
    def build_extensions(self):
        print("RUNNING build_ext")
        breakpoint()

ext_modules = [
    Extension(
        EXT_NAME,
        sources=[],
        py_limited_api=True,
    )
]

setup(
    cmdclass={
        "sdist": CustomSdist,
        "build_py": CopyBinaryFile,
        "build_ext": XmakeBuildExt,
    },
    ext_modules=ext_modules
)