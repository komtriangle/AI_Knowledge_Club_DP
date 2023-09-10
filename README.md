### Инструкция по запуску

Скачать репозиторий:

```powershell
git clone https://github.com/komtriangle/AI_Knowledge_Club_DP.git
```

Cкачать модель, разархивировать ее, положить папку **AI_Knowledge_Club_DP**
Google drive (https://drive.google.com/drive/folders/1ICPybvUfJqIIH58s1wsZV-_wdArvUu2r?usp=sharing)

Перейти в папку с docker-compose:

```powershell
cd AI_Knowledge_Club_DP/dockerItems
```

Запустить сервис:

```powershell
docker-compose up -d
```

```
Ссылка на swagger: http://87.242.91.137:8000/docs
```



### Описание файлов: 



```
EDA.ipynb - Ноутбук исследования данных, на диапазоны и корреляцию, первичный EDA.
```



```
als_reccomender.ipynb - файл для генерации предсказаний методом матричного разложения ALS. Файл содержит в себе подготовку данных и обучение модели ALS с использованием Pyspark. Также в ноутбуке есть функционал сохранения чекпойнтов модели и инференс на тестовых данных соревнования.
```



```
video_processing.ipynb - файл с обработкой текстовых данных информации о видео, построение эмбедингов и тематическое моделирование. Кластеринг и визуализация полученных результатов
```



