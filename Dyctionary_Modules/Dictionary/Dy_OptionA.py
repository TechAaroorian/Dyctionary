#!/usr/bin/env python3
ListOne = {
    'accomplish' :
    [
        """To accomplish something is to get it done. Peopleusually accomplish things that are sources of pride
        like goals or records. But people accomplish immoralacts as welllike scandals or cons.""",

        """The verb accomplish also meansto bring about or putinto effect. The CEO stood before the employees and outlined
        all she expected to be accomplished in the next year. She ended her speech by saying, "If we are to accomplish this,
        we must all work together ? and work hard ? but the rewards if we succeed will be great both for the company and for
        those that work here. Thank you for your efforts!""",

        "to gain with effort(v)",

        "put in effect(v)"
    ]
}


newData = ListOne['accomplish'][1].split("\n")
newData = (' ').join(newData)
newData = newData.split(" ")

finalData = []

for i in newData:
    if i != '' and i != ' ':
        finalData.append(i)

finalData = (' ').join(finalData)
print(finalData)
