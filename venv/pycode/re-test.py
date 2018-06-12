"""
正则表达式
regular expression      regex       RE
正则表达式是用来简洁表达一组字符串的表达式

通用的字符串表达框架
简洁表达一组字符串的表达式
针对字符串表达“简洁”和“特征”思想的工具
判断某字符串的特征归属

表达文本类型和特征（病毒、入侵）


正则表达式的使用：
编译：将符合正则表达式语法的字符串转换成正则表达式特征

正则表达式语法：
正则表达式由字符和操作符构成
    操作符：
        .   表示任何单个字符
        []  字符集，对单个字符给出取值范围
                [abc]表示a、b、c，[a-z]表示a到z单个字符
        [^] 非字符集，对单个字符给出排除范围
                [^abc]表示非a或b或c的单个字符
        *   前一个字符0次或无限次扩展
                abc*表示ab、abc、abcc、abccc等
        +   前一个字符1次或无限次扩展
                abc+ 表示abc、abcc、abccc等
        ?   前一个字符0次或1次扩展
                abc? 表示ab、abc
        |   左右表达式任意一个
                abc|def 表示abc或def
        {m}     扩展前一个字符m次
                    ab{2}c 表示abbc
        {m,n}   扩展前一个字符m至n次（含n）
                    ab{2,4}c 表示abbc,abbbc,abbbbc
        ^       匹配字符串开头
                    ^abc 表示abc且在一个字符串的开头
        $       匹配字符串结尾
                    abc$ 表示abc且在一个字符串的结尾
        ()      分组标记，内部只能使用|操作符
                    (abc)表示abc，(abc|def)表示abc或def
        \d      数字，等价于[0-9]
        \w      单词字符，等价于[A-Za-z0-9_]

^[A-Za-z]+$     由26个字母组成的字符串
^[A-Za-z0-9]+$  由26个字母和数字组成的字符串
^-?\d+$         整数形式的字符串
^[0-9]*[1-9][0-9]*$     正整数形式的字符串
[1-9]\d{5}      中国境内邮政编码，6位
[\u4e00-\u9fa5] 匹配中文字符
\d{3}-\d{8}|\d{4}-\d{7}     国内电话号码，010-68913536

IP地址格式：
255.255.255.255
\d+.\d+.\d+.\d+
\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}

0-99:       [1-9]?\d
100-199:    1\d{2}
200-249:    2[0-4]\d
250-255:    25[0-5]

(([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5]).){3}([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])


re 库的使用：
    导入：import re

    raw string 类型（原生字符串类型）
    re库采用raw string类型表示正则表达式，表示为：r'text'
    例如：r'[1-9]\d{5}'
    r'\d{3}-\d{8}'
    string 类型，更繁琐

re库的主要功能函数：
    re.search()     在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
        参数：
            pattern:正则表达式的字符串或原生字符串表示
            string:待匹配字符串
            flags:正则表达式使用时的控制标记
                re.I re.IGNORECASE:忽略正则表达式的大小写，[A-Z]能够匹配小写字符
                re.M re.MULTILINE：正则表达式中的^操作符能够将给定字符串的每行当作匹配开始
                re.S re.DOTALL: 正则表达式中的.操作能够匹配所有字符，默认匹配除换行外的所有字符
        例：
            >>> match = re.search(r'[1-9]\d{5}','BIT 100081')
            >>> if match:
            ...     print(match.group(0))
            ...
            100081

    re.match()      从一个字符串的开始位置起匹配正则表达式，返回match对象
        参数：
            pattern:正则表达式的字符串或原生字符串表示
            string:待匹配字符串
            flags:正则表达式使用时的控制标记
                re.I re.IGNORECASE:忽略正则表达式的大小写，[A-Z]能够匹配小写字符
                re.M re.MULTILINE：正则表达式中的^操作符能够将给定字符串的每行当作匹配开始
                re.S re.DOTALL: 正则表达式中的.操作能够匹配所有字符，默认匹配除换行外的所有字符
        例：
            >>> match = re.match(r'[1-9]\d{5}','100081 BIT')
            >>> match.group(0)
            '100081'

            >>> match = re.match(r'[1-9]\d{5}','BIT 100081')
            >>> match.group(0)
            Traceback (most recent call last):
              File "<input>", line 1, in <module>
            AttributeError: 'NoneType' object has no attribute 'group'

    re.findall()    搜索字符串，以列表类型返回全部能匹配的子串
        参数：
            pattern:正则表达式的字符串或原生字符串表示
            string:待匹配字符串
            flags:正则表达式使用时的控制标记
        例：
            >>> ls = re.findall(r"[1-9]\d{5}", "BIT100081 TSU100084")
            >>> ls
            ['100081', '100084']

    re.split()      将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
        参数：
            pattern:正则表达式的字符串或原生字符串表示
            string:待匹配字符串
            maxsplit: 最大分割数，（超过最大分割数的）剩余部分作为最后一个元素输出
            flags:正则表达式使用时的控制标记
        例：
            >>> re.split(r"[1-9]\d{5}", "BIT100081 TSU100084")
            ['BIT', ' TSU', '']
            >>> re.split(r"[1-9]\d{5}", "BIT100081 TSU100084", maxsplit = 1)
            ['BIT', ' TSU100084']

    re.finditer()   搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
        参数：
            pattern:正则表达式的字符串或原生字符串表示
            string:待匹配字符串
            flags:正则表达式使用时的控制标记
        例：
            >>> for m in re.finditer(r"[1-9]\d{5}", "BIT100081 TSU100084"):
            ...     if m:
            ...         print(m.group(0))
            ...
            100081
            100084

    re.sub()        在一个字符串中替换所有的匹配正则表达式的子串，返回替换后的字符串
        参数：
            pattern:正则表达式的字符串或原生字符串表示
            repl:替换匹配字符串的字符串
            string:待匹配字符串
            count:匹配的最大替换次数
            flags:正则表达式使用时的控制标记
        例：
            >>> re.sub(r"[1-9]\d{5}", ":zipcode", "BIT100081 TSU100084")
            'BIT:zipcode TSU:zipcode'

re的等价用法：
    函数式用法：一次性操作
        ^
        |
        ˇ
    面向对象用法：编译后的多次操作
    pat = re.compile(r"[1-9]\d{5]") #将原生字符串编译成一个正则表达式对象
    rst = pat.search("BIT 100081")

    regex = re.compile(pattern, flags = 0)
        参数：
            pattern:
            flags:
    regex对象的方法与上面讲的6个方法一样，只是参数中不用传入 pattern参数

re库的match对象类型：
    主要属性：
        .string :待匹配的文本
        .re ：匹配时使用的pattern对象（正则表达式）
        .pos ： 正则表式搜索文本的开始位置
        .endpos ： 正则表达式搜索文本的结束位置

    常用方法：
        .group(0) ：获得匹配后的字符串
        .start() ： 匹配字符串在原始字符串的开始位置
        .end() ： 匹配字符串在原始字符串的结束位置
        .span() ： 返回（.start(), .end()）

re库的贪婪匹配和最小匹配
    >>> match = re.search(r"PY.*N", "PYANBNCNDN")
    >>> match.group(0)
    'PYANBNCNDN' #re默认使用贪婪匹配，返回匹配最长的字符串

    最小匹配：
    >>> match = re.search(r"PY.*?N", "PYANBNCNDN")
    >>> match.group(0)
    'PYAN'

    *?      前一个字符0次或无限次扩展，最小匹配
    +?      前一个字符1次或无限次扩展，最小匹配
    ??      前一个字符0次或1次扩展，最小匹配
    {m,n}?  扩展前一个字符m至n次（含n），最小匹配


"""