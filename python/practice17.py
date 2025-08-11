p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subbscribe this"
p4 = "click this"

message = input("Enter your comment:")
if(p1 in message) or (p2 in message) or (p3 in message) or (p4 in message):
    print("Spam")
else:
    print("Not Spam")