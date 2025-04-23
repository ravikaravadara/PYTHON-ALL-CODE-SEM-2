def count_lower_upper(s):
    result = {"uppercase": sum(1 for c in s if c.isupper()), "lowercase": sum(1 for c in s if c.islower())}
    return result
print(count_lower_upper("Hello World!"))
