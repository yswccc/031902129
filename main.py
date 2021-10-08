import sys
class Node(object):  # 定义一个类由于初始化
    def __init__(self):
        self.children = None
        # 标记匹配到了关键词
        self.flag = False


def add_word(root, word):  # 添加词库，构建字典树，dfa算法
    if len(word) <= 0:
        return
    node = root
    for i in range(len(word)):
        if node.children == None:
            node.children = {}
            node.children[word[i]] = Node()

        elif word[i] not in node.children:
            node.children[word[i]] = Node()

        node = node.children[word[i]]
    node.flag = True


def init(word_list):  # 调用add_word函数，增加词库
    root = Node()
    for line in word_list:  # 遍历添加进来的字符串
        add_word(root, line)
    return root


# The encode of word is UTF-8
# The encode of message is UTF-8
def key_contain(message, root):
    res = []  # 用来存储查询出的关键词
    d_flag = {}  # 用来存储一行重复两次及以上的词
    for i in range(len(message)):
        p = root
        j = i
        while (j < len(message) and p.children != None and message[j] in p.children):
            if p.flag == True:  # 查找到关键词
                res.append(message[i:j])  # 切片找关键词
            p = p.children[message[j]]
            j = j + 1
        if p.children == None:
            res.append(message[i:j])
    return res
def dfa():
    count = 0
    word_path = sys.argv[1]
    org_path = sys.argv[2]
    ans_path = sys.argv[3]
    word_file = open(word_path, encoding='utf-8')
    org_file = open(org_path, encoding='utf-8')
    ans_file = open(ans_path, 'w', encoding='utf-8')
    org_list = org_file.readlines()
    word_list = word_file.readlines()
    result_list = []  # 以下至88行用于将文本words.txt读出的关键词中换行符号去掉（不去的话本人的函数无法使用）
    for i in word_list:
        if i != '':
            i = i.strip()
            if i != '':
                result_list.append(i)
    root = init(result_list)  # 调用init 构建树
    for i, item in enumerate(org_list):
        x = key_contain(item, root)  # item是按行读出的文本
        for key_word in x:  # x是存储关键词的集合，用key_word读出
            ans_file.write('Line' + str(i + 1) + ':' +' '+ '<' + key_word + '>'+' ' + key_word + '\n')
            count = count + 1
    word_file.close()
    org_file.close()
    ans_file.close()
    with open(ans_path, 'r+', encoding='utf-8') as f:  # 以下用来插入统计之后的Total
        content = f.read()
        f.seek(0, 0)
        f.write('Total' + ':' +' '+str(count) + '\n' + content)


if __name__ == '__main__':
    dfa()