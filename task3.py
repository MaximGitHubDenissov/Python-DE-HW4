import decimal

# decimal.getcontext().prec = 2
MULTIPLICITY = 50
# PERCENT = decimal.Decimal(15) / decimal.Decimal(1000)
PERCENT = 15 / 1000
# PERCENT_BONUS = decimal.Decimal(3) / decimal.Decimal(100)
PERCENT_BONUS = 3 / 100
COUNT_PERC = 3
# MIN_LIMIT = decimal.Decimal(30)
# MAX_LIMIT = decimal.Decimal(600)
MIN_LIMIT = 30
MAX_LIMIT = 600
# PERCENT_RICHNESS = decimal.Decimal(10) / decimal.Decimal(100)
PERCENT_RICHNESS = 10 / 100
RICHNESS_AMOUNT = 5_000_000
CMD_DEPOSIT = "1"
CMD_WITHDRAW = "2"
CMD_EXIT = "3"

balance = 0
operations = 0


def is_multiplicity() -> int:
    amount = 1
    while amount % MULTIPLICITY != 0:
        amount = int(input(f"Введите сумму кратную {MULTIPLICITY}: "))
    return amount


def is_bonus() -> int:
    global operations, balance
    if operations % COUNT_PERC == 0:
        bonus_sum = balance * PERCENT_BONUS
        balance += bonus_sum
        print(f"Сумма бонуса {bonus_sum}")
        return balance
    else:
        return balance


def is_richness() -> int:
    global balance
    if balance > RICHNESS_AMOUNT:
        sum_percent = balance * PERCENT_RICHNESS
        balance -= sum_percent
        print(f"Вычтен налог на богатство в размере {sum_percent}")
        return balance
    else:
        return balance


def main_menu():
    global operations, balance
    while True:
        action = input(
            f"пополнить-{CMD_DEPOSIT}\n"
            f"снять-{CMD_WITHDRAW}\n"
            f"выход-{CMD_EXIT}\n"
            f"Введите действие:  ")
        match action:
            case "1":
                amount = is_multiplicity()
                operations += 1
                balance += amount
                balance = is_bonus()
                balance = is_richness()
                print(f"Текущий баланс {balance}")
            case "2":
                amount = is_multiplicity()
                commission = amount * PERCENT
                if commission < MIN_LIMIT:
                    commission = MIN_LIMIT
                elif commission > MAX_LIMIT:
                    commission = MAX_LIMIT
                if commission + amount > balance:
                    print("На балансе недостаточно средств")
                else:
                    operations += 1
                    balance -= (amount + commission)
                    balance = is_bonus()
                    balance = is_richness()
                    print(f"Сумма снятия {amount}, комиссия {commission}, общая сумма {amount + commission}")
                    print(f"Текущий баланс {balance}")
            case "3":
                break
            case _:
                print("Введена неверная команда")


if __name__ == '__main__':
    main_menu()
