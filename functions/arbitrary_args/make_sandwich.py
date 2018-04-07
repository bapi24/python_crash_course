def make_sandwich(*items):
    print("The items you need on sandwich:")
    for item in items:
        print(" -" + item)

make_sandwich('cheese', 'whole wheat', 'nuts')
