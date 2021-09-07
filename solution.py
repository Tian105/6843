def welcome_assignment_answers(question):

   if   question == "In Slack, what is the secret passphrase posted in the #cyberfellows-computernetworking-fall2021 channel posted by a TA?":
        answer = "mTLS"
   elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
   elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
   elif question ==  "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
   elif question ==  "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
   elif question == "What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use MD5 hash generator and use the answer in your code":
        answer = "42b76fe51778764973077a5a94056724"
   elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
   elif question == "What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number":
        answer = 5
   elif question == "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number":
        answer = 4
   return (answer)




if __name__ == "__main__":

   debug_question1 = "In Slack, what is the secret passphrase posted in the #cyberfellows-computernetworking-fall2021 channel posted by a TA? - you have to hunt for this one in slack"
   debug_question2 = "Are encoding and encryption the same? - Yes/No"
   debug_question3 = "Is it possible to decrypt a message without a key? - Yes/No"
   debug_question4 = "Is it possible to decode a message without a key? - Yes/No"
   debug_question5 = "Is a hashed message supposed to be un-hashed? - Yes/No"
   debug_question6 = "What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use MD5 hash generator and use the answer in your code"
   debug_question7 = "Is MD5 a secured hashing algorithm? - Yes/No"
   debug_question8 = "What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number"
   debug_question9 = "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number"
   print(welcome_assignment_answers(debug_question1))
   print(welcome_assignment_answers(debug_question2))
   print(welcome_assignment_answers(debug_question3))
   print(welcome_assignment_answers(debug_question4))
   print(welcome_assignment_answers(debug_question5))
   print(welcome_assignment_answers(debug_question6))
   print(welcome_assignment_answers(debug_question7))
   print(welcome_assignment_answers(debug_question8))
   print(welcome_assignment_answers(debug_question9))