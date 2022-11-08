import random


fruits = ['apple', 'olive', 'tomato', 'melon', 'litchi',
          'mango', 'lime', 'kiwi', 'grapes', 'cherry',
          'banana', 'apricot', 'cucumber', 'guava', 'mulberry',
          'orange', 'papaya', 'pear', 'peach', 'berry']

animals = ['ants', 'hippo', 'panda', 'giraffe', 'bat', 'bear',
           'catfish', 'cheetah', 'lizard', 'wolf', 'zebra', 'eagle',
           'cobra', 'goose', 'penguin', 'frog', 'mouse', 'flamingo',
           'rabbit', 'crow', 'whale', 'lion', 'monkey', 'ostrich',
           'peacock', 'raccoon', 'rhinoceros', 'sheep', 'dogs',
           'squirrel', 'tiger', 'vulture']

accessories = ['ring', 'bangle', 'lipstick', 'handbag', 'crown',
               'necklace', 'watch', 'caps', 'glasses', 'wallet',
               'belts', 'comb', 'pendent', 'earring', 'scarf',
               'backpack', 'keychain', 'hairpin', 'shoes', 'hats',
               'jacket', 'boots', 'socks', 'stocking', 'muffler',
               'gloves', 'umbrella', 'ribbon']

stationary = ['notebook', 'tape', 'pencil', 'eraser', 'sharpener',
              'files', 'fevicol', 'inkpot', 'chalk', 'duster',
              'glue', 'paper', 'cutter', 'chart', 'colours',
              'stapler', 'marker', 'staples', 'clips', 'calculator',
              'envelope', 'register']

words = fruits + animals + accessories + stationary


word = random.choice(words)
print(f"Your word has {len(word)} letters")
print(len(word)*"_")
print(word)

