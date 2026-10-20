def media(notas):
    """Devuelve la media aritmética de una lista de notas."""
    return sum(notas) / len(notas)


def calificacion(nota):
    """Devuelve la calificación en texto de una nota numérica."""
    if nota < 5:
        return "Insuficiente"
    elif nota < 6:
        return "Suficiente"
    elif nota < 7:
        return "Bien"
    elif nota < 9:
        return "Notable"
    return "Sobresaliente"


if __name__ == "__main__":
    notas = [6.5, 7, 8.25, 5]
    print(f"Media: {media(notas):.2f}")