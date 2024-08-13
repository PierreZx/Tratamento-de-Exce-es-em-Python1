def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def conversor_temperatura():
    try:
        entrada = input("Informe a temperatura em Celsius: ")
        entrada = entrada.replace(",", ".")
        celsius = float(entrada)

        if celsius < -273.15:
            raise ValueError("Temperatura muito baixa para ser real.")
        elif celsius > 1000:
            raise ValueError("Temperatura muito alta para ser real.")
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"{celsius}°C é equivalente a {fahrenheit:.2f}°F")
    
    except ValueError as e:
        print(f"Erro: {e}. Por favor, insira uma temperatura válida.")
        
conversor_temperatura()
