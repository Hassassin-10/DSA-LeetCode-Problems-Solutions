            tens = (num // 10) % 10
            hundreds = num // 100

            need = [0] * 10
            need[ones] += 1
            need[tens] += 1
            need[hundreds] += 1

            possible = True

            for d in range(10):
                if need[d] > freq[d]:
                    possible = False
                    break

            if possible:
                ans += 1

        return ans

