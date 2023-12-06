def funcao_padrao():    
    import phonenumbers
    from phonenumbers import geocoder,carrier,timezone

    a = input("Numero: ")
    number = phonenumbers.parse(a)
        
    print(f"Location: {geocoder.description_for_number(number, 'en')}")
    print(f"Carrier: {carrier.name_for_number(number, 'en')}")
    print(f"Time Zone: {timezone.time_zones_for_number(number)}")