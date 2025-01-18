'''
    dice v1.1 by ulsmallzhou
    2025-01-18
'''
from random import seed, randint, sample
from time import time
seed(time())
from tkinter import Tk, Frame, Text, Scrollbar, Button, Canvas
from tkinter import INSERT, END
####################################################################################################
# TODO: 输入框上下键, 保底与上限[,,]


####################################################################################################
# 各类常量区
####################################################################################################
num_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operator_char = ['+', '-', '*']
compare_char = ['<', '>', '=', ':']
bracket_char = ['(', ')']
random_char = ['d', 'D']
legal_char_totle = num_char + operator_char + bracket_char + compare_char + random_char
legal_char_classic = num_char + operator_char + bracket_char + ['d']
legal_char_Dfunc = legal_char_classic + ['D']
legal_char_iftrue = legal_char_classic + compare_char[:-1]
legal_char_against = legal_char_classic + compare_char[-1:]
illegal_pears = ['()', ')0', ')1', ')2', ')3', ')4', ')5', ')6', ')7', ')8', ')9',
                 '0(', '1(', '2(', '3(', '4(', '5(', '6(', '7(', '8(', '9(', ')(',
                 '++', '+-', '+*', '-+', '--', '-*', '*+', '*-', '**', '(+', '(*', '+)', '-)', '*)']
MAX_ROLL = 100
MAX_CHAR = 500
WIDTH, HEIGHT = 800, 600
HEIGHT_IPT, HEIGHT_BUTTON, HEIGHT_OPT = 50, 30, 520
WIDTH_IPT, WIDTH_U_D, HEIGHT_U_D, WIDTH_CLEAR, WIDTH_START = 670, 15, 25, 15, 100
BAR = 20
BUTTON_WIDTH, BUTTON_HEIGHT = 70, 30
LENGTH_FLAG = 30
AUTHOR = 'ulsmallzhou'
FONT, FONT_TEXT = ('Consolas', 12, 'bold'), ('Consolas', 18, 'bold')
radix_16 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
codes = ['classic', 'D__func', 'if_true', 'against']
####################################################################################################



####################################################################################################
# 基础函数区
####################################################################################################
def sum(ipt: list[int]) -> int:
    '''对列表内的所有整数求和'''
    sum_value = 0
    for value in ipt:
        if not isinstance(value, int): return 0
        sum_value += value
    return sum_value
def split_simple(sep: str, ipt: str) -> list[str]:
    '''使用指定字符分割字符串'''
    result, start = [], 0
    while True:
        pos = ipt.find(sep, start)
        if pos == -1:
            result.append(ipt[start:])
            break
        else:
            result.append(ipt[start:pos])
            start = pos + len(sep)
    return result
def split(seps: list[str], ipt: str) -> list[str]:
    '''使用指定的若干字符分割字符串'''
    result = [ipt]
    for sep in seps:
        temp_result = []
        for item in result: temp_result.extend(split_simple(sep, item))
        result = temp_result
    return result
def filter_char(ipt: str) -> str:
    '''过滤非法字符'''
    result = ''
    for char in ipt:
        if char in legal_char_totle: result += char
    return result
def ifinteger(ipt: str) -> tuple[bool, int]:
    '''判断字符串是否为整数并给出其值'''
    if not isinstance(ipt, str) or ipt == '': return (False, 0)
    if ipt[0] == '-': ipt = ipt[1:]
    return (True, int(ipt)) if ipt.isdigit() else (False, 0)
def if_str_legal(ipt: str) -> bool:
    '''粗略判断字符串是否合法(是字符串且长度不超过限度)'''
    return bool(0 < len(ipt) <= MAX_CHAR) if isinstance(ipt, str) else False
####################################################################################################



####################################################################################################
# 合法性审查
####################################################################################################
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
def if_totally_inbracket(ipt: str) -> bool:
    '''检查字符串是否只有一组主要括号且在最外侧'''
    ifmatch, _, _, main_bracket_L, main_bracket_R = bracket_match(ipt)
    return ifmatch and len(main_bracket_L) == 1 and main_bracket_L[0] == 0 and main_bracket_R[0] == len(ipt) - 1
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
    fragments = split(['+', '-', '*'], ipt)
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
        if char not in legal_char_Dfunc: return False # 确保均为合法字符
    if len(ipt) < 3 or ipt[0] == 'D' or ipt[-1] == 'D' or ipt.count('D') != 1: return False
    fragments = split(['D'], ipt)
    if not (fragments[0].isdigit() and fragments[1].isdigit()): return False
    left_int, right_int = int(fragments[0]), int(fragments[1])
    return bool(right_int >= 3 and left_int >= 2 and left_int <= MAX_ROLL and right_int >= left_int)
def iflegal_iftrue(ipt: str) -> bool:
    for char in ipt:
        if char not in legal_char_iftrue: return False      # 确保均为合法字符
    if ipt[0] in '<>=' or ipt[-1] in '<>=': return False    # 确保首尾不是符号
    num_l, num_r, num_e = ipt.count('<'), ipt.count('>'), ipt.count('=')
    if num_e > 1 or num_l + num_r > 1: return False
    judge_sign = 1000 + num_l * 100 + num_r * 10 + num_e
    match judge_sign:
        case 1100:
            fragments = split(['<'], ipt)
            return iflegal_classic(fragments[0]) and iflegal_classic(fragments[1])
        case 1010:
            fragments = split(['>'], ipt)
            return iflegal_classic(fragments[0]) and iflegal_classic(fragments[1])
        case 1001:
            fragments = split(['='], ipt)
            return iflegal_classic(fragments[0]) and iflegal_classic(fragments[1])
        case 1101:
            if '<=' not in ipt: return False
            fragments = split(['<='], ipt)
            return iflegal_classic(fragments[0]) and iflegal_classic(fragments[1])
        case 1011:
            if '>=' not in ipt: return False
            fragments = split(['>='], ipt)
            return iflegal_classic(fragments[0]) and iflegal_classic(fragments[1])
        case _: return False
def iflegal_against(ipt: str) -> bool:
    for char in ipt:
        if char not in legal_char_against: return False # 确保均为合法字符
    fragments = split([':'], ipt)
    if '' in fragments: return False                    # 确保首尾不是符号且表达式合法
    for fragment in fragments:
        if not iflegal_classic(fragment): return False  # 确保每个分部合法
    return True
def iflegal_branch(ipt: str, code: str) -> bool:
    '''根据code选择不同的判断函数'''
    if not if_str_legal(ipt): return False  # 确保是不过长非空字符串
    ipt.replace(' ', '')                    # 去掉所有空格
    match code:
        case 'classic': return iflegal_classic(ipt)
        case 'D__func': return iflegal_Dfunc(ipt)
        case 'if_true': return iflegal_iftrue(ipt)
        case 'against': return iflegal_against(ipt)
        case _: return False
def iflegal_total(ipt: str) -> str:
    '''如果表达式合法则返回code'''
    for code in codes:
        if iflegal_branch(ipt, code): return code
    return ''
####################################################################################################


####################################################################################################
# 计算与显示
####################################################################################################
def num_str(ipt_num: int) -> str:
    '''默认输入合法, 即输入为整数'''
    return str(ipt_num) if ipt_num >= 0 else '(' + str(ipt_num) + ')'
def random_base(randrange: int) -> int:
    '''默认输入合法, 即输入为整数'''
    if randrange == 0: return 0
    if randrange > 0: return randint(1, randrange)
    if randrange < 0: return randint(randrange, -1)
def expression_split(ipt: str, if_d: bool) -> tuple[list[str]]:
    '''默认输入合法, 即输入为正常表达式'''
    _, _, _, mainbracket_L, mainbracket_R = bracket_match(ipt)
    mainbracket_num, mainbracket_text = len(mainbracket_L), []
    check_char = ['+', '-', '*', 'd'] if if_d else ['+', '-', '*']
    if mainbracket_num == 0:
        # split_char = '[+]|[-]|[*]|d' if if_d else '[+]|[-]|[*]'
        # fragments, operators = split_re(split_char, ipt), []
        split_char = ['+', '-', '*', 'd'] if if_d else ['+', '-', '*']
        fragments, operators = split(split_char, ipt), []
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
            fragments = split(['D'], ipt)
            return str(int(fragments[0])) + 'D' + str(int(fragments[1]))
        case 'if_true':
            judge_dict = {1100: '<', 1010: '>', 1001: '=', 1101: '<=', 1011: '>='}
            judge_sign = 1000 + ipt.count('<') * 100 + ipt.count('>') * 10 + ipt.count('=')
            fragments = split([judge_dict[judge_sign]], ipt)
            return standardization(fragments[0], 'classic') + judge_dict[judge_sign] + standardization(fragments[1], 'classic')
        case 'against':
            fragments = split([':'], ipt)
            return ':'.join([standardization(fragment, 'classic') for fragment in fragments])
def putbracket(ipt: tuple[int, list[str]]) -> tuple[int, list[str]]:
    '''确保字符串有且只有一个主要括号在最外面'''
    value, strings, strings_new = ipt[0], ipt[1], []
    for string in strings:
        if if_totally_inbracket(string): strings_new.append(string)
        else: strings_new.append('(' + string + ')')
    strings_new[-1] = num_str(value)
    return (value, strings_new)
def crossmerge(ipt_out: list, ipt_in: list) -> list:
    '''默认输入合法, 即两个输入均为列表且len(ipt_out) == len(ipt_in) + 1'''
    length = len(ipt_in)
    opt = []
    for eid in range(length): opt.extend([ipt_out[eid], ipt_in[eid]])
    opt.append(ipt_out[-1])
    return ''.join(opt)
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
    return (value_final, strings_opt + strings_final[1:])
def D_function(ipt: str) -> tuple[list, list[str]]:
    '''默认输入合法, 即数字D数字且数字大小符合要求'''
    fragments = split(['D'], ipt)
    D_left, D_right = int(fragments[0]), int(fragments[1])
    input_string = str(D_left) + 'D' + str(D_right)
    results = sample(range(1, D_right + 1), D_left)
    strings = [' ' + input_string, '=' + ','.join([str(value) for value in results])]
    return (results, strings)
def iftrue(ipt: str) -> tuple[str, list[str]]:
    '''默认输入合法, 即表达式-不等式-表达式'''
    judge_dict = {1100: '<', 1010: '>', 1001: '=', 1101: '<=', 1011: '>='}
    judge_sign = 1000 + ipt.count('<') * 100 + ipt.count('>') * 10 + ipt.count('=')
    fragments = split([judge_dict[judge_sign]], ipt)
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
        strings_opt.append((' ' + judge_dict[judge_sign] + ' ').join(thisline))
    lvalue, rvalue = values[0], values[1]
    value_dict = {1100: lvalue < rvalue, 1010: lvalue > rvalue, 1001: lvalue == rvalue, 1101: lvalue <= rvalue, 1011: lvalue >= rvalue}
    result = 'Success!' if value_dict[judge_sign] else 'Failure!'
    return (result, strings_opt)
def against(ipt: str) -> tuple[list, list[str]]:
    '''默认输入合法, 即表达式:表达式[:表达式]^n'''
    fragments = split([':'], ipt)
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
        strings_opt.append(' : '.join(thisline))
    return (values, strings_opt)
def branch(ipt: str, code: str) -> tuple[int | list | tuple, list[str]]:
    '''根据code选择不同的处理函数'''
    match code:
        case 'classic': return dice(ipt)
        case 'D__func': return D_function(ipt)
        case 'if_true': return iftrue(ipt)
        case 'against': return against(ipt)
        case _: return [0, []]
####################################################################################################


####################################################################################################
# 可视化框架
####################################################################################################
# 窗口
root = Tk()
root.title(f'Dice v1.1 - by {AUTHOR}')
root.geometry(str(WIDTH) + 'x' + str(HEIGHT))
root.resizable(False, False)
# 全局控制变量
input_string_list, input_temp, input_pin = [], '', -1
output_lines_list, output_value_list, output_types_list = [], [], []
# 结果输出
text_frame_2 = Frame(root)
text_frame_2.place(x = 0, y = HEIGHT - HEIGHT_OPT, width = WIDTH, height = HEIGHT_OPT)
text_opt = Text(text_frame_2, height = 100, width = 800, wrap = 'none', state = 'disabled', font = FONT_TEXT)
text_opt.place(x = 0, y = 0, width = WIDTH - BAR, height = HEIGHT_OPT - BAR)
scrollbar_y = Scrollbar(text_frame_2, orient = 'vertical', command = text_opt.yview)
scrollbar_y.place(x = WIDTH - BAR, y = 0, width = BAR, height = HEIGHT_OPT)
scrollbar_x = Scrollbar(text_frame_2, orient = 'horizontal', command = text_opt.xview)
scrollbar_x.place(x = 0, y = HEIGHT_OPT - BAR, width = WIDTH, height = BAR)
text_opt.config(yscrollcommand = scrollbar_y.set, xscrollcommand = scrollbar_x.set)
def change_flag(event):
    '''根据输入表达式合法性更新灯颜色'''
    canvas_legal.config(bg = '#00FF00' if iflegal_total(input_get()) != '' else 'red')
    text_ipt.edit_modified(False)
def output_totext(ipt_strings: list[str]):
    text_opt.config(state = 'normal')
    for string in ipt_strings: text_opt.insert(END, string + '\n')
    text_opt.insert(END, '\n')
    text_opt.config(state = 'disabled')
    seed(time())
    text_opt.see(END)
def output_create_record(lines: int, value: int | list | tuple, otype: str):
    output_lines_list.append(lines + 1)
    output_value_list.append(value)
    output_types_list.append(otype)
def output_delete_record(index: str) -> bool:
    '''返回值代表是否成功'''
    if len(output_lines_list) == 0: return False
    lists = [output_lines_list, output_value_list, output_types_list]
    match index:
        case 'last' :
            for alist in lists: del alist[-1]
        case 'first':
            for alist in lists: del alist[0]
        case 'all'  :
            for alist in lists: alist.clear()
    return True
def input_create_record(ipt: str):
    if ipt in input_string_list: del input_string_list[input_string_list.index(ipt)]
    input_string_list.append(ipt)
def input_get() -> str: return text_ipt.get('1.0', END)[:-1]
def show_result_base(ipt: str, code: str):
    if not iflegal_branch(ipt, code): return
    protect()
    value, strings = branch(ipt, code)
    match code:
        case 'classic':
            strings_opt = ['=' + (string[1:-1] if if_totally_inbracket(string) else string) for string in strings][:-1]
            strings_opt = [' ' + ipt] + strings_opt + ['=' + str(value)]
        case 'D__func':
            strings_opt = strings
        case 'if_true':
            strings_opt = ['=' + string for string in strings]
            strings_opt = [' ' + ipt] + strings_opt + [value]
        case 'against':
            strings_opt = ['=' + string for string in strings]
            strings_opt = [' ' + ipt] + strings_opt
    input_create_record(standardization(ipt, code))
    output_create_record(len(strings_opt), value, code)
    output_totext(strings_opt)
    unprotect()
def show_result():
    code = iflegal_total(input_get())
    if code != '': show_result_base(input_get(), code)
# 表达式输入
def up_ipt(): pass
def down_ipt(): pass
def clear_ipt(): text_ipt.delete('1.0', END)
INPUT_BUTTON_NUM = 4
text_frame_1 = Frame(root)
text_frame_1.place(x = 0, y = 0, width = WIDTH, height = HEIGHT_IPT)
text_ipt = Text(text_frame_1, height = 1, width = 20, wrap = 'none', font = FONT_TEXT)
text_ipt.place(x = 0, y = 0, width = WIDTH_IPT, height = HEIGHT_IPT - BAR)
scrollbar_ipt = Scrollbar(text_frame_1, orient = 'horizontal', command = text_ipt.xview)
scrollbar_ipt.place(x = 0, y = HEIGHT_IPT - BAR, width = WIDTH_IPT, height = BAR)
text_ipt.config(xscrollcommand = scrollbar_ipt.set)
text_ipt.bind('<Return>', lambda event: 'break')
text_ipt.bind('<Control-v>', lambda event: event.widget.insert(INSERT, filter_char(root.clipboard_get())) or 'break')
ipt_texts = ['↑', '↓', 'C', 'START']
ipt_funcs = [up_ipt, down_ipt, clear_ipt, show_result]
ipt_xs, ipt_ys = [WIDTH_IPT, WIDTH_IPT, WIDTH_IPT + WIDTH_U_D, WIDTH - BUTTON_WIDTH], [0, 25, 0, 0]
ipt_widths = [WIDTH_U_D, WIDTH_U_D, WIDTH_CLEAR, BUTTON_WIDTH]
ipt_heights = [HEIGHT_U_D, HEIGHT_U_D, HEIGHT_IPT, BUTTON_HEIGHT]
buttons_inputs = [Button(text_frame_1, text = ipt_texts[bid], font = FONT, command = ipt_funcs[bid]) for bid in range(INPUT_BUTTON_NUM)]
for bid in range(INPUT_BUTTON_NUM): buttons_inputs[bid].place(x = ipt_xs[bid], y = ipt_ys[bid], width = ipt_widths[bid], height = ipt_heights[bid])
canvas_legal = Canvas(text_frame_1, width = LENGTH_FLAG, height = LENGTH_FLAG, bg = 'red')
canvas_legal.place(x = WIDTH - BUTTON_WIDTH - LENGTH_FLAG, y = 0, width = LENGTH_FLAG, height = LENGTH_FLAG)
text_ipt.bind('<<Modified>>', change_flag)
# 快捷键
def quick_d100():
    ipt_string = input_get()
    if_integer, value = ifinteger(ipt_string)
    random_num = value if if_integer else 1
    show_result_base(f'{random_num}d100', 'classic')
def quick_d2():
    ipt_string = input_get()
    if_integer, value = ifinteger(ipt_string)
    random_num = value if if_integer else 1
    show_result_base(f'{random_num}d2', 'classic')
def quick_d10_d2(): show_result_base('1d10+1d2', 'classic')
def quick_d_d(): show_result_base('1d100:1d100', 'against')
def quick_RGB():
    protect()
    R_num, G_num, B_num = randint(0, 255), randint(0, 255), randint(0, 255)
    color_str = f'#{R_num:02X}{G_num:02X}{B_num:02X}'
    results = (R_num, G_num, B_num)
    strings = ['Random RGB:', f'(R,G,B) = ({R_num},{G_num},{B_num}) = ' + color_str]
    buttons_quicks[quick_texts.index('RGB')].config(bg = color_str)
    output_create_record(2, results, 'RGB')
    output_totext(strings)
    unprotect()
QUICK_BUTTON_NUM = 5
quick_frame = Frame(root)
quick_frame.place(x = 0, y = HEIGHT_IPT, width = QUICK_BUTTON_NUM * BUTTON_WIDTH, height = HEIGHT_BUTTON)
quick_texts = ['d100', 'd2', 'd10+d2', 'd:d', 'RGB']
quick_funcs = [quick_d100, quick_d2, quick_d10_d2, quick_d_d, quick_RGB]
buttons_quicks = [Button(quick_frame, text = quick_texts[bid], font = FONT, command = quick_funcs[bid]) for bid in range(QUICK_BUTTON_NUM)]
for bid in range(QUICK_BUTTON_NUM): buttons_quicks[bid].place(x = bid * BUTTON_WIDTH, y = 0, width = BUTTON_WIDTH, height = BUTTON_HEIGHT)
# 删除键
def delete_first():
    if len(output_lines_list) == 0: return
    protect()
    text_opt.config(state = 'normal')
    for _ in range(output_lines_list[0]): text_opt.delete('1.0', '1.end+1c')
    text_opt.config(state = 'disabled')
    output_delete_record('first')
    unprotect()
def delete_last():
    if len(output_lines_list) == 0: return
    protect()
    line_num = int(text_opt.index('end-1c').split('.')[0])
    text_opt.config(state = 'normal')
    for lid in range(output_lines_list[-1] + 1): text_opt.delete(f'{line_num - lid}.0', f'{line_num - lid}.end+1c')
    if len(output_lines_list) > 1: text_opt.insert(END, '\n')
    text_opt.config(state = 'disabled')
    output_delete_record('last')
    unprotect()
def delete_all():
    if len(output_lines_list) == 0: return
    protect()
    text_opt.config(state = 'normal')
    text_opt.delete('1.0', END)
    text_opt.config(state = 'disabled')
    output_delete_record('all')
    unprotect()
DELETE_BUTTON_NUM = 3
delete_frame = Frame(root)
delete_frame.place(x = WIDTH - 3 * BUTTON_WIDTH, y = HEIGHT_IPT, width = 3 * BUTTON_WIDTH, height = HEIGHT_BUTTON)
delete_texts = ['C-FIRST', 'C-LAST', 'C-ALL']
delete_funcs = [delete_first, delete_last, delete_all]
buttons_deletes = [Button(delete_frame, text = delete_texts[bid], font = FONT, command = delete_funcs[bid]) for bid in range(DELETE_BUTTON_NUM)]
for bid in range(DELETE_BUTTON_NUM): buttons_deletes[bid].place(x = bid * BUTTON_WIDTH, y = 0, width = BUTTON_WIDTH, height = BUTTON_HEIGHT)
# 保护函数
events = ['<Key>', '<Button-1>', '<Button-2>', '<Button-3>', '<B1-Motion>', '<B2-Motion>', '<B3-Motion>', '<Control-Key>']
buttons = [*buttons_quicks, *buttons_inputs, *buttons_deletes]
def protect():
    # 运行时保护
    for event in events: text_opt.bind(event, lambda event: 'break')
    for button in buttons: button.config(state = 'disabled')
    return
def unprotect():
    # 取消保护
    for button in buttons: button.config(state = 'normal')
    for event in events: text_opt.unbind(event)
    return
# 主循环
root.mainloop()
####################################################################################################
