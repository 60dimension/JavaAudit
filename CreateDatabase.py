# @Author: 60dimension
# @Date: 2023/4/2 12:28 下午

import os

SourceRoot='~/IdeaProjects/lowsec'
output='~/PycharmProjects/JavaAudit/database/lowsec'

#codeql createdatabse command
command='codeql database create --language=java --source-root '+SourceRoot+' ' +output

result=os.system(command)

print(result)

