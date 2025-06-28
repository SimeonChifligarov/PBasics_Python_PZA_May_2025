# Входът е поредица от цели числа и текст:
# •	На първия ред до получаване на командата "Finish" - име на филма – текст
# •	На втори ред – свободните места в салона за всяка прожекция – цяло число [1 … 100]
# •	За всеки филм, се чете по един ред до изчерпване на свободните места в залата или до получаване на командата "End":
# o	Типа на закупения билет - текст ("student", "standard", "kid")

total_tickets = 0
student_tickets = 0
standart_tickets = 0
kid_tickets = 0

while True:
    command = input()  # 'Finish', or movie, e.g. 'Taxi'

    if command == 'Finish':
        break

    seats_available = int(input())

    seats_bought = 0
    while True:
        ticket_type = input()  # 'End', or ticket_type of ['student', 'standard', 'kid']

        if ticket_type == 'End':
            break

        if ticket_type == 'student':
            student_tickets += 1
        elif ticket_type == 'standard':
            standart_tickets += 1
        elif ticket_type == 'kid':
            kid_tickets += 1

        seats_bought += 1
        total_tickets += 1

        if seats_bought >= seats_available:
            break

    percent_full = seats_bought / seats_available * 100  # 6 / 10 == 0.6 ; 0.6 * 100 == 60
    print(f'{command} - {percent_full:.2f}% full.')


students_percent = student_tickets / total_tickets * 100
standarts_percent = standart_tickets / total_tickets * 100
kids_percent = kid_tickets / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{students_percent:.2f}% student tickets.")
print(f"{standarts_percent:.2f}% standard tickets.")
print(f"{kids_percent:.2f}% kids tickets.")
