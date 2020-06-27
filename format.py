n1 = input("Enter a noun:")
v = input("Enter a verb:")
adj = input("Enter an adj:")
n2 = input("Enter a noun:")

# both of the following produce the same
result1 = "The {} {}s the {} {}".format(n1, v,adj, n2)
result2 = f"The {n1} {v}s the {adj} {n2}"

print(result1)
print(result2)