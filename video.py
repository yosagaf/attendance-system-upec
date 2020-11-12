import yaml

with open("configs/config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile)

print(cfg["files"]["detector"])
print(cfg["files"]["embedding-model"])
print(cfg["files"]["recognizer"])
print(cfg["files"]["le"])

