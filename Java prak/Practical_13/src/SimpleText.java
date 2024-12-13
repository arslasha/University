// Интерфейс для текста
interface Text {
    void display(); // Метод для отображения текста
}

// Класс для базового текста
class SimpleText implements Text {
    private String content;

    // Конструктор, принимающий текстовое содержимое
    public SimpleText(String content) {
        this.content = content;
    }

    // метод Отображает базовый текст
    @Override
    public void display() {
        System.out.println(content);
    }
}

// Абстрактный класс-декоратор, реализующий интерфейс Text
abstract class TextDecorator implements Text {
    protected Text decoratedText;

    // Конструктор, принимающий объект, который нужно "украшать"
    public TextDecorator(Text decoratedText) {
        this.decoratedText = decoratedText;
    }

    // Вызывает метод display() у базового объекта
    @Override
    public void display() {
        decoratedText.display();
    }
}

// Декоратор для добавления жирного текста
class BoldTextDecorator extends TextDecorator {
    public BoldTextDecorator(Text decoratedText) {
        super(decoratedText);
    }

    // Добавляет функционал жирного текста
    @Override
    public void display() {
        System.out.print("**"); // Оформление начала жирного текста
        decoratedText.display(); // Вызов отображения базового текста
        System.out.print("**"); // Оформление конца жирного текста
    }
}

// Декоратор для добавления курсивного текста
class ItalicTextDecorator extends TextDecorator {
    public ItalicTextDecorator(Text decoratedText) {
        super(decoratedText);
    }

    // Добавляет функционал курсивного текста
    @Override
    public void display() {
        System.out.print("_"); // Оформление начала курсивного текста
        decoratedText.display(); // Вызов отображения базового текста
        System.out.print("_"); // Оформление конца курсивного текста
    }
}

// Декоратор для добавления подчёркнутого текста
class UnderlineTextDecorator extends TextDecorator {
    public UnderlineTextDecorator(Text decoratedText) {
        super(decoratedText);
    }

    // Добавляет функционал подчёркивания текста
    @Override
    public void display() {
        System.out.print("__"); // Оформление начала подчёркивания
        decoratedText.display(); // Вызов отображения базового текста
        System.out.print("__"); // Оформление конца подчёркивания
    }
}