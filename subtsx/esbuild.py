import subprocess
import os
import urllib.request
import logging
from .common import *
from subpack import packages

logger = logging.getLogger(__name__)


class EsBuild:
    def __init__(self, version: Optional[str] = None):
        self.install = packages.EsBuild(version=version or vars.ESBUILD_VERSION)
        self.pmain: subprocess.Popen[bytes] | None = None
        

    def launch(self, entry: str | Path="index.tsx", *args: str):        
        self.install.ensure_installed()
        
        # launch the electron main process
        p = self.pmain = subprocess.Popen([
                self.install.artifact,
                str(entry),
                *args
            ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            # stderr=subprocess.PIPE,
        )

        if p.stdin is None or p.stdout is None:
            raise Exception("Electron process failed to pipe stdin & stdout")

        code = p.wait()
        print(p.stdout.read().decode())
        return code
