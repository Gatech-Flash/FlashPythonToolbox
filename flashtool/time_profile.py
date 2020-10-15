
def line_time_profiler(stop=False):
    def Inner(func):
        def wrapper(*args, **argv):
            from line_profiler import LineProfiler
            profile = LineProfiler()
            f_wrapped = profile(func)
            value = f_wrapped(*args, **argv)
            profile.print_stats()
            if stop:
                import ipdb; ipdb.set_trace()
            return value

        return wrapper
    return Inner

if __name__ == '__main__':
    @line_time_profiler()
    def f(n=1000):
        a = [1 for _ in range(n)]
        b = sum(a)

    f()
    f(10000)

    class C:
        @line_time_profiler()
        def f(self, n=1000):
            a = [1 for _ in range(n)]
            b = sum(a)

    ins = C()
    ins.f()
    ins.f(10000)


    @line_time_profiler(stop=True)
    def f(n=1000):
        a = [1 for _ in range(n)]
        b = sum(a)

    f()

