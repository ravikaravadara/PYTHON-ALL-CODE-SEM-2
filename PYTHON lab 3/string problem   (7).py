def generate_pythagorean_triplets(limit):
    

    triplets = []
    for m in range(2, int(limit**0.5) + 1):  
        for n in range(1, m):
            if (m + n) % 2 == 1 and math.gcd(m, n) == 1:
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2

                if a <= limit and b <= limit and c <= limit:
                    triplets.append(tuple(sorted((a, b, c))))  
    return sorted(list(set(triplets))) 



import math  
limit = 30
pythagorean_triplets = generate_pythagorean_triplets(limit)

print(f"Pythagorean triplets with side length <= {limit}:")
for triplet in pythagorean_triplets:
    print(triplet)





def generate_pythagorean_triplets_efficient(limit):
  """Generates Pythagorean triplets (a, b, c) <= limit efficiently using Euclid's formula."""
  triplets = set()  

  for m in range(2, int(math.sqrt(limit)) + 1):
    for n in range(1, m):
      if (m + n) % 2 == 1 and math.gcd(m, n) == 1:  
          a = m**2 - n**2
          b = 2 * m * n
          c = m**2 + n**2

          if c <= limit:  
            triplets.add(tuple(sorted((a, b, c))))

            
            k = 2
            while c * k <= limit:
              triplets.add(tuple(sorted((a*k, b*k, c*k))))
              k += 1
  return sorted(list(triplets))

limit = 30
pythagorean_triplets = generate_pythagorean_triplets_efficient(limit)

print(f"\nPythagorean triplets with side length <= {limit} (Efficient Method):")
for triplet in pythagorean_triplets:
    print(triplet)
