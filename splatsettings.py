DEFAULT_IMAGE = "default.png"  # The default team logo if you enter a team name that does not have a corresponding team image file. Must be in the same directory as the exe file

# The ink colors to be chosen.
# Must be png files with the exact name as listed in the quotes.
# Do not include .png
# Image size must be 24x24
SAMPLE_STRAWBERRY = "samples/sample_strawberry"
SAMPLE_ORANGE = "samples/sample_orange"
SAMPLE_BUTTERSCOTCH = "samples/sample_butterscotch"
SAMPLE_BANANA = "samples/sample_banana"
SAMPLE_YELLOW = "samples/sample_yellow"
SAMPLE_PASTELGREEN = "samples/sample_pastelgreen"
SAMPLE_SLIMEGREEN = "samples/sample_slimegreen"
SAMPLE_SKYBLUE = "samples/sample_skyblue"
SAMPLE_BLUE = "samples/sample_blue"
SAMPLE_BLUEPURPLE = "samples/sample_bluepurple"
SAMPLE_PURPLE = "samples/sample_purple"
SAMPLE_MAGENTA = "samples/sample_magenta"

# The background bars displayed on the scoreboard for the selected ink colors.
# Must be png files with the exact name as listed in the quotes.
# Do not include .png
# Image size must be 340x36
BG_STRAWBERRY = "backgrounds/background_strawberry"
BG_ORANGE = "backgrounds/background_orange"
BG_BUTTERSCOTCH = "backgrounds/background_butterscotch"
BG_BANANA = "backgrounds/background_banana"
BG_YELLOW = "backgrounds/background_yellow"
BG_PASTELGREEN = "backgrounds/background_pastelgreen"
BG_SLIMEGREEN = "backgrounds/background_slimegreen"
BG_SKYBLUE = "backgrounds/background_skyblue"
BG_BLUE = "backgrounds/background_blue"
BG_BLUEPURPLE = "backgrounds/background_bluepurple"
BG_PURPLE = "backgrounds/background_purple"
BG_MAGENTA = "backgrounds/background_magenta"
BG_CHAOS = "backgrounds/background_chaos"
BG_ORDER = "backgrounds/background_order"

# The background bars displayed on the box score for the selected ink colors.
# Must be png files with the exact name as listed in the quotes.
# Do not include .png
# Image size must be 50x36
BS_STRAWBERRY = "boxscores/boxscore_strawberry"
BS_ORANGE = "boxscores/boxscore_orange"
BS_BUTTERSCOTCH = "boxscores/boxscore_butterscotch"
BS_BANANA = "boxscores/boxscore_banana"
BS_YELLOW = "boxscores/boxscore_yellow"
BS_PASTELGREEN = "boxscores/boxscore_pastelgreen"
BS_SLIMEGREEN = "boxscores/boxscore_slimegreen"
BS_SKYBLUE = "boxscores/boxscore_skyblue"
BS_BLUE = "boxscores/boxscore_blue"
BS_BLUEPURPLE = "boxscores/boxscore_bluepurple"
BS_PURPLE = "boxscores/boxscore_purple"
BS_MAGENTA = "boxscores/boxscore_magenta"

# Game Header appears above each "inning"
# Must be png files with the exact name as listed in the quotes.
# Do not include .png
# Image size must be 50x24
BS_GAMEHEADER = "boxscores/boxscores_header"

# The folder where team logos are stored to (or rather, the path to that folder)
TEAMLOGOS_FOLDER = "teamlogos/"

# If you try to use a different font, you must also add it to graphics.py
# Not recommended if you don't know what you are doing.
TEAMNAME_FONT = 'Splatfont 2'
SCORE_FONT = 'Splatfont 2'

# Enter a basic color's name here to alter the text.
TEAMNAME_COLOR = 'white'  # Used all over the application really
SCORE_COLOR = 'white'  # Used for the score on the scoreboard
ALERT_COLOR = 'yellow'  # Used for messages like "Game recorded" in the settings window

# Changing these will affect the dimensions of things in the settings window. Recommendation is not to alter.
MAX_TEAMNAME_LENGTH = 24
MAX_SCORE_LENGTH = 3
ENTRY_FONT_SIZE = 12
TEAMNAME_FONT_SIZE = 18
SCORE_FONT_SIZE = 24
BOXSCORE_FONT_SIZE = 24
HEADER_FONT_SIZE = 16
