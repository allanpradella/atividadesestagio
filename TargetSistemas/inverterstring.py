def inverter_string(s):
    return s[::-1]

if __name__ == "__main__":
    string = input(f"Digite a string que será invertida: ")
    resultado = inverter_string(string)
    print(f"String invertida: {resultado}")
    