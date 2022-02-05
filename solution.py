### welcome_assignment_answers
### Input - All eight questions given in the assignment.
### Output - The right answer for the specific question.

#def welcome_assignment_answers(question):
    #Students do not have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
    #answer = ""
   # if question =="In slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
   #     answer ="mtls"
  #  elif question == "Are encoding and encryption the same? - Yes/No?":
    #    answer = "Yes"
  #  elif question == "Is it possible to decrypt a message without a key? - Yes/No?":
    #    answer = "Yes"
  #  elif question == "Is it possible to decode a message without a key? - Yes/No":
   #     answer = "Yes"
  #  elif question =="Is a hashed message supposed to be un-hashed? - Yes/No":
  #      answer="No"
  #  elif question =="What is the MD5 hashing value to the following message: 'NYU Computer Networking' ":
   #     answer="65fc2f78620c22cc1f483c7d7201b592"
  #  elif question =="Is MD5 a secured hashing algorithm? - Yes/No":
   #     answer="No"
  #  elif question == "What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number":
   #     answer=4
  #  elif question == "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number":
   #     answer=3
  #  else:
   #     answer = "Whats the Question"
  #  return(answer)

# Complete all the questions.


#if __name__ == "__main__":
    #use this space to debug and verify that the program works
#    debug_question = "Is MD5 a secured hashing algorithm? - Yes/No"
#    print(welcome_assignment_answers(debug_question))

###Questions:
###"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?"
###"Are encoding and encryption the same? - Yes/No"
###"Is it possible to decrypt a message without a key? - Yes/No"
###"Is it possible to decode a message without a key? - Yes/No"
###"Is a hashed message supposed to be un-hashed? - Yes/No"
###"What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use MD5 hash generator and use the answer in your code"
###"Is MD5 a secured hashing algorithm? - Yes/No"
###"What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number"
###"What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number"



def welcome_assignment_answers(question):
    switcher ={
      "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?" : "mtls",
      "Are encoding and encryption the same? - Yes/No" :"No",
      "Is it possible to decrypt a message without a key? - Yes/No": "No",
      "Is it possible to decode a message without a key? - Yes/No":"No",
      "Is a hashed message supposed to be un-hashed? - Yes/No":"No",
      "What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use MD5 hash generator and use the answer in your code": "65fc2f78620c22cc1f483c7d7201b592",
      "Is MD5 a secured hashing algorithm? - Yes/No":"No",
      "What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number":5,
      "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number":4,

    }
    return switcher.get(question, "nothing")    

if __name__ == "__main__":
    #use this space to debug and verify that the program works
   question = "Is MD5 a secured hashing algorithm? - Yes/No"
   print(welcome_assignment_answers(question))