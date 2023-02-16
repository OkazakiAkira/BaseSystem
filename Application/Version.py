class Version():
    """バージョン管理
    """
    major_ver = 1
    minor_ver = 0
    patch_ver = 0
    release_type = "α"
    
    def getVersionString():
        """バージョンの文字列を取得
        
        Returns:
            str: バージョン文字列
        """
        return f"v{Version.major_ver}.{Version.minor_ver}.{Version.patch_ver} {Version.release_type}"