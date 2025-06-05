class Person:
    def __init__(self,name, gender, age, study, work):
        self.name = name
        self.gender = gender
        self.age = age
        self.study = study
        self.work = work

id_1 = Person('Вася','муж.', 18, 'колледж', 'доставка')
id_2 = Person('Ярослав','муж.', 28, 'универ', 'сварщик')
id_3 = Person('Маша','жен.', 23, 'колледж', 'кассир')

print(id_1.__dict__)#12