import json


class JsonMixin:
    @classmethod
    def from_json(cls, data):
        kwargs = json.loads(data)
        return cls(**kwargs)


class GameHero(JsonMixin):
    def __init__(self, armor=None, weapons=None):
        self.armor = Armor(**armor)
        self.weapons = [Weapon(**kwargs) for kwargs in weapons]


class Armor(JsonMixin):
    def __init__(self, capacity=None, weight=None):
        self.capacity = capacity
        self.weight = weight


class Weapon(JsonMixin):
    def __init__(self, attack=None, range=None, name=None):
        self.attack = attack
        self.range = range
        self.name = name

serialized_hero_data = """{
    "armor": {"capacity": 10, "weight": 200},
    "weapons": [
        {"attack": 10, "range": 20, "name": "One-handed sword"},
        {"attack": 15, "range": 10, "name": "One-handed dagger"}
    ]
}"""

deserialized_hero_data = GameHero.from_json(serialized_hero_data)
