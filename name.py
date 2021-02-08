def combineNames(firstName, lastName):
    if len(firstName) == 0 or len(lastName) == 0:
        raise ValueError("firstName and lastName must both be non-empty")
    return firstName + " " + lastName
