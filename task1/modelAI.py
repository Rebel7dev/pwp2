import json

class ModelAI:
    counter = 0

    def __init__(self, name, version):
        self.name = name
        self.version = version
        ModelAI.counter += 1

    @classmethod
    def cout_model(cls):
        return (f"Liczba utworzonych obiektów: {cls.counter}")

    @classmethod
    def from_file(cls, filename):
        with open(filename, "r") as file:
            data = json.load(file)
        
        return cls(data['name'], data['version'])

modelParse = ModelAI.from_file("model.json")
print(modelParse.name, modelParse.version)
print(ModelAI.cout_model())

model2 = ModelAI("aaa", 9)
model3 = ModelAI("bbb", 8)
print(ModelAI.cout_model())
