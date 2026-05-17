def get_numeric_stat_from_modifier(modifier):
    return (modifier * 2) + 10

if __name__ == "__main__":
    temp = get_numeric_stat_from_modifier(modifier=-4)
    print(temp)