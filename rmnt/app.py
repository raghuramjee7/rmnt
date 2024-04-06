import typer
from orchestrator import start

cli = typer.Typer()

@cli.command()
def move(project_name: str):
    start(project_name)

if __name__=="__main__":
    cli()

