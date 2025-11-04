stone_durability = [1, 2, 1, 4]
dogs = [{
    "이름" : "루비독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "4",
    },{
    "이름" : "피치독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "3",
    },{
    "이름" : "씨-독",
    "나이" : "72년생",
    "점프력" : "2",
    "몸무게" : "1",
    },{
    "이름" : "코볼독",
    "나이" : "59년생",
    "점프력" : "1",
    "몸무게" : "1",
    },
]

def cross_the_bridge(stone_durability, dogs):
  answer = [i["이름"] for i in dogs]

  for i in dogs:
    dog_index = 0

    while dog_index <= len(stone_durability):
      dog_index += int(i["점프력"])
      stone_durability[dog_index - 1] -= int(i["몸무게"])

      if stone_durability[dog_index - 1] < 0:
        del answer[answer.index(i["이름"])]
        break
      else:
        break

  return answer


print(cross_the_bridge(stone_durability.copy(), dogs.copy()))
