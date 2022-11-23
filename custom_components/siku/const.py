"""Constants for the Siku Fan integration."""

DOMAIN = "siku"
DEFAULT_MANUFACTURER = "Siku"
DEFAULT_MODEL = "RV"
DEFAULT_NAME = "Fan"
DEFAULT_PORT = 4000

CONF_VERSION = "version"
CONF_ID = "idnum"

FAN_SPEEDS = ["01", "02", "03"]
DIRECTION_FORWARD = "00"
DIRECTION_ALTERNATING = "01"
DIRECTION_REVERSE = "02"
DIRECTIONS = {
    DIRECTION_FORWARD: "forward",
    DIRECTION_ALTERNATING: "alternating",
    DIRECTION_REVERSE: "reverse",
}

PRESET_MODE_AUTO = "auto"
PRESET_MODE_ON = "on"
PRESET_MODE_PARTY = "party"
PRESET_MODE_SLEEP = "sleep"
