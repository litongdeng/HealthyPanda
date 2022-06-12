#Goes to reflection.html

import random

questions = {'Do you have effective coping mechanisms?': 'Coping Mechanisms', 
  'In what ways do you respond effectively to stress?' : 'Understanding Stress', 
  'When is a recent time that you lost control or your emotions or responded to something in a harmful way?' : 'Emotional Control', 
  "How do you reset and take a break when life gets to be too much?" : 'Coping Mechanisms',
  "How does your response type vary depending on where you are?" : 'Response Types', 
  "How does your response type vary depending on who you're with?" : 'Response Types',
  "If you had to use just one response type for the rest of your life, which would it be?" : 'Response Types', 
  "There's a lot of commonly known advice for managing stress, such as exercise. Have you tried any of these methods? If so, did they work for you? If not, what's stopping you from trying them?" : 'Understanding Stress', 
  "Who in your life can you lean on for support? Do you feel like you rely on them too much or too little? Why?" : 'Emotional Support',
  "Have you ever opened up to someone and gotten an unexpected response? If not, when has the fear of how people respond kept you from saying something?" : 'Emotional Support'
  }
# question, category ==> key, value

instructions = ['Write two paragraphs.', 'Set a timer for 10 minutes and write as much as you can.', 'Think for a while and summerize your thoughts.', 'Meditate or go on a walk and write once you are done.', 'Do a messy write: Do not worry about full sentences or readability.', 'Write your reflection as a letter.', 'Write your reflection as an internet post.', 'Write however you want.', 'When you are done reflecting and/or writing, summerize with a haiku.']
# instructions

# we mix and match questions & instructions for prompts

card_categories = {
'Coping Mechanisms' : ['Conscious or unconscious strategies used to reduce unpleasant emotions.', ['Hobbies', 'Social support', 'Over-engaging in distractions'], 'https://www.goodtherapy.org/blog/psychpedia/coping-mechanisms'], 
                           
'Understanding Stress' : ["Your body's response to anything that requires attention or action.", ['Acute vs. chronic', 'Episodic acute stress', 'Eustress (positive stress)'], 'https://www.verywellmind.com/stress-and-health-3145086'],
                           
'Emotional Control': ['The ability to manage disturbing emotions and remain effective, even in stressful situations.', ['Emotional self-awareness', 'Expressing anger in a healthy way', 'NOT suppressing emotions'], 'https://www.mindful.org/emotional-self-control-matters/'],
                           
'Response Types': ['Four catagories for how someone responds to a percived danger.', ['Fight', 'Flight', 'Fawn', 'Freeze'], 'https://www.verywellmind.com/the-four-fear-responses-fight-flight-freeze-and-fawn-5205083'],
                           
'Emotional Support': ['The verbal and nonverbal processes by which one communicates care and concern for another, offering reassurance, empathy, comfort, and acceptance.', ['Listening closely during important discussions', 'Checking on how someone is doing', 'Hugs <3 (or respecting your boundaries if you dislike hugs)'], 'https://www.berkeleywellbeing.com/emotional-support.html']
}
# category, [definition, [examples, examples, examples], further reading] ==> key, value


keys = []
# keys list

def pick_prompt():
  for key, value in questions.items():
    keys.append(key)
  return random.choice(keys)
#randomly choose a question

def pick_instr():
  return random.choice(instructions)
#randomly choose an instruction

def find_category(key):
  return questions.get(key)
# find category the question is in

def find_info(key):
  return card_categories.get(key)
# find information for each category