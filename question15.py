l = input().split(",")
new_list = [str(int(x) ** 2) for x in l if int(x)%2 != 0]
print(",".join(new_list))