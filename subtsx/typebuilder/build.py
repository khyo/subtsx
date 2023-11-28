#!/usr/bin/env python3
import argparse
import re
import os
import shutil
from pathlib import Path
import subprocess


def main():
    parser = argparse.ArgumentParser(description='type builder for SubTSX')
    args = parser.parse_args()

    build()


def build():
    os.chdir(Path(__file__).parent)
    get_node_modules()

    combiner = Combiner(Path("preamble.ts"), Path("lib.d.ts"))
    combiner.combine(packages["voby"])
    combiner.flush()



class ImportScanner:
    def __init__(self, tsfile: 'TsFile') -> None:
        self.tsfile = tsfile
        self.imports: list[TsFile] = []
    
    def resolve(self):
        lines = [f"\ndeclare module '{self.tsfile.module_name}' {{\n"]
        with open(self.tsfile.path) as f:
            for line in f:
                lines.append(self.dispatch(line))
        lines.append("}\n")
        return lines


    STRAIGHT = re.compile(r'''^import\s+['"]([^'"]*)['"]''')
    def straight_import(self, line: str, path: str):
        tsfile = self.tsfile.resolve(path)
        self.imports.append(tsfile)
        return line.replace(path, tsfile.module_name)
    
    FROM = re.compile(r'''.*from\s+['"]([^'"]*)['"]''')
    def import_from(self, line: str, path: str):
        tsfile = self.tsfile.resolve(path)
        self.imports.append(tsfile)
        return line.replace(path, tsfile.module_name)

    def dispatch(self, line: str) -> str:
        if line.startswith("import") or line.startswith("export"):
            if (m := self.STRAIGHT.match(line)):
                path = m.groups()[0]
                return self.straight_import(line, path)
            elif (m := self.FROM.match(line)):
                print(m)
                path = m.groups()[0]
                return self.import_from(line, path)
        
        return line


class Combiner:
    def __init__(self, preamble: Path, outfile: Path):
        self.outfile = outfile
        self.preamble = preamble
        self.modules: dict[TsFile, list[str]] = {}

    def combine(self, package: "Package"):
        imp = ImportScanner(package.entry)
        self.modules[package.entry] = imp.resolve()

    def flush(self):
        with open(self.preamble) as f:
            preabmle = f.read()
        with open(self.outfile, mode="w") as f:
            f.write(preabmle)
            for tsfile, lines in self.modules.items():
                f.writelines(lines)

def get_node_modules():
    if Path("node_modules").exists():
        return
    shutil.rmtree("node_modules")
    sh("npm install")


def sh(*args: str, shell=True, **kwargs):
    return subprocess.run(args, shell=shell, encoding="utf8", **kwargs)


class Package:
    def __init__(self, name: str, entry_path: Path):
        self.name = name
        self.entry = TsFile(entry_path, self)
        self.root = self.entry.dir

class TsFile:
    def __init__(self, path: Path, package: Package):
        self.path = path
        self.dir = path.parent
        self.package = package

    def resolve(self, path: str) -> 'TsFile':
        # look at installed package first
        pack = packages.get(path)
        if pack is not None:
            return pack.entry
        
        # look at relative paths
        tsfile = self.dir.joinpath(path)
        if tsfile.is_dir():
            tsfile = tsfile.joinpath("index.d.ts")
        return TsFile(tsfile, self.package)

    @property
    def module_name(self) -> str:
        root = f"si/{self.package.name}"
        if self.package.entry == self:
            return root
        
        p = self.package_path
        if p.name.endswith("index.d.ts"):
            x = str(p.parent)
        else:
            x = str(p)
            if x.endswith(".d.ts"):
                x = x[:-5]
        return f"{root}/{x}"
        # if self.path.name == "index.d.ts":
        
        # x = str(self.package_path)
        # if x.endswith("/index.d.ts"):
        #     return x[:-len("/index.d.ts")]
    
    @property
    def package_path(self) -> Path:
        return self.path.relative_to(self.package.root)


NODE_MODULES = Path("node_modules")

packages = {
    "oby": Package("oby", NODE_MODULES.joinpath("oby", "dist", "index.d.ts")),
    "voby": Package("voby", NODE_MODULES.joinpath("voby", "dist", "index.d.ts")),
    "htm": Package("htm", NODE_MODULES.joinpath("htm", "dist", "htm.d.ts")),
}


if __name__ == "__main__":
    main()
