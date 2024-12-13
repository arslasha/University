// Абстрактный класс Logger, определяет базовую структуру обработчиков
abstract class Logger {
    protected Logger nextLogger; // Следующий обработчик в цепочке

    // Устанавливает следующего обработчика
    public void setNextLogger(Logger nextLogger) {
        this.nextLogger = nextLogger;
    }

    // Метод для обработки сообщения
    public void logMessage(String level, String message) {
        if (nextLogger != null) { // Если есть следующий обработчик
            nextLogger.logMessage(level, message); // Передаём запрос дальше
        }
    }
}

// Конкретный обработчик для сообщений уровня INFO
class InfoLogger extends Logger {
    public void logMessage(String level, String message) {
        if ("INFO".equals(level)) { // Если уровень сообщения INFO
            System.out.println("INFO: " + message); // Обрабатываем сообщение
        } else if (nextLogger != null) { // Если уровень другой, передаём дальше
            nextLogger.logMessage(level, message);
        }
    }
}

// Конкретный обработчик для сообщений уровня WARNING
class WarningLogger extends Logger {
    public void logMessage(String level, String message) {
        if ("WARNING".equals(level)) { // Если уровень сообщения WARNING
            System.out.println("WARNING: " + message); // Обрабатываем сообщение
        } else if (nextLogger != null) { // Если уровень другой, передаём дальше
            nextLogger.logMessage(level, message);
        }
    }
}

// Конкретный обработчик для сообщений уровня ERROR
class ErrorLogger extends Logger {
    public void logMessage(String level, String message) {
        if ("ERROR".equals(level)) { // Если уровень сообщения ERROR
            System.out.println("ERROR: " + message); // Обрабатываем сообщение
        } else if (nextLogger != null) { // Если уровень другой, передаём дальше
            nextLogger.logMessage(level, message);
        }
    }
}

// Конкретный обработчик для сообщений уровня CRITICAL
class CriticalLogger extends Logger {
    public void logMessage(String level, String message) {
        if ("CRITICAL".equals(level)) { // Если уровень сообщения CRITICAL
            System.out.println("CRITICAL: " + message); // Обрабатываем сообщение
        } else if (nextLogger != null) { // Если уровень другой, передаём дальше
            nextLogger.logMessage(level, message);
        }
    }
}

// Конкретный обработчик для сообщений уровня DEBUG
class DebugLogger extends Logger {
    public void logMessage(String level, String message) {
        if ("DEBUG".equals(level)) { // Если уровень сообщения DEBUG
            System.out.println("DEBUG: " + message); // Обрабатываем сообщение
        } else if (nextLogger != null) { // Если уровень другой, передаём дальше
            nextLogger.logMessage(level, message);
        }
    }
}

public class Main {
    public Main() {
    }

    public static void main(String[] args) {
        Logger infoLogger = new InfoLogger();
        Logger warningLogger = new WarningLogger();
        Logger errorLogger = new ErrorLogger();
        Logger criticalLogger = new CriticalLogger();
        Logger debugLogger = new DebugLogger();
        infoLogger.setNextLogger(warningLogger);
        warningLogger.setNextLogger(errorLogger);
        errorLogger.setNextLogger(criticalLogger);
        criticalLogger.setNextLogger(debugLogger);
        infoLogger.logMessage("INFO", "This is an informational message.");
        infoLogger.logMessage("WARNING", "This is a warning message.");
        infoLogger.logMessage("ERROR", "This is an error message.");
        infoLogger.logMessage("CRITICAL", "This is a critical message.");
        infoLogger.logMessage("DEBUG", "This is a debug message.");
    }
}