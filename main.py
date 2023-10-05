from just_eat_client import create_client


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
    
    postalcode = input("Enter postal code: ")
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
