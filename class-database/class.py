class Human:
    def __init__(self, surname, name, sex, growth):
        self.surname = surname
        self.name = name
        self.sex = sex
        self.growth = growth

    def __repr__(self):
        return repr((self.surname, self.name, self.sex, self.growth))


class HumanDatabase:
    humanDatabaseList = []

    def addHuman(self, human):
        self.humanDatabaseList.append(human)

    def printHuman(self):
        print(self.humanDatabaseList)

    def defineAverageGrowth(self):
        femaleGrowthSum = 0
        femaleAmount = 0
        maleGrowthSum = 0
        maleAmount = 0
        for human in self.humanDatabaseList:
            if human.sex == "female":
                femaleGrowthSum += human.growth
                femaleAmount += 1
            else:
                maleGrowthSum += human.growth
                maleAmount += 1
        print("Средний рост мужчин -", maleGrowthSum / maleAmount)
        print("Средний рост женщин -", femaleGrowthSum / femaleAmount)

    def findTheTallestMale(self):
        theTallestMale = self.humanDatabaseList[0]
        growthOfTheTallest = theTallestMale.growth
        for human in self.humanDatabaseList:
            if human.sex == "male" and growthOfTheTallest < human.growth:
                theTallestMale = human
        print("Самый высокий мужчина -", theTallestMale.name, theTallestMale.surname, "с ростом", theTallestMale.growth)

    def get_name(human):
        return human.growth

    def sortListByGrowth(self):
        print("Отсортированный по возрастанию роста список:", sorted(self.humanDatabaseList, key=lambda human: human.growth))

    def findBySurname(self, targetSurname):
        result = Human("","","",0)
        for human in self.humanDatabaseList:
            if human.surname == targetSurname:
                result = human
                break
        if(result.name == ""):
            print("Такого человека найти не удалось")
            return 0
        else:
            print("Найденный человек с такой фамилией -", result)
            return result

    def editHumanData(self, targetHuman, idOfField, newData):
        if idOfField == 0:
            targetHuman.surname = newData
        elif idOfField == 1:
            targetHuman.name = newData
        elif idOfField == 2:
            targetHuman.sex = newData
        elif idOfField == 3:
            targetHuman.growth = newData
        print("Обновленная информация о пользователе -", targetHuman)



    def findBySurnameAndEdit(self, targetSurname, idOfField, newData):
        result = self.findBySurname(targetSurname)
        if(result != 0):
            self.editHumanData(result, idOfField, newData)



humanDb = HumanDatabase()

humanDb.addHuman(Human("Ivanov", "Vladimir", "male", 175))
humanDb.addHuman(Human("Petrov", "Oleg", "male", 125))
humanDb.addHuman(Human("Sidorova", "Oksana", "female", 1175))
humanDb.addHuman(Human("Puchkov", "Vladimir", "male", 125))
humanDb.addHuman(Human("Smirnova", "Elena", "female", 175))
humanDb.addHuman(Human("Vlasov", "Kolya", "male", 1175))


humanDb.defineAverageGrowth()
humanDb.findTheTallestMale()
humanDb.sortListByGrowth()
humanDb.findBySurnameAndEdit("Smirnova", 3, 2232)
