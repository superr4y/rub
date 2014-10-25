def s1(n,k)
  # Stirling Zahl erster Art
  if (n == 0 and k == 0) or (n == k)
    return 1
  end
  if k == 0
    return 0
  end
  return s1(n-1, k-1) + (n-1)*s1(n-1, k)
end

def s2(n,k)
  # Stirling Zahl zweiter Art
  if (k > n)
    return 0
  end
  if (n == 0 and k == 0)
    return 1
  end
  if (k == 0)
    return 0
  end
  return s2(n-1, k-1) + k*s2(n-1,k)
end

puts s1(10,4)

puts s2(7,5)
