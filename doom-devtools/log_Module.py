import datetime

allow_printing = True
allow_warning = True
allow_error = True
def log(process: str, text: str, mode: str):
    timestamp = datetime.datetime.now().strftime("%c")
    body = f"{timestamp} {process}: {text}"

    if mode.lower() == "normal":
        if allow_printing:
            print(body)
    elif mode.lower() == "warning":
        if allow_warning:
            print(f"WARNING: {body}")
    elif mode.lower() == "error":
        if allow_error:
            raise Exception(body)
    
    return body

log("LOG", "TEST PRINT", "Normal")
