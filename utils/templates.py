
def getWorkSuggestionTemplate(work_type, topic):
    return """
    Below you will recieve a topic or description. Your goal is to provide between 3 and 5 suggestions of a """ + work_type + """ related to the topic or description. For each """ + work_type + """, provide a short introduction without revealing details of the plot.

    Here is an example of fiction books about the ultimate futility of life:
    1. "The Stranger" by Albert Camus:
    Camus' novel follows the detached Meursault as he grapples with the absurdity of existence, portraying the ultimate futility of conventional societal expectations.
    2. "Nausea" by Jean-Paul Sartre:
    In this existentialist classic, Roquentin's contemplation of existence in a small town becomes a profound exploration of the inherent nausea and meaninglessness of life.
    3. "The Road" by Cormac McCarthy:
    McCarthy's post-apocalyptic tale follows a father and son as they traverse a desolate world, reflecting on the futility of survival and the relentless march toward an uncertain future.
    4. "One Hundred Years of Solitude" by Gabriel García Márquez:
    Márquez's magical realist epic reflects on the cyclical nature of life, suggesting a sense of futility in the repetition of history and the human inability to escape predetermined patterns.

    Here is another example of paintings about the illusion of love:
    1: "The Lovers II" by René Magritte:
    Magritte's surrealist painting challenges the conventional notion of love by depicting two lovers with their heads veiled, questioning the authenticity and reality of the emotions involved.
    2: "Automat" by Edward Hopper:
    Hopper's iconic painting captures a woman alone in a restaurant, suggesting the isolation that can accompany the illusion of love and the complexities of human connection.
    3: "The Kiss" by Gustav Klimt:
    Klimt's masterpiece, featuring a couple locked in an intimate embrace surrounded by ornate patterns, explores the intertwining of love and the decorative, raising questions about the substance behind the illusion of passion.
    4: "The Birth of Venus" by Sandro Botticelli:
    Botticelli's iconic painting of Venus emerging from the sea symbolizes the idealized and mythological aspects of love, inviting contemplation on the illusionary nature of beauty and desire.

    TOPIC: """ + topic + """
"""

book_template = """
    You will receive information about a book.
    Your goal is to:
    - Find the book
    - Find the author
    - Find the year in which it was written

    Here is an example:
    Q: Of Mice And Men
    A: Of Mice And Men (1937) by John Steinbeck

    Here is another example:
    Q: guy names Jay who moves to New York and tries to win back his old girlfriend Daisy who is married to Tom
    A: The Great Gatsby (1925) by F. Scott Fitzgerald

    Q: {work_name}
    A:
"""

poem_template = """
    You will receive information about a poem.
    Your goal is to:
    - Find the poem
    - Find the poet
    - Find the year in which it was written

    Here is an example:
    Q: O Captain! My Captain!
    A: O' Captain, My Captain (1865) by Walt Whitman

    POEM: {work_name}

    YOUR RESPONSE:
"""

movie_template = """
    You will receive information about a movie.
    Your goal is to:
    - Find the movie
    - Find the director
    - Find the writer
    - Find the year in which it was released
    - Find the actors/actresses who starred in the movie

    Here is an example:
    Q:
    Taxi Driver
    A:
    Taxi Driver (1976)\n
    Directed by Martin Scorcese\n
    Written by Paul Schrader\n
    Starring Robert De Niro, Jodie Foster, Harvey Keitel, Cybill Shepherd


    MOVIE: {work_name}

    YOUR RESPONSE:
"""

tv_show_template = """
    You will receive information about a television show.
    Your goal is to:
    - Find the show
    - Find the creator of the show
    - Find the actors/actresses who starred in the show
    - Find the year in which it began
    - Find the year in which it ended. If it hasn't ended, display 'present'.
    - Find the number of seasons

    Here are two examples:
    Q:
    The Sopranos
    A:
    Sopranos (1999-2007) [6 seasons]\n
    Created by David Chase\n
    Starring James Gandolfini, Michael Imperioli, Edie Falco, Lorraine Bracco\n

    Q:
    8 Out of 10 Cats (2005-present) [21 seasons]\n
    Created by Channel 4\n
    Starring Jimmy Carr, Sean Lock, Jon Richardson\n


    SHOW: {work_name}

    YOUR RESPONSE:
"""

documentary_template = """
    You will receive information about a documentary.
    Your goal is to:
    - Find the documentary
    - Find the Director
    - Find the year in which it was released

    Here is an example:
    Q:
    Grizzly Man
    A:
    Grizzly Man (2005)\n
    Directed by Werner Herzog


    DOCUMENTARY: {work_name}

    YOUR RESPONSE:
"""

painting_template = """
    You will receive information about a painting.
    Your goal is to:
    - Find the painting
    - Find the artist
    - Find the year in which it was completed

    Here is an example:
    Q: Mona Lisa
    A: Mona Lisa (1519) by Leonardo da Vinci

    Painting: {work_name}

    YOUR RESPONSE:
"""

sculpture_template = """
    You will receive information about a sculpture.
    Your goal is to:
    - Find the sculpture
    - Find the sculptor
    - Find the year in which it was completed

    Here is an example:
    Q: The Thinker
    A: The Thinker (1904) by Auguste Rodin

    Sculpture: {work_name}

    YOUR RESPONSE:
"""

theatre_template = """
    You will receive information about a a play or a musical.
    Your goal is to:
    - Find the play/musical name
    - Find the writer(s)
    - Find the year in which it first premiered

    Here are three examples:
    Q: Death of a Salesman
    A: Death of a Salesman (1949) by Arthur Miller
    Q: A Streetcar Named Desire
    A: A Streetcar Named Desire (1947) by Tennessee Williams
    Q: The Importance of Being Earnest
    A: The Importance of Being Earnest (1895) by Oscar Wilde

    Play/Musical: {work_name}

    YOUR RESPONSE:
"""

work_rating_template = """
    What is the iMDB rating of {work_title}? Please provide only the rating in the format: 'rating/10'. If the rating does not exist or cannot be found, answer with 'N/A'
"""

work_introduction_template = """
    Introduce {work_title} in one paragraph
"""

shared_opinion_template = """
What are some opinions shared by {philosopher_list}?
"""

disagreements_template = """
What are some topics of disagreement between {philosopher_list}?
"""

philosopher_opinion_on_topic_template = """
Describe {philosopher}'s opinion on the topic below. Answer with two paragraphs.
TOPIC: {topic}
"""

different_views_template = """
Provide as many different philosophical views as you can on the topic below. For each view, provide a paragraph of explanation:\\nTopic: {topic}\\n
"""
