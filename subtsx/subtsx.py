import json
from .esbuild import *
from subelectron import Electron


class TsxElectron(Electron):
    def __init__(self, title: str, tsxpath: str | Path, electron_version: Optional[str] = None) -> None:
        p = Path(tsxpath)
        if not p.is_absolute():
            p = p.resolve()
        
        super().__init__(title, electron_version, p.parent)
        self.entry = p.name
        self.esbuild = EsBuild(version=vars.ESBUILD_VERSION)

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
