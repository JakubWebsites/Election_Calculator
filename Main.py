import P

# instruction of users
P.print_instr()

# user gives info about electoral district
hm_seats = int(input("Ile mandatów jest możliwych do zdobycia w tym okręgu? "))
hm_parties = int(input("Ile partii wzięło udział w wyborach w tym okręgu? "))
party_list = []
party_list = P.create_party_list(hm_parties, party_list)

# user gives info about system
system = int(input("""
W jakim systemie zostaną przeliczone głosy?
d'Hondta - wybierz 1
Sainte-Lague - wybierz 2
Hare'a-Niemayera - wybierz 3 
"""))
scope = [1, 2, 3]
while system not in scope:
    system = int(input("""
Wybierz 1, 2 lub 3
d'Hondta - wybierz 1
Sainte-Lague - wybierz 2
Hare'a-Niemayera - wybierz 3 
"""))

# calculations for d'Hondt system
if system == 1:

    # creating quotients' lists for each party
    for p in party_list:
        divisor = 1
        x = 0
        while x < hm_seats:
            quotient = p.votes/divisor
            p.quotients_list.append(quotient)
            divisor += 1
            x += 1

# creating list of all qoutients
    all_quotients = []
    for p in party_list:
        for quotient in p.quotients_list:
            all_quotients.append(quotient)

# looking for biggests quotients
    big_quotients = []
    x = 0
    while x < hm_seats:
        the_biggest = P.find_the_biggest(all_quotients)
        x += 1
        big_quotients.append(the_biggest)
        all_quotients.sort(key=int, reverse=True)
        all_quotients.pop(0)
    winning_quotients = list(set(big_quotients))

# distribution of seats
    x = len(winning_quotients)
    while x > 0:
        P.give_the_seat(party_list, winning_quotients)
        winning_quotients.sort(key=int, reverse=True)
        winning_quotients.pop(0)
        x -= 1

# calculations for Sainte-Lague system
elif system == 2:

    # creatig quotients' lists for each party
    for p in party_list:
        divisor = 1
        x = 0
        while x < hm_seats:
            quotient = p.votes/divisor
            p.quotients_list.append(quotient)
            divisor += 2
            x += 1

# creating list of all qoutients
    all_quotients = []
    for p in party_list:
        for quotient in p.quotients_list:
            all_quotients.append(quotient)

# looking for biggests quotients
    big_quotients = []
    x = 0
    while x < hm_seats:
        the_biggest = P.find_the_biggest(all_quotients)
        x += 1
        big_quotients.append(the_biggest)
        all_quotients.sort(key=int, reverse=True)
        all_quotients.pop(0)
    winning_quotients = list(set(big_quotients))

# distribution of seats
    x = len(winning_quotients)
    while x > 0:
        P.give_the_seat(party_list, winning_quotients)
        winning_quotients.sort(key=int, reverse=True)
        winning_quotients.pop(0)
        x -= 1

# calculations for Hare-Niemayer system
elif system == 3:

    # all parties' votes addition
    total = P.calc_total(party_list)

# distribution of seats part 1
    for p in party_list:
        p.hn_quot = (p.votes*hm_seats)/total
        p.hn_intgr = int((p.votes*hm_seats)/total)
        p.hn_rem = p.hn_quot-p.hn_intgr
        x = p.hn_intgr
        while x > 0:
            p.get_seat()
            x -= 1

# distribution of seats part 2
    used_seats = P.check_seats(party_list)
    if used_seats < hm_seats:
        remainders_list = P.full_remainders_list(party_list)
        remainders_list = sorted(remainders_list)
        while used_seats != hm_seats:
            the_biggest = remainders_list[-1]
            for p in party_list:
                if p.hn_rem == the_biggest:
                    p.get_seat()
                    del remainders_list[-1]
                    used_seats += 1

# show results
P.show_results(party_list)
