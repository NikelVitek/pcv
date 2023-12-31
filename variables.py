'''
Proměnné v Pythonu
Python je typově odvozovaný jazyk, proto nemusíme explicitně definovat typ proměnné.
Typ proměnné je určen na základě přiřazené hodnoty.
Pro přiřazení hodnoty proměnné se používá znak rovnítko ("=").
'''

# Proměnné v Pythonu - primitivní datové typy
# Je zvykem používat podtržítko u víceslovných názvů proměnných.
students_count = 1000
rating = 4.99
# Hodnota může být přiřazena i více proměnným najednou:
x = y = z = 0

# Boolean hodnota musí začínat velkým písmenem
is_published = False

# Python obsahuje i speciální literál None - nulovou hodnotu
iq = None
# print('Jeho IQ = ', iq)

'''
V Pythonu se ale ve skutečnosti nepřiřazují do proměnných hodnoty, ale jen reference na objekt (hodnotu).
Každý objekt (instance třídy) má jedinečnou hodnotu (value), typ (type) a identitu (ID).
Proto i typy proměnných poukazují na určitou výchozí třídu, z níž byl objekt vytvořen. 
Identita objektu je vyjádřena jeho identifikačním číslem (ID), které je adresou paměťového místa, ve kterém je hodnota uložena. 
Některé objekty mohou mít explicitně přiřazené jméno, obecně označované jako proměnná:
'''

'''Úkol A'''
#? Najděte na Internetu, jakými funkcemi lze v Pythonu zjistit
#? a) typ objektu
#? b) identitu objektu (jeho adresu v paměti)
#? Ukažte to na příkladech proměnných students_count, rating, is_published a vypište výstupy do konzole


students_count = 42
rating = 3
is_published = True

# Zjištění typu objektů
print("Variable type of  students_count:", type(students_count))
print("Variable type of rating:", type(rating))
print("Variable type of is_published:", type(is_published))

# Zjištění identity objektů
print("Identity of students_count:", id(students_count))
print("Identity of rating:", id(rating))
print("Identity of is_published:", id(is_published))


# Numerické operátory
# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# Zbytek po celočíselném dělení
# print(10 % 3)
# Celočíselné dělení
# print(10 // 3)
# Mocnina
# print(2 ** 10)

'''
Příklady použití numerických literálů (numeric literals)
'''
binary = 0b1010 #Binary Literals
octal = 0o310 #Octal Literal
decimal = 100 #Decimal Literal
hexadecimal = 0x12c #Hexadecimal Literal

# print(binary, octal, decimal, hexadecimal)
# Převod desítkového čísla na binární, oktalové a hexadecimální
# print(bin(255), oct(255), hex(255))


# Převod binárního čísla na desítkové
# print(int('0100', base=2))
# Převod hexadecimálního čísla na desítkové
# print(int('100', base=16))


'''Úkol B'''
#? Vypište do poznámky všechny bitové operátory, které nabízí Python
'''
Bitový OR (|): Provádí bitový OR mezi jednotlivými bity dvou čísel.
Bitový AND (&): Provádí bitový AND mezi jednotlivými bity dvou čísel.
Bitový XOR (^): Provádí bitový XOR mezi jednotlivými bity dvou čísel.
Bitový NOT (~): Provádí bitovou negaci (inverzi) jednotlivých bitů čísla.
Bitový posun doleva (<<): Posune bity čísla o určitý počet pozic doleva.
Bitový posun doprava (>>): Posune bity čísla o určitý počet pozic doprava.
'''
myself_binary = int('01010010', 2)  # Převod binárního čísla na desítkové
print("Binární číslo v desítkové soustavě:", myself_binary)
print(myself_binary)
shifted_binary = myself_binary >> 2
shifted_decimal = int(bin(shifted_binary), 2)
print(shifted_decimal)
hex_number = int("1A", 16)
bitwise_product = hex_number & myself_binary
print(bitwise_product)
result = f"Binární součin čísla 0x1A a {bin(myself_binary)} je {bin(bitwise_product)}."
print(result)



'''Python plně podporuje operace v plovoucí řádové čárce (tj. desetinná čísla). 
Operátor pracující s různými typy operandů si nejprve zkonvertuje celá čísla na čísla 
v plovoucí řádové čárce a následně provede výpočet (obdobné chování jako v jazyce C).
Výsledek je vždy desetinné číslo.
'''
#Float Literal
float_1 = 10.5
float_2 = 1.5e2 # Zápis reálného čísla pomocí exponentu = 1.5 * (10 ** 2)
#print(float_1 + float_2)


# Použití vestavěných matematických funkcí
# print(round(rating))
# Použití importovaného modulu math a jeho metod
import math
# print(math.floor(rating))
# print(math.cos(45))

# Zjištění datového typu
# x = input("x: ")
# Vrátí typ str - proto je nutná typová konverze - int(), float()
# Typová konverze
# print(int(x) + 20)

# Komplexní čísla a Python
'''Python plně podporuje komplexní čísla, přičemž imaginární číslo je zapisováno s příponou "j" nebo "J". 
Komplexní čísla zapisujeme ve tvaru "(Re + Imj)" nebo je můžeme vytvořit pomocí interní funkce "complex(Re, Im)":
'''
#Complex Literal
complex = 3.14j

'''Komplexní čísla jsou vždy reprezentována dvojicí desetinných čísel, reálnou a imaginární částí. 
Chceme-li získat velikosti těchto částí čísla z, použijeme zápisu z.real a z.imag:'''
# z = 4.5 + 0.5j
# print(z, z.imag, z.real)

'''Poněvadž v matematice neexistuje způsob, jak převést komplexní číslo na reálné, 
ani Python nedovoluje použití konverzních funkcí float(), int() a long() s komplexním argumentem. 
Raději použijte funkci abs(z) pro získání absolutní hodnoty komplexního čísla, 
nebo zápis z.real reprezentují reálnou část čísla: 
'''
# Následující řádek vyvolá chybu
# print(float(z))
#
# print(abs(z))
# Je totéž jako sqrt(z.real**2 + z.imag**2)

'''
Funguje pouze  v interaktivní konzoli!
Speciální proměnná _ reprezentuje předešlý výsledek.

>>> urok = 12.5 / 100
>>> penize = 100.50
>>> penize * urok
12.5625
>>> penize + _
113.0625
>>> round(_, 2)
113.06
>>>

Varování: Hodnota proměnné _ by nikdy neměla být modifikována uživatelem. 
Pokud byste jí přiřadili hodnotu, vytvořili byste nezávislou lokální proměnnou se stejným jménem, 
která by zakryla interní proměnnou s tímto chováním.'''


