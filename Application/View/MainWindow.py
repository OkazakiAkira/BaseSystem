from PySide6 import QtWidgets

from Logger import set_up_logger
from Resources import Resources


class MainWindow(QtWidgets.QMainWindow):
    """
    アプリケーションのメインウィンドウ
    """
    def __init__(self, parent=None):
        """
        コンストラクタ

        :param parent: 呼び出し元
        :type parent: 呼び出し元に依存
        """
        # Logger生成
        self.logger = set_up_logger(__name__)
        # ウィンドウ初期化
        super().__init__(parent)
        # UI初期化
        self.set_view()
        # Controller設定
        self.set_control()

    def set_view(self):
        """
        UI初期化
        """
        # ウィンドウタイトル
        self.setWindowTitle(Resources.window_title)

        # レイアウト
        self.main_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_hlayout = QtWidgets.QHBoxLayout()
        self.main_widget.setLayout(self.main_hlayout)

    def set_control(self):
        """
        Controller設定
        """
        pass