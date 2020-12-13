# --*--utf-8--*--
"""
BigWin 交易Time规则 
在中国股票市场，目前只支持T+1 也就是说，
1，我们需要跟踪交割单的标记来标记它是否在这个时刻可以被sell掉，【T+1限制】✅
2, 我们需要对已经停盘的股票限制交易， ✅
3，我们需要对涨停的股票限制买入 ，和上面相反，也是写在数据库里的；✅
4，我们需要对跌停的股票限制卖出, 在原始数据上做标注；以开盘是否跌停为限制，分钟界别以当前分钟做限制✅
5，买入的时候，要看看仓位剩余资金是否支持买入， 这个时候买入是把所有钱全部买入1手为止✅
6，卖出不能超过持仓数量；✅
"""
import datetime
from bigwin.data_manager.data_proxy import DataProxy

# 用到两部分数据 一部分是数据库 另一部分是持仓

class TranscationManager(object):
    """
    每次买卖都要经过这个接口 
    重要前提：下单接口中，我们每下单一次，都会绑定一个股票对应的订单号以及买入的时间
    使用场景： 用户直接买入后 过几天 用了卖出api 那么 我们逐个对已经存在的股票 和其订单号做检查 找到可以被卖出的股票即可；
    也就是说 持仓的股票 是由股票代码：「订单号：「日期： 几手」」这样的模式组成
    """
    STOCK = "STOCK"
    MONEY = "money"
    
    def __init__(self, 
                order_id: str, 
                now_date: str, 
                order_follow_id: str, 
                portfolio: dict, 
                order_msg: dict, 
                config: dict):
        """
        order_id: 衍生品编号
            "600132"
        now_date: 就是我们的当日回测日期
            "2020-01-01"
        order_follow_id： 订单编号
            "diuwf314bib" SHA256
        portfolio: 持仓衍生品信息  主要由 持仓衍生品代码 和其订单号 和 其买入日期 以及 持有几手组成
            {"STOCK": {"600132": {"swhudiq123": {"2020-01-01": 20}, "dwqwqd": {"2020-01-09": 30}}}, "money": 1111}
            这部分是有持仓+ 现金组成
        order_msg: 交割信息
            客户要买/卖 几手股票 或者多少仓位百分比的股票 或者 多少钱的股票 ✅
            {"buy"/"sell", : {"600132": {"percent"/"money"/"hand"}}}
            //我们要考虑每次用户下单的时候 不可能是并行的 因为持仓这个物理不支持并行 
            所以每一次请求 必定是单次请求
        config: 回测参数
        --> 重要的一点 凡事涉及到回测的 我们先把回测时间确定好 去数据库捞的时候  遇到A股票 就存储好 遇到B股票 就存储好



        """
        self.start_date = config.get("start_date")
        self.end_date = config.get("end_date")
        self.order_id = order_id
        self.now_date = now_date
        self.order_follow_id = order_follow_id
        self.portfolio = portfolio
        self.order_msg = order_msg
        self.frequency = config.get("frequency")
        self.remain_money = self.portfolio.get(self.MONEY)
        self.remain_stock = self.portfolio.get(self.STOCK)
        self.data_df = DataProxy(self.order_id, self.start_date, self.end_date, self.frequency)


    
    def get_this_day_stop(self):
        """
        通过数据库 找到这个频率下 是否是停盘的
        """
        # TODO 20201213 需要马俊杰提供文档 后续方便开发
        data_df = self.data_df.data_show_df




    def analyse_order(self):
        """
        分析用户交割行为 为后续管道作准备
        """
        buy_or_sell = self.order_msg.keys()
        order_detail = self.order_msg.get(buy_or_sell)

        









