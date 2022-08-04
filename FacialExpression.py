from deepface import DeepFace

#database is folder data model face emotion
print("----------------------------------------------------\n")

programname= "Mood Elevator"
version= "1.0"
devby= "Developed by Black Panthers"
print(programname)
print(version)
print(devby)

print("----------------------------------------------------\n")


an_emot = DeepFace.stream("database", model_name='DeepFace') #Analyze Emotion from face with using library DeepFace
print(an_emot)









