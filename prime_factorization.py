def prime_factorization(limit):
    if limit < 2:
        return f"Prime factorization of {limit} is not defined"

    result = "Here we go...\n"
    limitclone = limit
    prime_factors = []

    trrry = 2
    i = 2
    k = 0

    max_width = len(str(limit)) + 1  # Calculate the maximum width for alignment

    while limit != 1:
        while trrry <= limit:
            i = 2
            j = 0

            while trrry > i:
                if trrry % i == 0:
                    j = 1

                if j == 1:
                    break

                i += 1

            if j == 0 and limit % trrry == 0:
                result += f"{str(trrry).rjust(max_width)} | {str(limit).rjust(max_width)}\n"
                prime_factors.append(trrry)
                result += "---------\n"
                limit = limit // trrry
                trrry = 2
                break
            else:
                trrry += 1

        k += 1

    if limit == 1:
        result += f"{str(1).rjust(max_width)} | {''.rjust(max_width)}\n"
        result += "---------\n\n\n\n\n\n"
        prime_factors_str = " X ".join(map(str, prime_factors))
        result += f"{prime_factors_str} = {limitclone} "

    return result
