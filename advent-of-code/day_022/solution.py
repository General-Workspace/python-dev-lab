from time import perf_counter as measure_time

def performance_profiler(method):
    """
    A decorator that measures and prints the execution time of a method.
    
    This decorator wraps the given method and calculates its execution time,
    providing performance insights for the decorated function.
    
    Args:
        method (callable): The function to be timed
    
    Returns:
        callable: A wrapper function that measures the method's execution time
    """
    def timing_wrapper(*args, **kwargs):
        # Record the start time before method execution
        start_time = measure_time()
        
        # Execute the original method
        result = method(*args, **kwargs)
        
        # Print the execution time with high precision
        print(
            f"Method {method.__name__} took: "
            f"{measure_time() - start_time:2.5f} sec"
        )
        
        # Return the original method's result
        return result
    return timing_wrapper


# Function to calculate the next secret number based on the rules
def evolve_secret(secret_number):
    # Step 1: Multiply by 64, mix, prune
    secret_number ^= (secret_number * 64) % 16777216
    secret_number %= 16777216

    # Step 2: Divide by 32, round down, mix, prune
    secret_number ^= (secret_number // 32) % 16777216
    secret_number %= 16777216

    # Step 3: Multiply by 2048, mix, prune
    secret_number ^= (secret_number * 2048) % 16777216
    secret_number %= 16777216

    return secret_number


@performance_profiler
def generate_two_thousand_new_secret_numbers(values):
    total = 0
    for x in values:
        for _ in range(2000):
            x = evolve_secret(x)
        total += x
    return total


@performance_profiler
def get_most_bananas(values):
    total = {}
    for x in values:
        last = x % 10
        pattern_list = []
        for _ in range(2000):
            x = evolve_secret(x)
            temp = x % 10
            pattern_list.append((temp - last, temp))
            last = temp
        seen = set()
        for i in range(len(pattern_list)-4):
            pat = tuple(x[0] for x in pattern_list[i:i+4])
            val = pattern_list[i+3][1]
            if pat not in seen:
                seen.add(pat)
                if pat not in total:
                    total[pat] = val
                else:
                    total[pat] += val
    return max(total.values())


def read_file(file_path):
    with open(file_path, "r") as f:
        lines = f.read().strip().splitlines()
    
    return [int(x) for x in lines]


if __name__ == "__main__":
    values = read_file("input.txt")

    print(f"Part 1:", generate_two_thousand_new_secret_numbers(values))
    print(f"Part 2:", get_most_bananas(values))