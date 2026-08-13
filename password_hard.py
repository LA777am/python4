class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        has_lower = False
        has_upper = False
        has_digit = False

        for ch in password:
            if ch.islower():
                has_lower = True
            elif ch.isupper():
                has_upper = True
            elif ch.isdigit():
                has_digit = True

        missing = 0

        if not has_lower:
            missing += 1
        if not has_upper:
            missing += 1
        if not has_digit:
            missing += 1

        runs = []
        count = 1

        for i in range(1, n):
            if password[i] == password[i - 1]:
                count += 1
            else:
                if count >= 3:
                    runs.append(count)
                count = 1

        if count >= 3:
            runs.append(count)

        replacements = 0

        for length in runs:
            replacements += length // 3

        if n < 6:
            return max(6 - n, missing)

        if n <= 20:
            return max(replacements, missing)

        delete_count = n - 20
        deletions = delete_count

        for i in range(len(runs)):
            if deletions == 0:
                break

            if runs[i] % 3 == 0:
                runs[i] -= 1
                deletions -= 1

        for i in range(len(runs)):
            if deletions < 2:
                break

            if runs[i] % 3 == 1:
                runs[i] -= 2
                deletions -= 2

        for i in range(len(runs)):
            if deletions < 3:
                break

            if runs[i] % 3 == 2:
                runs[i] -= 3
                deletions -= 3

        for i in range(len(runs)):
            if deletions < 3:
                break

            possible = (runs[i] // 3) * 3
            d = min(possible, deletions)
            d -= d % 3

            runs[i] -= d
            deletions -= d

        replacements = 0

        for length in runs:
            replacements += length // 3

        return delete_count + max(replacements, missing)