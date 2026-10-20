def media(notas):
    """Devuelve la media aritmética de una lista de notas."""
    return sum(notas) / len(notas)


if __name__ == "__main__":
    notas = [6.5, 7, 8.25, 5]
    print(f"Media: {media(notas):.2f}")
