def avg(*args):
        total = 0
        for arg in args:
            total += arg
        return total/len(args)