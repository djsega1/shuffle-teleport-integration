import subprocess

from walkoff_app_sdk.app_base import AppBase


class CheckTctl(AppBase):
    """
    An example of a Walkoff App.
    Inherit from the AppBase class to have Redis, logging, and console logging set up behind the scenes.
    """
    __version__ = "1.0.0"
    app_name = "CheckTctl"  # this needs to match "name" in api.yaml

    def __init__(self, redis, logger, console_logger=None):
        """
        Each app should have this __init__ to set up Redis and logging.
        :param redis:
        :param logger:
        :param console_logger:
        """
        super().__init__(redis, logger, console_logger)

    def check_tctl_version(self, custom_str="123"):
        command = "tctl version"
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        return f"{output}\n{error}\n{custom_str}"


if __name__ == "__main__":
    CheckTctl.run()