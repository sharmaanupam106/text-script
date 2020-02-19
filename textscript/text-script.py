from ConfigUtils import Setup
from Logger import Logger
from TextController import WordCatcher, KeyboardEmulator

if __name__ == "__main__":

    # Current app version / / Ensure this is correct during updates
    text_script_version = "1.3.0"

    """
    Initialize Logger
    """

    # Initialize Logger
    L = Logger()

    L.log.debug(f"Program started from text-script. Version: {text_script_version}")

    """
    Configure Settings
    """

    # Initialize setup
    setup = Setup(L, text_script_version)

    # Check if config file exists, and is up to date
    setup.config_exists()

    # Print stats to console
    setup.get_stats()

    # Gets a list with default, local, and remote directories
    directories = setup.find_directories()

    """
    Initialize Text Controller
    """

    # Load shortcuts and file directories
    shortcut_list, file_dir_list = setup.shortcut_setup(directories)

    L.log.debug("Retrieved shortcut_list, file_dir_list:")

    # Check if new shortcuts have been added
    setup.new_shortcut_check(shortcut_list)

    # Initializes KeyboardEmulator instance
    k = KeyboardEmulator(L)

    # Initialize WordCatcher
    w = WordCatcher(L, k, shortcut_list, file_dir_list)
