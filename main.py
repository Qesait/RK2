from operator import itemgetter
from math import inf


class HardDrive:
    """Жёсткий диск"""

    def __init__(self, id, model, size, computer_id):
        self.id = id
        self.model = model
        self.size = size
        self.computer_id = computer_id


class Computer:
    """Компьютер"""

    def __init__(self, id, processor):
        self.id = id
        self.processor = processor


class HDComp:
    """
    'Жёсткий диск компьютера' для реализации
    связи многие-ко-многим
    """

    def __init__(self, computer_id, hard_drive_id):
        self.computer_id = computer_id
        self.hard_drive_id = hard_drive_id


def task_1(one_to_many):
    """
    «Компьютер» и «Жёсткий диск» связаны соотношением один-ко-многим.
    Выведите список всех жёстких дисков фирмы «Western Digital»,
    и названия процессоров компьютеров, в которые они установлены.
    """

    return [(record[0], record[2]) for record in one_to_many if record[0].startswith('Western Digital')]


def task_2(one_to_many):
    """
    «Компьютер» и «Жёсткий диск» связаны соотношением один-ко-многим.
    Выведите список процессоров компьютеров с минимальным объёмом диска в каждом компьютере,
    отсортированный по минимальному объёму диска.
    """

    mins = {}
    for model, size, processor in one_to_many:
        mins[processor] = min(mins.get(processor, inf), size)
    return sorted(mins.items(), key=itemgetter(1))


def task_3(many_to_many):
    """
    «Компьютер» и «Жёсткий диск» связаны соотношением многие-ко-многим.
    Вернуть список всех связанных жёстких дисков и компьютеров,
    отсортированный по объёму жёстких дисков, сортировка по компьютерам произвольная.
    """

    return sorted(many_to_many, key=itemgetter(1))
