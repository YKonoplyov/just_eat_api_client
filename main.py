from just_eat_client import create_client
import re


def validate_postalcode(postalcode: str) -> bool:
    """
    Validates postalcode
    """
    ex = r"^([A-Za-z][A-Ha-hJ-Yj-y]?[0-9][A-Za-z0-9]? ?[0-9][A-Za-z]{2}|[Gg][Ii][Rr] ?0[Aa]{2})$"

    if len(postalcode) < 4:
        ex = r"^\w{1,2}\d{1,2}"

    if not re.match(ex, postalcode):
        return False
    return True


def main() -> None:
    """
    The main function to interact with the Just Eat API, input postal codes,
    and optionally write restaurant data to a JSON file.
    """
    client = create_client()

    write_dict = {
        "y": True,
        "n": False,
    }
    while True: 
        postalcode = input("Enter postal code: ")
        if validate_postalcode(postalcode=postalcode):
            break
        print("Please enter valid postal code")

    while True:
        need_write = input(
            "Write restaurants data to .json file? (y/N): "
        ).lower()
        if need_write == "y" or need_write == "n":
            write = write_dict.get(need_write)
            break
        print("Input not recognized")
    client.from_postal_code(postalcode=postalcode, write=write)


if __name__ == "__main__":
    main()
