# coding=utf-8
from __future__ import annotations
from enum import IntEnum


class RecentIndicator(IntEnum):
    """
    近日指标提示（对应 RECENT_INDICATOR 字段 0x7D，整数码以 float 存储）。

    基于 /tdx/tdx.csv (2026-05-19) + /tdx/20260520.csv 全量分组交叉验证（每组最多50样本，100%一致）。

    用法::

        from opentdx.enums import RecentIndicator

        # 从行情接口获取原始码
        ri = quotes_data['recent_indicator']  # float, e.g. 32.0
        ind = RecentIndicator(int(ri))

        # 属性
        ind.name       # 'BEAR_ARRANGE'
        ind.value      # 32
        ind.display_name  # '空头排列'
        ind.polarity   # '多头' / '空头' / '中性'
        ind.is_bull    # True / False
        ind.is_bear    # True / False

        # 按多空分类筛选
        bull_signals = [v for v in RecentIndicator if v.is_bull]  # 13个
        bear_signals = [v for v in RecentIndicator if v.is_bear]  # 13个
    """

    MACD_GOLDEN      = 1   # MACD金叉
    MACD_DEATH       = 2   # MACD死叉
    EXPMA_GOLDEN     = 5   # EXPMA金叉
    EXPMA_DEATH      = 6   # EXPMA死叉
    KDJ_GOLDEN       = 10  # KDJ金叉
    KDJ_DEATH        = 11  # KDJ死叉
    BOLL_UP          = 20  # 上穿BOLL上轨
    BOLL_DOWN        = 21  # 跌破BOLL下轨
    BULL_ARRANGE     = 31  # 多头排列
    BEAR_ARRANGE     = 32  # 空头排列
    MA_CONVERGE      = 33  # 均线粘合
    BREAK_UP         = 50  # 向上突破平台
    BREAK_DOWN       = 51  # 向下突破平台
    PLATFORM         = 52  # 平台整理
    BOTTOM_REVERSAL  = 60  # 底部反转
    HIGH_RETREAT     = 61  # 高位回落
    SURGE_UP         = 70  # 放量上攻
    SURGE_DOWN       = 71  # 放量下挫
    PRICE_VOL_UP     = 80  # 价量齐升
    PRICE_VOL_DOWN   = 81  # 价量齐跌
    MILD_UP          = 90  # 温和放量上攻
    MILD_DOWN        = 91  # 温和放量下跌
    PHASE_SURGE      = 92  # 阶段放量
    PHASE_SHRINK     = 93  # 阶段缩量
    TOP_SURGE        = 94  # 顶部放量
    TOP_SHRINK       = 95  # 顶部缩量
    BOTTOM_SHRINK    = 97  # 底部缩量

    @property
    def display_name(self) -> str:
        return _CHINESE.get(self.value, f'未知({self.value})')

    @property
    def polarity(self) -> str:
        return _POLARITY.get(self.value, '中性')

    @property
    def is_bull(self) -> bool:
        return self.polarity == '多头'

    @property
    def is_bear(self) -> bool:
        return self.polarity == '空头'


_BULL = {1, 5, 10, 20, 31, 33, 50, 60, 70, 80, 90, 92, 97}     # MACD金,EXPMA金,KDJ金,BOLL上穿,多头,均线粘合,向上突,底部反转,放量上攻,价量齐升,温和放量上,阶段放量,底部缩量
_BEAR = {2, 6, 11, 21, 32, 51, 61, 71, 81, 91, 93, 94, 95}   # MACD死,EXPMA死,KDJ死,BOLL跌破,空头,向下突,高位回落,放量下挫,价量齐跌,温和放量下,阶段缩量,顶部放量,顶部缩量

_POLARITY = {v: '多头' for v in _BULL} | {v: '空头' for v in _BEAR}

_CHINESE = {
    1:  'MACD金叉',
    2:  'MACD死叉',
    5:  'EXPMA金叉',
    6:  'EXPMA死叉',
    10: 'KDJ金叉',
    11: 'KDJ死叉',
    20: '上穿BOLL上轨',
    21: '跌破BOLL下轨',
    31: '多头排列',
    32: '空头排列',
    33: '均线粘合',
    50: '向上突破平台',
    51: '向下突破平台',
    52: '平台整理',
    60: '底部反转',
    61: '高位回落',
    70: '放量上攻',
    71: '放量下挫',
    80:  '价量齐升',
    81:  '价量齐跌',
    90: '温和放量上攻',
    91: '温和放量下跌',
    92: '阶段放量',
    93:  '阶段缩量',
    94:  '顶部放量',
    95:  '顶部缩量',
    97: '底部缩量',
}
