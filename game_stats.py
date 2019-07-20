class GameStas():
    """跟踪游戏的统计信息"""
    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.rest_stats()
        self.height_score = 0
        #游戏刚启动时处于非活动状态
        self.game_ative = False
    def rest_stats(self):
        """初始化游戏在运行期间可能变化的统计信息"""
        self.plane_left = self.ai_settings.plane_limit
        self.score = 0
        self.level = 1