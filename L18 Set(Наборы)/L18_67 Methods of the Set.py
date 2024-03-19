photo_size = {'1920x1080', '800x600'}
other_size = {'800x600', '1024x768'}
photo_size.add('1024x768')
all_size = photo_size.union(other_size)
print(len(photo_size))
print(photo_size)
print(all_size)
intersection_size = photo_size.intersection(other_size)
print(intersection_size)

nums = {10, 5, 35}
others_nums = {20, 5, 12, 10, 35}
res = nums.issubset(others_nums)  # 'nums' este submultimea lui 'other_nums'
print(res)  # True
res2 = others_nums.issuperset(nums)  # 'others_nums' este supramultimea lui 'nums'
print(res2)  # True
