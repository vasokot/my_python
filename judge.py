class multifilter():
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        if pos >= neg:
            return True
        else:
            return False


    def judge_any(pos, neg):
    # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        if  pos >=1:
            return True
        else:
            return False



    def judge_all(pos, neg):
    # допускает элемент, если его допускают все функции (neg == 0)
        if neg == 0:
            return True
        else:
            return False



    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.judge = judge
        self.lst = iterable
        self.funcs = funcs
        self.i = 0

    def __next__(self):
        if self.i < len(self.lst):
            self.pos = 0
            self.neg = 0
            for foo in self.funcs:
                if foo(self.lst[self.i]):
                    self.pos += 1
                else:
                    self.neg += 1

            if self.judge(self.pos, self.neg):
                self.i += 1
                return self.lst[self.i-1]
            else:
                self.i += 1
                return next(self)

        else:
            raise StopIteration


    def __iter__(self):
    # возвращает итератор по результирующей последовательности
        return self


def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5)))

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))