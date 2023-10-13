import logging
# Configure logging and modify how logging is formatted
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
# Ask user for the logger level
logger_level_input = input("Enter logging level name: ")
# Convert the input logger level to uppercase
logger_level_input = logger_level_input.upper()
# Ask the user for the message they want to log
message_input = input("Enter your message: ")

# Define the valid logging levels with their perspective numerical value
logging_levels = {"DEBUG": logging.DEBUG, "INFO": logging.INFO, "WARNING": logging.WARNING, "ERROR": logging.ERROR, "CRITICAL": logging.CRITICAL}

# Determine if the user input for logger level is in the valid logging levels
if logger_level_input in logging_levels:
    # Retrieve the value of the logger level the user inputted
    level_name = logging_levels[logger_level_input]
    # Set logging level and  print the log message
    logging.log(level_name, message_input)
else:
# Provide an invalid message once the inputted logger level is not in the valid logging levels
    print("Invalid logging level input")



