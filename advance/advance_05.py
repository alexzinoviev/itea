import random, math

class Pool:
    def __init__(self, w, l, b_f, s_f):
        self._w = w
        self._l = l
        self._fishes = self._create_fishes(BigFish, b_f) + \
                      self._create_fishes(SmallFish, s_f)

    def _create_fishes(self, cls, qty):
        return [cls(
            random.randint(1, self._w),
            random.randint(1, self._l)
        ) for _ in range(qty)]


    def move_fishes(self):
        for fish in self._fishes:
            fish.move()

    def get_width(self):
        return self._w

    def get_length(self):
        return self._l

    def get_nearest_small_fish(self, x, y):
        return min([fish for fish in self._fishes if isinstance(fish, Eatable)]),# проверяем что наша рыба принадлежит классу SmallFish
        key=lambda _ : _.get_distance(x,y)

    def __repr__(self):
        return  '\n'.join([str(fish) for fish in self._fishes])


class Fish:
    def __init__(self, x, y, pool):
        self._x = x
        self._y = y
        self._pool = pool

    def get_distance(self, x, y):
        return math.hypot(self._x - x, self._y - y)

    def __repr__(self):
        return "{}(x={}, y={})".format(
            self.__class__.__name__,
            self._x,
            self._y
        )


class Eatable:
    pass


class SmallFish(Fish, Eatable):
    def __init__(self, x, y, pool: Pool):
        super().__init__(x, y, pool)

    def move(self):
        self._x = self._x + random.randint(-1, 1)
        self._y = self._y + random.randint(-1, 1)
        self._x = 1 if self._x < 1 else self._x
        self._x = self._pool.get_width() if self._x > self._pool.get_width()\
            else self._x
        self._y = 1 if self._y < 1 else self._y
        self._y = self._pool.get_length() if self._y > self._pool.get_length()\
            else self._y





class BigFish(Fish):
    def __init__(self, x, y, pool):
        super().__init__(x, y, pool)

    def move(self):
        pass


if __name__ == '__main__':
    p = Pool(10, 10, 3, 5)
    print(p)