import os

Root = 'a'
Dest = 'b'

for (root, dirs, files) in os.walk(Root):
    new_root = root.replace(Root, Dest, 1)
    if not os.path.exists(new_root):
        os.mkdir(new_root)
    
    for d in dirs:
        d = os.path.join(new_root, d)
        if not os.path.exists(d):
            os.mkdir(d)
    
    for f in files:
        # 把文件名分解为 文件名.扩展名
        # 在这里可以添加一个 filter，过滤掉不想复制的文件类型，或者文件名
        (shotname, extension) = os.path.splitext(f)
        # 原文件的路径
        old_path = os.path.join(root, f)
        new_name = shotname + '_bak' + extension
        # 新文件的路径
        new_path = os.path.join(new_root, new_name)
        try:
            # 复制文件
            open(new_path, 'wb').write(open(old_path, 'rb').read())
        except IOError as e:
            print(e)