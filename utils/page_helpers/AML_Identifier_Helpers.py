
def getWorkTitle(infoOutput, work_type):
    if (work_type == "Book" or work_type == "Poem" or work_type == "Painting" or work_type == "Sculpture" or work_type == "Play/Musical"):
        return infoOutput
    elif work_type == "Movie":
        try:
            title = infoOutput[0:infoOutput.index("Directed by")]
        except:
            title = ""
    elif work_type == "TV Show":
        try:
            title = infoOutput[0:infoOutput.index('[')]
        except:
            title = ""
    elif work_type == "Documentary":
        try:
            title = infoOutput[0:(infoOutput.index(')') + 1)]
        except:
            title = ""
    
    return title

