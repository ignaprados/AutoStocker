# funcion para obtener el tiempo actual
def get_current_time():
    time_update = datetime.now()                                                                # obtener la fecha y hora actual
    now = time_update.strftime("%d/%m/%Y %H:%M:%S")                                             # formatear la fecha y hora actual
    return now                                                                                  # retornar fecha