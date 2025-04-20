class Solution:

    def find_shortest_string(arr):
        shortest = arr[0]
        for i in range(len(arr)):
            if len(arr[i]) < len(shortest):
                shortest = arr[i]
        return shortest

    if __name__ == '__main__':


        print("Expecting: 'a'")
        print(find_shortest_string(['aaa', 'a', 'bb', 'ccc']))

        print("")

        print("Expecting: 'hi'")
        print(find_shortest_string(['cat', 'hi', 'dog', 'an']))

        print("")

        print("Expecting: 'lily'")
        print(find_shortest_string(['flower', 'juniper', 'lily', 'dandelion']))

        print("")

        print("Expecting: 'cat'")
        print(find_shortest_string(['cat']))