s = {'name':'zs',"age":20,'height':170}

# # 增加键值对：weight
# zs['weight'] = 70
#
# zs['weight'] = 80   # 覆盖掉原值
# print(zs)


# 增加键值对：weight
zs.setdefault('weight',70)
zs.setdefault('weight',80)   # 不覆盖，
# zs.setdefault('name','ls')   # 不能修改
print(zs)
