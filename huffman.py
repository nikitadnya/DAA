

import heapq

def huffman(text):
   
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    
    heap = [[freq[ch], [ch]] for ch in freq]
    heapq.heapify(heap)

    
    codes = {ch: "" for ch in freq}

    
    while len(heap) > 1:
        f1, chars1 = heapq.heappop(heap)   
        f2, chars2 = heapq.heappop(heap)   

        
        for ch in chars1:
            codes[ch] = '0' + codes[ch]
        for ch in chars2:
            codes[ch] = '1' + codes[ch]

       
        heapq.heappush(heap, [f1 + f2, chars1 + chars2])

    return codes


text = input("Enter text: ")
codes = huffman(text)
print("\nCharacter | Code")
for ch in sorted(codes):
    print(f"   {ch}     |  {codes[ch]}")
