from random import randint

if __name__ == '__main__':
    n = int(input("참여할 플레이어 수를 입력해주세요 (최대 3명): "))
    n += 1

    score = [0 for _ in range(n)]
    # ex). [0, 0, 0, 0], 여기서 computer score의 index는 0

    while 1:
        r = 0
        cur_score = 0
        computer_random_roll = 1 # computer가 계속 Roll할지 Bank할지 randint를 통해 결정하도록 함, 0이면 Bank, 1이면 계속 Roll
        while (r != 1): # computer
            print("----------------------------------------------------")
            print("현재 Computer가 진행중" + '\n')
            r = randint(1, 6)
            print("현재 주사위 눈의 수: " + str(r))
            print("----------------------------------------------------\n")
            cur_score += r # 가독성을 위해
            if (r == 1):
                cur_score = 0
                break

            ##flag = input("계속 Roll을 진행하시겠습니까? (y/n): ")
            computer_random_roll = randint(0, 1)

            if (computer_random_roll == 0):   # Bank
                score[0] += cur_score
                print("\n현재 Computer의 score: " + str(score[0]))
                break
        if (score[0] >= 50):
            break
        print("\n\n")


        player_win = False
        for i in range(1, n):
            print("----------------------------------------------------")
            print("현재 진행중인 Player는 " + str(i) + '\n')
            cur_score = 0
            r = 0
            while (r != 1): # player1
                r = randint(1, 6)
                print("현재 주사위 눈의 수: " + str(r))
                print("----------------------------------------------------\n")
                cur_score += r # 가독성을 위해
                if (r == 1):
                    cur_score = 0
                    break

                flag = input("계속 Roll을 진행하시겠습니까? (y/n): ")

                if (flag == 'n'):   # Bank
                    score[i] += cur_score
                    print("\n현재 player " + str(i) + "의 score: " + str(score[i]))
                    break
            if (score[i] >= 50):
                player_win = True
                break
            print("\n\n")
        if (player_win):
            break


    print("\n\n최종 스코어")
    for i in range(n):
        if (i == 0):
            print("Computer Score: " + str(score[i]))
        else:
            print("Player " + str(i) + " Score: " + str(score[i]))
