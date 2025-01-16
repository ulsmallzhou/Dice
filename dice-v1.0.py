'''
    dice v1.0 by ulsmallzhou
    2025-01-15
'''
from numpy import sum as sum_all
from random import seed, randint
from time import time
from re import split as split_re, sub
seed(time())
from tkinter import Tk, Frame, Text, Scrollbar, Button, Canvas
from tkinter import INSERT, END
####################################################################################################



####################################################################################################
# 各类常量区
####################################################################################################
legal_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', 'd', '+', '-', '*']
operator_char = ['+', '-', '*']
num_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'd']
identify_code_0 = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0,
                   '8': 0, '9': 0, '(': 2, ')': 2, 'd': 1, '+': 3, '-': 3, '*': 3}
illegal_pears = ['()', ')0', ')1', ')2', ')3', ')4', ')5', ')6', ')7', ')8', ')9',
                 '0(', '1(', '2(', '3(', '4(', '5(', '6(', '7(', '8(', '9(', ')(',
                 '++', '+-', '+*', '-+', '--', '-*', '*+', '*-', '**', '(+', '(*', '+)', '-)', '*)']
MAX_ROLL = 100
MAX_CHAR = 500
events = ['<Key>', '<Button-1>', '<Button-2>', '<Button-3>', '<B1-Motion>', '<B2-Motion>', '<B3-Motion>', '<Control-Key>']
WIDTH, HEIGHT = 800, 600
HEIGHT_IPT, HEIGHT_BUTTON, HEIGHT_OPT = 50, 30, 520
WIDTH_IPT, WIDTH_START, WIDTH_QUICK, WIDTH_DELETE = 700, 100, 100, 100
BAR = 20
BUTTON_WIDTH, BUTTON_HEIGHT = 70, 30
LENGTH_FLAG = 30
AUTHOR = 'ulsmallzhou'
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

def iflegal_dfunction(ipt: str):
    '''纯数字+d表达式合法性审查'''
    if not isinstance(ipt, str): return False   # 确保是字符串
    if len(ipt) == 0: return False              # 确保非空
    for char in ipt:
        if char not in num_char: return False   # 确保均为数字或d
    if 'd' not in ipt: return True              # 纯数字合法
    first_d, d_num = ipt.find('d'), ipt.count('d')
    for cid in range(d_num):
        if ipt[cid + first_d] != 'd': return False
    return True

def iflegal_nobracket(ipt: str) -> bool:
    '''无括号指令合法性审查'''
    if not isinstance(ipt, str): return False   # 确保是字符串
    if len(ipt) == 0: return False              # 确保非空
    for char in ipt:
        if char not in legal_char: return False # 确保均为合法字符
    if '(' in ipt or ')' in ipt: return False   # 确保无括号
    if ipt[0] == '-': ipt = '0' + ipt           # 首位为负号则特殊处理
    fragments = split_re('[+]|[-]|[*]', ipt)
    if '' in fragments: return False            # 确保首尾不是符号且表达式合法
    f_num = len(fragments)
    for fid in range(f_num):                    # 数字+d片段合法性判别
        if not iflegal_dfunction(fragments[fid]): return False
    return True                                 # 所有数字均合法则表达式合法

def iflegal(ipt: str) -> bool:
    '''指令合法性审查'''
    if not isinstance(ipt, str): return False   # 确保是字符串
    if len(ipt) == 0: return False              # 确保非空
    if len(ipt) > MAX_CHAR: return False        # 确保长度不超过最大长度
    for char in ipt:
        if char not in legal_char: return False # 确保均为合法字符
    for illagal_pear in illegal_pears:
        if illagal_pear in ipt: return False    # 确保没有非法连接组合
    if_bracket_match, _, _, mainbracket_L, mainbracket_R = bracket_match(ipt)
    if not if_bracket_match: return False       # 确保括号匹配
    mainbracket_num = len(mainbracket_L)
    if mainbracket_num == 0: return iflegal_nobracket(ipt)  # 进入无括号判别阶段
    else:
        for bid in range(mainbracket_num):
            if not iflegal(ipt[mainbracket_L[bid] + 1:mainbracket_R[bid]]): return False
            inner_length = mainbracket_R[bid] - mainbracket_L[bid] + 1
            ipt = ipt[:mainbracket_L[bid]] + '0' * inner_length + ipt[mainbracket_R[bid] + 1:]
        return iflegal_nobracket(ipt)
####################################################################################################


####################################################################################################
# 计算与显示
####################################################################################################
def num_str(ipt_num: int) -> str:
    # 默认输入合法, 即输入为整数
    return str(ipt_num) if ipt_num >= 0 else '(' + str(ipt_num) + ')'

def random_base(randrange: int) -> int:
    # 默认输入合法, 即输入为整数
    if randrange == 0: return 0
    if randrange > 0: return randint(1, randrange)
    if randrange < 0: return randint(randrange, -1)

def split(ipt: str, if_d: bool) -> tuple[list[str]]:
    # 默认输入合法, 即输入为正常表达式
    _, _, _, mainbracket_L, mainbracket_R = bracket_match(ipt)
    mainbracket_num, mainbracket_text = len(mainbracket_L), []
    check_char = ['+', '-', '*', 'd'] if if_d else ['+', '-', '*']
    if mainbracket_num == 0:
        split_char = '[+]|[-]|[*]|d' if if_d else '[+]|[-]|[*]'
        fragments, operators = split_re(split_char, ipt), []
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

def standardization(ipt: str) -> str:
    # 默认输入为合法字符串
    if ipt[0] == '-': ipt = '0' + ipt
    if ipt[0] == 'd': ipt = '1' + ipt
    if ipt[-1] == 'd': ipt = ipt + '100'
    replace_0 = ['+d', '-d', '*d', '(d', 'd+', 'd-', 'd*', 'd)', '(-']
    replace_1 = ['+1d', '-1d', '*1d', '(1d', 'd100+', 'd100-', 'd100*', 'd100)', '(0-']
    for rid in range(len(replace_0)): ipt = ipt.replace(replace_0[rid], replace_1[rid])
    return ipt

def putbracket(ipt: tuple[int, list[str]]) -> tuple[int, list[str]]:
    # 为字符串添加前后括号
    value, strings, strings_new = ipt[0], ipt[1], []
    for string in strings: strings_new.append('(' + string + ')')
    strings_new[-1] = num_str(value)
    return (value, strings_new)

def crossmerge(ipt_out: list, ipt_in: list) -> list:
    # 默认输入合法, 即两个输入均为列表且len(ipt_out) == len(ipt_in) + 1
    length = len(ipt_in)
    opt = []
    for eid in range(length): opt.extend([ipt_out[eid], ipt_in[eid]])
    opt.append(ipt_out[-1])
    return ''.join(opt)

def calculation(values: list[int], operators: list[str]) -> tuple[int, list[str]]:
    # 默认输入合法, 即两个输入均为列表且len(values) == len(operators) + 1
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
    # 默认输入合法, 即三个输入均为整数且d_num为正
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
        result_opt = sum_all(results)
        opt_strs.append(num_str(result_opt))
        return (result_opt, opt_strs)
    result_0, strings_opt = d_right, []
    for dice_id in range(d_num):
        strings_opt.append('1' + 'd' * (d_num - dice_id) + num_str(result_0))
        result_0 = random_base(result_0)
    strings_opt.append(num_str(result_0))
    return (result_0, strings_opt)

def random_nooperator(ipt: str) -> tuple[int, list[str]]:
    # 默认输入合法, 即无外部加减乘
    fragments, operators = split(ipt, True)
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
    # 默认输入合法
    ipt = standardization(ipt)
    fragments, operators = split(ipt, False)
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
####################################################################################################


####################################################################################################
# 可视化框架
####################################################################################################
# 窗口
root = Tk()
root.title(f'Dice v1.0 - by {AUTHOR}')
root.geometry(str(WIDTH) + 'x' + str(HEIGHT))
root.resizable(False, False)
# 表达式输入
text_frame_1 = Frame(root)
text_frame_1.place(x = 0, y = 0, width = WIDTH_IPT, height = HEIGHT_IPT)
text_ipt = Text(text_frame_1, height = 1, width = 20, wrap = 'none', font=('Consolas', 18, 'bold'))
text_ipt.place(x = 0, y = 0, width = WIDTH_IPT, height = HEIGHT_IPT - BAR)
scrollbar_ipt = Scrollbar(text_frame_1, orient = 'horizontal', command = text_ipt.xview)
scrollbar_ipt.place(x = 0, y = HEIGHT_IPT - BAR, width = WIDTH_IPT, height = BAR)
text_ipt.config(xscrollcommand = scrollbar_ipt.set)
text_ipt.bind('<Return>', lambda event: 'break')
text_ipt.bind('<Control-v>', lambda event: event.widget.insert(INSERT, sub(r'[^0-9+\-*d()]', '', root.clipboard_get())) or 'break')
# 结果输出
output_lines_list = []
text_frame_2 = Frame(root)
text_frame_2.place(x = 0, y = HEIGHT - HEIGHT_OPT, width = WIDTH, height = HEIGHT_OPT)
text_opt = Text(text_frame_2, height = 100, width = 800, wrap = 'none', state = 'disabled', font=('Consolas', 18, 'bold'))
text_opt.place(x = 0, y = 0, width = WIDTH - BAR, height = HEIGHT_OPT - BAR)
scrollbar_y = Scrollbar(text_frame_2, orient = 'vertical', command = text_opt.yview)
scrollbar_y.place(x = WIDTH - BAR, y = 0, width = BAR, height = HEIGHT_OPT)
scrollbar_x = Scrollbar(text_frame_2, orient = 'horizontal', command = text_opt.xview)
scrollbar_x.place(x = 0, y = HEIGHT_OPT - BAR, width = WIDTH, height = BAR)
text_opt.config(yscrollcommand = scrollbar_y.set, xscrollcommand = scrollbar_x.set)
def show_result_base(ipt: str):
    protect()
    if not iflegal(ipt): return
    value, strings = dice(ipt)
    output_lines_list.append(len(strings) + 2)
    strings_opt = ['=' + string for string in strings][:-1]
    text_opt.config(state = 'normal')
    text_opt.insert(END, ' ' + ipt + '\n')
    for string in strings_opt: text_opt.insert(END, string + '\n')
    text_opt.insert(END, '=' + str(value) + '\n\n')
    seed(time())
    text_opt.config(state = 'disabled')
    unprotect()
def show_result(): show_result_base(text_ipt.get('1.0', END)[:-1])
def quick_d100():
    random_num = 1
    ipt_string = text_ipt.get('1.0', END)[:-1]
    if ipt_string.isdigit(): random_num = int(ipt_string)
    if ipt_string != '' and ipt_string[0] == '-' and ipt_string[1:].isdigit(): random_num = -int(ipt_string[1:])
    show_result_base(f'{random_num}d100')
def quick_d10_d2(): show_result_base('1d10+1d2')
def quick_d_d(): show_result_base('1d100-1d100')
# 合法显示与开始按钮
work_frame = Frame(root)
work_frame.place(x = WIDTH_IPT, y = 0, width = WIDTH_START, height = HEIGHT_IPT)
canvas_legal = Canvas(work_frame, width = LENGTH_FLAG, height = LENGTH_FLAG, bg = 'red')
canvas_legal.place(x = 0, y = 0, width = LENGTH_FLAG, height = LENGTH_FLAG)
text_ipt.bind('<<Modified>>', lambda event: canvas_legal.config(bg = '#00FF00' if iflegal(text_ipt.get('1.0', END)[:-1]) else 'red'))
text_ipt.bind('<<Modified>>', lambda event: text_ipt.edit_modified(False), add = '+')
start_button = Button(work_frame, text = "START", font = ('Consolas', 12, 'bold'), command = show_result)
start_button.place(x = LENGTH_FLAG, y = 0, width = BUTTON_WIDTH, height = BUTTON_HEIGHT)
# 快捷键
quick_frame = Frame(root)
quick_frame.place(x = 0, y = HEIGHT_IPT, width = 3 * BUTTON_WIDTH, height = HEIGHT_BUTTON)
quick_button_1 = Button(quick_frame, text = "d100", font = ('Consolas', 12, 'bold'), command = quick_d100)
quick_button_1.place(x = 0, y = 0, width = BUTTON_WIDTH, height = BUTTON_HEIGHT)
quick_button_2 = Button(quick_frame, text = "d10+d2", font = ('Consolas', 12, 'bold'), command = quick_d10_d2)
quick_button_2.place(x = BUTTON_WIDTH, y = 0, width = BUTTON_WIDTH, height = BUTTON_HEIGHT)
quick_button_3 = Button(quick_frame, text = "d-d", font = ('Consolas', 12, 'bold'), command = quick_d_d)
quick_button_3.place(x = 2 * BUTTON_WIDTH, y = 0, width = BUTTON_WIDTH, height = BUTTON_HEIGHT)
# 删除键
def delete_first():
    global output_lines_list
    if output_lines_list == []: return
    protect()
    text_opt.config(state = 'normal')
    for _ in range(output_lines_list[0]): text_opt.delete('1.0', '1.end+1c')
    text_opt.config(state = 'disabled')
    unprotect()
    del output_lines_list[0]
def delete_last():
    global output_lines_list
    if output_lines_list == []: return
    protect()
    line_num = int(text_opt.index('end-1c').split('.')[0])
    text_opt.config(state = 'normal')
    for lid in range(output_lines_list[-1] + 1): text_opt.delete(f'{line_num - lid}.0', f'{line_num - lid}.end+1c')
    if len(output_lines_list) > 1: text_opt.insert(END, '\n')
    text_opt.config(state = 'disabled')
    unprotect()
    del output_lines_list[-1]
def delete_all():
    global output_lines_list
    if output_lines_list == []: return
    protect()
    text_opt.config(state = 'normal')
    text_opt.delete('1.0', END)
    text_opt.config(state = 'disabled')
    unprotect()
    output_lines_list = []
delete_frame = Frame(root)
delete_frame.place(x = WIDTH - 3 * BUTTON_WIDTH, y = HEIGHT_IPT, width = 3 * BUTTON_WIDTH, height = HEIGHT_BUTTON)
delete_button_first = Button(delete_frame, text = "C-FIRST", font = ('Consolas', 12, 'bold'), command = delete_first)
delete_button_first.place(x = 0, y = 0, width = BUTTON_WIDTH, height = BUTTON_HEIGHT)
delete_button_last = Button(delete_frame, text = "C-LAST", font = ('Consolas', 12, 'bold'), command = delete_last)
delete_button_last.place(x = BUTTON_WIDTH, y = 0, width = BUTTON_WIDTH, height = BUTTON_HEIGHT)
delete_button_all = Button(delete_frame, text = "C-ALL", font = ('Consolas', 12, 'bold'), command = delete_all)
delete_button_all.place(x = 2 * BUTTON_WIDTH, y = 0, width = BUTTON_WIDTH, height = BUTTON_HEIGHT)
# 保护函数
buttons = [start_button, quick_button_1, quick_button_2, quick_button_3, delete_button_first, delete_button_last, delete_button_all]
def protect():
    # 运行时保护
    for event in events: text_opt.bind(event, lambda event: 'break')
    for button in buttons: button.config(state = 'disabled')
def unprotect():
    # 取消保护
    for button in buttons: button.config(state = 'normal')
    for event in events: text_opt.unbind(event)
# 主循环
root.mainloop()
####################################################################################################