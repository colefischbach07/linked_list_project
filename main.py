from singly_linked_list import SinglyLinkedList
from split_evens_odds import SplitEvensOdds


def main():
    print("=== Singly Linked List Demonstration ===")

    values = [10, 20, 30, 40, 50]

    forward_list = SinglyLinkedList()
    forward_list.build_list_forward(values)
    print("\nForward list:")
    print(forward_list)

    backward_list = SinglyLinkedList()
    backward_list.build_list_backward(values)
    print("\nBackward list:")
    print(backward_list)

    print("\n=== Insert and Remove ===")

    forward_list.insert_after(20, 25)
    print("After inserting 25 after 20:")
    print(forward_list)

    forward_list.remove(30)
    print("After removing 30:")
    print(forward_list)

    duplicate_list = SinglyLinkedList()
    duplicate_list.build_list_forward([10, 20, 20, 30, 20])

    print("\nBefore remove_all:")
    print(duplicate_list)

    removed = duplicate_list.remove_all(20)

    print("After remove_all(20):")
    print(duplicate_list)
    print("Number removed:", removed)

    print("\n=== Split Evens and Odds ===")

    split_list = SplitEvensOdds()
    split_list.build_list_forward([10, 13, 14, 18, 21])

    print("Original list before split:")
    print(split_list)

    even_list, odd_list = split_list.split_even_odd()

    print("Even list:")
    print(even_list)

    print("Odd list:")
    print(odd_list)

    print("Original list after split:")
    print(split_list)

    print("\n=== Inherited Operation ===")

    inherited_test = SplitEvensOdds()
    inherited_test.append(5)
    inherited_test.append(10)
    inherited_test.prepend(1)

    print(inherited_test)

    print("\n=== Error Handling ===")

    try:
        forward_list.remove(100)
    except ValueError as error:
        print("Handled error:", error)


if __name__ == "__main__":
    main()