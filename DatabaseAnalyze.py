# @Author: 60dimension
# @Date: 2023/4/2 1:29 下午
import os

database='~/PycharmProjects/JavaAudit/database/lowsec/'
query='/Users/seckeep/PycharmProjects/codeql/java/ql/src/Security/CWE/CWE-089/'

#codeql database analyze command
command='codeql database analyze '+database+' --format=sarif-latest --output=./output.csv'+' '

result=os.system(command)


