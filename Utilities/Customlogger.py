import logging

class logGen:
    @staticmethod
    def logger():
        logging.basicConfig(filename="\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%y %I:%M:%s %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
#
# import logging
#
# class TestLogger:
#     def __init__(self):
#         self.logger = logging.getLogger("TestLogger")
#         self.logger.setLevel(logging.INFO)
#
#         # Create a console handler and set level to info
#         ch = logging.StreamHandler()
#         ch.setLevel(logging.INFO)
#
#         # Create a file handler and set level to info
#         fh = logging.FileHandler("test.log")
#         fh.setLevel(logging.INFO)
#
#         # Create a formatter
#         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
#         # Add the formatter to the handlers
#         ch.setFormatter(formatter)
#         fh.setFormatter(formatter)
#
#         # Add the handlers to the logger
#         if not self.logger.handlers:  # Prevent adding multiple handlers if already configured
#             self.logger.addHandler(ch)
#             self.logger.addHandler(fh)
#
#     def log_info(self, message):
#         self.logger.info(message)
#
# # Usage
# if __name__ == "__main__":
#     test_logger = TestLogger()
#     test_logger.log_info("This is an info message.")
