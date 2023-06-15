def do_connect():
    # Importamos modulo network
    import network                            
    global sta_if
    # Instanciamos el objeto -sta_if- para controlar la interfaz STA
    sta_if = network.WLAN(network.STA_IF)
    # COMIENZA EL BUCLE - SI NO EXISTE CONEXION
    if not sta_if.isconnected():
        # Activamos el interfaz STA del ESP32
        sta_if.active(True)
        # Iniciamos la conexion con el AP
        sta_if.connect("<DACJ>", "<121053848522>")            
        print('Conectando a la red', SSID + "...")
        # SI NO SE ESTABLECE
        while not sta_if.isconnected():           
            # REPITE EL BUCLE
            pass
    # MUESTRA EN PANTALLA    
    print('CONFIGURACION DE RED(IP/MASCARA/GATEWAY/DNS:', sta_if.ifconfig())