import random

chunin_exam = ['Sasuke', 'Hanzo', 'Sakura', 'Naruto', 'Shikamaru', 'Ino', 'Chouji', 'Kabuto', 'Vitas', 'Gaara',
               'Temary',
               'Канкуро', 'Рок Ли', 'Неджи', 'Тентен', 'Шино', 'Хината', 'Заку', 'Кагари', 'Оборо', 'Муби', 'Шигуре',
               'Йорои',
               'Акамару']
ninja_index = random.randint(0, len(chunin_exam) - 1)
print(chunin_exam[ninja_index])
