# Frequency counting seems a bit awkward and tedious here
# Use prime factor decomposition, i.e. map characters to prime #s s.t. anagrams have same product


class Solution:
    def generate_prime_numbers(self, n: int) -> List[int]:
        """Generate a list of the first n prime numbers."""
        primes = []
        candidate = 2
        while len(primes) < n:
            is_prime = all(candidate % prime != 0 for prime in primes)
            if is_prime:
                primes.append(candidate)
            candidate += 1
        return primes

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        import string
        
        if input == [""]:
            return [[""]]

        char_to_prime = {char: prime for char, prime in zip(string.ascii_lowercase, self.generate_prime_numbers(26))}
        output = []

        group_map = {
            # prime number char product : idx
        }
        for idx, string in enumerate(strs):
            product = 1
            for c in string:
                product *= char_to_prime[c]
            
            if product not in group_map:
                group_map[product] = [idx]
            else:
                group_map[product].append(idx)
        
        for product, index_list in group_map.items():
            output.append([strs[i] for i in index_list])
        return output
            