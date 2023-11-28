import json
from .esbuild import *
from subelectron import Electron
from subtsx.common import vars

class TsxElectron(Electron):
    def __init__(self, title: str, tsxpath: str | Path, electron_version: Optional[str] = None) -> None:
        p = Path(tsxpath)
        if not p.is_absolute():
            p = p.resolve()
        
        super().__init__(title, electron_version, p.parent)
        self.entry = p.name
        self.esbuild = EsBuild(version=vars.ESBUILD_VERSION)
    
    def ensure_types(self, path: Path | str = "."):
        path = Path(path)
        tdir = path.joinpath("node_modules", "@types")
        if tdir.joinpath("subtsx").exists():
            return
        tdir.mkdir(parents=True, exist_ok=True)
        import shutil
        shutil.copytree(vars.lib_dir.joinpath("root", "@types"), tdir, dirs_exist_ok=True)

    def launch(self):
        self.esbuild.install.ensure_installed()
        
        plugin = f'plugin:{vars.lib_dir.joinpath("plugin", "subtsx.js")}'

        plugin_options = dict(
            esbuild=str(self.esbuild.install.artifact),
            wd=str(self.proj_dir), 
            entry=self.entry,
            cache=str(self.cache),
            fresh=self.fresh,
        )
        
        return super().launch(plugin, json.dumps(plugin_options))
