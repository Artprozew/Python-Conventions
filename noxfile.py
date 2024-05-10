import nox


@nox.session(python=False)
def lint(session):
    """Runs the lint suite"""
    # session.run("poetry", "install")
    session.run("black", "--check", ".")
    session.run("flake8", ".")


@nox.session(python=False)
def typing(session):
    """Runs the typing suite"""
    session.run("mypy", ".")
