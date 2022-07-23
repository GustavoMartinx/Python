class Count:
    count = 0 # atributo de classe

    @classmethod
    def inc(cls):
        cls.count += 1
        return cls.count

    def inst(self):
        return "I'm fine!"
    
    @classmethod
    def dec(cls):
        cls.count -= 1
        return cls.count

    @staticmethod
    def more_one(n):
        return n + 1

c1 = Count()
print(c1.inst())

print(Count.inc())
print(Count.inc())
print(Count.inc())
print(Count.dec())
print(Count.dec())
print(Count.dec())
print(Count.more_one(99))
