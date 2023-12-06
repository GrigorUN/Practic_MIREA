import basic

while True:
    text = input('>>> ')
    if text.lower() == 'exit':
        break
    
    result, error = basic.run('<stdin>', text)

    if error:
        print(error.as_string())
    elif result:
        print(repr(result))
