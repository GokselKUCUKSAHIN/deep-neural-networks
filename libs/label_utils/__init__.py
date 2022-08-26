from typing import List
from typing import Dict


def load_labels_for_keras(path="labels.txt") -> Dict[int, str]:
    labels = {}
    with open(path, 'r') as file:
        for id, label in list(map(lambda pair: (int(pair[0]), pair[1]), map(lambda line: line.replace('\n', '').split(' '), file.readlines()))):
            labels[id] = label
        return labels


def render_bar(per: float, max_len=25):
    fill = round(max_len * per)
    left = max_len - fill
    return f"|{'█' * fill}{' ' * left}|"


def plot_activation(p_list, labels: Dict[int, str]) -> None:
    for i, val in enumerate(p_list):
        print(f"{labels[i]: <20}: {render_bar(val)} {val: .3f} %")


def save_labels_for_keras(label_list: List[str]) -> None:
    with open('labels.txt', 'w') as file:
        labels = "\n".join(list(map(lambda en: f"{en[0]} {en[1]}", enumerate(label_list))))
        file.write(labels)
