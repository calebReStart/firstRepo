{"filter":false,"title":"inslinWeight.py","tooltip":"/NextLab/inslinWeight.py","undoManager":{"mark":33,"position":33,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":11},"action":"insert","lines":["import json"],"id":1}],[{"start":{"row":0,"column":11},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":0,"column":11},"end":{"row":1,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":0,"column":11},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":27},"action":"insert","lines":["def readJsonFile(fileName):"],"id":4}],[{"start":{"row":2,"column":27},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"insert","lines":["    "]},{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":["d"]},{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["a"]},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["t"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["a"]}],[{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":[" "],"id":6},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["="]}],[{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":[" "],"id":7}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":11},"action":"remove","lines":["data = "],"id":8},{"start":{"row":3,"column":4},"end":{"row":6,"column":15},"action":"insert","lines":["data = \"\"","    with open('files/insulin.json') as json_file:","        data = json.load(json_file)","    return data"]}],[{"start":{"row":3,"column":4},"end":{"row":6,"column":15},"action":"remove","lines":["data = \"\"","    with open('files/insulin.json') as json_file:","        data = json.load(json_file)","    return data"],"id":10},{"start":{"row":3,"column":4},"end":{"row":9,"column":15},"action":"insert","lines":["data = \"\"","    try:","        with open(fileName) as json_file:","            data = json.load(json_file)","    except IOError:","        print(\"Could not read file\")","    return data"]}],[{"start":{"row":2,"column":0},"end":{"row":9,"column":15},"action":"remove","lines":["def readJsonFile(fileName):","    data = \"\"","    try:","        with open(fileName) as json_file:","            data = json.load(json_file)","    except IOError:","        print(\"Could not read file\")","    return data"],"id":11},{"start":{"row":2,"column":0},"end":{"row":6,"column":15},"action":"insert","lines":["def readJsonFile(fileName):","    data = \"\"","    with open('files/insulin.json') as json_file:","        data = json.load(json_file)","    return data"]}],[{"start":{"row":6,"column":15},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":12},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]},{"start":{"row":7,"column":4},"end":{"row":8,"column":0},"action":"insert","lines":["",""]},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"remove","lines":["    "],"id":13}],[{"start":{"row":7,"column":4},"end":{"row":8,"column":0},"action":"remove","lines":["",""],"id":14},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"insert","lines":["p"],"id":15},{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"insert","lines":["r"]},{"start":{"row":7,"column":2},"end":{"row":7,"column":3},"action":"insert","lines":["i"]},{"start":{"row":7,"column":3},"end":{"row":7,"column":4},"action":"insert","lines":["n"]}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":6},"action":"insert","lines":["()"],"id":16}],[{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["d"],"id":17},{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["a"]},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["t"]},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["a"]}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["t"],"id":18}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "],"id":19}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "],"id":20}],[{"start":{"row":6,"column":15},"end":{"row":7,"column":0},"action":"remove","lines":["",""],"id":21}],[{"start":{"row":6,"column":25},"end":{"row":6,"column":26},"action":"remove","lines":[")"],"id":22},{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"remove","lines":["a"]},{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"remove","lines":["t"]},{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"remove","lines":["a"]},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"remove","lines":["d"]},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"remove","lines":["("]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"remove","lines":["t"]},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"remove","lines":["n"]},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"remove","lines":["i"]},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"remove","lines":["r"]},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"remove","lines":["p"]}],[{"start":{"row":6,"column":15},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":23},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "],"id":24},{"start":{"row":6,"column":15},"end":{"row":7,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":6,"column":15},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":25},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "],"id":26}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"insert","lines":["p"],"id":27},{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"insert","lines":["r"]},{"start":{"row":7,"column":2},"end":{"row":7,"column":3},"action":"insert","lines":["i"]},{"start":{"row":7,"column":3},"end":{"row":7,"column":4},"action":"insert","lines":["n"]},{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["t"]}],[{"start":{"row":7,"column":5},"end":{"row":7,"column":7},"action":"insert","lines":["()"],"id":28}],[{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["d"],"id":29},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["t"]}],[{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"remove","lines":["t"],"id":30}],[{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"remove","lines":[")"],"id":40},{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"remove","lines":["d"]},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"remove","lines":["("]},{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"remove","lines":["t"]},{"start":{"row":7,"column":3},"end":{"row":7,"column":4},"action":"remove","lines":["n"]},{"start":{"row":7,"column":2},"end":{"row":7,"column":3},"action":"remove","lines":["i"]},{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"remove","lines":["r"]},{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"remove","lines":["p"]},{"start":{"row":6,"column":15},"end":{"row":7,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":6,"column":15},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":41},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]},{"start":{"row":7,"column":4},"end":{"row":8,"column":0},"action":"insert","lines":["",""]},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"remove","lines":["    "],"id":42}],[{"start":{"row":8,"column":0},"end":{"row":15,"column":15},"action":"insert","lines":["def readJsonFile(fileName):","    data = \"\"","    try:","        with open(fileName) as json_file:","            data = json.load(json_file)","    except IOError:","        print(\"Could not read file\")","    return data"],"id":43}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":2},"action":"insert","lines":["# "],"id":44},{"start":{"row":3,"column":0},"end":{"row":3,"column":2},"action":"insert","lines":["# "]},{"start":{"row":4,"column":0},"end":{"row":4,"column":2},"action":"insert","lines":["# "]},{"start":{"row":5,"column":0},"end":{"row":5,"column":2},"action":"insert","lines":["# "]},{"start":{"row":6,"column":0},"end":{"row":6,"column":2},"action":"insert","lines":["# "]}]]},"ace":{"folds":[],"scrolltop":12.50000052452088,"scrollleft":0,"selection":{"start":{"row":2,"column":2},"end":{"row":6,"column":17},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1678460326032,"hash":"f92fcea3c0804ef306b853842e551fdcc97776dc"}