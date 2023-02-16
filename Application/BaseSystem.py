# import os
import sys
# import PySide6
from PySide6 import QtWidgets

from Logger import set_up_logger
from View.MainWindow import MainWindow

# PySide6のプラグインパス設定
# dirname = os.path.dirname(PySide6.__file__)
# plugin_path = os.path.join(dirname, "plugins", "platforms")
# os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = plugin_path

if __name__ == "__main__":
    # ロガー生成
    logger = set_up_logger(__name__)
    # logger.debug("start")
    logger.info("アプリケーション起動")
    # logger.warning("start")
    # logger.error("start")
    # logger.critical("start")
    try:
        app = QtWidgets.QApplication(sys.argv)
        win = MainWindow()
        win.show()
        logger.info("アプリケーション正常終了")
        sys.exit(app.exec())
    except Exception as e:
        logger.error(f"アプリケーション異常終了:{str(e)}")
