import urllib2
import urllib
import threading
import Queue



target_url = "http://192.168.1.1"
wordlist_file = "/tmp/all.txt"  # from SVNDigger
resume = None


def build_wordlist(wordlist_file):
    # read in the word list
    fd = open(wordlist_file, "rb")
    raw_words = fd.readlines()
    fd.close()

    found_resume = False
    words = Queue.Queue()

    for word in raw_words:

        word = word.rstrip()

        if resume is not None:

            if found_resume:
                words.put(word)
            else:
                if word == resume:
                    found_resume = True
                    print "Resuming wordlist from: %s" % resume

        else:
            words.put(word)

    return words


word_queue = build_wordlist(wordlist_file)
print (word_queue)