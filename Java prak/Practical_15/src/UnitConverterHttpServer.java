    import java.io.*;
    import java.net.*;
    import java.util.HashMap;
    import java.util.Map;

    public class UnitConverterHttpServer {
        // Порт, на котором будет запущен сервер
        private static final int PORT = 8080;

        public static void main(String[] args) {
            try (ServerSocket serverSocket = new ServerSocket(PORT)) {
                // Запуск сервера и сообщение о том, что он работает
                System.out.println("Unit Converter HTTP Server запущен на порту " + PORT);

                // Бесконечный цикл для обработки входящих подключений
                while (true) {
                    try (Socket clientSocket = serverSocket.accept()) {
                        // Обработка каждого клиента
                        handleClient(clientSocket);
                    }
                }
            } catch (IOException e) {
                // Обработка ошибок запуска сервера
                System.err.println("Ошибка запуска сервера: " + e.getMessage());
            }
        }

        // Метод для обработки клиентских запросов
        private static void handleClient(Socket clientSocket) throws IOException {
            BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            PrintWriter out = new PrintWriter(clientSocket.getOutputStream());

            // Читаем первую строку запроса (метод, путь и версия HTTP)
            String line = in.readLine();
            if (line == null) return;

            // Разделяем строку на части: метод, путь и версию
            String[] requestParts = line.split(" ");
            String method = requestParts[0];
            String path = requestParts[1];

            // Если метод GET и путь начинается с "/convert", вызываем обработчик
            if (method.equals("GET") && path.startsWith("/convert")) {
                handleConvert(path, out);
            } else {
                // Если путь не распознан, возвращаем ошибку 404
                sendHttpResponse(out, 404, "<html><body><h1>404 Not Found</h1></body></html>");
            }

            // Отправляем ответ клиенту
            out.flush();
        }

        // Метод для обработки конвертации единиц
        private static void handleConvert(String path, PrintWriter out) {
            // Разбираем параметры запроса
            Map<String, String> queryParams = parseQueryParams(path);
            try {
                // Получаем значение для конвертации, исходные и целевые единицы
                double value = Double.parseDouble(queryParams.get("value"));
                String from = queryParams.get("from");
                String to = queryParams.get("to");

                // Выполняем конвертацию
                double result = convertUnits(value, from, to);

                // Отправляем успешный ответ с результатом
                sendHttpResponse(out, 200, "<html><body><h1>Conversion Result</h1>" +
                        "<p>" + value + " " + from + " = " + result + " " + to + "</p></body></html>");
            } catch (Exception e) {
                // Обрабатываем ошибки, возвращая клиенту HTTP 400
                sendHttpResponse(out, 400, "<html><body><h1>Invalid Request</h1>" +
                        "<p>Ensure you provide valid value, from, and to parameters.</p></body></html>");
            }
        }

        // Метод для выполнения конвертации единиц
        private static double convertUnits(double value, String from, String to) {
            // Карта с коэффициентами для преобразования между единицами
            Map<String, Double> conversionRates = new HashMap<>();
            conversionRates.put("meters_to_kilometers", 0.001);
            conversionRates.put("kilometers_to_meters", 1000.0);
            conversionRates.put("grams_to_kilograms", 0.001);
            conversionRates.put("kilograms_to_grams", 1000.0);
            conversionRates.put("celsius_to_kelvin", 1.0);
            conversionRates.put("kelvin_to_celsius", -1.0);

            // Генерируем ключ для поиска коэффициента
            String key = from + "_to_" + to;

            // Проверяем, поддерживается ли такая конвертация
            if (!conversionRates.containsKey(key)) {
                throw new IllegalArgumentException("Unsupported conversion");
            }

            double conversionRate = conversionRates.get(key);

            // Обработка специальных случаев для температуры
            if (key.equals("celsius_to_kelvin")) {
                return value + 273.15;
            } else if (key.equals("kelvin_to_celsius")) {
                return value - 273.15;
            }

            // Обычная конвертация через коэффициент
            return value * conversionRate;
        }

        // Метод для разбора параметров строки запроса
        private static Map<String, String> parseQueryParams(String path) {
            Map<String, String> queryParams = new HashMap<>();
            String[] parts = path.split("\\?");
            if (parts.length > 1) {
                String[] pairs = parts[1].split("&");
                for (String pair : pairs) {
                    String[] keyValue = pair.split("=");
                    if (keyValue.length == 2) {
                        queryParams.put(keyValue[0], keyValue[1]);
                    }
                }
            }
            return queryParams;
        }

        // Метод для отправки HTTP-ответа
        private static void sendHttpResponse(PrintWriter out, int statusCode, String body) {
            // Формируем HTTP-заголовки
            out.println("HTTP/1.1 " + statusCode + " OK");
            out.println("Content-Type: text/html");
            out.println("Content-Length: " + body.length());
            out.println();

            // Отправляем тело ответа
            out.println(body);
        }
    }
    //http://localhost:8080/convert?value=100&from=meters&to=kilometers