code = ['a.sh', 'b.java', 'c.cpp', 'd.go', 'e.sql', 'f.py']

# 让.sh文件和.py文件有用户可执行权限
for code_name in code:
    print(code_name, code_name.endswith(('.sh', '.py')))

res = [code_name for code_name in code if code_name.endswith(('.sh','.py'))]
print(res)