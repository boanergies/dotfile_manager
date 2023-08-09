import typer


def main(dotfile_project_path: str, github_cli: bool = False, https_pull: bool = False):
    """Command to pull down the specified dotfiles repo and set up
    the dev environment accordingly. The default is expecting to clone
    using ssh.

    Args:
        dotfile_project_path (str): path name given when checking out a gitlab/github project using ssh or gh or https
        github_cli (bool, optional): indicate if using the github cli. Defaults to False.
        https_pull (bool, optional): indicate if using https to clone a git project
    """
    print("Hello world")


if __name__ == "__main__":
    typer.run(main)
