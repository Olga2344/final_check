import requests
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def exchange():
    # Получаем названия валют из комбо-боксов
    cur_name=t_combobox.get()
    crypto_name=crypto_combobox.get()
    o_m_cur_name=o_m_combobox.get()
    # Получаем коды валют из словаре
    cur_code=currency_dict.get(t_combobox.get())
    crypto_code=crypto_currencies.get(crypto_combobox.get())
    o_m_cur_code=currency_dict.get(o_m_combobox.get())
    # Проверяем наличие всех необходимых кодов валют
    if cur_code and crypto_code and o_m_cur_code:
        try:
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_code}&vs_currencies={cur_code}%2C{o_m_cur_code}"
            headers = {"accept": "application/json", "x-cg-demo-api-key": "CG-W89GTPWPQ9mbknFKrg5Cfbu7 "}

            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data=response.json()
            # Проверяем, есть ли нужная информация в ответе API
            if cur_code  and o_m_cur_code in data[crypto_code]:
                exchange_rate=data[crypto_code][cur_code]
                o_m_exchange_rate = data[crypto_code][o_m_cur_code]
                # Отображаем результат обмена в диалоговом окне
                mb.showinfo('Exchange Currency', f'Exchange rate: \n\nfor 1 unit of {crypto_name}'
                                                 f'\n{exchange_rate:.4f} {cur_name} or \n'
                                                 f'{o_m_exchange_rate:.4f} {o_m_cur_name} \n')
            else:
                # Выводим ошибку, если указанная валюта не определена
                mb.showerror('Error', f'Currency {cur_code} is not defined')
        except Exception as e:
            # Обрабатываем любые другие исключения
            mb.showerror('Error', f'Happened problem: {e}')
    else:
        # Предупреждение, если пользователь не выбрал ни одну валюту
        mb.showwarning('Attention!', 'Choose a currency')
# Создание основного окна приложения
window=Tk()
window.title('Exchanges currency')
window.geometry('200x300')

# Словарь с кодами валют и их названиями на английском языке
currency_dict = {
    'US Dollar': 'usd',
    'Euro': 'eur',
    'Japanese Yen': 'jpy',
    'British Pound': 'gbp',
    'Canadian Dollar': 'cad',
    'Australian Dollar': 'aud',
    'Chinese Yuan': 'cny',
    'Russian Ruble': 'rub',
    'New Zealand Dollar': 'nzd'
}
# Словарь с криптовалютами и их кодами
crypto_currencies = {
    "Bitcoin": "bitcoin",
    "Ethereum": "ethereum",
    "Litecoin": "litecoin",
    "1984": "1984-token",
    "Binance Coin": "binancecoin",
    "EOS": "eos",
    "Ripple": "ripple",
    "Stellar": "stellar",
    "Chainlink": "chainlink"
}
# Создание элементов интерфейса
Label(text='Choose crypto name').pack(padx=10, pady=5)

crypto_combobox=ttk.Combobox(values=list(crypto_currencies.keys()))
crypto_combobox.pack()

Label(text='Choose name currency').pack(padx=10, pady=5)

t_combobox=ttk.Combobox(values=list(currency_dict.keys()))
t_combobox.pack()

Label(text='Choose one more name currency').pack(padx=10, pady=5)
o_m_combobox=ttk.Combobox(values=list(currency_dict.keys()))
o_m_combobox.pack()

Button(text='Get info', command=exchange).pack(padx=10, pady=5)
# Запуск основного цикла приложения
window.mainloop()