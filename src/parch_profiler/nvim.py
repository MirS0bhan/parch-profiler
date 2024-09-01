from typing import Optional

from plumbum.cmd import git
from os.path import expanduser

from vlidt import BaseModel


class NvimConfig(BaseModel):
    url: Optional[str] = None


nvim_git_dir = f"{expanduser('~')}/.config/nvim/.git"
nvim_work_tree = f"{expanduser('~')}/.config/nvim/"

_dir = ["--git-dir", nvim_git_dir, "--work-tree", nvim_work_tree]


def nvim_upstream():
    """
    Retrieves the Git remote repositories for the specified Git directory and working tree.
    """
    try:
        # Execute the Git command with the specified Git directory and working tree
        remote = git[*_dir, "remote", "-v", "get-url", "origin"]().strip()
        return NvimConfig(remote)
    except Exception as e:
        print(f"Error retrieving Git remotes: {e}. cant resolve nvim config upstream")
        return None


def nvim_clone(url: str):
    git["clone", url, nvim_work_tree]()
