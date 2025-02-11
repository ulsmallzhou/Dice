'''
    dice v1.4 by ulsmallzhou
    2025-02-11
'''
####################################################################################################
# region 导入区
####################################################################################################
from random import seed, randint, sample
from time import time, localtime
seed(time())
from tkinter import Tk, Widget, Event, PhotoImage
from tkinter import Frame, Text, Scrollbar, Button, Canvas, Label, Toplevel
from tkinter import INSERT, END, LEFT, RIGHT, SOLID
from base64 import b64decode, b64encode
from os import path, makedirs, listdir
from io import BytesIO
from math import ceil
from functools import wraps
from typing import Union, TypeVar, Generic, Any, TypeAlias
from collections.abc import Callable
from itertools import chain, zip_longest
from traceback import format_tb
# endregion
####################################################################################################



####################################################################################################
# region 类型检查区
####################################################################################################
notgeneric_type = {'int': int, 'float': float, 'bool': bool, 'str': str, 'Callable': Callable, 'complex': complex, 'bytes': bytes}
generic_type = {'list': list, 'tuple': tuple, 'set': set, 'dict': dict}
def check_type(value: Any, type_hint: str) -> bool:
    '''检查变量类型'''
    if not isinstance(type_hint, str): raise NewError(f'Wrong hint: str needed but {type(type_hint)}')
    if value is None: return False
    type_hint = type_hint.replace(' ', '')
    all_types = {**notgeneric_type, **generic_type} # 全体类型
    if type_hint in all_types: return isinstance(value, all_types[type_hint])   # 简单类型直接匹配
    if type_hint == '': raise NewError(f'Wrong hint: no typename found')
    char_id, bracket_num, L_bracket, R_bracket, dividers = 0, 0, [], [], [] # 检查括号匹配同时记录切点
    for char in type_hint:
        if char == '[':
            if bracket_num == 0: L_bracket.append(char_id)
            bracket_num += 1
        elif char == ']':
            if bracket_num == 0: raise NewError(f'Wrong hint format: bracket not closed')
            bracket_num -= 1
            if bracket_num == 0: R_bracket.append(char_id)
        if char == '|' and bracket_num == 0: dividers.append(char_id)
        char_id += 1
    if bracket_num != 0: raise NewError(f'Wrong hint format: bracket not closed')
    L_edges, R_edges = [0] + [divider + 1 for divider in dividers], [divider - 1 for divider in dividers] + [len(type_hint) - 1]
    cuts, pairs = len(L_edges), len(L_bracket)
    for cid in range(cuts):
        string_cut = type_hint[L_edges[cid]:R_edges[cid] + 1]
        ifinside = [L_edges[cid] <= L_bracket[bid] and R_bracket[bid] <= R_edges[cid] for bid in range(pairs)]
        insidepairs = sum(ifinside)
        if insidepairs >= 2: raise NewError(f'Wrong hint format: too many brackets')
        if insidepairs == 0:
            if string_cut in all_types: result = isinstance(value, all_types[string_cut])
            else: raise NewError(f'Wrong hint: unknown type {string_cut}')
            if result: return True
        else:
            bid = ifinside.index(True)
            if L_edges[cid] == L_bracket[bid]: raise NewError(f'Wrong hint format: wrong left bracket place')
            if R_bracket[bid] != R_edges[cid]: raise NewError(f'Wrong hint format: wrong right bracket place')
            typename, subtypestr = type_hint[L_edges[cid]:L_bracket[bid]], type_hint[L_bracket[bid] + 1:R_bracket[bid]]
            char_id, bracket_num, subdividers = 0, 0, []    # 检查括号匹配同时记录切点
            for char in subtypestr:
                bracket_num = bracket_num + int(char == '[') - int(char == ']')
                if char == ',' and bracket_num == 0: subdividers.append(char_id)
                char_id += 1
            subtype_num = len(subdividers) + 1
            l_edges, r_edges = [0] + [divider + 1 for divider in subdividers], subdividers + [len(subtypestr)]
            subtypes = [subtypestr[l_edges[sid]:r_edges[sid]] for sid in range(subtype_num)]
            if typename not in generic_type: raise NewError(f'Wrong hint: unknown generic type {typename}')
            result = False
            match typename:
                case 'list':
                    if not isinstance(value, list): result = False
                    elif subtype_num == 1: result = all(check_type(subvalue, subtypes[0]) for subvalue in value)
                    elif subtype_num != len(value): result = False
                    else: result = all(check_type(subvalue, subtype) for subvalue, subtype in zip(value, subtypes))
                case 'tuple':
                    if not isinstance(value, tuple): result = False
                    elif subtype_num == 1: result = all(check_type(subvalue, subtypes[0]) for subvalue in value)
                    elif subtype_num != len(value): result = False
                    else: result = all(check_type(subvalue, subtype) for subvalue, subtype in zip(value, subtypes))
                case 'set':
                    if not isinstance(value, set): result = False
                    elif subtype_num != 1: raise NewError(f'Wrong hint format: too many subtypes')
                    else: result = all(check_type(subvalue, subtypes[0]) for subvalue in value)
                case 'dict':
                    if not isinstance(value, dict): result = False
                    elif subtype_num == 1: raise NewError(f'Wrong hint format: missing subtype of dict.value')
                    elif subtype_num != 2: raise NewError(f'Wrong hint format: too many subtypes')
                    else: 
                        keys_check = all(check_type(subvalue, subtypes[0]) for subvalue in value.keys())
                        values_check = all(check_type(subvalue, subtypes[1]) for subvalue in value.values())
                        result = keys_check and values_check
            if result: return True
    return False
def check_types(values: list[Any], type_hints: list[str]) -> bool:
    '''检查多个变量的类型'''
    if not (check_type(values, 'list | tuple') and check_type(type_hints, 'list[str]')): raise NewError(0)
    if len(values) != len(type_hints): raise NewError(2)
    return all(check_type(value, type_hint) for value, type_hint in zip(values, type_hints))
# endregion
####################################################################################################



####################################################################################################
# region 各类常量区
####################################################################################################
VERSION = '1.4'
# region 程序图标
# 图标base64字符串
iconbase64_strss = [
    '9TbBD6cAAAAASUVORK5CYII=']
iconbase64_str = ''.join(iconbase64_strss)
# endregion
# region 特殊骰点结果
# RGB相关
radix_16 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
# 扑克牌
poker_0 = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
poker_red   = ['\u2665' + pok for pok in poker_0] + ['\u2666' + pok for pok in poker_0] + ['JOKER']
poker_black = ['\u2660' + pok for pok in poker_0] + ['\u2663' + pok for pok in poker_0] + ['joker']
poker_cards = poker_red + poker_black
# 麻将牌
majang_0 = ['一', '二', '三', '四', '五', '六', '七', '八', '九']
majang_sp = ['东风', '南风', '西风', '北风', '红中', '发财', '白板']
majang_cards = [mj + '筒' for mj in majang_0] + [mj + '条' for mj in majang_0] + [mj + '万' for mj in majang_0] + majang_sp
# 卦象
gua_8 = ['乾', '巽', '离', '艮', '兑', '坎', '震', '坤']
gua_64 = [['乾'  , '姤'  , '同人', '遁'  , '履'  , '讼'  , '无妄', '否'], ['小畜', '巽'  , '家人', '渐'  , '中孚', '涣'  , '益'  , '观'],
          ['大有', '鼎'  , '离'  , '旅'  , '睽'  , '未济', '噬嗑', '晋'], ['大畜', '蛊'  , '贲'  , '艮'  , '损'  , '蒙'  , '颐'  , '剥'],
          ['夬'  , '大过', '革'  , '咸'  , '兑'  , '困'  , '随'  , '萃'], ['需'  , '井'  , '既济', '蹇'  , '节'  , '坎'  , '屯'  , '比'],
          ['大壮', '恒'  , '丰'  , '小过', '归妹', '解'  , '震'  , '豫'], ['泰'  , '升'  , '明夷', '谦'  , '临'  , '师'  , '复'  , '坤']]
gua_64_rank = [[1 , 44, 13, 33, 10, 6 , 25, 12], [9 , 57, 37, 53, 61, 59, 42, 20], [14, 50, 30, 56, 38, 64, 21, 35], [26, 18, 22, 52, 41, 4 , 27, 23],
               [43, 28, 49, 31, 58, 47, 17, 45], [5 , 48, 63, 39, 60, 29, 3 , 8 ], [34, 32, 55, 62, 54, 40, 51, 16], [11, 46, 36, 15, 19, 7 , 24, 2 ]]
gua_64_unicode = ['\u4DC0', '\u4DC1', '\u4DC2', '\u4DC3', '\u4DC4', '\u4DC5', '\u4DC6', '\u4DC7',
                  '\u4DC8', '\u4DC9', '\u4DCA', '\u4DCB', '\u4DCC', '\u4DCD', '\u4DCE', '\u4DCF',
                  '\u4DD0', '\u4DD1', '\u4DD2', '\u4DD3', '\u4DD4', '\u4DD5', '\u4DD6', '\u4DD7',
                  '\u4DD8', '\u4DD9', '\u4DDA', '\u4DDB', '\u4DDC', '\u4DDD', '\u4DDE', '\u4DDF',
                  '\u4DE0', '\u4DE1', '\u4DE2', '\u4DE3', '\u4DE4', '\u4DE5', '\u4DE6', '\u4DE7',
                  '\u4DE8', '\u4DE9', '\u4DEA', '\u4DEB', '\u4DEC', '\u4DED', '\u4DEE', '\u4DEF',
                  '\u4DF0', '\u4DF1', '\u4DF2', '\u4DF3', '\u4DF4', '\u4DF5', '\u4DF6', '\u4DF7',
                  '\u4DF8', '\u4DF9', '\u4DFA', '\u4DFB', '\u4DFC', '\u4DFD', '\u4DFE', '\u4DFF']
# 塔罗牌
large_arcana = ['O-愚者', 'I-魔术师', 'II-女祭司', 'III-女皇', 'IV-皇帝', 'V-教皇',
                'VI-恋人', 'VII-战车', 'VIII-力量', 'IX-隐者', 'X-命运之轮',
                'XI-正义', 'XII-倒吊人', 'XIII-死神', 'XIV-节制', 'XV-恶魔', 'XVI-塔',
                'XVII-星星', 'XVIII-月亮', 'XIX-太阳', 'XX-审判', 'XXI-世界']
small_arcana_0 = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '侍从', '骑士', '皇后', '国王']
small_arcana = ['权杖-' + rank for rank in small_arcana_0] + ['圣杯-' + rank for rank in small_arcana_0] + \
               ['宝剑-' + rank for rank in small_arcana_0] + ['星币-' + rank for rank in small_arcana_0]
total_arcana = large_arcana + small_arcana
# endregion
# region 合法字符
num_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operator_char = ['+', '-', '*']
compare_char = ['<', '>', '=', '≤', '≥', '≠']
against_char = ['|']
bracket_char = ['(', ')']
random_char = ['d', 'D']
special_char = ['!', 'R', 'G', 'B', 'P', 'O', 'K', 'M', 'A', 'J', 'U', 'T', 'L']
legal_char_totle = num_char + operator_char + bracket_char + compare_char + random_char + special_char
legal_char_classic = num_char + operator_char + bracket_char + ['d']
legal_char_Dfunc = legal_char_classic + ['D']
legal_char_iftrue = legal_char_classic + compare_char
legal_char_against = legal_char_classic + against_char
illegal_pears = ['()', ')0', ')1', ')2', ')3', ')4', ')5', ')6', ')7', ')8', ')9',
                 '0(', '1(', '2(', '3(', '4(', '5(', '6(', '7(', '8(', '9(', ')(',
                 '++', '+-', '+*', '-+', '--', '-*', '*+', '*-', '**', '(+', '(*', '+)', '-)', '*)']
base64_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/', '=']
base64_divide_char = [' ', '!', '@', '#', '.', '-', '[', ']']
legal_base64_char = base64_char + base64_divide_char
# endregion
# region UI常量
exestart = localtime()
MIN_WIDTH, MINHEIGHT = 500, 300
MAX_ROLL = 100
MAX_CHAR = 500
WIDTH, HEIGHT = 900, 700
HEIGHT_IPT, HEIGHT_LABEL, HEIGHT_BUTTON, HEIGHT_OPT = 50, 40, 30, 540
WIDTH_TITLE, WIDTH_IPT, WIDTH_U_D, HEIGHT_U_D, WIDTH_CLEAR, WIDTH_START = 60, 710, 15, 25, 15, 100
WIDTH_IPT_T = WIDTH_IPT + WIDTH_TITLE
WIDTH_C_D = WIDTH_U_D + WIDTH_CLEAR
BAR = 20
BUTTON_WIDTH, BUTTON_HEIGHT = 70, 30
LENGTH_FLAG = 30
HEIGHT_COLORSHOW, WIDTH_COLORSHOW = HEIGHT_IPT * 2 - 5 - LENGTH_FLAG, BUTTON_WIDTH + LENGTH_FLAG
HEIGHT_ABOVE = HEIGHT_IPT * 2 + HEIGHT_BUTTON * 2
AUTHOR = 'ulsmallzhou'
FONT_CHINESE_BOLD, FONT_CHINESE_UNBOLD = ('宋体', 18, 'bold'), ('宋体', 18, 'normal')
FONT_BUTTON_BOLD, FONT_BUTTON_UNBOLD = ('Consolas', 12, 'bold'), ('Consolas', 12, 'normal')
FONT_TEXT_BOLD, FONT_TEXT_UNBOLD = ('Consolas', 18, 'bold'), ('Consolas', 18, 'normal')
FONT_TIP_TITLE, FONT_TIP = ('宋体', 18, 'bold'), ('宋体', 12, 'normal')
TIPWINDOW_WIDTH, TIPWINDOW_HEIGHT = 600, 400
TIP_DELAY = 1000
TIP_CHANGEPAGE_WIDTH = 30
TIP_PAGE_HEIGHT = 30
TIP_TEXT_WIDTH = TIPWINDOW_WIDTH - 2 * TIP_CHANGEPAGE_WIDTH
TIP_TEXT_HEIGHT, TIP_TITLE_HEIGHT = 28, 30
# endregion
# region 特殊指令处理
codes = ['classic', 'D__func', 'if_true', 'against', 'special']
SPECIAL_ROLL_TYPES = 6
special_roll_list = ['RGB', 'POK', 'MAJ', 'GUA', 'TLL', 'TLA']
special_maxroll_list = [10, 10, 10, 10, 10, 10]
# endregion
# region 程序说明
guide_titles = ['首页', '程序界面', '合法指令', '描述嵌入', '直接输出', '更新说明']
guide_texts = [
    ['', '',
        '      欢迎使用Dice程序, 当前窗口为程序的使用说明',
        '      点击左右按键可以翻页, 或直接点击上方按钮前往对应页面',
        '      若在使用过程中发现程序做出的任何疑似bug的行为, 欢迎告知',
        '      (尤其是程序直接退出的时候)', '', '', '',
        '                        程序版本: {}'.format(VERSION),
        '                        程序作者: {}'.format(AUTHOR)],
    [
        '程序界面主要由四部分组成, 分别是控制栏、输入区、功能键、输出区',
        '控制栏包含5个按钮如下:',
        '    [显示模式]按钮按下后可以在详细模式与简洁模式之间切换',
        '    [log 导出]按钮按下后将生成本次运行的日志',
        '    [极值模式]按钮按下后将改变极值(大成功大失败)的判定方式',
        '    [提示模式]按钮按下后将显示或隐藏各部件的提示框',
        '    [字体切换]按钮按下后程序界面的字体将在加粗与不加粗之间切换',
        '    [直接模式]按钮按下后可以在直接输出模式与普通模式之间切换',
        '输入区包含两个输入文本框与若干按钮:',
        '    [指令]框内可以输入指令, 右侧指示灯绿色亮起说明指令合法',
        '    [描述]框内可以输入描述, 可以使用\u02C8[]\u02C8将指令嵌入对应位置',
        '    指令与描述输入完成后, 按下回车或按下右侧START开始计算'],
    ['', '', '',
        '功能键包含快捷键与删除键两类如下:',
        '    [快捷键]可以快速完成骰点, 共6个, 具体功能可以查看提示',
        '    [删除键]可以删除显示区内的指定部分, 共3个, 具体功能可以查看提示',
        '输出区包含一个输出文本框, 显示程序运行的结果, 可复制但不能手动编辑'],
    [
        '一个合法的指令应当遵循以下规则之一:',
        '    经典模式: 一个[合法计算式]即构成合法指令',
        '    去重模式: \u02C8[正整数]D[正整数]\u02C8即构成合法指令',
        '    比较模式: \u02C8[合法计算式][比较符][合法计算式]\u02C8即构成合法指令',
        '    对抗模式: 用\u02C8|\u02C8隔开任意数目\u02C8[合法计算式]\u02C8即构成合法指令',
        '    特殊模式: \u02C8[类别代号][不超过10的正整数]\u02C8即构成合法指令',
        '注意事项:',
        '    指令中的任何符号均为半角符号',
        '    d两侧的数字可以是任何整数, 但左侧绝对值过大时将被替换为100',
        '    指令表达式与描述文本均不应当超过500字, 否则程序不会继续',
        '    去重模式中左侧数字至少为2且必须不大于右侧数字',
        '    比较模式中比较符应当为<>=≤≥≠中的一个(<= >= !=视同≤ ≥ ≠)'],
    [
        '一个合法的计算式遵循如下规则:',
        '    (1)\u02C8[正整数]\u02C8与\u02C8(-[正整数])\u02C8与\u02C80\u02C8是合法整数',
        '    (2)\u02C8[合法整数][若干个d][合法整数]\u02C8是合法的计算式',
        '    (3)在(2)的规则中, 若干个d两侧的部分可以缺省, 默认值为1与100',
        '    (4)\u02C8[合法计算式][+或-或*][合法计算式]\u02C8是合法的计算式',
        '    (5)\u02C8([合法计算式])\u02C8视同合法整数, 因而也可以作为d前后的参数',
        '    (6)合法整数也是合法的计算式',
        '    (7)计算式运算的优先级为\u02C8()\u02C8 > \u02C8d\u02C8 > \u02C8*\u02C8 > \u02C8+\u02C8 = \u02C8-\u02C8',
        '    (8)合法计算式首字符不为\u02C8-\u02C8时, 在其前添加一个\u02C8-\u02C8仍为合法表达式',
        '合法计算式举例:',
        '    \u02C820\u02C8; \u02C8d\u02C8(等同于\u02C81d100\u02C8); \u02C8dd50\u02C8(等同于\u02C81d(1d50)\u02C8)',
        '    \u02C8(2d3+3)d*d\u02C8(等同于\u02C8(1d3+1d3+3)d100*1d100\u02C8)'],
    ['',
        '目前已经加入的类别代号:',
        '    RGB: 随机颜色, 其结果将在START键下方展示框内显示',
        '    POK: 随机扑克牌, 从54张中选出, 不重复',
        '    MAJ: 随机麻将牌, 从34张中选出, 不重复',
        '    GUA: 随机六十四卦, 从64卦中选出, 可重复',
        '    TLL: 随机塔罗牌, 从大阿卡那22张中选出, 不重复, 带正逆位',
        '    TLA: 随机塔罗牌, 从大小阿卡那共78张中选出, 不重复, 带正逆位',
        '特殊指令也可以仅有类别代号, 此时默认抽数为1, 如\u02C8RGB\u02C8等同于\u02C8RGB1\u02C8'],
    ['', '',
        '普通模式下在描述文本中加入占位符\u02C8[]\u02C8, 可以把计算结果嵌入描述文本中:',
        '    若占位符有且仅有一个, 所有结果都将嵌入该占位符的位置',
        '    若占位符有多个且与指令所得结果数量匹配, 结果将分别嵌入对应位置',
        '注意事项:',
        '    占位符的格式为\u02C8[]\u02C8, 中括号必须为半角符号且中间不能有字符',
        '    能够产生多个结果的指令包括去重模式, 对抗模式, 特殊模式',
        '    多个占位符但与结果数量不匹配时, 占位符无效, 视同无占位符情形'],
    [
        '当[直接模式]按钮显示\u02C8直接\u02C8时, 程序将启用直接输出功能:',
        '    此时描述栏内容将直接被输出到显示区内的新行, 同时描述栏将清空',
        '    此时若描述文本满足中括号匹配且中括号内是合法指令, 则指令将执行',
        '    嵌入\u02C8[]\u02C8内的指令执行后结果将直接嵌入',
        '    注意中括号匹配除括号闭合外, 不能存在嵌套',
        '使用范例:',
        '    键入\u02C8test\u02C8后回车, 则显示\u02C8test\u02C8(正常直接输出)',
        '    键入\u02C8a[1d100]b[ERR]c[]\u02C8后回车, 则显示\u02C8a[1d100=79]b[ERR]c[]\u02C8',
        '    (中括号匹配时, 其中的合法指令将被执行并嵌入, 其他情况直接输出)',
        '    键入\u02C8test[[1d100]]\u02C8后回车, 则显示\u02C8test[[1d100]]\u02C8',
        '    (中括号嵌套, 导致中括号匹配被破坏, 内容被直接输出)'],
    ['',
        'V1.0:',
        '    实现了骰点表达式识别与计算的基本逻辑, 搭建完成了整体UI框架',
        'V1.1:',
        '    实现了更多快捷键, 新增了去重指令、比较指令、对抗指令',
        'V1.2:',
        '    实现了骰点的描述功能与骰点结果在描述中的嵌入功能',
        '    实现了log的记录功能与导出功能, 新增结果显示的简洁模式',
        'V1.3:',
        '    实现了描述文本的直接输出功能, 新增了特殊指令',
        '    实现了程序窗体的大小适应功能, 新增颜色预览功能'],
    [
        'V1.4:',
        '    给各个部件增加了提示语, 并实现了程序使用说明书(本窗口)的功能',
        '    新增字体显示模式切换功能, 可由界面内控制键切换加粗与不加粗显示',
        '    实现了带颜色的输出功能, 并将骰点结果的大成失情况体现在颜色上',
        '    实现了程序的错误处理机制']]
guide_directpages = [0, 1, 3, 6, 7, 8]
# endregion
# endregion
####################################################################################################



####################################################################################################
# region 资源读取区
####################################################################################################
def verify_resource_integrity() -> tuple[bool, str]:
    '''尝试读取素材文件'''
    if not path.exists('resource.dat'): return (False, None)
    try:
        with open('resource.dat', 'rb') as datafile: resource_data = datafile.read()
    except: return (False, None)
    try: resource_str = b64decode(resource_data)
    except: return (False, None)
    return (True, resource_str)
def load_resource_str(resource_str: str) -> tuple[bool, dict[str, dict[str, dict[str, str]]]]:
    '''尝试将完整资源切割为资源文件字符串'''
    for char in resource_str:
        if char not in legal_base64_char: return (False, None)
    resource = {}
    dirs = resource_str.split(' ### ')
    for dirid in range(len(dirs)):
        if '#' in dirs[dirid]: return (False, None)
        namelen = dirs[dirid].find(']')
        if namelen == -1 or dirs[dirid][0] != '[': return (False, None)
        dir_name, dir_file = dirs[dirid][1:namelen], dirs[dirid][namelen + 1:]
        resource[dir_name] = {}
        subdirs = dir_file.split(' @@ ')
        for subdirid in range(len(subdirs)):
            if '@' in subdirs[subdirid]: return (False, None)
            namelen = subdirs[subdirid].find(']')
            if namelen == -1 or subdirs[subdirid][0] != '[': return (False, None)
            subdir_name, subdir_file = subdirs[subdirid][1:namelen], subdirs[subdirid][namelen + 1:]
            resource[dir_name][subdir_name] = {}
            basefiles = subdir_file.split(' ! ')
            for fileid in range(len(basefiles)):
                if '!' in basefiles[fileid] or ' ' in basefiles[fileid]: return (False, None)
                namelen = basefiles[fileid].find(']')
                if namelen == -1 or basefiles[fileid][0] != '[': return (False, None)
                file_name, file = basefiles[fileid][1:namelen], basefiles[fileid][namelen + 1:]
                for char in file:
                    if char not in base64_char: return (False, None)
                resource[dir_name][subdir_name][file_name] = file
    return (True, resource)
def str_to_file(resources_str: dict[str, dict[str, dict[str, str]]]) -> tuple[bool, dict[str, dict[str, dict[str, bytes]]]]:
    '''尝试将资源文件字符串转换回文件'''
    resources = {}
    for key_0 in resources_str:
        resources[key_0] = {}
        for key_1 in resources_str[key_0]:
            resources[key_0][key_1] = {}
            for key_2 in resources_str[key_0][key_1]:
                try: file = b64decode(str(resources_str[key_0][key_1][key_2]).encode('utf-8'))
                except: return (False, None)
                resources[key_0][key_1][key_2] = file
    return (True, resources)
def base64_to_png(base64_bytes: bytes) -> PhotoImage:
    '''base64字符串转图片'''
    image_stream = BytesIO(base64_bytes)
    image = PhotoImage(data = image_stream.getvalue())
    image_stream.close()
    return image
def base64_to_strdict(base64_bytes: bytes) -> str:
    '''base64字符串转str'''
    string = base64_bytes.decode('utf-8')
    wronglist = ['\r\n', '\n\r', '\r', '\uFF08', '\uFF09']
    rightlist = ['\n'  , '\n'  , '\n', '('     , ')'     ]
    for cid in range(len(wronglist)): string = string.replace(wronglist[cid], rightlist[cid])
    return string
# endregion
####################################################################################################



####################################################################################################
# region 自定义类区
####################################################################################################
class NewError(Exception):
    '''
        自定义异常\n简写代号:\n
            0 -> Wrong input type
            1 -> Wrong order
            2 -> Size not match
    '''
    errors = ['Wrong input type', 'Wrong order', 'Size not match']
    def __init__(self, arg: str | int):
        match arg:
            case message if isinstance(message, str): super().__init__(message)
            case mid if isinstance(mid, int) and 0 <= mid < len(self.errors): super().__init__(self.errors[mid])
            case _: super().__init__('Unknown error')
class Color:
    '''颜色类'''
    def __init__(self, color: str | tuple[int, int, int]):
        errormessages = ['Color.__init__() only accept str or tuple[int, int, int]',
                         'Wrong color format', 'Value out of range']
        if check_type(color, 'str'):
            if not (len(color) == 7 and color[0] == '#' and all(c in radix_16 for c in color[1:])): raise NewError(errormessages[1])
            self.r16str = color
            self.RGB = (int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16))
        elif check_type(color, 'tuple[int, int, int]'):
            if not all(0 <= cv <= 255 for cv in color): raise NewError(errormessages[2])
            self.r16str = f'#{color[0]:02X}{color[1]:02X}{color[2]:02X}'
            self.RGB = color
        else: raise NewError(errormessages[0])
    def __str__(self) -> str: return self.r16str
    def __int__(self) -> int: return int(self.r16str[1:], 16)
    def __repr__(self) -> str: return f'Color(color = {self.r16str!r})'
    def __eq__(self, anothercolor: 'Color') -> bool:
        if not check_type(anothercolor, 'Color'): raise NewError(0)
        return self.r16str == anothercolor.r16str
    def get_R(self) -> int: return self.RGB[0]
    def get_G(self) -> int: return self.RGB[1]
    def get_B(self) -> int: return self.RGB[2]
    def get_RGB(self) -> tuple[int, int, int]: self.RGB
    def RGBstr(self) -> str: return f'({self.RGB[0]:03d},{self.RGB[1]:03d},{self.RGB[2]:03d})'
    def reverse(self):
        self.RGB = (255 - self.RGB[0], 255 - self.RGB[1], 255 - self.RGB[2])
        self.r16str = f'#{self.RGB[0]:02X}{self.RGB[1]:02X}{self.RGB[2]:02X}'
notgeneric_type['Color'] = Color
GREEN, BLUE, WHITE, LIGHTYELLOW = Color('#00FF00'), Color('#0000FF'), Color('#FFFFFF'), Color('#FFFFC0')
BLACK, RED, DARKGREEN, DARKGRAY = Color('#000000'), Color('#FF0000'), Color('#00BB00'), Color('#666666')
LIGHTBLUE = Color('#00CCFF')
TIP_COLOR = LIGHTYELLOW
RESULT_COLOR, SUCCESS_COLOR, FAILURE_COLOR, TEXT_COLOR = DARKGRAY, DARKGREEN, RED, BLACK
COLORS = [BLACK, RED, GREEN, BLUE, WHITE, DARKGREEN, DARKGRAY, LIGHTYELLOW]
specialcolor_majang = {'东风': BLACK, '南风': BLACK, '西风': BLACK, '北风': BLACK, '红中': RED, '发财': DARKGREEN}
class ColorOutput:
    '''带颜色输出'''
    def __init__(self, text: str, color: Color = BLACK):
        errormessages = ['ColorOutput.__init__() only accept str and Color', 'Empty string']
        if not (isinstance(text, str) and isinstance(color, Color)): raise NewError(errormessages[0])
        if text == '': raise NewError(errormessages[1])
        self.text, self.color = text, color
    def __str__(self) -> str: return f'[color={self.color}:{self.text}]'
    def __repr__(self) -> str: return f'ColorOutput(text = {self.text!r}, color = {self.color!r})'
    def ifsamecolor(self, anotheropt: 'ColorOutput') -> bool:
        if not check_type(anotheropt, 'C_O'): raise NewError(0)
        return self.color == anotheropt.color
C_O: TypeAlias = ColorOutput
notgeneric_type['C_O'], notgeneric_type['ColorOutput'] = C_O, ColorOutput
class ColorOutputList:
    '''
        带颜色输出序列\n
        accepttypes = [list[C_O]] or [str, Color] or [list[str], list[Color]] or [str] or [C_O]
    '''
    def __init__(self, *args):
        accepttypes = ['[list[C_O]]', '[list[str], list[Color]]', '[str, Color]', '[str]', '[C_O]']
        errormessages = [f'ColorOutputList.__init__() only accept ' + ' or '.join(accepttypes),
                         'Empty string', 'Size not match']
        match args:
            case [text, color] if check_types(args, ['str', 'Color']):
                if text == '': raise NewError(errormessages[1])
                self.texts = [C_O(text, color)]
            case [texts, colors] if check_types(args, ['list[str]', 'list[Color]']):
                if len(texts) != len(colors): raise NewError(2)
                self.texts = [C_O(text, color) for text, color in zip(texts, colors)]
            case [texts] if check_types(args, ['list[C_O]']):
                if len(texts) == 0: raise NewError(errormessages[1])
                self.texts = texts
            case [text] if check_types(args, ['str']):
                if text == '': raise NewError(errormessages[1])
                self.texts = [C_O(text)]
            case [ctext] if check_types(args, ['C_O']): self.texts = [ctext]
            case _: raise NewError(errormessages[0])
        self.simplify()
    def __str__(self) -> str: return ''.join([str(text) for text in self.texts])
    def __add__(self, other: Union['ColorOutputList', list[C_O], C_O, str]) -> 'ColorOutputList':
        errormessage = 'ColorOutputList.__add__() only accept ColorOutputList or list[ColorOutput]'
        if isinstance(other, ColorOutputList): return ColorOutputList(self.texts + other.texts)
        elif check_type(other, 'list[C_O]'): return ColorOutputList(self.texts + other)
        elif check_type(other, 'C_O'): return ColorOutputList(self.texts + [other])
        elif check_type(other, 'str'): return ColorOutputList(self.texts + [C_O(other)])
        raise NewError(errormessage)
    def __radd__(self, other: Union['ColorOutputList', list[C_O], C_O, str]) -> 'ColorOutputList':
        errormessage = 'ColorOutputList.__radd__() only accept ColorOutputList or list[ColorOutput]'
        if isinstance(other, ColorOutputList): return ColorOutputList(other.texts + self.texts)
        elif check_type(other, 'list[C_O]'): return ColorOutputList(other + self.texts)
        elif check_type(other, 'C_O'): return ColorOutputList([other] + self.texts)
        elif check_type(other, 'str'): return ColorOutputList([C_O(other)] + self.texts)
        else: raise NewError(errormessage)
    def __iadd__(self, other: Union['ColorOutputList', list[C_O]]) -> 'ColorOutputList':
        errormessage = 'ColorOutputList.__add__() only accept ColorOutputList or list[ColorOutput]'
        if isinstance(other, ColorOutputList):
            self.texts.extend(other.texts)
            self.simplify()
            return self
        elif check_type(other, 'list[C_O]'):
            self.texts.extend(other)
            self.simplify()
            return self
        raise NewError(errormessage)
    def simplify(self):
        pin = 0
        while(pin + 1 < len(self.texts)):
            if self.texts[pin].ifsamecolor(self.texts[pin + 1]):
                self.texts[pin] = C_O(self.texts[pin].text + self.texts[pin + 1].text, self.texts[pin].color)
                self.texts.pop(pin + 1)
            else: pin += 1
    def get(self) -> tuple[tuple[str], tuple[str], int]: return (*zip(*[(ctext.text, ctext.color) for ctext in self.texts]), len(self.texts))
    def get_onlystr(self) -> str: return ''.join([ctext.text for ctext in self.texts])
C_O_L: TypeAlias = ColorOutputList
notgeneric_type['C_O_L'], notgeneric_type['ColorOutputList'] = C_O_L, ColorOutputList
class ResourceTree:
    '''资源树'''
    processfunc: dict[str, Callable[[str], Union[PhotoImage, str]]] = \
        {'pictures': base64_to_png, 'textlists': base64_to_strdict}
    def __init__(self, resources: dict[str, dict[str, dict[str]]]):
        '''默认resources是一个三层的字典'''
        self.resources = resources
        self.bottom_keys, self.middle_keys, self.top_keys = {}, {}, list(self.resources.keys())
        for key_0 in self.resources:
            self.bottom_keys[key_0], self.middle_keys[key_0] = {}, list(self.resources[key_0].keys())
            for key_1 in self.resources[key_0]:
                self.bottom_keys[key_0][key_1] = list(self.resources[key_0][key_1].keys())
                for key_2 in self.resources[key_0][key_1]:
                    self.resources[key_0][key_1][key_2] = self.processfunc[key_0](self.resources[key_0][key_1][key_2])
    def __getitem__(self, key: str):
        if not isinstance(key, str): raise NewError('key must be str')
        keys = key.split('/')
        if len(keys) != 3: raise NewError('key must be like [key_0/key_1/key_2]')
        if keys[0] not in self.top_keys: raise NewError(f'key_0 [{keys[0]}] not found')
        if keys[1] not in self.middle_keys[keys[0]]: raise NewError(f'key_1 [{keys[1]}] not found')
        if keys[2] not in self.bottom_keys[keys[0]][keys[1]]: raise NewError(f'key_2 [{keys[2]}] not found')
        return self.resources[keys[0]][keys[1]][keys[2]]
    def __str__(self) -> str: return str(self.bottom_keys).replace('{', '[').replace('}', ']')
    def get_keys(self, key: str = '') -> list[str]:
        if not isinstance(key, str): raise NewError('key must be str')
        if key == '': return self.top_keys
        depth, keys = key.count('/'), key.split('/')
        if depth >= 2: raise NewError('wrong key depth')
        elif depth == 0:
            if keys[0] not in self.top_keys: raise NewError(f'key_0 [{keys[0]}] not found')
            return self.middle_keys[keys[0]]
        elif depth == 1:
            if keys[0] not in self.top_keys: raise NewError(f'key_0 [{keys[0]}] not found')
            if keys[1] not in self.middle_keys[keys[0]]: raise NewError(f'key_1 [{keys[1]}] not found')
            return self.bottom_keys[keys[0]][keys[1]]
class ToolTip:
    '''提示文本框'''
    def __init__(self, widget: Widget, text: str):
        self.widget, self.text, self.tipwindow, self.id = widget, text, None, None
        self.x = self.y = 0
        self.widget.bind("<Enter>", self.schedule_showtip)
        self.widget.bind("<Leave>", self.hidetip)
    def schedule_showtip(self, event: Event):
        '''Schedule to display text in tooltip window after delay'''
        self.x, self.y = event.x_root + 10, event.y_root
        if self.id: self.widget.after_cancel(self.id)
        self.id = self.widget.after(TIP_DELAY, self.showtip)
    def showtip(self):
        '''Display text in tooltip window'''
        if not showtip_mode or self.tipwindow or not self.text: return
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f'+{self.x}+{self.y}')
        label = Label(tw, text = self.text, justify = LEFT, background = TIP_COLOR,
                      relief = SOLID, borderwidth = 1, font = FONT_TIP)
        label.pack(ipadx = 4)
    def hidetip(self, event: Event):
        '''Hide the tooltip if it exists'''
        tw = self.tipwindow
        self.tipwindow = None
        if self.id: self.id = self.widget.after_cancel(self.id)
        if tw: tw.destroy()
class GuideViewer:
    '''程序使用说明窗体'''
    def __init__(self, master: Widget, titles: list[str], pages: list[list[str]], directpages: list[int]):
        self.master, self.titles, self.pages, self.directpages = master, titles, pages, directpages
        self.current_page, self.page_num, self.title_num = 0, len(pages), len(titles)
        # 创建新窗口
        self.window = Toplevel(master)
        self.window.title(f'使用说明 v{VERSION} - by {AUTHOR}')
        self.window.geometry(f'{TIPWINDOW_WIDTH}x{TIPWINDOW_HEIGHT}')
        self.window.resizable(False, False)
        self.window.iconphoto(False, icon_image)
        self.window.grab_set()
        self.window.transient(master)
        # 显示文本
        self.title_label = Label(self.window, font = FONT_TIP_TITLE, text = ' ', justify = 'center')
        self.title_label.place(x = TIP_CHANGEPAGE_WIDTH, y = TIP_PAGE_HEIGHT, width = TIP_TEXT_WIDTH, height = TIP_TITLE_HEIGHT)
        self.lines, base_y = 12, TIP_PAGE_HEIGHT + TIP_TITLE_HEIGHT
        self.content_labels = [Label(self.window, font = FONT_TIP, text = 'test', anchor = 'w') for _ in range(self.lines)]
        for lid in range(self.lines):   # <= 340
            place_y = base_y + lid * TIP_TEXT_HEIGHT
            self.content_labels[lid].place(x = TIP_CHANGEPAGE_WIDTH, y = place_y, width = TIP_TEXT_WIDTH, height = TIP_TEXT_HEIGHT)
        # 翻页按钮
        self.prev_button = Button(self.window, text = '/\n\\', command = self.prev_page)
        self.prev_button.place(x = 0, y = 0, width = TIP_CHANGEPAGE_WIDTH, height = TIPWINDOW_HEIGHT)
        self.next_button = Button(self.window, text = '\\\n/', command = self.next_page)
        self.next_button.place(x = TIPWINDOW_WIDTH - TIP_CHANGEPAGE_WIDTH, y = 0, width = TIP_CHANGEPAGE_WIDTH, height = TIPWINDOW_HEIGHT)
        self.window.bind('<Left>', lambda event: self.prev_page())
        self.window.bind('<Right>', lambda event: self.next_page())
        self.window.bind('<Return>', lambda event: self.next_page())
        self.window.bind('<Up>', lambda event: self.prev_page())
        self.window.bind('<Down>', lambda event: self.next_page())
        self.window.bind('<space>', lambda event: self.next_page())
        self.window.bind('<Escape>', lambda event: self.window.destroy())
        # 直接去往按钮
        self.pagetitle = [sum([bid >= dpage for dpage in self.directpages]) - 1 for bid in range(self.page_num)]
        button_width = TIP_TEXT_WIDTH // self.title_num
        buttons_pages = [Button(self.window, text = f'{self.titles[bid]}', font = FONT_BUTTON_BOLD,
                                command = (lambda page = self.directpages[bid]: self.display_text(page))) for bid in range(self.title_num)]
        for bid in range(self.title_num):
            buttons_pages[bid].place(x = bid * button_width + TIP_CHANGEPAGE_WIDTH, y = 0, width = button_width, height = TIP_PAGE_HEIGHT)
        self.display_text(0)
    def display_text(self, page: int):
        self.current_page = page
        lines = len(self.pages[self.current_page])
        if lines >= self.lines: strings = self.pages[self.current_page][:self.lines]
        else: strings = self.pages[self.current_page] + [''] * (self.lines - lines)
        for lid in range(self.lines): self.content_labels[lid].configure(text = strings[lid])
        self.title_label.configure(text = self.titles[self.pagetitle[self.current_page]])
    def next_page(self): self.display_text(self.current_page + 1 if self.current_page < len(self.pages) - 1 else 0)
    def prev_page(self): self.display_text(self.current_page - 1 if self.current_page > 0 else len(self.pages) - 1)
class CardViewer:   # TODO
    '''抽卡展示窗体'''
    def __init__(self, master: Widget):
        self.maste = master
        # 创建新窗口
        self.window = Toplevel(master)
        self.window.title(f'抽卡！ v{VERSION} - by {AUTHOR}')
        self.window.geometry(f'{TIPWINDOW_WIDTH}x{TIPWINDOW_HEIGHT}')
        self.window.resizable(False, False)
        self.window.iconphoto(False, icon_image)
        self.window.grab_set()
        self.window.transient(master)
class FightViewer:  # TODO
    '''简易战斗计算窗体'''
    def __init__(self, master: Widget):
        self.maste = master
        # 创建新窗口
        self.window = Toplevel(master)
        self.window.title(f'战斗, 爽! v{VERSION} - by {AUTHOR}')
        self.window.geometry(f'{TIPWINDOW_WIDTH}x{TIPWINDOW_HEIGHT}')
        self.window.resizable(False, False)
        self.window.iconphoto(False, icon_image)
        self.window.grab_set()
        self.window.transient(master)
# endregion
####################################################################################################



####################################################################################################
# region 基础函数区
####################################################################################################
def findall(ipt: str, char: str) -> list[int]:
    '''返回字符串中指定字符的所有位置'''
    if not (isinstance(ipt, str) and isinstance(char, str)): raise NewError(f'str needed but got {type(ipt)}')
    if len(char) != 1: raise NewError(f'len(char) should be 1 but got {len(char)}')
    return [i for i in range(len(ipt)) if ipt[i] == char]
def sign(ipt: int) -> int: return (ipt > 0) - (ipt < 0)
def split_multiple(seps: list[str], ipt: str) -> list[str]:
    '''使用指定的若干字符分割字符串'''
    result = [ipt]
    for sep in seps:
        temp_result = []
        for item in result: temp_result.extend(item.split(sep))
        result = temp_result
    return result
def filter_char(ipt: str) -> str:
    '''过滤非法字符'''
    result = ''
    for char in ipt:
        if char in legal_char_totle: result += char
    return result
def filter_chinese(ipt: str) -> str:
    '''过滤非法字符(中文)'''
    return ipt.replace('\n', '').replace('\r', '')
def ifinteger(ipt: str) -> tuple[bool, int]:
    '''判断字符串是否为整数并给出其值'''
    if not isinstance(ipt, str) or ipt == '' or ipt == '-': return (False, 0)
    if ipt[0] == '-': return (True, int(ipt)) if ipt[1:].isdigit() else (False, 0)
    else: return (True, int(ipt)) if ipt.isdigit() else (False, 0)
def ifpositive(ipt: str) -> tuple[bool, int]:
    '''判断字符串是否为正整数并给出其值'''
    if_integer, value = ifinteger(ipt)
    if not if_integer or value <= 0: return (False, 0)
    return (True, value)
def if_str_legal(ipt: str) -> bool:
    '''粗略判断字符串是否合法(是字符串且长度不超过限度)'''
    return bool(0 < len(ipt) <= MAX_CHAR) if isinstance(ipt, str) else False
def if_describe_legal(ipt: str) -> bool:
    '''粗略判断描述字符串是否合法(是字符串且长度不超过限度)'''
    return bool(len(ipt) <= MAX_CHAR) if isinstance(ipt, str) else False
def if_totally_inbracket(ipt: str) -> bool:
    '''检查字符串是否只有一组主要括号且在最外侧'''
    ifmatch, _, _, main_bracket_L, main_bracket_R = bracket_match(ipt)
    return ifmatch and len(main_bracket_L) == 1 and main_bracket_L[0] == 0 and main_bracket_R[0] == len(ipt) - 1
def bracket_match(ipt: str) -> list[bool, list[int]]:
    '''返回字符串小括号是否成功匹配以及匹配时返回全部左右小括号位置'''
    if not isinstance(ipt, str): return [False, [], [], [], []] # 确保是字符串
    bracket_L, bracket_R, char_id, bracket_steak, main_bracket_L, main_bracket_R = [], [], 0, [], [], []
    for char in ipt:
        if char == '(':
            if len(bracket_steak) == 0: main_bracket_L.append(char_id)
            bracket_steak.append(char_id)
        elif char == ')':
            if len(bracket_steak) == 0: return [False, [], [], [], []]
            bracket_L.append(bracket_steak[-1])
            bracket_R.append(char_id)
            bracket_steak.pop()
            if len(bracket_steak) == 0: main_bracket_R.append(char_id)
        char_id += 1
    return [len(bracket_steak) == 0, bracket_L, bracket_R, main_bracket_L, main_bracket_R]
def squarebracket_nonest_match(ipt: str) -> tuple[bool, list[int], list[int]]:
    '''返回字符串中括号是否成功匹配且无嵌套以及匹配时返回全部最外层左右中括号位置'''
    if not isinstance(ipt, str): return [False, [], []] # 确保是字符串
    char_id, bracket_flag, main_bracket_L, main_bracket_R = 0, False, [], []
    for char in ipt:
        if char == '[':
            if bracket_flag: return [False, [], []]
            main_bracket_L.append(char_id)
            bracket_flag = True
        elif char == ']':
            if not bracket_flag: return [False, [], []]
            main_bracket_R.append(char_id)
            bracket_flag = False
        char_id += 1
    return (not bracket_flag, main_bracket_L, main_bracket_R)
def squarebracket_match(ipt: str) -> tuple[bool, list[int], list[int]]:
    '''返回字符串中括号是否成功匹配以及匹配时返回全部最外层左右中括号位置'''
    if not isinstance(ipt, str): return [False, [], [], [], []] # 确保是字符串
    char_id, bracket_num, main_bracket_L, main_bracket_R = 0, 0, [], []
    for char in ipt:
        if char == '[':
            if bracket_num == 0: main_bracket_L.append(char_id)
            bracket_num += 1
        elif char == ']':
            if bracket_num == 0: return [False, [], [], [], []]
            bracket_num -= 1
            if bracket_num == 0: main_bracket_R.append(char_id)
        char_id += 1
    return [bracket_num == 0, main_bracket_L, main_bracket_R]
def num_str(ipt_num: int) -> str:
    '''默认输入合法, 即输入为整数'''
    return str(ipt_num) if ipt_num >= 0 else '(' + str(ipt_num) + ')'
def random_base(randrange: int) -> int:
    '''默认输入合法, 即输入为整数'''
    if randrange == 0: return 0
    if randrange > 0: return randint(1, randrange)
    if randrange < 0: return randint(randrange, -1)
def putbracket(ipt: tuple[int, list[str]]) -> tuple[int, list[str]]:
    '''确保字符串有且只有一个主要括号在最外面'''
    value, strings, strings_new = ipt[0], ipt[1], []
    for string in strings:
        if if_totally_inbracket(string): strings_new.append(string)
        else: strings_new.append('(' + string + ')')
    strings_new[-1] = num_str(value)
    return (value, strings_new)
def crossmerge(ipt_out: list[str], ipt_in: list[str]) -> str:
    '''默认输入合法, 即两个输入均为列表且len(ipt_out) == len(ipt_in) + 1'''
    length = len(ipt_in)
    opt = []
    for eid in range(length): opt.extend([ipt_out[eid], ipt_in[eid]])
    opt.append(ipt_out[-1])
    return ''.join(opt)
def listmerge(ipt_l: list, ipt_r: list) -> list:
    '''默认输入合法, 即两个输入均为列表, 输出列表以ipt_l的元素起始'''
    merged_list = list(chain(*zip_longest(ipt_l, ipt_r, fillvalue = None)))
    return [item for item in merged_list if item is not None]
def listdivide(ipt_list: list, divider: Any) -> list:
    '''将divider插入ipt_list任何两个元素之间, 并返回新列表'''
    if not isinstance(ipt_list, list): raise NewError(0)
    if len(ipt_list) <= 1: return ipt_list
    out_list = [ipt_list[0]]
    for cid in range(len(ipt_list) - 1): out_list.extend([divider, ipt_list[cid + 1]])
    return out_list
def expression_split(ipt: str, if_d: bool) -> tuple[list[str]]:
    '''默认输入合法, 即输入为正常表达式'''
    _, _, _, mainbracket_L, mainbracket_R = bracket_match(ipt)
    mainbracket_num, mainbracket_text = len(mainbracket_L), []
    check_char = ['+', '-', '*', 'd'] if if_d else ['+', '-', '*']
    if mainbracket_num == 0:
        split_char = ['+', '-', '*', 'd'] if if_d else ['+', '-', '*']
        fragments, operators = split_multiple(split_char, ipt), []
        for char in ipt:
            if char in check_char: operators.append(char)
    else:
        for bid in range(mainbracket_num):
            mainbracket_text.append(ipt[mainbracket_L[bid]:mainbracket_R[bid] + 1])
            inner_length = mainbracket_R[bid] - mainbracket_L[bid] + 1
            ipt = ipt[:mainbracket_L[bid]] + '#' * inner_length + ipt[mainbracket_R[bid] + 1:]
        fragments, operators, split_place, length = [], [], [-1], len(ipt)
        for cid in range(length):
            if ipt[cid] in check_char:
                operators.append(ipt[cid])
                split_place.append(cid)
        split_num = len(split_place)
        split_place.append(length)
        for bid in range(mainbracket_num):
            ipt = ipt[:mainbracket_L[bid]] + mainbracket_text[bid] + ipt[mainbracket_R[bid] + 1:]
        for sid in range(split_num):
            fragments.append(ipt[split_place[sid] + 1:split_place[sid + 1]])
    return (fragments, operators)
def gua8_2_gua64(gua_u: int, gua_d: int):
    gua_rank, gua_name = gua_64_rank[gua_u][gua_d], gua_64[gua_u][gua_d]
    return f'{gua_name}({gua_rank},{gua_64_unicode[gua_rank - 1]})'
def split_emptypair(ipt: str) -> list[C_O_L]:
    '''把字符串从空中括号对中间切开'''
    if not isinstance(ipt, str): raise NewError(0)
    if ipt == '': return []
    splitplace = ipt.find('[]')
    if splitplace == -1: return [C_O_L(ipt)]
    return [C_O_L(ipt[:splitplace + 1]), *split_emptypair(ipt[splitplace + 1:])]
def texts_modify(texts: list[str], modifier: str) -> list[str]:
    '''对非彩色文本作前置修饰'''
    if not check_types([texts, modifier], ['list[str]', 'str']): raise NewError(0)
    if texts == []: return []
    length = len(modifier)
    texts[0] = ' ' * length + texts[0]
    for lid in range(1, len(texts)): texts[lid] = modifier + texts[lid]
    return texts
def texts_unmodify(texts: list[str], modifier_len: int) -> list[str]:
    '''对非彩色文本作前置修饰'''
    if not check_types([texts, modifier_len], ['list[str]', 'int']): raise NewError(0)
    if texts == []: return []
    for text in texts:
        if len(text) < modifier_len: raise NewError(2)
        text = text[modifier_len:]
    return texts
# endregion
####################################################################################################



####################################################################################################
# region 合法性审查
####################################################################################################
def iflegal_classic_dfunction(ipt: str):
    '''纯数字+d表达式合法性审查'''
    if len(ipt) == 0: return False              # 确保非空
    for char in ipt:
        if char not in (num_char + ['d']): return False # 确保均为数字或d
    if 'd' not in ipt: return True              # 纯数字合法
    first_d, d_num = ipt.find('d'), ipt.count('d')
    for cid in range(d_num):
        if ipt[cid + first_d] != 'd': return False
    return True
def iflegal_classic_nobracket(ipt: str) -> bool:
    '''无括号指令合法性审查'''
    if len(ipt) == 0: return False              # 确保非空
    for char in ipt:
        if char not in legal_char_classic: return False # 确保均为合法字符
    if '(' in ipt or ')' in ipt: return False   # 确保无括号
    if ipt[0] == '-': ipt = '0' + ipt           # 首位为负号则特殊处理
    fragments = split_multiple(['+', '-', '*'], ipt)
    if '' in fragments: return False            # 确保首尾不是符号且表达式合法
    f_num = len(fragments)
    for fid in range(f_num):                    # 数字+d片段合法性判别
        if not iflegal_classic_dfunction(fragments[fid]): return False
    return True                                 # 所有数字均合法则表达式合法
def iflegal_classic(ipt: str) -> bool:
    '''经典骰点指令合法性审查'''
    if len(ipt) == 0: return False              # 确保非空
    for char in ipt:
        if char not in legal_char_classic: return False # 确保均为合法字符
    for illagal_pear in illegal_pears:
        if illagal_pear in ipt: return False    # 确保没有非法连接组合
    if_bracket_match, _, _, mainbracket_L, mainbracket_R = bracket_match(ipt)
    if not if_bracket_match: return False       # 确保括号匹配
    mainbracket_num = len(mainbracket_L)
    if mainbracket_num == 0: return iflegal_classic_nobracket(ipt)  # 进入无括号判别阶段
    else:
        for bid in range(mainbracket_num):
            if not iflegal_classic(ipt[mainbracket_L[bid] + 1:mainbracket_R[bid]]): return False
            inner_length = mainbracket_R[bid] - mainbracket_L[bid] + 1
            ipt = ipt[:mainbracket_L[bid]] + '0' * inner_length + ipt[mainbracket_R[bid] + 1:]
        return iflegal_classic_nobracket(ipt)
def iflegal_Dfunc(ipt: str) -> bool:
    for char in ipt:
        if char not in legal_char_Dfunc: return False   # 确保均为合法字符
    if len(ipt) < 3 or ipt[0] == 'D' or ipt[-1] == 'D' or ipt.count('D') != 1: return False
    fragments = ipt.split('D')
    ifp_l, left_int = ifpositive(fragments[0])
    ifp_r, right_int = ifpositive(fragments[1])
    if not (ifp_l and ifp_r): return False
    return bool(right_int >= 3 and left_int >= 2 and left_int <= MAX_ROLL and right_int >= left_int)
def iflegal_iftrue(ipt: str) -> bool:
    ipt = ipt.replace('<=', '≤').replace('>=', '≥').replace('!=', '≠')  # 替换双拼写法
    for char in ipt:
        if char not in legal_char_iftrue: return False  # 确保均为合法字符
    if ipt[0] in compare_char or ipt[-1] in compare_char: return False  # 确保首尾不是符号
    compare_char_num = [ipt.count(char) for char in compare_char]
    if sum(compare_char_num) != 1: return False         # 确保只有一个比较符号
    compare_sign = compare_char[compare_char_num.index(1)]
    fragments = ipt.split(compare_sign)
    return iflegal_classic(fragments[0]) and iflegal_classic(fragments[1])
def iflegal_against(ipt: str) -> bool:
    for char in ipt:
        if char not in legal_char_against: return False # 确保均为合法字符
    fragments = ipt.split('|')
    if '' in fragments: return False                    # 确保首尾不是符号且表达式合法
    for fragment in fragments:
        if not iflegal_classic(fragment): return False  # 确保每个分部合法
    return True
def iflegal_special(ipt: str) -> tuple[bool, str, int]:
    if ipt[-1] not in num_char: ipt = ipt + '1'
    for sid in range(SPECIAL_ROLL_TYPES):
        order_len = len(special_roll_list[sid])
        if ipt[:order_len] == special_roll_list[sid]:
            if_positive, value = ifpositive(ipt[order_len:])
            if if_positive and (value <= special_maxroll_list[sid]): return (True, special_roll_list[sid], value)
    return (False, '', 0)
def iflegal_branch(ipt: str, code: str) -> bool:
    '''根据code选择不同的判断函数'''
    if not if_str_legal(ipt): return False  # 确保是不过长非空字符串
    ipt.replace(' ', '')                    # 去掉所有空格
    match code:
        case 'classic': return iflegal_classic(ipt)
        case 'D__func': return iflegal_Dfunc(ipt)
        case 'if_true': return iflegal_iftrue(ipt)
        case 'against': return iflegal_against(ipt)
        case 'special': return iflegal_special(ipt)[0]
        case _: return False
def iflegal_total(ipt: str) -> str:
    '''如果表达式合法则返回code'''
    for code in codes:
        if iflegal_branch(ipt, code): return code
    return ''
def iflegal_direct_describe(ipts: list[str]) -> list[str]:
    '''检测若干部分的字符串是否全部合法并返回每个部分的code'''
    return [iflegal_total(ipt) for ipt in ipts]
def standardization(ipt: str, code: str) -> str:
    '''默认输入为合法字符串'''
    replace_0 = ['+d', '-d', '*d', '(d', 'd+', 'd-', 'd*', 'd)', '(-']
    replace_1 = ['+1d', '-1d', '*1d', '(1d', 'd100+', 'd100-', 'd100*', 'd100)', '(0-']
    match code:
        case 'classic':
            if ipt[0] == '-': ipt = '0' + ipt
            if ipt[0] == 'd': ipt = '1' + ipt
            if ipt[-1] == 'd': ipt = ipt + '100'
            for rid in range(len(replace_0)): ipt = ipt.replace(replace_0[rid], replace_1[rid])
            return ipt
        case 'D__func':
            fragments = ipt.split('D')
            return str(int(fragments[0])) + 'D' + str(int(fragments[1]))
        case 'if_true':
            ipt = ipt.replace('<=', '≤').replace('>=', '≥').replace('!=', '≠')
            compare_sign = compare_char[[ipt.count(char) for char in compare_char].index(1)]
            fragments = ipt.split(compare_sign)
            return standardization(fragments[0], 'classic') + compare_sign + standardization(fragments[1], 'classic')
        case 'against':
            fragments = ipt.split('|')
            return '|'.join([standardization(fragment, 'classic') for fragment in fragments])
        case 'special':
            _, order, roll_num = iflegal_special(ipt)
            return order + str(roll_num)
# endregion
####################################################################################################



####################################################################################################
# region 极端值判断
####################################################################################################
def minmax_listmerge(ranges: list[tuple[int, int]]) -> tuple[int, int]:
    '''默认输入合法'''
    return (min([range[0] for range in ranges]), max([range[1] for range in ranges]))
def minmax_merge(range_1: tuple[int, int], range_2: tuple[int, int], operator: str) -> tuple[int, int]:
    match operator:
        case '+': return (range_1[0] + range_2[0], range_1[1] + range_2[1])
        case '-': return (range_1[0] - range_2[1], range_1[1] - range_2[0])
        case '*':
            values = [range_1[0] * range_2[0], range_1[0] * range_2[1], range_1[1] * range_2[0], range_1[1] * range_2[1]]
            return (min(values), max(values))
    return (0, 0)
def minmax_calculation(ranges: list[tuple[int, int]], operators: list[str]) -> tuple[int, int]:
    '''默认输入合法, 即两个输入均为列表且len(values) == len(operators) + 1'''
    while('*' in operators):
        first_index = operators.index('*')
        newrange = minmax_merge(ranges[first_index], ranges[first_index + 1], '*')
        ranges = ranges[:first_index] + [newrange] + ranges[first_index + 2:]
        operators = operators[:first_index] + operators[first_index + 1:]
    while(operators != []):
        newrange = minmax_merge(ranges[0], ranges[1], '+') if operators[0] == '+' else minmax_merge(ranges[0], ranges[1], '-')
        ranges = [newrange] + ranges[2:]
        operators = operators[1:]
    return ranges[0]
def minmax_dfunction(d_left: int, d_right: int) -> tuple[int, int]:
    '''默认输入合法, 即三个输入均为整数且d_num为正'''
    signs = sign(d_left) * sign(d_right)
    return (0, 0) if signs == 0 else ((d_left * d_right, -1) if signs == -1 else (1, d_left * d_right))
def minmax_nooperator(ipt: str) -> tuple[int, int]:
    '''默认输入合法, 即无外部加减乘'''
    fragments, operators = expression_split(ipt, True)
    d_num = len(operators)
    if operators == []: return minmax_dice(ipt[1:-1]) if ipt[0] == '(' else (int(ipt), int(ipt))
    leftt, right = fragments[0], fragments[-1]
    leftt_min, leftt_max = minmax_dice(leftt[1:-1]) if leftt[0] == '(' else (int(leftt), int(leftt))
    right_min, right_max = minmax_dice(right[1:-1]) if right[0] == '(' else (int(right), int(right))
    return minmax_listmerge([minmax_dfunction(leftt_min, right_min), minmax_dfunction(leftt_max, right_min),
                             minmax_dfunction(leftt_min, right_max), minmax_dfunction(leftt_max, right_max)])
def minmax_dice(ipt: str) -> tuple[int, int]:
    '''默认输入合法'''
    ipt = standardization(ipt, 'classic')
    fragments, operators = expression_split(ipt, False)
    if operators == []: return minmax_nooperator(ipt)
    return minmax_calculation([minmax_dice(fragment) for fragment in fragments], operators)
def decide_extreme(value: int, minvalue: int, maxvalue: int) -> Color:
    '''默认输入合法, 即输入为整数且最小值<=输入值<=最大值'''
    # extreme_list = ['无大成失', '1点', '2点', '3点', '4点', '5点', '3%', '4%', '5%']
    range_100 = (maxvalue - minvalue) / 100
    delta_list: list[int] = [-1, 0, 1, 2, 3, 4, ceil(3 * range_100 - 1), ceil(4 * range_100 - 1), ceil(5 * range_100 - 1)]
    succ, fail = maxvalue - delta_list[extreme_mode], minvalue + delta_list[extreme_mode]
    if value >= succ: return SUCCESS_COLOR
    elif value <= fail: return FAILURE_COLOR
    return RESULT_COLOR
# endregion
####################################################################################################



####################################################################################################
# region 计算与显示
####################################################################################################
def calculation(values: list[int], operators: list[str]) -> tuple[int, list[str]]:
    '''默认输入合法, 即两个输入均为列表且len(values) == len(operators) + 1'''
    values_str = [num_str(value) for value in values]
    opt_strings = [crossmerge(values_str, operators)]
    while('*' in operators):
        first_index = operators.index('*')
        newvalue = values[first_index] * values[first_index + 1]
        values = values[:first_index] + [newvalue] + values[first_index + 2:]
        operators = operators[:first_index] + operators[first_index + 1:]
    values_str = [num_str(value) for value in values]
    new_string = crossmerge(values_str, operators)
    if opt_strings[0] != new_string: opt_strings.append(new_string)
    while(operators != []):
        newvalue = values[0] + values[1] if operators[0] == '+' else values[0] - values[1]
        values = [newvalue] + values[2:]
        operators = operators[1:]
    opt_strings.append(num_str(values[0]))
    return (values[0], opt_strings)
def random_dfunction(d_left: int, d_right: int = 100, d_num: int = 1) -> tuple[int, list[str]]:
    '''默认输入合法, 即三个输入均为整数且d_num为正'''
    if d_left == 0: return (0, ['0' + 'd' * d_num + num_str(d_right), '0'])
    if d_right == 0: return (0, [num_str(d_left) + 'd' * d_num + '0', '0'])
    if d_left < 0:  # 该块后d_left为正
        result, strings = random_dfunction(-d_left, -d_right, d_num)
        strings.insert(0, num_str(d_left) + 'd' * d_num + num_str(d_right))
        return (result, strings)
    if d_left > 1:  # 该块后d_left == 1
        d_left = min(d_left, MAX_ROLL)  # 避免d_left过大
        results, stringss, opt_strs = [], [], [num_str(d_left) + 'd' * d_num + num_str(d_right)]
        for _ in range(d_left):
            result, strings = random_dfunction(1, d_right, d_num)
            results.append(result)
            stringss.append(strings)
        str_num = len(stringss[0])
        for line_id in range(str_num):
            str_trans = '('
            for part in range(d_left):
                str_trans = str_trans + stringss[part][line_id] + '+'
            opt_strs.append(str_trans[:-1] + ')')
        result_opt = sum(results)
        opt_strs.append(num_str(result_opt))
        return (result_opt, opt_strs)
    result_0, strings_opt = d_right, []
    for dice_id in range(d_num):
        strings_opt.append('1' + 'd' * (d_num - dice_id) + num_str(result_0))
        result_0 = random_base(result_0)
    strings_opt.append(num_str(result_0))
    return (result_0, strings_opt)
def random_nooperator(ipt: str) -> tuple[int, list[str]]:
    '''默认输入合法, 即无外部加减乘'''
    fragments, operators = expression_split(ipt, True)
    d_num = len(operators)
    if operators == []: return putbracket(dice(ipt[1:-1])) if ipt[0] == '(' else (int(ipt), [str(int(ipt))])
    leftt, right = fragments[0], fragments[-1]
    leftt_value, leftt_strs = putbracket(dice(leftt[1:-1])) if leftt[0] == '(' else (int(leftt), [num_str(int(leftt))])
    right_value, right_strs = putbracket(dice(right[1:-1])) if right[0] == '(' else (int(right), [num_str(int(right))])
    value, strings_d = random_dfunction(leftt_value, right_value, d_num)
    length_l, length_r = len(leftt_strs), len(right_strs)
    length_max = max(length_l, length_r)
    strings = []
    for line_id in range(length_max):
        if line_id >= length_l: leftt_strs.append(leftt_strs[-1])
        if line_id >= length_r: right_strs.append(right_strs[-1])
        strings.append(leftt_strs[line_id] + 'd' * d_num + right_strs[line_id])
    strings = strings + strings_d[1:]
    return (value, strings)
def dice(ipt: str) -> tuple[int, list[str]]:
    '''默认输入合法'''
    ipt = standardization(ipt, 'classic')
    fragments, operators = expression_split(ipt, False)
    parts_num = len(fragments)
    if operators == []: return random_nooperator(ipt)
    values: list[int] = []
    stringss: list[list[str]] = []
    for fragment in fragments:
        value, strings = dice(fragment)
        values.append(value)
        stringss.append(strings)
    lengths = [len(strings) for strings in stringss]
    max_length, strings_opt = max(lengths), []
    for line_id in range(max_length):
        for part_id in range(parts_num):
            if line_id >= lengths[part_id]: stringss[part_id].append(stringss[part_id][-1])
        thisline = [strings[line_id] for strings in stringss]
        strings_opt.append(crossmerge(thisline, operators))
    value_final, strings_final = calculation(values, operators)
    strings_opt.extend(strings_final[1:])
    return (value_final, strings_opt)
def nopro_calculation(values: list[int], operators: list[str]) -> int:
    '''默认输入合法, 即两个输入均为列表且len(values) == len(operators) + 1'''
    while('*' in operators):
        first_index = operators.index('*')
        newvalue = values[first_index] * values[first_index + 1]
        values = values[:first_index] + [newvalue] + values[first_index + 2:]
        operators = operators[:first_index] + operators[first_index + 1:]
    while(operators != []):
        newvalue = values[0] + values[1] if operators[0] == '+' else values[0] - values[1]
        values = [newvalue] + values[2:]
        operators = operators[1:]
    return values[0]
def nopro_random_dfunction(d_left: int, d_right: int = 100, d_num: int = 1) -> int:
    '''默认输入合法, 即三个输入均为整数且d_num为正'''
    if d_left == 0 or d_right == 0: return 0
    if d_left < 0: return nopro_random_dfunction(-d_left, -d_right, d_num)
    if d_left > 1:  # 该块后d_left == 1
        d_left = min(d_left, MAX_ROLL)  # 避免d_left过大
        return sum([nopro_random_dfunction(1, d_right, d_num) for _ in range(d_left)])
    result_0 = d_right
    for _ in range(d_num): result_0 = random_base(result_0)
    return result_0
def nopro_random_nooperator(ipt: str) -> int:
    '''默认输入合法, 即无外部加减乘'''
    fragments, operators = expression_split(ipt, True)
    d_num = len(operators)
    if operators == []: return nopro_dice(ipt[1:-1])[0] if ipt[0] == '(' else int(ipt)
    leftt, right = fragments[0], fragments[-1]
    leftt_value = nopro_dice(leftt[1:-1])[0] if leftt[0] == '(' else int(leftt)
    right_value = nopro_dice(right[1:-1])[0] if right[0] == '(' else int(right)
    return nopro_random_dfunction(leftt_value, right_value, d_num)
def nopro_dice(ipt: str) -> tuple[int, list[str]]:
    '''默认输入合法'''
    ipt = standardization(ipt, 'classic')
    fragments, operators = expression_split(ipt, False)
    if operators == []: return (nopro_random_nooperator(ipt), [])
    values = [nopro_dice(fragment)[0] for fragment in fragments]
    return (nopro_calculation(values, operators), [])
def D_function(ipt: str) -> tuple[list[int], list[str]]:
    '''默认输入合法, 即数字D数字且数字大小符合要求'''
    fragments = ipt.split('D')
    D_left, D_right = int(fragments[0]), int(fragments[1])
    input_string = str(D_left) + 'D' + str(D_right)
    results = sample(range(1, D_right + 1), D_left)
    strings = [input_string, ','.join([str(value) for value in results])]
    return (results, strings)
def nopro_D_function(ipt: str) -> tuple[list[int], list[str]]:
    '''默认输入合法, 即数字D数字且数字大小符合要求'''
    D_left, D_right = [int(fragment) for fragment in ipt.split('D')][:2]
    return (sample(range(1, D_right + 1), D_left), [])
def iftrue(ipt: str) -> tuple[tuple[int, int, str, str], list[str]]:
    '''默认输入合法, 即表达式-不等式-表达式'''
    ipt = ipt.replace('<=', '≤').replace('>=', '≥').replace('!=', '≠')
    compare_sign = compare_char[[ipt.count(char) for char in compare_char].index(1)]
    fragments = ipt.split(compare_sign)
    values: list[int] = []
    stringss: list[list[str]] = []
    for fragment in fragments:
        value, strings = dice(fragment)
        strings = [string[1:-1] if if_totally_inbracket(string) else string for string in strings]
        values.append(value)
        stringss.append(strings)
    lengths = [len(strings) for strings in stringss]
    max_length, strings_opt = max(lengths), []
    for line_id in range(max_length):
        for eid in range(2):
            if line_id >= lengths[eid]: stringss[eid].append(stringss[eid][-1])
        thisline = [strings[line_id] for strings in stringss]
        strings_opt.append((' ' + compare_sign + ' ').join(thisline))
    lvalue, rvalue = values[0], values[1]
    value_dict = {'<': lvalue < rvalue, '≤': lvalue <= rvalue, '=': lvalue == rvalue,
                  '>': lvalue > rvalue, '≥': lvalue >= rvalue, '≠': lvalue != rvalue}
    result = '成功!' if value_dict[compare_sign] else '失败!'
    return ((lvalue, rvalue, compare_sign, result), strings_opt)
def nopro_iftrue(ipt: str) -> tuple[tuple[int, int, str, str], list[str]]:
    '''默认输入合法, 即表达式-比较符-表达式'''
    ipt = ipt.replace('<=', '≤').replace('>=', '≥').replace('!=', '≠')
    compare_sign = compare_char[[ipt.count(char) for char in compare_char].index(1)]
    values = [nopro_dice(fragment)[0] for fragment in ipt.split(compare_sign)]
    lvalue, rvalue = values[0], values[1]
    value_dict = {'<': lvalue < rvalue, '≤': lvalue <= rvalue, '=': lvalue == rvalue,
                  '>': lvalue > rvalue, '≥': lvalue >= rvalue, '≠': lvalue != rvalue}
    result = '成功!' if value_dict[compare_sign] else '失败!'
    return ((lvalue, rvalue, compare_sign, result), [])
def against(ipt: str) -> tuple[list[int], list[str]]:
    '''默认输入合法, 即表达式:表达式[:表达式]^n'''
    fragments = ipt.split('|')
    values: list[int] = []
    stringss: list[list[str]] = []
    expression_num = len(fragments)
    for fragment in fragments:
        value, strings = dice(fragment)
        strings = [string[1:-1] if if_totally_inbracket(string) else string for string in strings]
        values.append(value)
        stringss.append(strings)
    lengths = [len(strings) for strings in stringss]
    max_length, strings_opt = max(lengths), []
    for line_id in range(max_length):
        for eid in range(expression_num):
            if line_id >= lengths[eid]: stringss[eid].append(stringss[eid][-1])
        thisline = [strings[line_id] for strings in stringss]
        strings_opt.append('| ' + ' | '.join(thisline) + ' |')
    return (values, strings_opt)
def nopro_against(ipt: str) -> tuple[list[int], list[str]]:
    '''默认输入合法, 即表达式|表达式[|表达式]^n'''
    return ([nopro_dice(fragment)[0] for fragment in ipt.split('|')], [])
def special(ipt: str) -> tuple[list[Color | tuple[int] | str | tuple[str, bool]], list[str]]:
    opt_value = []
    _, order, roll_num = iflegal_special(ipt)
    match order:
        case 'RGB': opt_value = [Color((randint(0, 255), randint(0, 255), randint(0, 255))) for _ in range(roll_num)]
        case 'POK': opt_value = sample(poker_cards, roll_num)
        case 'MAJ': opt_value = sample(majang_cards, roll_num)
        case 'GUA': opt_value = [(randint(0, 7), randint(0, 7)) for _ in range(roll_num)]
        case 'TLL': opt_value = [(a_card, bool(randint(0, 1))) for a_card in sample(large_arcana, roll_num)]
        case 'TLA': opt_value = [(a_card, bool(randint(0, 1))) for a_card in sample(total_arcana, roll_num)]
    return (opt_value, [])
def branch(ipt: str, code: str, mode: bool) -> tuple[int | str | list | tuple, list[str]]:
    '''根据code和mode(True: 详细)选择不同的处理函数'''
    match (code, mode):
        case ('classic', True): value, texts = dice(ipt)
        case ('classic', False): value, texts = nopro_dice(ipt)
        case ('D__func', True): value, texts = D_function(ipt)
        case ('D__func', False): value, texts = nopro_D_function(ipt)
        case ('if_true', True): value, texts = iftrue(ipt)
        case ('if_true', False): value, texts = nopro_iftrue(ipt)
        case ('against', True): value, texts = against(ipt)
        case ('against', False): value, texts = nopro_against(ipt)
        case ('special', True) | ('special', False): value, texts = special(ipt)
        case _: value, texts = [None, []]
    match code:
        case 'classic' | 'D__func' | 'against': texts = texts_modify(texts, '= ')
        case 'if_true': texts = texts_modify(texts, '→ ')
    return (value, texts)
def embed(iptstr: str, code: str, value: int | str | list | tuple) -> tuple[C_O_L, list[C_O_L]]:
    '''本身不承担计算任务, 仅用作文本嵌入'''
    if not (isinstance(iptstr, str) and isinstance(code, str)): raise NewError(0)
    if code not in codes or not iflegal_branch(iptstr, code): raise NewError(1)
    ipt_std = standardization(iptstr, code)
    match code:
        case 'classic':
            if not check_type(value, 'int'): raise NewError(0)
            fincolor = decide_extreme(value, *minmax_dice(ipt_std))
            final = C_O_L([ipt_std + '=', str(value)], [TEXT_COLOR, fincolor])
            final_list = [final]
        case 'D__func':
            if not check_type(value, 'list[int]'): raise NewError(0)
            final_list = [C_O_L(str(avalue), RESULT_COLOR) for avalue in value]
            final = sum(listdivide(final_list, ','), C_O_L(ipt_std + '='))
        case 'if_true':
            if not check_type(value, 'tuple[int, int, str, str]'): raise NewError(0)
            str_list = [ipt_std + '→', f'{value[0]}{value[2]}{value[1]}', ',', value[3]]
            col_list = [TEXT_COLOR, RESULT_COLOR, TEXT_COLOR, SUCCESS_COLOR if value[3] == '成功!' else FAILURE_COLOR]
            final = C_O_L(str_list, col_list)
            final_list = [final]
        case 'against':
            if not check_type(value, 'list[int]'): raise NewError(0)
            ipts = ipt_std.split('|')
            colors = [decide_extreme(avalue, *minmax_dice(ipt)) for ipt, avalue in zip(ipts, value)]
            final_list = [C_O_L([ipt + '=', str(avalue)], [TEXT_COLOR, color]) for ipt, avalue, color in zip(ipts, value, colors)]
            insertedlist = listdivide(final_list, '|')
            final = sum(insertedlist[1:], insertedlist[0])
        case 'special':
            _, order, _ = iflegal_special(ipt_std)
            match order:
                case 'RGB':
                    if not check_type(value, 'list[Color]'): raise NewError(0)
                    final_list = [C_O_L(str(avalue), RESULT_COLOR) for avalue in value]
                case 'POK':
                    if not check_type(value, 'list[str]'): raise NewError(0)
                    final_list = [C_O_L(avalue, RED if avalue in poker_red else BLACK) for avalue in value]
                case 'MAJ':
                    if not check_type(value, 'list[str]'): raise NewError(0)
                    final_list = [C_O_L(avalue, specialcolor_majang[avalue] if avalue in specialcolor_majang else RESULT_COLOR) for avalue in value]
                case 'GUA':
                    if not check_type(value, 'list[tuple[int]]'): raise NewError(0)
                    final_list = [C_O_L(gua8_2_gua64(avalue[0], avalue[1]), RESULT_COLOR) for avalue in value]
                case 'TLL' | 'TLA':
                    if not check_type(value, 'list[tuple[str, bool]]'): raise NewError(0)
                    card_orders = [('(正)', DARKGREEN) if avalue[1] else ('(逆)', RED) for avalue in value]
                    final_list = [C_O_L([avalue[0], anorder[0]], [RESULT_COLOR, anorder[1]]) for avalue, anorder in zip(value, card_orders)]
            insertedlist = listdivide(final_list, ',')
            final = sum(insertedlist[1:], insertedlist[0])
    return (final, final_list)
# endregion
####################################################################################################



####################################################################################################
# region 可视化框架
####################################################################################################
# 窗口
root = Tk()
root.title(f'Dice v{VERSION} - by {AUTHOR}')
root.geometry(str(WIDTH) + 'x' + str(HEIGHT))
root.minsize(MIN_WIDTH, MINHEIGHT)
icon_image = base64_to_png(b64decode(iconbase64_str.encode('utf-8')))
root.iconphoto(False, icon_image)
# 全局控制变量
input_string_list, input_temp, input_pin,  = [], '', -1
output_lines_list, output_value_list, output_types_list, output_ranks_list = [], [], [], []
output_lists = [output_lines_list, output_value_list, output_types_list, output_ranks_list]
displayed_output = ''
display_mode: bool = True
extreme_mode: int = 0
showtip_mode: bool = False
if_bold_mode: bool = True
direct__mode: bool = False
logs_strings, logs_types, log_times, log_num, errlog = [], [], [], 0, ''
# 程序控制区
def dynamic_controls_size(event):
    '''根据窗口大小调整各控件大小和位置'''
    window_width, window_height = root.winfo_width(), root.winfo_height()
    # 程序控制区
    label_explain.place(x = window_width - BUTTON_HEIGHT, y = 0, width = BUTTON_HEIGHT, height = BUTTON_HEIGHT)
    # 结果输出区
    text_frame_2.place(x = 0, y = HEIGHT_ABOVE, width = window_width, height = window_height - HEIGHT_ABOVE)
    text_opt.place(x = 0, y = 0, width = window_width - BAR, height = window_height - HEIGHT_ABOVE - BAR)
    scrollbar_y.place(x = window_width - BAR, y = 0, width = BAR, height = window_height - HEIGHT_ABOVE)
    scrollbar_x.place(x = 0, y = window_height - HEIGHT_ABOVE - BAR, width = window_width, height = BAR)
    # 内容输入区
    text_frame_1.place(x = 0, y = BUTTON_HEIGHT, width = window_width, height = HEIGHT_IPT * 2)
    width_ipttext_new = window_width - WIDTH + WIDTH_IPT_T - WIDTH_TITLE
    text_ipt.place(x = WIDTH_TITLE, y = 0, width = width_ipttext_new, height = HEIGHT_IPT - BAR)
    scrollbar_ipt.place(x = WIDTH_TITLE, y = HEIGHT_IPT - BAR, width = width_ipttext_new, height = BAR)
    text_describe.place(x = WIDTH_TITLE, y = HEIGHT_IPT, width = width_ipttext_new, height = HEIGHT_IPT - BAR)
    scrollbar_describe.place(x = WIDTH_TITLE, y = HEIGHT_IPT * 2 - BAR, width = width_ipttext_new, height = BAR)
    text_input_control_frame.place(x = window_width - WIDTH + WIDTH_IPT_T, y = 0, width = WIDTH - WIDTH_IPT_T, height = HEIGHT_IPT * 2)
    # 删除键
    delete_frame.place(x = window_width - 3 * BUTTON_WIDTH, y = HEIGHT_IPT * 2 + BUTTON_HEIGHT, width = 3 * BUTTON_WIDTH, height = HEIGHT_BUTTON)
def change_button_text(name: str, newtext: str):
    '''改变控制区按钮文本'''
    if not (isinstance(name, str) and isinstance(newtext, str)): raise NewError(0)
    buttons_controls[control_names.index(name)].config(text = newtext)
def create_log(ipt_strings: list[str], ipt_type: str):
    '''创建一条log'''
    if not (check_type(ipt_strings, 'list[str]') and isinstance(ipt_type, str)): raise NewError(0)
    logs_strings.append(ipt_strings)
    logs_types.append(ipt_type)
    now = localtime()
    log_times.append(f'{now.tm_hour}:{now.tm_min}:{now.tm_sec}')
    globals()['log_num'] += 1
def export_log():
    '''导出全部log'''
    if not path.exists('__logs__'): makedirs('__logs__')
    now = localtime()
    timestr_start = f'{exestart.tm_year}-{exestart.tm_mon}-{exestart.tm_mday} {exestart.tm_hour}:{exestart.tm_min}:{exestart.tm_sec}'
    timestr_log = f'{now.tm_year}-{now.tm_mon}-{now.tm_mday} {now.tm_hour}:{now.tm_min}:{now.tm_sec}'
    log_name = f'_{now.tm_year}-{now.tm_mon}-{now.tm_mday}-{now.tm_hour}-{now.tm_min}-{now.tm_sec}_log.txt'
    with open('__logs__\\' + log_name, 'w', encoding = 'utf-8') as log_file:
        log_file.write('Program start time: ' + timestr_start + '\n')
        log_file.write('Log export time: ' + timestr_log + '\n')
        log_file.write(f'Total logs: {log_num} ({log_num - len(output_ranks_list)} deleted)\n\n')
        for log_id in range(log_num):
            log_file.write(f'log {log_id + 1}' + f'' if log_id in output_ranks_list else f' (deleted)')
            log_file.write(f': ({log_times[log_id]}){logs_types[log_id]}\n')
            for string in logs_strings[log_id]: log_file.write(string + '\n')
            log_file.write('\n')
        log_file.write('final outputs:\n\n')
        log_file.write(displayed_output)
        if errlog != '': log_file.write('\n\nerror log:\n' + errlog)
def display_mode_switch():
    '''切换显示模式, 简洁或详细'''
    global display_mode
    display_mode = not display_mode
    change_button_text('display', '详细' if display_mode else '简洁')
def extreme_mode_switch():
    '''切换大成失模式'''
    global extreme_mode
    extreme_list = ['无大成失', '1点', '2点', '3点', '4点', '5点', '3%', '4%', '5%']
    extreme_mode = 0 if extreme_mode == len(extreme_list) - 1 else extreme_mode + 1
    change_button_text('extreme', extreme_list[extreme_mode])
def showtip_mode_switch():
    '''切换提示模式'''
    global showtip_mode
    showtip_mode = not showtip_mode
    change_button_text('tip', '有提示' if showtip_mode else '无提示')
def font_mode_switch():
    '''切换显示字体'''
    global if_bold_mode
    if_bold_mode = not if_bold_mode
    change_button_text('bold', '加粗' if if_bold_mode else '不加粗')
    for button in buttons: button.config(font = FONT_BUTTON_BOLD if if_bold_mode else FONT_BUTTON_UNBOLD)
    for label in labels: label.config(font = FONT_CHINESE_BOLD if if_bold_mode else FONT_CHINESE_UNBOLD)
    for textbox in textboxs: textbox.config(font = FONT_TEXT_BOLD if if_bold_mode else FONT_TEXT_UNBOLD)
def direct_mode_switch():
    '''切换直接模式'''
    global direct__mode
    direct__mode = not direct__mode
    change_button_text('direct', '直接' if direct__mode else '普通')
    bindfunc: Callable[[], None] = direct_describe if direct__mode else show_result
    # 修改执行函数
    text_describe.bind('<Return>', lambda event: bindfunc() or 'break')
    buttons_inputs[ipt_names.index('start')].config(command = bindfunc)
    buttons_inputs[ipt_names.index('up')].config(command = None if direct__mode else up_ipt)
    buttons_inputs[ipt_names.index('down')].config(command = None if direct__mode else down_ipt)
    buttons_inputs[ipt_names.index('clear_u')].config(command = None if direct__mode else clear_ipt)
    if direct__mode: input_set('直接输入模式下该输入框禁用')
    text_ipt.config(state = 'disabled' if direct__mode else 'normal')
    if not direct__mode: input_set('')
    text_ipt.config(bg = '#FFFFC0' if direct__mode else '#FFFFFF')
def protect(function_to_protect: Callable):
    '''窗口保护修饰器'''
    if not isinstance(function_to_protect, Callable): raise NewError(0)
    @wraps(function_to_protect)
    def protected_func(*args, **kwargs):
        for event in events: text_opt.bind(event, lambda event: 'break')
        for button in buttons: button.config(state = 'disabled')
        root.title(f'Dice v{VERSION} - by {AUTHOR} - 正在运行中...')
        function_to_protect(*args, **kwargs)
        root.title(f'Dice v{VERSION} - by {AUTHOR}')
        for button in buttons: button.config(state = 'normal')
        for event in events: text_opt.unbind(event)
        globals()['displayed_output'] = text_opt.get('1.0', END)[:-1]
    return protected_func
root.bind('<Configure>', dynamic_controls_size)
CTRL_BUTTON_NUM = 6
control_frame = Frame(root)
control_frame.place(x = 0, y = 0, width = WIDTH, height = BUTTON_HEIGHT)
control_names = ['display', 'log', 'extreme', 'tip', 'bold', 'direct']
control_texts = ['详细', 'LOG', '无大成失', '无提示', '加粗', '普通']
control_funcs = [display_mode_switch, export_log, extreme_mode_switch, showtip_mode_switch, font_mode_switch, direct_mode_switch]
buttons_controls = [Button(control_frame, text = control_texts[bid], font = FONT_BUTTON_BOLD, command = control_funcs[bid]) for bid in range(CTRL_BUTTON_NUM)]
for bid in range(CTRL_BUTTON_NUM): buttons_controls[bid].place(x = bid * BUTTON_WIDTH, y = 0, width = BUTTON_WIDTH, height = BUTTON_HEIGHT)
# 程序说明
def show_guide_window(event): GuideViewer(root, guide_titles, guide_texts, guide_directpages)
label_explain = Label(control_frame, text = '\u24D8', font = FONT_CHINESE_BOLD)
label_explain.place(x = WIDTH - BUTTON_HEIGHT, y = 0, width = BUTTON_HEIGHT, height = BUTTON_HEIGHT)
label_explain.bind("<Button-1>", show_guide_window)
# 结果输出
text_frame_2 = Frame(root)
text_frame_2.place(x = 0, y = HEIGHT - HEIGHT_OPT, width = WIDTH, height = HEIGHT_OPT)
text_opt = Text(text_frame_2, height = 100, width = 800, wrap = 'none', state = 'disabled', font = FONT_TEXT_BOLD)
text_opt.place(x = 0, y = 0, width = WIDTH - BAR, height = HEIGHT_OPT - BAR)
scrollbar_y = Scrollbar(text_frame_2, orient = 'vertical', command = text_opt.yview)
scrollbar_y.place(x = WIDTH - BAR, y = 0, width = BAR, height = HEIGHT_OPT)
scrollbar_x = Scrollbar(text_frame_2, orient = 'horizontal', command = text_opt.xview)
scrollbar_x.place(x = 0, y = HEIGHT_OPT - BAR, width = WIDTH, height = BAR)
text_opt.config(yscrollcommand = scrollbar_y.set, xscrollcommand = scrollbar_x.set)
text_opt.config(selectbackground = 'lightblue')
for color in COLORS: text_opt.tag_configure(color, foreground = color)
def change_flag(event):
    '''根据输入表达式合法性更新指示灯颜色'''
    canvas_legal.config(bg = GREEN if iflegal_total(input_get()) != '' else RED)
    text_ipt.edit_modified(False)
def output_totext(ipt_strings: list[str], ifblank: bool):
    '''向显示区输出文本'''
    if not (check_type(ipt_strings, 'list[str]') and isinstance(ifblank, bool)): raise NewError(0)
    text_opt.config(state = 'normal')
    for string in ipt_strings: text_opt.insert(END, string + '\n')
    if ifblank: text_opt.insert(END, '\n')
    text_opt.config(state = 'disabled')
    seed(randint(0, 1000) + time() + randint(0, 1000))
    text_opt.see(END)
def output_totext_colored(outputs: list[C_O_L], ifblank: bool):
    '''向显示区输出带颜色的文本, 颜色格式为#FFFFFF'''
    if not check_types([outputs, ifblank], ['list[C_O_L]', 'bool']): raise NewError(0)
    for ssid in range(len(outputs)):
        strings, colors, length = outputs[ssid].get()
        text_opt.config(state = 'normal')
        for oid in range(length): text_opt.insert(END, strings[oid], colors[oid])
        text_opt.insert(END, '\n')
        text_opt.config(state = 'disabled')
    text_opt.config(state = 'normal')
    if ifblank: text_opt.insert(END, '\n')
    text_opt.config(state = 'disabled')
    seed(randint(0, 1000) + time() + randint(0, 1000))
    text_opt.see(END)
def output_create_record(lines: int, value: int | str | list | tuple, otype: str | list[str], ifblank: bool):
    '''记录输出内容'''
    if not (isinstance(lines, int) and check_type(otype, 'str | list[str]')): raise NewError(0)
    if not (check_type(value, 'int | str | list | tuple') and isinstance(ifblank, bool)): raise NewError(0)
    append_list = [lines + int(ifblank), value, otype, log_num]
    for lid in range(len(output_lists)): output_lists[lid].append(append_list[lid])
def output_delete_record(index: str) -> bool:
    '''返回值代表是否成功'''
    if index not in ['last', 'first', 'all']: raise NewError(1)
    if len(output_lines_list) == 0: return False
    match index:
        case 'last' :
            for alist in output_lists: del alist[-1]
        case 'first':
            for alist in output_lists: del alist[0]
        case 'all'  :
            for alist in output_lists: alist.clear()
    return True
def input_create_record(ipt: str):
    if not isinstance(ipt, str): raise NewError(0)
    if ipt in input_string_list: del input_string_list[input_string_list.index(ipt)]
    input_string_list.append(ipt)
    globals()['input_temp'] = ''
    globals()['input_pin'] = len(input_string_list)
def input_get() -> str: return text_ipt.get('1.0', END)[:-1]
def input_set(temp: str):
    if not isinstance(temp, str): raise NewError(0)
    clear_ipt()
    text_ipt.insert(END, temp)
def describe_get() -> str: return filter_chinese(text_describe.get('1.0', END)[:-1])
@protect
def show_result_base(ipt: str, code: str):
    if not (isinstance(ipt, str) and isinstance(code, str)): raise NewError(0)
    if code not in codes: raise NewError(1)
    if not iflegal_branch(ipt, code): return
    describe = describe_get()
    if not if_describe_legal(describe): return
    value, prostrings = branch(ipt, code, display_mode)
    final, final_list = embed(ipt, code, value)
    ipt_std = standardization(ipt, code)
    describe_parts = split_emptypair(describe)
    c_describe = C_O_L(describe + ': ')
    bracket_num = len(describe_parts) - 1
    match code: # 输出文本特殊处理, 包含描述的插入
        case 'classic' | 'if_true':
            if bracket_num == 1: string_opt = describe_parts[0] + final + describe_parts[1]
            elif describe != '': string_opt = c_describe + final
            else: string_opt = C_O_L('Result: ') + final
        case 'D__func' | 'against':
            if bracket_num == 1: string_opt = describe_parts[0] + final + describe_parts[1]
            elif bracket_num == len(value): string_opt = sum(listmerge(final_list, describe_parts[1:]), describe_parts[0])
            elif describe != '': string_opt = c_describe + final
            else: string_opt = C_O_L('Results: ') + final
        case 'special':
            _, order, roll_num = iflegal_special(ipt)
            if order == 'RGB': showcolors([[Color(text.get_onlystr()) for text in final_list]])
            special_name = {'RGB': C_O_L('随机RGB: '), 'POK': C_O_L('随机扑克牌: '), 'MAJ': C_O_L('随机麻将牌: '),
                            'GUA': C_O_L('随机六十四卦: '), 'TLL': C_O_L('随机塔罗牌: '), 'TLA': C_O_L('随机塔罗牌: ')}
            if roll_num == 1 and describe == '': string_opt = special_name[order] + final
            elif bracket_num == 1: string_opt = describe_parts[0] + final + describe_parts[1]
            elif bracket_num == roll_num: string_opt = sum(listmerge(final_list, describe_parts[1:]), describe_parts[0])
            elif describe != '': string_opt = c_describe + final
            else: string_opt = special_name[order] + final
    strings_log = [string_opt.get_onlystr()]
    input_create_record(ipt_std)
    output_create_record(1 + len(prostrings), value, code, display_mode)
    create_log(strings_log, code)
    if len(prostrings) != 0: output_totext(prostrings, False)
    output_totext_colored([string_opt], display_mode)
def show_result():
    code = iflegal_total(input_get())
    if code == '': return
    show_result_base(input_get(), code)
# 表达式输入
def up_ipt():
    global input_pin, input_temp
    if len(input_string_list) == 0 or input_pin <= 0: return
    if input_pin == len(input_string_list): input_temp = input_get()
    input_pin -= 1
    input_set(input_string_list[input_pin])
def down_ipt():
    global input_pin, input_temp
    if len(input_string_list) == 0 or input_pin < 0 or input_pin == len(input_string_list): return
    input_pin += 1
    input_set(input_string_list[input_pin] if input_pin < len(input_string_list) else input_temp)
def clear_ipt(): text_ipt.delete('1.0', END)
def clear_describe(): text_describe.delete('1.0', END)
def showcolors(colorss: list[list[Color]]):
    '''展示随机RGB所得颜色'''
    if not check_type(colorss, 'list[list[Color]]'): raise NewError(0)
    length_total = len(colorss)
    for lid in range(length_total):
        length = len(colorss[lid])
        for cid in range(length):
            left = int(cid * (WIDTH_COLORSHOW / length))
            top = int(lid * (HEIGHT_COLORSHOW / length_total))
            canvas_showcolor.create_rectangle(left, top, WIDTH_COLORSHOW, HEIGHT_COLORSHOW, fill = colorss[lid][cid].r16str)
@protect
def direct_describe():
    describe = describe_get()
    clear_describe()
    if not if_describe_legal(describe): return
    ifmatch, L_mainbracket, R_mainbracket = squarebracket_nonest_match(describe)
    if not ifmatch or len(L_mainbracket) == 0:
        output_create_record(1, '__describe__', 'direct', False)
        create_log([describe], 'direct')
        output_totext_colored([C_O_L(describe)], False)
    else:
        contents = [describe[ledge + 1:redge] for ledge, redge in zip(L_mainbracket, R_mainbracket)]
        codes = iflegal_direct_describe(contents)
        for cid in range(len(codes) - 1, -1, -1):
            if codes[cid] == '': [codes.pop(cid), L_mainbracket.pop(cid), R_mainbracket.pop(cid), contents.pop(cid)]
        contents = [standardization(content, code) for content, code in zip(contents, codes)]
        L_edge, R_edge = [0] + R_mainbracket, L_mainbracket + [len(describe) - 1]
        describe_parts = [C_O(describe[ledge:redge + 1]) for ledge, redge in zip(L_edge, R_edge)]
        embed_optss = [embed(ipt, code, branch(ipt, code, False)[0])[0] for ipt, code in zip(contents, codes)]
        output_create_record(1, [coptl.get_onlystr() for coptl in embed_optss], codes, False)
        colorss = []
        for cid in range(len(codes)):
            if codes[cid] == 'special' and contents[cid][:3] == 'RGB': colorss.append([Color(color) for color in embed_optss[cid].get_onlystr().split(',')])
        if len(colorss) > 0: showcolors(colorss)
        colored_opt = C_O_L([describe_parts[0]])
        for oid in range(len(embed_optss)): colored_opt += embed_optss[oid] + [describe_parts[oid + 1]]
        create_log([colored_opt.get_onlystr()], f'direct[{','.join(codes)}]')
        output_totext_colored([colored_opt], False)
text_frame_1 = Frame(root)
text_frame_1.place(x = 0, y = BUTTON_HEIGHT, width = WIDTH, height = HEIGHT_IPT * 2)
    # 指令输入框
label_order = Label(text_frame_1, text = '指令', font = FONT_CHINESE_BOLD)
label_order.place(x = 0, y = 0, width = WIDTH_TITLE, height = HEIGHT_LABEL)
text_ipt = Text(text_frame_1, height = 1, width = 20, wrap = 'none', font = FONT_TEXT_BOLD)
text_ipt.place(x = WIDTH_TITLE, y = 0, width = WIDTH_IPT, height = HEIGHT_IPT - BAR)
scrollbar_ipt = Scrollbar(text_frame_1, orient = 'horizontal', command = text_ipt.xview)
scrollbar_ipt.place(x = WIDTH_TITLE, y = HEIGHT_IPT - BAR, width = WIDTH_IPT, height = BAR)
text_ipt.config(xscrollcommand = scrollbar_ipt.set)
text_ipt.bind('<Return>', lambda event: show_result() or 'break')
text_ipt.bind('<Control-v>', lambda event: event.widget.insert(INSERT, filter_char(root.clipboard_get())) or 'break')
    # 描述输入框
label_describe = Label(text_frame_1, text = '描述', font = FONT_CHINESE_BOLD)
label_describe.place(x = 0, y = HEIGHT_IPT, width = WIDTH_TITLE, height = HEIGHT_LABEL)
text_describe = Text(text_frame_1, height = 1, width = 20, wrap = 'none', font = FONT_TEXT_BOLD)
text_describe.place(x = WIDTH_TITLE, y = HEIGHT_IPT, width = WIDTH_IPT, height = HEIGHT_IPT - BAR)
scrollbar_describe = Scrollbar(text_frame_1, orient = 'horizontal', command = text_describe.xview)
scrollbar_describe.place(x = WIDTH_TITLE, y = HEIGHT_IPT * 2 - BAR, width = WIDTH_IPT, height = BAR)
text_describe.config(xscrollcommand = scrollbar_describe.set)
text_describe.bind('<Return>', lambda event: show_result() or 'break')
text_describe.bind('<Control-v>', lambda event: event.widget.insert(INSERT, filter_chinese(root.clipboard_get())) or 'break')
    # 输入区按钮
text_input_control_frame = Frame(text_frame_1)
text_input_control_frame.place(x = WIDTH_IPT_T, y = 0, width = WIDTH - WIDTH_IPT_T, height = HEIGHT_IPT * 2)
INPUT_BUTTON_NUM = 5
ipt_names = ['up', 'down', 'clear_u', 'start', 'clear_d']
ipt_texts = ['↑', '↓', 'C', 'START', 'C']
ipt_funcs = [up_ipt, down_ipt, clear_ipt, show_result, clear_describe]
ipt_xs = [0, 0, WIDTH_U_D, WIDTH_U_D * 2 + LENGTH_FLAG, 0]
ipt_ys = [0, 25, 0, 5, HEIGHT_IPT]
ipt_widths = [WIDTH_U_D, WIDTH_U_D, WIDTH_CLEAR, BUTTON_WIDTH, WIDTH_C_D]
ipt_heights = [HEIGHT_U_D, HEIGHT_U_D, HEIGHT_IPT, BUTTON_HEIGHT, HEIGHT_IPT]
buttons_inputs = [Button(text_input_control_frame, text = ipt_texts[bid], font = FONT_BUTTON_BOLD, command = ipt_funcs[bid]) for bid in range(INPUT_BUTTON_NUM)]
for bid in range(INPUT_BUTTON_NUM): buttons_inputs[bid].place(x = ipt_xs[bid], y = ipt_ys[bid], width = ipt_widths[bid], height = ipt_heights[bid])
text_ipt.bind('<<Modified>>', change_flag)
    # 合法性指示灯与颜色展示
canvas_legal = Canvas(text_input_control_frame, width = LENGTH_FLAG, height = LENGTH_FLAG, bg = 'red')
canvas_legal.place(x = WIDTH_U_D * 2, y = 5, width = LENGTH_FLAG, height = LENGTH_FLAG)
canvas_showcolor = Canvas(text_input_control_frame, width = LENGTH_FLAG, height = LENGTH_FLAG, bg = WHITE)
canvas_showcolor.place(x = WIDTH_U_D * 2, y = 5 + LENGTH_FLAG, width = WIDTH_COLORSHOW, height = HEIGHT_COLORSHOW)
# 快捷键
def quick_d100():
    if_integer, value = ifinteger(input_get())
    show_result_base(f'{value if if_integer else 1}d100', 'classic')
def quick_d2():
    if_integer, value = ifinteger(input_get())
    show_result_base(f'{value if if_integer else 1}d2', 'classic')
def quick_d10_d2(): show_result_base('1d10|1d2', 'against')
def quick_d_d(): show_result_base('1d100|1d100', 'against')
def quick_RGB(): show_result_base('RGB1', 'special')
def quick_POKER(): show_result_base('POK1', 'special')
QUICK_BUTTON_NUM = 6
quick_frame = Frame(root)
quick_frame.place(x = 0, y = HEIGHT_IPT * 2 + BUTTON_HEIGHT, width = QUICK_BUTTON_NUM * BUTTON_WIDTH, height = HEIGHT_BUTTON)
quick_texts = ['d100', 'd2', 'd10|d2', 'd|d', 'RGB', 'POKER']
quick_funcs = [quick_d100, quick_d2, quick_d10_d2, quick_d_d, quick_RGB, quick_POKER]
buttons_quicks = [Button(quick_frame, text = quick_texts[bid], font = FONT_BUTTON_BOLD, command = quick_funcs[bid]) for bid in range(QUICK_BUTTON_NUM)]
for bid in range(QUICK_BUTTON_NUM): buttons_quicks[bid].place(x = bid * BUTTON_WIDTH, y = 0, width = BUTTON_WIDTH, height = BUTTON_HEIGHT)
# 删除键
@protect
def delete_first():
    if len(output_lines_list) == 0: return
    text_opt.config(state = 'normal')
    for _ in range(output_lines_list[0]): text_opt.delete('1.0', '1.end+1c')
    text_opt.config(state = 'disabled')
    output_delete_record('first')
@protect
def delete_last():
    if len(output_lines_list) == 0: return
    line_num = int(text_opt.index('end-1c').split('.')[0])
    text_opt.config(state = 'normal')
    for lid in range(output_lines_list[-1] + 1): text_opt.delete(f'{line_num - lid}.0', f'{line_num - lid}.end+1c')
    if len(output_lines_list) > 1: text_opt.insert(END, '\n')
    text_opt.config(state = 'disabled')
    output_delete_record('last')
@protect
def delete_all():
    if len(output_lines_list) == 0: return
    text_opt.config(state = 'normal')
    text_opt.delete('1.0', END)
    text_opt.config(state = 'disabled')
    output_delete_record('all')
DELETE_BUTTON_NUM = 3
delete_frame = Frame(root)
delete_frame.place(x = WIDTH - 3 * BUTTON_WIDTH, y = HEIGHT_IPT * 2 + BUTTON_HEIGHT, width = 3 * BUTTON_WIDTH, height = HEIGHT_BUTTON)
delete_texts = ['C-FIRST', 'C-LAST', 'C-ALL']
delete_funcs = [delete_first, delete_last, delete_all]
buttons_deletes = [Button(delete_frame, text = delete_texts[bid], font = FONT_BUTTON_BOLD, command = delete_funcs[bid]) for bid in range(DELETE_BUTTON_NUM)]
for bid in range(DELETE_BUTTON_NUM): buttons_deletes[bid].place(x = bid * BUTTON_WIDTH, y = 0, width = BUTTON_WIDTH, height = BUTTON_HEIGHT)
# 控件汇总
buttons = buttons_quicks + buttons_inputs + buttons_deletes + buttons_controls
labels = [label_order, label_describe, label_explain]
textboxs = [text_ipt, text_describe, text_opt]
events = ['<Key>', '<Button-1>', '<Button-2>', '<Button-3>', '<B1-Motion>', '<B2-Motion>', '<B3-Motion>', '<Control-Key>']
# 介绍区
ToolTip(buttons_controls[control_names.index('display')], '点击切换输出显示模式\n详细模式: 计算过程将被完全展现, 有空行\n简洁模式: 过程略去, 压缩到一行, 无空行')
ToolTip(buttons_controls[control_names.index('log')], '点击导出日志(程序关闭时会自动导出)')
ToolTip(buttons_controls[control_names.index('extreme')], '点击切换大成功大失败的判定方式\n仅经典模式与对抗模式支持大成失的判定')
ToolTip(buttons_controls[control_names.index('tip')], '点击显示或隐藏提示')
ToolTip(label_explain, '点击显示程序使用说明')
ToolTip(label_order, '该文本框为指令输入框, 输入指令后在该框内回车或按下右侧START即可执行')
ToolTip(label_describe, '该文本框为描述输入框, 输入描述后按下右侧START即可在骰点输出中增加描述\n在描述内使用[]作为占位符可以让指令栏的骰点结果自动填充在指定位置\n在该框内直接按下回车将触发直接输入功能, 描述框内的内容将被直接显示到输出框, 且使用[]框起的指令将被计算')
ToolTip(buttons_inputs[ipt_names.index('up')], '上一次输入')
ToolTip(buttons_inputs[ipt_names.index('down')], '下一次输入')
ToolTip(buttons_inputs[ipt_names.index('clear_u')], '清除指令框的内容')
ToolTip(buttons_inputs[ipt_names.index('start')], '开始计算随机数')
ToolTip(buttons_inputs[ipt_names.index('clear_d')], '清除描述框的内容')
ToolTip(canvas_legal, '显示当前输入的指令是否合法\n合法时为绿色, 否则为红色')
ToolTip(canvas_showcolor, '展示随机得到的颜色')
ToolTip(buttons_quicks[quick_texts.index('d100')], '进行一次1d100\n若指令框内是一个正整数, 则进行该数次d100')
ToolTip(buttons_quicks[quick_texts.index('d2')], '进行一次1d2\n若指令框内是一个正整数, 则进行该数次d2')
ToolTip(buttons_quicks[quick_texts.index('d10|d2')], '进行一次1d10|1d2, 可用于事件选择骰')
ToolTip(buttons_quicks[quick_texts.index('d|d')], '进行一次1d100|1d100, 可用于双方直接拼点')
ToolTip(buttons_quicks[quick_texts.index('RGB')], '进行一次RGB1获得一个随机颜色')
ToolTip(buttons_quicks[quick_texts.index('POKER')], '进行一次POK1获得一张随机扑克牌')
ToolTip(buttons_deletes[delete_texts.index('C-FIRST')], '删除显示区最上方一条记录')
ToolTip(buttons_deletes[delete_texts.index('C-LAST')], '删除显示区最下方一条记录')
ToolTip(buttons_deletes[delete_texts.index('C-ALL')], '删除显示区全部记录')
# 主循环
def custom_excepthook(type, value, traceback):
    globals()['errlog'] = f'Caught an exception: {type.__name__}(value = {value})\nStack trace:\n{''.join(format_tb(traceback))}'
    if root: root.destroy()
root.report_callback_exception = custom_excepthook
root.mainloop()
export_log()
# endregion
####################################################################################################
