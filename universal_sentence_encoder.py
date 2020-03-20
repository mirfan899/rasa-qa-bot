# https://www.nishanpantha.com.np/programming/universal-sentence-encoder-semantic-search.html
import re

import numpy as np
import tensorflow_hub as hub


def get_features(texts):
    if type(texts) is str:
        texts = [texts]
        return embed(texts)


def semantic_search(query, data, vectors):
    query = process_text(query)
    print("Extracting features...")
    print(get_features(query)[0])
    query_vec = get_features(query)[0]
    res = []
    for i, d in enumerate(data):
        qvec = vectors[i]
        sim = cosine_similarity(query_vec, qvec)
        res.append((sim, d[:100], i))
    return sorted(res, key=lambda x: x[0], reverse=True)


def cosine_similarity(v1, v2):
    mag1 = np.linalg.norm(v1)
    mag2 = np.linalg.norm(v2)
    if (not mag1) or (not mag2):
        return 0
    return np.dot(v1, v2) / (mag1 * mag2)


def test_similarity(text1, text2):
    vec1 = get_features(text1)[0]
    vec2 = get_features(text2)[0]
    print(vec1.shape)
    return cosine_similarity(vec1, vec2)


# tensorflow hub module for Universal sentence Encoder

module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"

embed = hub.load(module_url)


def remove_stopwords(stop_words, tokens):
    res = []
    for token in tokens:
        if not token in stop_words:
            res.append(token)
    return res


def process_text(text):
    text = text.encode('ascii', errors='ignore').decode()
    text = text.lower()
    text = re.sub(r'http\S+', ' ', text)
    text = re.sub(r'#+', ' ', text)
    text = re.sub(r'@[A-Za-z0-9]+', ' ', text)
    text = re.sub(r"([A-Za-z]+)'s", r"\1 is", text)
    text = re.sub(r"won't", "will not ", text)
    text = re.sub(r"isn't", "is not ", text)
    text = re.sub(r"can't", "can not ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub('\W', ' ', text)
    text = re.sub(r'\d+', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    return text


# def lemmatize(tokens):
#     lemmatizer = nltk.stem.WordNetLemmatizer()
#     lemma_list = []
#     for token in tokens:
#         lemma = lemmatizer.lemmatize(token, 'v')
#         if lemma == token:
#             lemma = lemmatizer.lemmatize(token)
#         lemma_list.append(lemma)
#     # return [ lemmatizer.lemmatize(token, 'v') for token in tokens ]     return lemma_list


def process_all(text):
    text = process_text(text)
    return text


data = [
    "who are you?",
    "where do you live?",
    "what are your goals?",
    "what does life mean to you?",
    """I bet you know about the classic Mario game and probably have played it. You are on a quest, moving from levels to levels in search of a princess that has been kidnapped. You crush all the spooky dogs and flying turtles with the superpowers such as transforming into giant, shooting out bullets. But hey! On top of the energy of a naive Mario, you seamlessly have played the never-ending game of Pacman — yes the world where these elusive ghosts chase you (the ultimate player) for the reason that seems mysterious. Lust It’s funny how you move around the strange two-dimensional world, just for the sake of eating, eating and eating. Yes, the only reason you move is with this mysterious force to devour everything in the path. You can never get enough of it. In your life, there is always something more you want. That need never gets quenched. The game is a reflection of lust. Eternal Dissatisfaction Your lust never dies. You move from level to level. Your existence has no meaning. Your life is an endless rush into oblivion. You don’t realize what you have been missing the whole time. You don’t even dare to stop. Because if you do, the ghosts in your mind devour you completely. There’s always this dissatisfaction in your life that interrupts the harmony between your soul and the world outside. Desire Desire is something that bounds life itself to the existence. Your desire for more; more never ends. Money, love, life, and all the chaos. That’s all you think of. You can’t put aside your desires and be yourself. You can’t really focus on your own “I, Me and Myself” against the world that wants more and more. Levels upon levels upon levels, your existence thrive upon these uncanny behaviors. Achievement While life is chasing you and you are chasing the unknowns, there comes a point in life where you feel achieved. You feel you can conquer the world. You can triumph over the ghosts in your mind. That satisfaction of achievement ultimately boosts your inner pride; hence your inner peace is restored. It’s this factor that really factors out all the negativity in your life. But, again life happens. The achievement; you can’t really get enough of it. Hence, the ultimate cycle continues: Lust, dissatisfaction, desire and achievement makes you who you should be. i live in the land of nowhere. I am doing fine in my life which is very chaos. I am trying to find myself among chaos and peace.""",
    """I am paradox and there exists a theoretical limit to human mind that any imagination is not unbound yet there is something that meets the eye. The eye itself is an absolute organ to wisdom. Wisdom is something that is derived from mutation of knowledge with experience. Yet, there exists a paradox on how much wise a man is even if there is no bound to the lies s/he tells. You suffer; you struggle. Struggle is the path to the wisdom and yet there lies a paradox on how much one can tolerate. Tolerance is eternal; knowledge is bounded. Endurance is a paradox. Paradox in a sense that you never know how much a mind can endure until you have exposed everything to the mind. You can laugh; you can cry. It’s ok to cry. Cry you heart out. Crying is a spiritual path to let your sufferings out to the ever paradoxical world. You can laugh your ass off but you can never put your heart into the laughing unless you know what the context is. Every animal struggles, endures, cries and laughs. One can suffer spiritually as well as physically. If spiritually one feels the sufferings, there’ll be no peace of mind. Yet there lies a paradox in life. Paradox in life is paradoxical. “Paradox” itself is a paradox. You cannot define the absolute lifespan of a paradox because you never get to live physically throughout your life. Indeed, life mocks everyone. It’s like that little piece of paper that slits your throat and you’ll never know how you died because you were blind the whole time. You may not feel the pain. But the suffering is real. Now, knowledge is that paper and you are the wisdom. Knowlege pours life into nullness, yet it is can kill one’s spirit. Knowlege has never been an absolute wisdom. Absoluteness of a wisdom can never really exists. Existence in a sense one can never feel the real happiness until s/he has transcended to some meta reality. Reality mocks everyone. It has been from the ancient times. Time is a fuzzy feeling. Fuzziness persists. Yet, you always tell “how much” time has gone by. Because you feel time. You never really kiss it. Those sarcastic tone that every time gives. Time creeps yet it slips away. You never really know what it can give you. Time is pretty paradoxical. Paradoxical in a sense that you always procrastinate. Procrastination is real, so is your mind. Theoretically, time can fall and you can too. You can never really know the feeling. Now, there lies a paradox about mind itself. Mind is nothing but your brain and your brain is only the combinations of indidvidual cells. Now the greatest paradox of mind is the consciousness. You feel, suffer, look, taste, struggle, endure. It’s all in your mind and you still have a feeling of unity of your mind and body. So, who gets the wisdom? Consciousness is just a combination of chemicals and the signals that overpower your brain. There really exists a dilemma on who/what controls you and perhaps who are you in a true sense. In the end, you are just living a life full of paradoxes and whole reality you perceive has been established on the basis of assumptions. Life is just an assumption and you should be the one who can hypothesize, transcend, believe, execute, halt and moreover live with personal satisfaction.""",
    """It’s funny how most of the humans loathe cockroaches. Well, it’s in human nature to develop some kinds of fear against creepiness and Entomophobia persists really hard in the mind. Despite the fact, cockroaches have always intrigued me. Not because I like to kill ’em all; but how we humans are pretty similar to cockroaches in terms of behaviours and opportunities we ought to seek. Humans, the opportunity-seeking being, lash out during high time. A small opportunity tend to spawn dozens of humans from nowhere. We crawl out from the hell’s kitchen of our own mind to snatch something that might be ours if we really tried hard. Yet, before these dark times, we incubate our mind for lesser known reasons. Procrastination and precrastination sway our mind lest we be helding our seemingly-unartistic thoughts. There’s fear of beings with higher skills and intelligent. So, we try to slither quickly to rule over the things we want/wanted; like cockroaches trying to snatch the food before the humans pulverize them. We try to come clean It’s funny how we humans think cockroaches as the creature of dirt and roughness. We despise them, yet we are hidden from the fact that cockroaches are pretty clean insects. As enotmologist say, cockroaches constantly clean (groom) themselves. They run their legs and antennae over their bodies, then clean those appendages with their mouthparts. Ever see a cat groom? Cockroaches make cats look like slobs. It might be they despise us in fact. So, we try to come clean as well. We act as if we are the only thing that can do something for own greater good. We try to act cool, fake a smile, fake our social activities and above all fake the social-online status just to be treated like a mighty little creature. And that’s the reason we try to show ourselves clean. Clean in a sense of own twisted reputations that illusions the real “self”. We are creepy Cockroaches give you creeps. But we humans are no different. We slither over the land of hidden likeness, infatuation, love and lust. These are similar words with different sentiments. In our life we struggle hard to find someone we can have connection mentally. But that’s a long journey — a very long and timeless road. Before finding someone we feel connected to, the other phases try to creep into the mind; seep through our lustful nature. I don’t know what cockroaches are thinking But I do know humans are more savage, and lesser being than cockroaches. The nuisance to the nature. The resentment among each other. The creatures that try to live in a reality powered by chaos illusions….""",
    """life is just like this very stage where we keep on moving back/forth. And most of the time, we feel much comfortable around the middle part. Or just staying at one point. Learning is a continuous process. It happens throughout our life. Right from the birth till our inevitable fate, death.""",
    """We are all no-brainers. You have someone in your chat list who can really inspire you to learn stuffs. (Dog knows what, s/he really cares about you, perhaps.) Asking about the things you find difficult to grasp can really clear your confusion on the topics. You expose your true self by asking questions. If that’s a drag, just don’t fret about it. Take a nap. Reboot your mind for a fresh start for the formal actions mentioned. And, don’t forget to attain seminars and meetups for self-improvement. Interaction with people might boost your confidence at some level. Yes, I know being an introvert is a let down. But, hey! At least we can give it a try. Still we learn nothing""",
    """As the human civilization soar high through the unknown passage of time, knowledge has been the essence in every life. Knowledge is the information and we human thrive for information; not to smooth-out our whole life, but to find pleasure and happiness. Human beings rise on the giant shoulder of the knowledge that has been passed down from generations, so that the future won’t live like dead. The very books, scrolls, papers, that has powered the information pool of today is the key that our source of knowledge is enriched and well lived. Gathering knowledge is good enough to make one’s life. However being “wise” is more than simply having knowledge. It is one thing to memorize the books and facts. However it is the wise thing to use those knowledge to drive the forces for betterment. Boxing up concept is good enough , but ability to think outside the box is greater. (as In the passage by Bertrand Russell) The very example of nuclear outbreak is enough to make us realize the boundaries where knowledge and wisdom get separated as two entities. The creation of nuclear energy is from knowledge. However had mankind been wise enough, the atomic bombing would not be alive in the history books we read today. The very core of every civilization may be the knowledge that powers it. However, it is the wisest words earned through experience of life and death that could have made humans a boon to nature. You may know how to propose a girl (that’s knowledge). However it is the wisdom to find “true love and happiness”. He who refines the knowledge can seek the wisdom that was not sought. A person that has learnt the way of life and time may have wisdom because he/she has stood up from the mistakes that had been committed in the life. “Knowledge is power, wisdom is light”, as I say. We humans have developed and advanced so much through the knowledge that has been passed down from generation to generation, we are more informative and knowledgeable today than the people were in the past. The sole reason is “tons” of information that we have today. Be it from Sir Isaac Newton, Leonardo Da Vinci, Aristotle to Sigmund Freud to that professor who teaches in your class. I don’t mean to wipe out their legacy, here Well, they are all knowledgeable, informative and can make you understand the concept of so-called world. You may have better information from the information-pool of tons of books and the internet of lies, there are few in million who are wise enough. People in the past were much WISER than that of today. And it is not the matter of simplicity that defines the wisdom, it is much complex that ought to be. Life, death, self-awareness, experience, feelings, sense of priority, comprehensiveness, are all that summed up to refine a centered-knowledge into the wiser information for wisdom. We may have progressed in science, technology, health,etc through the infinite knowledge-pool we have today but we do not know much about how to teach wisdom. In the course of time, the wiser words had been abandoned in favour of personal or community improvements. Those awesome people of the past who learnt the hard way through struggle , experiences were wise enough to give you “revival” potion for your life, for humanity and mankind. Just as a growing child senses the world through a mere physical form, gradually gains the hold of the world outside, it is the wisdom that teaches that child to act in the puppeted-world to have a self-esteem and to love others; world-centered knowledge he/she gains and gradually gains wisdom. that is wisdom, an evolved knowledge; gained selfishly or selflessly""",

]

data_processed = list(map(process_text, data))
BASE_VECTORS = embed(data)

semantic_search("what is your name", data_processed, BASE_VECTORS)
