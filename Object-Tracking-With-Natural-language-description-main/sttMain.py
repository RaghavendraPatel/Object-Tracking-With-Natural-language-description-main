from Recorder import record_audio



import speech_recognition as sr
from os import path

def stt_key():
    record_audio(5, 'command.wav')
    r = sr.Recognizer()
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "command.wav")
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file  

        try:
            cmd = r.recognize_google(audio)
            print("You said " + cmd)
        except sr.UnknownValueError:
            print("Could not understand audio")
            return []
        except sr.RequestError as e:
            print("Could not request results from Speech Recognition service; {0}".format(e))


    #wth noun removal

    import nltk
    from nltk.tokenize import word_tokenize
    from nltk import ne_chunk
    # from nltk.corpus import stopwords
    # print(stopwords.words("english"))
    # cmd = "person"
    cmd_tokens = word_tokenize(cmd)
    # for token in cmd_tokens:
    #     print(nltk.pos_tag([token]))

    cmd_tags = nltk.pos_tag(cmd_tokens)
    ne = ne_chunk(cmd_tags)
    print(ne)
    # print(type(ne))
    ll=[]
    def traverse_tree(tree):
        # print("tree:", tree)
        for subtree in tree:
            # print(subtree)
            if len(subtree)==2 and subtree[1] == 'NN':
                print(subtree[0])
                ll.append(subtree[0])
            if type(subtree) == nltk.tree.Tree:
                traverse_tree(subtree)
    traverse_tree(ne)
    return ll