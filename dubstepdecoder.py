def song_decoder(song):
    lyrics = list(song)
    reallyrics = []
    i = 0
    wub = False
    while i < len(lyrics):
        if lyrics[i] == "W":
            if lyrics[i + 1] == "U":
                if lyrics[i + 2] == "B" and wub == False:
                    reallyrics.append(" ")
                    i += 3
                    wub = True
                else:
                    i += 3
        else:
            reallyrics.append(lyrics[i])
            wub = False
            i += 1
    x = "".join(reallyrics).strip()
    print(x)


song_decoder("WU")
