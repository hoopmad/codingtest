'''
    2023 개인정보 수집 유효기간 // 풀이중
'''

today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2020.07.01 D", "2018.12.28 Z"]

def solution(today, terms, privacies):
    answer = []
    t_year, t_month, t_day = map(int, today.split('.'))
    terms_list = []

    for k in range(len(terms)):
        terms_list += terms[k].split()

    terms_dict = {terms_list[i]: int(terms_list[i + 1]) for i in range(0, len(terms_list), 2)}

    for i in range(len(privacies)):
        date, pri = privacies[i].split()
        year, month, day = map(int, date.split('.'))

        if pri in terms_dict:
            cycle = terms_dict[pri]//12
            cycle_month = terms_dict[pri]%12
            total_months = month + cycle_month

            if total_months<12:
                if day-1:
                    day -= 1
                    month += cycle_month
                    year += cycle
                else:
                    day=28
                    month += cycle_month-1
                    if month == 0:
                        month = 12
                        year += cycle-1
                    else:
                        year += cycle
            else:
                if day-1:
                    day -= 1
                    month = total_months%12
                    year += cycle+1
                else:
                    day=28
                    month += cycle_month-1
                    if month == 0:
                        month = 12
                        year += cycle-1
                    else:
                        year += cycle
        
        print(year, month, day)

        if t_year > year:
            answer.append(i+1)
        elif t_month > month:
            answer.append(i+1)
        elif t_day > day:
            answer.append(i+1)

    print(answer)
    return answer

solution(today, terms, privacies)