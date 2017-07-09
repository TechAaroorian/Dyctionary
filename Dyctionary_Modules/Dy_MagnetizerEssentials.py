#!/usr/bin/env python3
import time

class DyMagnetizerEssentials:
    def __init__(self, ):
        magnet = 0
        
        dinnerResponse = ['nope!', "I'm a machine", 'I will never take dinner',
                      'Yeah! I have a many bites of bytes', 'Its funny', 'no, never']
        lunchResponse = ['nope!', "I'm a machine", 'I will never take lunch',
                           'Yeah! I have a many bites of bytes', 'Its funny', 'no, never']
        self.goodMorning = ['good morning', 'very good morning', 'good morning to you', 'a very good morning']
        self.goodAfternoon = ['good afternoon', 'very good afternoon', 'good afternoon to you', 'a very good afternoon']
        self.goodEvening = ('good evening', 'very good evening', 'good evening to you', 'a very good evening')
        self.goodNight = ['good night', 'good night! sweet dreams', 'good night to you', 'good night! take care']
                
        ListOneQ1 = ['what', 'does', magnet, 'mean']
        ListOneQ2 = ['what', 'is', 'the', 'meaning', 'of', magnet]
        ListOneQ3 = ['what', 'is', 'meaning', 'of', magnet]
        ListOneQ4 = ['what', 'is', magnet]
        ListOneQ5 = ['what', 'do', 'you', 'know', 'about', magnet]
        ListOneQ6 = ['what', 'do', 'you', 'think', 'about', magnet]
        ListOneQ7 = ['what', 'you', 'know', 'about', magnet]
        ListOneQ8 = ['what', 'you', 'think', 'about', magnet]
        ListOneQ9 = ['do', 'you', 'know', 'about', magnet]
        ListOneQ10 = ['do', 'you', 'know', magnet]
        ListOneQ11 = [magnet, 'mean']
        ListOneQ12 = [magnet, 'meaning']
        ListOneQ13 = [magnet, 'mean', 'please']
        ListOneQ14 = [magnet, 'meaning', 'please']
        ListOneQ15 = ['please', 'tell', 'me', 'the', 'mean', 'of', magnet]
        ListOneQ16 = ['please', 'tell', 'me', 'the', 'meaning', 'of', magnet]
        ListOneQ17 = ['could', 'you', 'please', 'tell', 'me', 'the', 'mean', 'of', magnet]
        ListOneQ18 = ['could', 'you', 'please', 'tell', 'me', 'the', 'meaning', 'of', magnet]
        ListOneQ19 = ['tell', 'me', 'the', 'mean', 'of', magnet]
        ListOneQ20 = ['tell', 'me', 'the', 'meaning', 'of', magnet]



        self.ListOne = [ListOneQ1, ListOneQ2, ListOneQ3, ListOneQ4, ListOneQ5, ListOneQ6, ListOneQ7, ListOneQ8, ListOneQ9, ListOneQ10,
                        ListOneQ11, ListOneQ12, ListOneQ13, ListOneQ14, ListOneQ15, ListOneQ16, ListOneQ17, ListOneQ18, ListOneQ19,
                        ListOneQ20]
        
        self.chatResponse = {
            'hi dictionary'                     : ('hi', 'hi there', 'haii..'),
            'hello dictionary'                  : ('hello', 'hi', 'hello there', 'haii..'),
            'how are you'                       : ('Fine..', 'Fine.. Thank you..', 'Good', 'awesome..', 'Very well.. Thank you'),
            'what is your name'                 : ('Dyctionary', 'My name is Dyctionary', 'My cheif call me Dyctionary', 'I am Dyctionary'),
            'your name'                         : ('Dyctionary', 'My name is Dyctionary', 'My creator call me Dyctionary', 'I am Dyctionary'),
            'time please'                       : 'call time module',
            'what is the time now'              : 'call time module',
            'what is the current time'          : 'call time module',
            'current time please'               : 'call time module',
            'what time is it'                   : 'call time module',
            'have you got the time'             : 'call time module',
            'have you got the time please'      : 'call time module',
            'could you tell me the time'        : 'call time module',
            'could you tell me what time is it' : 'call time moudle',
            'what date is it today'             : 'call date module',
            'what is today date'                : 'call date module',
            'what is the date of today'         : 'call date module',
            'date please'                       : 'call date module',
            'could you tell me the date'        : 'call date module',
            'what day is it today'              : 'call day module',
            'what is the day of today'          : 'call day module',
            'could you tell me a joke'          : 'call joke module',
            'can you tell me a joke'            : 'call joke module',
            'have you taken dinner'             : dinnerResponse,
            'you take dinner'                   : dinnerResponse,
            'have you take dinner'              : dinnerResponse,
            'you taken dinner'                  : dinnerResponse,
            'have you taken launch'             : lunchResponse,
            'you take launch'                   : lunchResponse,
            'have you takee launch'             : lunchResponse,
            'you taken launch'                  : lunchResponse,
            'good morning'                      : 'call mmn module',
            'good afternoon'                    : 'call mmn module',
            'good evening'                      : 'call mmn module',
            'good night'                        : 'call mmn module',
            'how many days this month'          : 'call monthday module'
        }


        self.chatKey = list(self.chatResponse.keys())



















