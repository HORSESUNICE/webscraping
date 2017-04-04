import re
import string
import operator

def isCommon(ngram):
    commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it", "i", "that", "for", "you", "he", "with", "on", "do", "say", "this", "they", "is", "an", "at", "but","we", "his", "from", "that", "not", "by", "she", "or", "as", "what", "go", "their","can", "who", "get", "if", "would", "her", "all", "my", "make", "about", "know", "will","as", "up", "one", "time", "has", "been", "there", "year", "so", "think", "when", "which", "them", "some", "me", "people", "take", "out", "into", "just", "see", "him", "your", "come", "could", "now", "than", "like", "other", "how", "then", "its", "our", "two", "more", "these", "want", "way", "look", "first", "also", "new", "because", "day", "more", "use", "no", "man", "find", "here", "thing", "give", "many", "well"]
    for word in ngram:
        if word in commonWords:
            return True
    return False

def cleanText(input):
    input = re.sub('\n+', " ", input).lower()
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = re.sub("u\.s\.", "us", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    return input

def cleanInput(input):
    input = cleanText(input)
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

def getNgrams(input, n):
    input = cleanInput(input)
    output = {}
    for i in range(len(input)-n+1):
        if isCommon(input[i:i+n]) is False:
            ngramTemp = " ".join(input[i:i + n])
            if ngramTemp not in output:
                output[ngramTemp] = 0
            output[ngramTemp] += 1
    return output

def getFirstSentenceContaining(ngram, content):
    #print(ngram)
    content=content.lower()
    sentences = content.split(".")
    for sentence in sentences:
        if ngram in sentence.strip():
            return sentence.strip()[0].upper()+sentence.strip()[1:]+'.'
    return ""


content='''
I stand here today humbled by the task before us, grateful for the trust you have bestowed, mindful of the sacrifices borne by our ancestors. I thank President Bush for his service to our nation, as well as the generosity and cooperation he has shown throughout this transition.   Forty-four Americans have now taken the presidential oath. The words have been spoken during rising tides of prosperity and the still waters of peace. Yet, every so often the oath is taken amidst gathering clouds and raging storms. At these moments, America has carried on not simply because of the skill or vision of those in high office, but because We the People have remained faithful to the ideals of our forbearers, and true to our founding documents.  So it has been. So it must be with this generation of Americans.   That we are in the midst of crisis is now well understood. Our nation is at war, against a far-reaching network of violence and hatred. Our economy is badly weakened, a consequence of greed and irresponsibility on the part of some, but also our collective failure to make hard choices and prepare the nation for a new age. Homes have been lost; jobs shed; businesses shuttered. Our health care is too costly; our schools fail too many; and each day brings further evidence that the ways we use energy strengthen our adversaries and threaten our planet.   These are the indicators of crisis, subject to data and statistics. Less measurable but no less profound is a sapping of confidence across our land - a nagging fear that America’s decline is inevitable, and that the next generation must lower its sights.   Today I say to you that the challenges we face are real. They are serious and they are many. They will not be met easily or in a short span of time. But know this, America - they will be met.   On this day, we gather because we have chosen hope over fear, unity of purpose over conflict and discord.   On this day, we come to proclaim an end to the petty grievances and false promises, the recriminations and worn out dogmas, that for far too long have strangled our politics.  We remain a young nation, but in the words of Scripture, the time has come to set aside childish things. The time has come to reaffirm our enduring spirit; to choose our better history; to carry forward that precious gift, that noble idea, passed on from generation to generation: the God-given promise that all are equal, all are free, and all deserve a chance to pursue their full measure of happiness.   In reaffirming the greatness of our nation, we understand that greatness is never a given. It must be earned. Our journey has never been one of short-cuts or settling for less. It has not been the path for the faint-hearted - for those who prefer leisure over work, or seek only the pleasures of riches and fame. Rather, it has been the risk-takers, the doers, the makers of things - some celebrated but more often men and women obscure in their labor, who have carried us up the long, rugged path towards prosperity and freedom.   For us, they packed up their few worldly possessions and traveled across oceans in search of a new life.   For us, they toiled in sweatshops and settled the West; endured the lash of the whip and plowed the hard earth.   For us, they fought and died, in places like Concord and Gettysburg; Normandy and Khe Sanh.  Time and again these men and women struggled and sacrificed and worked till their hands were raw so that we might live a better life. They saw America as bigger than the sum of our individual 

ambitions; greater than all the differences of birth or wealth or faction.   This is the journey we continue today. We remain the most prosperous, powerful nation on Earth. Our workers are no less productive than when this crisis began. Our minds are no less inventive, our goods and services no less needed than they were last week or last month or last year. Our capacity remains undiminished. But our time of standing pat, of protecting narrow interests and putting off unpleasant decisions - that time has surely passed. Starting today, we must pick ourselves up, dust ourselves off, and begin again the work of remaking America.   For everywhere we look, there is work to be done. The state of the economy calls for action, bold and swift, and we will act - not only to create new jobs, but to lay a new foundation for growth. We will build the roads and bridges, the electric grids and digital lines that feed our commerce and bind us together. We will restore science to its rightful place, and wield technology’s wonders to raise health care’s quality and lower its cost. We will harness the sun and the winds and the soil to fuel our cars and run our factories. And we will transform our schools and colleges and universities to meet the demands of a new age. All this we can do. And all this we will do.   Now, there are some who question the scale of our ambitions - who suggest that our system cannot tolerate too many big plans. Their memories are short. For they have forgotten what this country has already done; what free men and women can achieve when imagination is joined to common purpose, and necessity to courage.   What the cynics fail to understand is that the ground has shifted beneath them - that the stale political arguments that have consumed us for so long no longer apply. The question we ask today is not whether our government is too big or too small, but whether it works - whether it helps families find jobs at a decent wage, care they can afford, a retirement that is dignified. Where the answer is yes, we intend to move forward. Where the answer is no, programs will end. And those of us who manage the public’s dollars will be held to account - to spend wisely, reform bad habits, and do our business in the light of day - because only then can we restore the vital trust between a people and their government.   Nor is the question before us whether the market is a force for good or ill. Its power to generate wealth and expand freedom is unmatched, but this crisis has reminded us that without a watchful eye, the market can spin out of control - and that a nation cannot prosper long when it favors only the prosperous. The success of our economy has always depended not just on the size of our Gross Domestic Product, but on the reach of our prosperity; on our ability to extend opportunity to every willing heart - not out of charity, but because it is the surest route to our common good.   As for our common defense, we reject as false the choice between our safety and our ideals. Our Founding Fathers, faced with perils we can scarcely imagine, drafted a charter to assure the rule of law and the rights of man, a charter expanded by the blood of generations. Those ideals still light the world, and we will not give them up for expedience’s sake. And so to all other peoples and governments who are watching today, from the grandest capitals to the small village where my father was born: know that America is a friend of each nation and every man, woman, and child who seeks a future of peace and dignity, and that we are ready to lead once more.  Recall that earlier generations faced down fascism  not just with missiles and tanks, but with sturdy alliances and enduring convictions. They understood that our power alone cannot protect us, nor does it entitle us to do as we please. Instead, they knew that our power grows through its 

prudent use; our security emanates from the justness of our cause, the force of our example, the tempering qualities of humility and restraint.   We are the keepers of this legacy. Guided by these principles once more, we can meet those new threats that demand even greater effort - even greater cooperation and understanding between nations. We will begin to responsibly leave Iraq to its people, and forge a hard-earned peace in Afghanistan. With old friends and former foes, we will work tirelessly to lessen the nuclear threat, and roll back the specter of a warming planet. We will not apologize for our way of life, nor will we waver in its defense, and for those who seek to advance their aims by inducing terror and slaughtering innocents, we say to you now that our spirit is stronger and cannot be broken; you cannot outlast us, and we will defeat you.   Now, there are some who question the scale of our ambitions - who suggest that our system cannot tolerate too many big plans. Their memories are short. For they have forgotten what this country has already done; what free men and women can achieve when imagination is joined to common purpose, and necessity to courage.   What the cynics fail to understand is that the ground has shifted beneath them - that the stale political arguments that have consumed us for so long no longer apply. The question we ask today is not whether our government is too big or too small, but whether it works - whether it helps families find jobs at a decent wage, care they can afford, a retirement that is dignified. Where the answer is yes, we intend to move forward. Where the answer is no, programs will end. And those of us who manage the public’s dollars will be held to account - to spend wisely, reform bad habits, and do our business in the light of day - because only then can we restore the vital trust between a people and their government.  Nor is the question before us whether the market is a force for good or ill. Its power to generate wealth and expand freedom is unmatched, but this crisis has reminded us that without a watchful eye, the market can spin out of control - and that a nation cannot prosper long when it favors only the prosperous. The success of our economy has always depended not just on the size of our Gross Domestic Product, but on the reach of our prosperity; on our ability to extend opportunity to every willing heart - not out of charity, but because it is the surest route to our common good.   As for our common defense, we reject as false the choice between our safety and our ideals. Our Founding Fathers, faced with perils we can scarcely imagine, drafted a charter to assure the rule of law and the rights of man, a charter expanded by the blood of generations. Those ideals still light the world, and we will not give them up for expedience’s sake. And so to all other peoples and governments who are watching today, from the grandest capitals to the small village where my father was born: know that America is a friend of each nation and every man, woman, and child who seeks a future of peace and dignity, and that we are ready to lead once more.   We are the keepers of this legacy. Guided by these principles once more, we can meet those new threats that demand even greater effort - even greater cooperation and understanding between nations. We will begin to responsibly leave Iraq to its people, and forge a hard-earned peace in Afghanistan. With old friends and former foes, we will work tirelessly to lessen the nuclear threat, and roll back the specter of a warming planet. We will not apologize for our way of life, nor will we waver in its defense, and for those who seek to advance their aims by inducing terror and slaughtering innocents, we say to you now that our spirit is stronger and cannot be broken; you cannot outlast us, and we will defeat you.
'''
ngrams = getNgrams(content, 2)
# key = operator.itemgetter(1) 返回第一个元素
sortedNGrams = sorted(ngrams.items(), key = operator.itemgetter(1), reverse = True)
# print(sortedNGrams)
for k,v in sortedNGrams:
    if v>2:
        print(getFirstSentenceContaining(k,content))
'''
('united states', 10), ('executive department', 4), ('general government', 4), 
('called upon', 3), ('chief magistrate', 3), ('mr jefferson', 3), ('legislative body', 3), 
('same causes', 3), ('government should', 3), ('whole country', 3)
'''
