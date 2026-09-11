# Appendix F Solutions: Environment Setup and Troubleshooting

1. Global installation allows projects to overwrite shared versions and makes reproduction harder; isolation gives the project a specific dependency context.
2. `python3 -m venv .venv` followed by `source .venv/bin/activate`.
3. `.venv\Scripts\Activate.ps1`.
4. It invokes pip through the selected Python interpreter, reducing the chance of installing into another environment.
5. `python -c "import sys; print(sys.executable)"`.
6. VS Code selects an interpreter for editing and terminals, while every notebook also selects a kernel. They can point to different environments.
7. Print `sys.executable`, run `python -m pip show pandas`, then install the requirements with `python -m pip install -r requirements.txt` if appropriate.
8. Python may import the local file before the real package, causing missing attributes or circular imports.
9. Inspect the exact path, ownership, and intended operation. Do not use administrator privileges automatically; follow organisational controls.
10. It exposes package downloads to interception and hides the actual certificate, proxy, or approved-index problem.
11. Operating system, processor architecture, Python version, package version, installer/source, and full error are useful.
12. It clears variables, imports, and cached state, revealing cells that cannot run from a fresh ordered execution.
13. When unexplained changes have accumulated and the environment can be reproduced from declared dependencies.
14. Confirm the exact path, that it is the project environment, and that source code or irreplaceable data are not stored inside it.
15. Goal, exact command, full error, OS, architecture, Python executable/version, package versions, commit, branch, and minimal example are valid choices. Remove secrets.
16. Hardware, parallel scheduling, library algorithms, and floating-point behaviour can still differ.
17. `python -m compileall src scripts` and `python -m json.tool data/dictionaries/nrg_schema.json`.
18. The report is not ready: activate the intended `.venv` and install declared dependencies, including pytest, through its Python interpreter.
19. A single change preserves causal evidence about what fixed or changed the failure.
20. Example: confirm branch, Git status, executable, active `.venv`, kernel, package versions, data version, clean execution, tests, and recorded limitations. Any seven precise steps earn credit.
