def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) and not isinstance(dog_age, int):
        raise TypeError("Age should be integer")

    age_dict = {"cat_age": cat_age, "dog_age": dog_age}
    human_age = []
    for key, value in age_dict.items():
        if value < 0:
            raise ValueError("Age should be 0+")
        if value <= 15:
            human_age.append(value // 15)
        elif 16 <= value <= 24:
            human_age.append(1 + (value - 15) // 9)
        else:
            if key == "cat_age":
                human_age.append(2 + (value - 24) // 4)
            if key == "dog_age":
                human_age.append(2 + (value - 24) // 5)

    return human_age
