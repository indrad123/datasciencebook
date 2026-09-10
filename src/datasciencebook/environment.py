"""Environment diagnostics that avoid importing optional packages."""
from __future__ import annotations
import importlib.metadata, json, os, platform, shutil, sys
from pathlib import Path


def package_version(name: str) -> str | None:
    if not isinstance(name,str) or not name.strip(): raise ValueError("name must be non-empty")
    try:return importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:return None


def environment_report(packages=("numpy","pandas","matplotlib","scipy","scikit-learn","jupyterlab","pytest")):
    return {"python":platform.python_version(),"executable":sys.executable,"platform":platform.platform(),"cwd":str(Path.cwd()),"virtual_environment":os.environ.get("VIRTUAL_ENV"),"commands":{name:shutil.which(name) for name in ("git","python","jupyter")},"packages":{name:package_version(name) for name in packages}}


def readiness(report):
    if not isinstance(report,dict):raise ValueError("report must be a dictionary")
    issues=[]
    if not report.get("virtual_environment"):issues.append("virtual environment is not active")
    if not report.get("commands",{}).get("git"):issues.append("git command is unavailable")
    missing=[name for name,value in report.get("packages",{}).items() if value is None]
    if missing:issues.append("missing packages: "+", ".join(missing))
    return {"ready":not issues,"issues":issues}


def save_report(report,path):
    target=Path(path);target.parent.mkdir(parents=True,exist_ok=True);target.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8");return target
