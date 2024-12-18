const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin'); // Импорт плагина
const MiniCssExtractPlugin = require('mini-css-extract-plugin'); // Импорт плагина для извлечения CSS

module.exports = {
  entry: './src/scripts/index.js', // Входная точка для JavaScript
  output: {
    path: path.resolve(__dirname, 'dist'), // Директория для сборки
    filename: 'main.js', // Имя выходного файла
  },
  module: {
    rules: [
      {
        test: /\.css$/, // Загрузка CSS файлов
        use: [
          MiniCssExtractPlugin.loader, // Извлечение CSS в отдельный файл
          'css-loader', // Загрузка и обработка CSS
        ],
      },
      {
        test: /\.(png|jpg|svg)$/, // Загрузка изображений
        type: 'asset/resource',
        generator: {
          filename: 'images/[name][ext]', // Путь для изображений
        },
      },
      {
        test: /\.(woff|woff2|eot|ttf|otf)$/, // Загрузка шрифтов
        type: 'asset/resource',
        generator: {
          filename: 'fonts/[name][ext]', // Путь для шрифтов
        },
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html', // Шаблон HTML
      filename: 'index.html',       // Выходной файл HTML
    }),
    new MiniCssExtractPlugin({
      filename: 'main.css', // Имя выходного CSS файла
    }),
  ],
  devServer: {
    static: path.resolve(__dirname, 'dist'), // Папка для сервера разработки
    port: 8080, // Порт для локального хостинга
    open: true, // Автоматическое открытие браузера
  },
};
