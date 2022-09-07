def logger():
    import logging
    import logging.handlers

    loger = logging.getLogger()
    loger.setLevel(logging.INFO)  # set logger level

    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")  # set logger format

    filehandler = logging.FileHandler("C:/Projects/OrangeHRM/logfile.log")  # set file for logger log
    filehandler.setFormatter(formatter)  # add format to filehandler

    stream_handler = logging.StreamHandler()  # print log into the console
    stream_handler.setFormatter(formatter)  # set log format in the console

    loger.addHandler(filehandler)  # add object to logger
    loger.addHandler(stream_handler)

    return loger
