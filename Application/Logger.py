from logging import getLogger, config
import yaml
import pathlib
import datetime

def set_up_logger(module_name=__name__):
    """Loggerの生成

    Parameters
    ----------
    module_name : str, optional
        モジュール名, by default __name__

    Returns
    -------
    Logger
        ロガー
    """
    # Logger設定ファイル名定義
    log_config_file = pathlib.Path.cwd().joinpath("config", "log_config.yml")
    # ログファイル出力先設定
    log_output_dir = pathlib.Path.cwd().joinpath("Logs")
    log_output_dir.mkdir(exist_ok=True, parents=True)
    # ログファイル名定義
    log_filename = log_output_dir.joinpath(
        "App_{}.log".format(datetime.datetime.now().strftime("%Y%m%d"))
        )
    
    try:
        # Logger設定ファイル読込
        with open(log_config_file, "r", encoding="utf-8") as f:
            log_conf = yaml.safe_load(f)
        # ログファイル名設定
        log_conf["handlers"]["file"]["filename"] = log_filename
        # 設定適用
        config.dictConfig(log_conf)
        # Logger生成
        logger = getLogger(module_name)
    except Exception as e:
        # Logger設定ファイル読込エラー時は、以下のデフォルト設定
        config.dictConfig({
            # バージョン(1で固定)
            "version": 1,
            # 出力フォーマットの設定
            "formatters":{
                "customFormat": {
                    "format": "%(asctime)s | %(levelname)-8s | %(name)s | %(module)s | %(funcName)s | %(lineno)d | %(message)s"
                }
            },
            # ハンドラの設定
            "handlers": {
                "file": {
                    "class": "logging.FileHandler",
                    "level": "DEBUG",   # 必要に応じて変更
                    "formatter": "customFormat",
                    "encoding": "utf-8",
                    "filename": log_filename
                },
                "console": {
                    "class": "logging.StreamHandler",
                    "level": "DEBUG",   # 必要に応じて変更
                    "formatter": "customFormat"
                }
            },
            # ルート
            "root": {
                "level": "INFO",
                "handlers": ["file"]
            },
            # 指定していない設定はrootの設定を採用
            "disable_existing_loggers": False
        })
        # Logger生成
        logger = getLogger(module_name)
        # エラー書き込み
        logger.error(f"Logger設定ファイル読込エラー:{str(e)}【デフォルト設定でログを生成します】")

    return logger