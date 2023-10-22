from glob import glob


def _as_module(fixture_path: str) -> str:
    return fixture_path.replace("/", ".").replace("\\", ".").replace(".py", "")


pytest_plugins = [
    # "atomic_aurora_backend.shows.tests.fixtures"
    _as_module(fixture_path)
    for fixture_path in glob("atomic_aurora_backend/**/fixtures.py", recursive=True)
]
