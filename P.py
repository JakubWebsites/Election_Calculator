class Party(object):
    def __init__(self):
        self.ask_party_name()
        self.ask_party_votes()
        self.seats = 0
        self.quotients_list = []
        self.hn_quot = 0
        self.hn_intgr = 0
        self.hn_rem = 0

    def ask_party_name(self):
        self.party_name = input("Podaj nazwę lub skrót partii: ")

    def ask_party_votes(self):
        self.votes = int(input("Podaj liczbę głosów, którą zdobyła partia " + self.party_name + ": "))

    def get_seat(self):
        self.seats += 1


def print_instr():
    print("""
KALKULATOR WYBORCZY

Program służy do symulacji rezultatów wyborów w pojedynczym okręgu.

Użytkownik zostanie poproszony o podanie informacji o liczbie
miejsc(mandatów), które zostaną przyznane oraz o liczbie
partii, które wzięły udział w wyborach w tym okręgu.
Proszę o podanie tych danych w formie liczb całkowitych większych od zera!

Następnie użytkownik zostanie poproszony o podanie nazw i liczby
głosów oddanych na poszczególne partie. O ile nazwa może zawierać dowolne znaki,
to przy podawaniu liczby głosów proszę o liczby całkowite większe od zera.

Na koniec program poprosi użytkownika o wybór jednego z najczęściej
stosowanych systemów do przeliczania głosów na uzyskane mandaty.
Proszę o wybór systemu poprzez podanie odpowiadającej mu cyfry: 1, 2 lub 3.

Dziękuję!
""")


def calc_total(p_list):
    t = 0
    for p in p_list:
        t += p.votes
    return t


def create_party_list(hm_p, p_list):
    x = 0
    while x < hm_p:
        p = Party()
        p_list.append(p)
        x += 1
    return p_list


def find_the_biggest(quotients_list):
    quotients_list.sort(key=int, reverse=True)
    the_b = quotients_list[0]
    return the_b


def give_the_seat(p_list, win_list):
    win_list.sort(key=int, reverse=True)
    the_b = win_list[0]
    for p in p_list:
        for q in p.quotients_list:
            if q == the_b:
                p.get_seat()


def check_seats(p_list):
    used_seats = 0
    for p in p_list:
        used_seats += p.seats
    return used_seats


def full_remainders_list(p_list):
    rem_list = []
    for p in p_list:
        rem_list.append(p.hn_rem)
    return rem_list


def find_the_biggest_r(r_list):
    the_br = r_list[0]


def show_results(p_list):
    for p in p_list:
        if p.seats == 0:
            print("Partia ", p.party_name, " nie otrzymuje mandatu.")
        elif p.seats == 1:
            print("Partia ", p.party_name, " otrzymuje ", p.seats, " mandat.")
        elif p.seats == 2:
            print("Partia ", p.party_name, " otrzymuje ", p.seats, " mandaty.")
        elif p.seats == 3:
            print("Partia ", p.party_name, " otrzymuje ", p.seats, " mandaty.")
        elif p.seats == 4:
            print("Partia ", p.party_name, " otrzymuje ", p.seats, " mandaty.")
        elif p.seats > 4:
            print("Partia ", p.party_name, " otrzymuje ", p.seats, " mandatów.")
