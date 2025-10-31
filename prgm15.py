color_list1=input("enter first color list(comma separated: ").split(',')
color_list2=input("enter second color list(comma separated; ").split(',')
diff= [color for color in color_list1 if color not in color_list2]
print("colors in list1 not in list2:",diff)
