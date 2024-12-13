public class DecoratorPatternDemo {
    public static void main(String[] args) {
        // Создаём базовый текст
        Text simpleText = new SimpleText("Hello, World!");

        // Декорируем текст жирным
        Text boldText = new BoldTextDecorator(simpleText);

        // Декорируем текст курсивом
        Text italicText = new ItalicTextDecorator(simpleText);

        // Декорируем текст подчёркиванием
        Text underlinedText = new UnderlineTextDecorator(simpleText);

        // Применяем несколько декораторов вместе
        Text fancyText = new BoldTextDecorator(new ItalicTextDecorator(new UnderlineTextDecorator(simpleText)));

        // Демонстрация
        System.out.println("Базовый текст:");
        simpleText.display();

        System.out.println("\n\nЖирный текст:");
        boldText.display();

        System.out.println("\n\nКурсивный текст:");
        italicText.display();

        System.out.println("\n\nПодчёркнутый текст:");
        underlinedText.display();

        System.out.println("\n\nЖирный, курсивный и подчёркнутый текст:");
        fancyText.display();
    }
}