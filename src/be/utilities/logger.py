import logging

logger = logging.getLogger(">>>")


def add_log(response):
    logger.info("Request URL: " + response.request.method + " " + response.request.url)
    logger.info("Request Header: " + str(response.request.headers))
    logger.info("Request Body: " + str(response.request.body))
    logger.info("Response Header: " + str(response.headers))
    logger.info("Response Body: " + str(response.content))
