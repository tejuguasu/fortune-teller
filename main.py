import random


class FortuneTellerMobileApp(object):
    @staticmethod
    def random_guess(messages_list):
        if not messages_list:
            messages_list = FORTUNE_COOKIE_FUNNY_MESSAGES
        return random.choice(messages_list)


class FortuneTellerWebsite(object):
    @staticmethod
    def random_guess(messages_list):
        # print('debug: {}'.format(len(messages_list)))
        return random.choice(messages_list)


class FortuneTellerNonRepetitive(object):

    def __init__(self, items):
        self.messages = list(items)
        self.taboo = []

    def add_result(self, item):
        if item not in self.messages:
            self.messages.append(item)

    def random_guess(self):
        while len(self.taboo) < len(self.messages):
            message = random.choice(self.messages)
            if message not in self.taboo:
                self.taboo.append(message)
                return message

    def clear_taboo(self):
        pass


FORTUNE_GUESSES_MAGIC_8_BALL = (
    'Yes, definitely',
    'It is certain',
    'It is decidedly so',
    'Without a doubt',
    'You may rely on it',
    'As I see it, yes',
    'Most Likely',
    'Outlook good',
    'Signs point to yes',
    'Reply hazy, try again',
    'Ask again later',
    'Better not tell you now',
    'Cannot predict now',
    'Concentrate and ask again',
    'Don''t count on it',
    'My reply is no',
    'My sources say no',
    'Outlook not so good',
    'Very doubtful'
)

FORTUNE_COOKIE_FUNNY_MESSAGES = (
    'You will be hungry again in one hour',
    'Now would be a good time to take up a new sport',
    'You are not illiterate',
    'Three can keep a secret, if you get rid of two',
    'Borrow money from pessimists, they don''t expect it back',
    'Starting tomorrow, stop procrastinating'
)

FORTUNE_WISE_MESSAGES = (
    'When your mother asks, "Do you want a piece of advice?" it is a mere formality. It does not matter if you answer yes or no. You''re going to get it anyway. --Erma Bombeck',
    'My advice to you is get married: If you find a good wife you''ll be happy; if not, you''ll become a philosopher. --Socrates',
    'A dog teaches a boy fidelity, perseverance, and to turn around three times before lying down.',
    'If you think dogs can''t count, try putting three dog biscuits in your pocket and then giving Fido only two of them.',
    'Always forgive your enemies; nothing annoys them so much. --Oscar Wilde'
)