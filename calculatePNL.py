def caclulatePNL(stream):
    i = 0
    trades = {}
    while i < len(stream):
        entry = stream[i]
        if entry[2] not in trades:
            trades[entry[2]] = [entry[0], entry[1], entry[3]]
