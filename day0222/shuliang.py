import re
#* 匹配前一个字符出现0次或者无限次，即可有可无
result = re.findall("12*","13,45612,12,12789")
print(result)

#+ 匹配前一个字符出现1次或者无限次，即至少有1次
result = re.findall("ha+","hah,hanhanahhaa,aha")
print(result)

#? 匹配前一个字符出现1次或者0次，即要么有1次，要么没有
result = re.findall("ha?","hah,hanhanahhaa,aha")
print(result)

#{m} 匹配前一个字符出现m次
result = re.findall("nh{1}","nhaonio,nhhao,nnhaonh")
print(result)

#{m,} 匹配前一个字符至少出现m次
result = re.findall("ni{1}","nhaonio,nihhao,ninhaonih")
print(result)

#{m,n} 匹配前一个字符出现从m到n次
result = re.findall("ni{1,3}","nhaoniio,inihhao,niiinhaonih")
print(result)


