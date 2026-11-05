#In normal base-10, columns are repersented by 100s, 10s ,1s.
#In normal base-2, columns are doubled when the move left (like, 128,64,32,---)

#Converting Binary to Decimal math example:-
#lets convert 00101110 into deicmal -> 
#So first is 2 ** 0 = 1, second is 2 ** 1, third is 2 ** 2, fourth is 2 ** 3, fifth is 0, sixth is 2 ** 5, and rest all are 0.
#Ans- 46 is the answer.

#Python provides a direct method to reduce this overhead of calculating this manually by adding the [0b] prefix before the number.
binary_digit = 0b00101110
print(binary_digit)