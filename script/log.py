import logging

logger = logging.basicConfig(level=logging.INFO, filename="sw.log", filemode="w",
                             format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)
