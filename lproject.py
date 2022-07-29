
import click
from utils.projects import copy_project, copy_folder

@click.group()
def cli():
    pass


@click.command(help="Copy a project.")
@click.option('--id', '--project_id', help="id: ID of Project to copy.")
@click.argument('id', required=False)
# @click.option('--name', '--project_name', help="name: Name of Project to copy.")
@click.option('--source', default='Source',  help="Source,  overrides value labeled in looker.ini file.")
@click.option('--destination', default='Destination',  help="Destination tag, overrides value in looker.ini file.")
@click.option('--github_org', default=None, help="Git Hub Organization, overrides value defined in .env file.")
@click.option('--branch', default=None, help="Target branch to copy, otherwise uses active branch.")
@click.option('--folder_name', default=None, help="Name of folder to copy.")
def copy(id, source, destination, github_org, branch, folder_name):
    if id is None and folder_name is None:
        click.echo("Project ID or Folder required for Copy operation.")
        return

    # convert to parameters to full names for easier debugging
    project_id = id
    # project_name = name
    ini_source = source or None
    ini_destination = destination or None
    env_github_org = github_org or None
    branch_name = branch or None
    folder_name = folder_name or None

    if project_id:
        copy_project(project_id, ini_source, ini_destination, env_github_org, branch_name)

    if folder_name:
        copy_folder(folder_name, None, ini_source, ini_destination)


cli.add_command(copy)

if __name__ == '__main__':
    cli()


