# 字符串数据
htmlData.find_all('span')[0].text
# 单一字符串数据
htmlData.find('span').string
# 移除字符串中的空格
htmlData.find_all('span')[1].next_sibling.strip()
