import subprocess
import os
import urllib.request
import logging
from .common import *


logger = logging.getLogger(__name__)


class EsBuild:
    def __init__(self, version: Optional[str] = None):
        self.install = Installation(version=version or vars.ESBUILD_VERSION)
        self.pmain: subprocess.Popen[bytes] | None = None
        

    def launch(self, entry: str | Path="index.tsx", *args: str):        
        self.install.ensure_installed()
        
        # launch the electron main process
        p = self.pmain = subprocess.Popen([
                self.install.exe,
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


class Installation:
    INDENT = "      "
    
    def __init__(self, version: str) -> None:
        self.version = version.lower().strip("v")
        self.name = f'esbuild-{self.version}'
        self.path = se_vars.elec_dir.joinpath(self.name)
        self.exe = self.path.joinpath("package", "bin", "esbuild")

    def install(self):
        tmp = se_vars.elec_dir.joinpath("tmp")
        tmp.mkdir(exist_ok=True, parents=True)
        ark_file = str(tmp.joinpath(self.name + ".tgz"))

        print(self.INDENT + "downloading esbuild...", flush=True)
        
        if se_vars.is_posix:
            platform_name = "linux"
            extraction_method = "tar -xf {0} -C {1}"
        else:
            platform_name = "win32"
            extraction_method = "unzip {0} -d {1}"  # TODO: update this

        # https://registry.npmjs.org/@esbuild/linux-x64/-/linux-x64-0.19.4.tgz
        # https://registry.npmjs.org/@esbuild/win32-x64/-/win32-x64-0.19.4.tgz
        archive_url = f"https://registry.npmjs.org/@esbuild/{platform_name}-x64/-/{platform_name}-x64-{self.version}.tgz"
        logger.info("src: %s", archive_url)
        logger.info("dst: %s", ark_file)
        urllib.request.urlretrieve(archive_url, ark_file)
        
        print(self.INDENT + "extracting archive...", flush=True)

        extraction_cmd = extraction_method.format(ark_file, self.path)
        logger.info("extracting via: %s", extraction_cmd)

        self.path.mkdir(exist_ok=True, parents=True)
        subprocess.run(extraction_cmd, shell=True, stdout=subprocess.PIPE).check_returncode()

        os.unlink(ark_file)

    def ensure_installed(self):
        if not self.exe.exists():
            self.install()
