import sys

def main():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # Parse total at-bats and their outcomes
    n = int(input_data[0])
    at_bats = [int(x) for x in input_data[1:n+1]]

    total_bases = 0
    official_at_bats = 0

    # Process each at-bat
    for outcome in at_bats:
        if outcome != -1:  # Ignore walks
            total_bases += outcome
            official_at_bats += 1

    # Compute and output the slugging percentage
    slugging_percentage = total_bases / official_at_bats
    print(slugging_percentage)

if __name__ == '__main__':
    main()
