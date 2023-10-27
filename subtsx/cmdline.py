#!/usr/bin/env python3
import argparse, subprocess, os, shutil
from .common import *
from .version import VERSION
import subelectron.shortcut as shortcut
from .esbuild import EsBuild

def sh(cmd, shell=True, **kwargs):
    subprocess.call(cmd, shell=shell, **kwargs)


def make_posix_shortcut(path: Path | str, name: str, png_file: Optional[Path | str]=None):
    path = str(path)
    shortcut.desktopfile(
        path, 
        exec=f'/bin/bash -c "subelectron --cwd=\'{os.getcwd()}\'"', 
        icon=str(png_file or vars.lib_dir.joinpath("default", "icon.png")),
        terminal=False,
        name=name
    )
    os.chmod(path, 0o777)


def make_windows_shortcut(path: Path | str, ico_file:  Optional[Path | str]=None):
    pythonw = shutil.which("pythonw") or "pythonw"
    shortcut.lnkfile(
            str(path),
            target=pythonw,
            arguments='-m "subelectron.cmdline"',
            icon=str(ico_file or vars.lib_dir.joinpath("default", "icon.ico")),
            wd=str(Path.cwd())
    )


def main():
    parser = argparse.ArgumentParser(description="TSX Gui Platform")
    parser.set_defaults(func=build)
    parser.add_argument('-c', '--cwd', help="cwd", default="")
    parser.add_argument('--version', help="print version", action="store_true")

    subparsers = parser.add_subparsers(title="commands")
    sparser = subparsers.add_parser("build", help="build TSX gui into dist/*.js|css")
    sparser.set_defaults(func=build)
    sparser.add_argument('entry', help='entry point file', nargs='*', default="index.tsx")

    args = parser.parse_args()

    if args.cwd:
        cwd = Path(args.cwd)
        if cwd.name.endswith(".desktop"):
            cwd = cwd.parent
            
        os.chdir(cwd)

    if args.version:
        print("subtsx v{}.{}.{} @ {}".format(*VERSION, vars.lib_dir))
        return

    if args.func:
        args.func(args)
    else:
        parser.parse_args("-h")


def build(args):
    esb = EsBuild()
    esb.launch(
        args.entry, 
        "--bundle", 
        "--sourcemap",
        "--sourcemap",
        "--outfile=dist/out.js",
        "--jsx-factory=h",
        "--jsx-fragment=Fragment",
    )
    

if __name__ == "__main__":
    main()
