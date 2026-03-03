def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def find_longest_sequence_merge(cards):
    jokers_count = 0
    unique_cards = []
    seen = set()
    
    for c in cards:
        if c == 0:
            jokers_count += 1
        elif c not in seen:
            unique_cards.append(c)
            seen.add(c)

    if not unique_cards:
        return jokers_count


    unique_cards = merge_sort(unique_cards)

    max_length = 0
    left = 0
    n_unique = len(unique_cards)
    
    for right in range(n_unique):
        gaps = (unique_cards[right] - unique_cards[left]) - (right - left)
        
        while gaps > jokers_count:
            left += 1
            gaps = (unique_cards[right] - unique_cards[left]) - (right - left)
            
        current_length = (right - left + 1) + jokers_count
        max_length = max(max_length, current_length)

    return min(max_length, len(cards))

