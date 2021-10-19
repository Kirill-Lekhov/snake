from operator import add


def create_body(direction: tuple, head: list, sections_number: int = 3):
    if not sections_number:
        return head

    head.append(tuple(map(add, head[-1], direction)))
    sections_number -= 1

    return create_body(direction, head, sections_number)


if __name__ == "__main__":
    pass
