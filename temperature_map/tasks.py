from itertools import count
import pathlib
import os

import requests

from celery import shared_task
from datetime import datetime, timedelta

from temperature_map.models import PointsPlace, WeatherDataMeteosource, WeatherDataPrediction


def formatted_ts():
    return str(datetime.now().strftime('%d %b %y %I:%M %p')) + '\n'


def write_log_new(log_txt, log_path="logs/meteosource_weather_data_log.txt"):
    file_dir = pathlib.Path(__file__).parent.resolve()
    log_path = os.path.join(str(file_dir), log_path)
    if os.path.isfile(log_path):
        file_size = os.path.getsize(log_path)
    else:
        file_size = 0
    if file_size > 1024 * 1000 * 2:
        with open(log_path, 'w', encoding='utf-8') as f:
            f.write(log_txt)
    else:
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(log_txt)


@shared_task
def insert_meteosource_weather_data():
    try:
        points_places = PointsPlace.objects.all()

        for pp in points_places:
            url = 'https://www.meteosource.com/api/v1/flexi/point?sections=daily&language=en&units=auto&key=4on31zz6iiv63jz2n3j9sdtq24ebjx5e27xx97v8&place_id={}'.format(pp.place_id)
            response = requests.get(url=url)
            if response.status_code == 200:
                data = response.json()
                
                for row in data['daily']['data']:
                    defaults = {
                        'place_id': pp.place_id,
                        'day': row['day'],
                        'weather': row['weather'],
                        'icon': row['icon'],
                        'summary': row['summary'],
                        'predictability': row['predictability'],
                        'all_day_weather': row['all_day']['weather'] if 'weather' in row['all_day'] else None,
                        'all_day_icon': row['all_day']['icon'] if 'icon' in row['all_day'] else None,
                        
                        'all_day_temperature': row['all_day']['temperature'] if 'temperature' in row['all_day'] else None,
                        'all_day_temperature_min': row['all_day']['temperature_min'] if 'temperature_min' in row['all_day'] else None,
                        'all_day_temperature_max': row['all_day']['temperature_max'] if 'temperature_max' in row['all_day'] else None,
                        
                        'all_day_feels_like': row['all_day']['feels_like'] if 'feels_like' in row['all_day'] else None,
                        'all_day_feels_like_min': row['all_day']['feels_like_min'] if 'feels_like_min' in row['all_day'] else None,
                        'all_day_feels_like_max': row['all_day']['feels_like_max'] if 'feels_like_max' in row['all_day'] else None,
                        
                        'all_day_soil_temperature': row['all_day']['soil_temperature'] if 'soil_temperature' in row['all_day'] else None,
                        'all_day_soil_temperature_min': row['all_day']['soil_temperature_min'] if 'soil_temperature_min' in row['all_day'] else None,
                        'all_day_soil_temperature_max': row['all_day']['soil_temperature_max'] if 'soil_temperature_max' in row['all_day'] else None,
                        
                        'all_day_wind_chill': row['all_day']['wind_chill'] if 'wind_chill' in row['all_day'] else None,
                        'all_day_wind_chill_min': row['all_day']['wind_chill_min'] if 'wind_chill_min' in row['all_day'] else None,
                        'all_day_wind_chill_max': row['all_day']['wind_chill_max'] if 'wind_chill_max' in row['all_day'] else None,
                        
                        'all_day_dew_point': row['all_day']['dew_point'] if 'dew_point' in row['all_day'] else None,
                        'all_day_dew_point_min': row['all_day']['dew_point_min'] if 'dew_point_min' in row['all_day'] else None,
                        'all_day_dew_point_max': row['all_day']['dew_point_max'] if 'dew_point_max' in row['all_day'] else None,
                        
                        'all_day_surface_temperature': row['all_day']['surface_temperature'] if 'surface_temperature' in row['all_day'] else None,
                        'all_day_surface_temperature_min': row['all_day']['surface_temperature_min'] if 'surface_temperature_min' in row['all_day'] else None,
                        'all_day_surface_temperature_max': row['all_day']['surface_temperature_max'] if 'surface_temperature_max' in row['all_day'] else None,
                        
                        'all_day_wind_speed': row['all_day']['wind']['wind_speed'] if 'wind_speed' in row['all_day']['wind'] else None,
                        'all_day_wind_gusts': row['all_day']['wind']['wind_gusts'] if 'wind_gusts' in row['all_day']['wind'] else None,
                        'all_day_wind_dir': row['all_day']['wind']['wind_dir'] if 'wind_dir' in row['all_day']['wind'] else None,
                        'all_day_wind_angle': row['all_day']['wind']['wind_angle'] if 'wind_angle' in row['all_day']['wind'] else None,
                        
                        'all_day_cloud_cover_total': row['all_day']['cloud_cover']['total'] if 'cloud_clover' in row['all_day'] and 'total' in row['all_day']['cloud_cover'] else None,
                        'all_day_cloud_cover_low': row['all_day']['cloud_cover']['low'] if 'cloud_clover' in row['all_day'] and  'low' in row['all_day']['cloud_cover'] else None,
                        'all_day_cloud_cover_middle': row['all_day']['cloud_cover']['middle'] if 'cloud_clover' in row['all_day'] and  'middle' in row['all_day']['cloud_cover'] else None,
                        'all_day_cloud_cover_high': row['all_day']['cloud_cover']['high'] if 'cloud_clover' in row['all_day'] and  'high' in row['all_day']['cloud_cover'] else None,
                        
                        'all_day_pressure': row['all_day']['pressure'] if 'pressure' in row['all_day'] else None,
                        
                        'all_day_precipitation_total': row['all_day']['precipitation']['total'] if 'total' in row['all_day']['precipitation'] else None,
                        'all_day_precipitation_type': row['all_day']['precipitation']['type'] if 'type' in row['all_day']['precipitation'] else None,

                        'all_day_probability_precipitation': row['all_day']['probability']['precipitation'] if 'precipitation' in row['all_day']['probability'] else None,
                        'all_day_probability_storm': row['all_day']['probability']['storm'] if 'storm' in row['all_day']['probability'] else None,
                        'all_day_probability_freeze': row['all_day']['probability']['freeze'] if 'freeze' in row['all_day']['probability'] else None,
                        
                        'all_day_ozone': row['all_day']['ozone'] if 'ozone' in row['all_day'] else None,
                        'all_day_humidity': row['all_day']['humidity'] if 'humidity' in row['all_day'] else None,
                        'all_day_snow_depth': row['all_day']['snow_depth'] if 'snow_depth' in row['all_day'] else None,
                        'all_day_visibility': row['all_day']['visibility'] if 'visibility' in row['all_day'] else None,

                        'morning_weather': row['morning']['weather'] if row['morning'] is not None else None,
                        'morning_icon': row['morning']['icon'] if row['morning'] is not None else None,
                        'morning_temperature': row['morning']['temperature'] if row['morning'] is not None else None,
                        'morning_feels_like': row['morning']['feels_like'] if row['morning'] is not None else None,
                        'morning_soil_temperature': row['morning']['soil_temperature'] if row['morning'] is not None else None,
                        'morning_wind_chill': row['morning']['wind_chill'] if row['morning'] is not None else None,
                        'morning_dew_point': row['morning']['dew_point'] if row['morning'] is not None else None,
                        'morning_surface_temperature': row['morning']['surface_temperature'] if row['morning'] is not None else None,
                        
                        'morning_wind_speed': row['morning']['wind']['speed'] if row['morning'] is not None else None,
                        'morning_wind_gusts': row['morning']['wind']['gusts'] if row['morning'] is not None else None,
                        'morning_wind_dir': row['morning']['wind']['dir'] if row['morning'] is not None else None,
                        'morning_wind_angle': row['morning']['wind']['angle'] if row['morning'] is not None else None,
                        
                        'morning_cloud_cover_total': row['morning']['cloud_cover']['total'] if row['morning'] is not None else None,
                        'morning_cloud_cover_low': row['morning']['cloud_cover']['low'] if row['morning'] is not None else None,
                        'morning_cloud_cover_middle': row['morning']['cloud_cover']['middle'] if row['morning'] is not None else None,
                        'morning_cloud_cover_high': row['morning']['cloud_cover']['high'] if row['morning'] is not None else None,
                        
                        'morning_pressure': row['morning']['pressure'] if row['morning'] is not None else None,
                        
                        'morning_precipitation_total': row['morning']['precipitation']['total'] if row['morning'] is not None else None,
                        'morning_precipitation_type': row['morning']['precipitation']['type'] if row['morning'] is not None else None,
                        
                        'morning_probability_precipitation': row['morning']['probability']['precipitation'] if row['morning'] is not None else None,
                        'morning_probability_storm': row['morning']['probability']['storm'] if row['morning'] is not None else None,
                        'morning_probability_freeze': row['morning']['probability']['freeze'] if row['morning'] is not None else None,
                        
                        'morning_ozone': row['morning']['ozone'] if row['morning'] is not None else None,
                        'morning_humidity': row['morning']['humidity'] if row['morning'] is not None else None,
                        'morning_snow_depth': row['morning']['snow_depth'] if row['morning'] is not None else None,
                        'morning_visibility': row['morning']['visibility'] if row['morning'] is not None else None,

                        'afternoon_weather': row['afternoon']['weather'] if row['afternoon'] is not None else None,
                        'afternoon_icon': row['afternoon']['icon'] if row['afternoon'] is not None else None,
                        'afternoon_temperature': row['afternoon']['temperature'] if row['afternoon'] is not None else None,
                        'afternoon_feels_like': row['afternoon']['feels_like'] if row['afternoon'] is not None else None,
                        'afternoon_soil_temperature': row['afternoon']['soil_temperature'] if row['afternoon'] is not None else None,
                        'afternoon_wind_chill': row['afternoon']['wind_chill'] if row['afternoon'] is not None else None,
                        'afternoon_dew_point': row['afternoon']['dew_point'] if row['afternoon'] is not None else None,
                        'afternoon_surface_temperature': row['afternoon']['vsurface_temperature'] if row['afternoon'] is not None else None,
                        
                        'afternoon_wind_speed': row['afternoon']['wind']['speed'] if row['afternoon'] is not None else None,
                        'afternoon_wind_gusts': row['afternoon']['wind']['gusts'] if row['afternoon'] is not None else None,
                        'afternoon_wind_dir': row['afternoon']['wind']['dir'] if row['afternoon'] is not None else None,
                        'afternoon_wind_angle': row['afternoon']['wind']['angle'] if row['afternoon'] is not None else None,
                        
                        'afternoon_cloud_cover_total': row['afternoon']['cloud_cover']['total'] if row['afternoon'] is not None else None,
                        'afternoon_cloud_cover_low': row['afternoon']['cloud_cover']['low'] if row['afternoon'] is not None else None,
                        'afternoon_cloud_cover_middle': row['afternoon']['cloud_cover']['middle'] if row['afternoon'] is not None else None,
                        'afternoon_cloud_cover_high': row['afternoon']['cloud_cover']['high'] if row['afternoon'] is not None else None,
                        
                        'afternoon_pressure': row['afternoon']['pressure'] if row['afternoon'] is not None else None,
                        
                        'afternoon_precipitation_total': row['afternoon']['precipitation']['total'] if row['afternoon'] is not None else None,
                        'afternoon_precipitation_type': row['afternoon']['precipitation']['type'] if row['afternoon'] is not None else None,
                        
                        'afternoon_probability_precipitation': row['afternoon']['probability']['precipitation'] if row['afternoon'] is not None else None,
                        'afternoon_probability_storm': row['afternoon']['probability']['storm'] if row['afternoon'] is not None else None,
                        'afternoon_probability_freeze': row['afternoon']['probability']['freeze'] if row['afternoon'] is not None else None,
                        
                        'afternoon_ozone': row['afternoon']['ozone'] if row['afternoon'] is not None else None,
                        'afternoon_humidity': row['afternoon']['humidity'] if row['afternoon'] is not None else None,
                        'afternoon_snow_depth': row['afternoon']['snow_depth'] if row['afternoon'] is not None else None,
                        'afternoon_visibility': row['afternoon']['visibility'] if row['afternoon'] is not None else None,

                        'evening_weather': row['evening']['weather'] if row['evening'] is not None else None,
                        'evening_icon': row['evening']['icon'] if row['evening'] is not None else None,
                        'evening_temperature': row['evening']['temperature'] if row['evening'] is not None else None,
                        'evening_feels_like': row['evening']['feels_like'] if row['evening'] is not None else None,
                        'evening_soil_temperature': row['evening']['soil_temperature'] if row['evening'] is not None else None,
                        'evening_wind_chill': row['evening']['wind_chill'] if row['evening'] is not None else None,
                        'evening_dew_point': row['evening']['dew_point'] if row['evening'] is not None else None,
                        'evening_surface_temperature': row['evening']['vsurface_temperature'] if row['evening'] is not None else None,
                        
                        'evening_wind_speed': row['evening']['wind']['speed'] if row['evening'] is not None else None,
                        'evening_wind_gusts': row['evening']['wind']['gusts'] if row['evening'] is not None else None,
                        'evening_wind_dir': row['evening']['wind']['dir'] if row['evening'] is not None else None,
                        'evening_wind_angle': row['evening']['wind']['angle'] if row['evening'] is not None else None,
                        
                        'evening_cloud_cover_total': row['evening']['cloud_cover']['total'] if row['evening'] is not None else None,
                        'evening_cloud_cover_low': row['evening']['cloud_cover']['low'] if row['evening'] is not None else None,
                        'evening_cloud_cover_middle': row['evening']['cloud_cover']['middle'] if row['evening'] is not None else None,
                        'evening_cloud_cover_high': row['evening']['cloud_cover']['high'] if row['evening'] is not None else None,
                        
                        'evening_pressure': row['evening']['pressure'] if row['evening'] is not None else None,
                        
                        'evening_precipitation_total': row['evening']['precipitation']['total'] if row['evening'] is not None else None,
                        'evening_precipitation_type': row['evening']['precipitation']['type'] if row['evening'] is not None else None,
                        
                        'evening_probability_precipitation': row['evening']['probability']['precipitation'] if row['evening'] is not None else None,
                        'evening_probability_storm': row['evening']['probability']['storm'] if row['evening'] is not None else None,
                        'evening_probability_freeze': row['evening']['probability']['freeze'] if row['evening'] is not None else None,
                        
                        'evening_ozone': row['evening']['ozone'] if row['evening'] is not None else None,
                        'evening_humidity': row['evening']['humidity'] if row['evening'] is not None else None,
                        'evening_snow_depth': row['evening']['snow_depth'] if row['evening'] is not None else None,
                        'evening_visibility': row['evening']['visibility'] if row['evening'] is not None else None,

                        'astro_sun_rise': row['astro']['sun']['rise'] if row['astro'] is not None else None,
                        'astro_sun_set': row['astro']['sun']['set'] if row['astro'] is not None else None,
                        'astro_sun_always_up': row['astro']['sun']['always_up'] if row['astro'] is not None else None,
                        'astro_sun_always_down': row['astro']['sun']['always_down'] if row['astro'] is not None else None,

                        'astro_moon_phase': row['astro']['moon']['phase'] if row['astro'] is not None else None,
                        'astro_moon_rise': row['astro']['moon']['rise'] if row['astro'] is not None else None,
                        'astro_moon_set': row['astro']['moon']['set'] if row['astro'] is not None else None,
                        'astro_moon_always_up': row['astro']['moon']['always_up'] if row['astro'] is not None else None,
                        'astro_moon_always_down': row['astro']['moon']['always_down'] if row['astro'] is not None else None,
                        
                        'statistics_temperature_avg': row['statistics']['temperature']['avg'] if row['statistics'] is not None else None,
                        'statistics_temperature_avg_min': row['statistics']['temperature']['avg_min'] if row['statistics'] is not None else None,
                        'statistics_temperature_avg_max': row['statistics']['temperature']['avg_max'] if row['statistics'] is not None else None,
                        'statistics_temperature_record_min': row['statistics']['temperature']['record_min'] if row['statistics'] is not None else None,
                        'statistics_temperature_record_max': row['statistics']['temperature']['record_max'] if row['statistics'] is not None else None,

                        'statistics_wind_avg_speed': row['statistics']['wind']['avg_speed'] if row['statistics'] is not None else None,
                        'statistics_wind_avg_angle': row['statistics']['wind']['avg_angle'] if row['statistics'] is not None else None,
                        'statistics_wind_avg_dir': row['statistics']['wind']['avg_dir'] if row['statistics'] is not None else None,
                        'statistics_wind_max_speed': row['statistics']['wind']['max_speed'] if row['statistics'] is not None else None,
                        'statistics_wind_max_gust': row['statistics']['wind']['max_gust'] if row['statistics'] is not None else None,

                        'statistics_precipitation_avg': row['statistics']['precipitation']['avg'] if row['statistics'] is not None else None,
                        'statistics_precipitation_probability': row['statistics']['precipitation']['probability'] if row['statistics'] is not None else None,
                    }

                    obj, created = WeatherDataMeteosource.objects.update_or_create(
                        place_id=pp.place_id, 
                        day=row['day'], 
                        defaults=defaults
                    )
                    print("data updated or created of ===> ", pp.place_id)
            else:
                print("Error occurs at ===> ", pp.place_id)
                pass
        
        write_log_new(log_txt="Meteosource data inserted at: " + formatted_ts())
        print("Meteosource data inserted at: " + formatted_ts())

    except Exception as exp:
        write_log_new(log_txt="Error at: " + formatted_ts())
        print("Error at: " + formatted_ts())


@shared_task
def update_prediction_data_with_meteosource_data():
    try:
        places = PointsPlace.objects.all()
        start_date = datetime.today()

        for day in range(30):
            current_date = start_date + timedelta(days=day)
            str_current_date = current_date.strftime("%Y-%m-%d")

            for place in places:
                meteosource_data = WeatherDataMeteosource.objects.filter(place_id=place.place_id, day=str_current_date)
                prediction_data = WeatherDataPrediction.objects.filter(station=place.name, c_date=str_current_date)
                
                if prediction_data:
                    for prediction in prediction_data:
                        if prediction.data_type == 'temperature':
                            for meteosource in meteosource_data:
                                prediction.value = meteosource.all_day_temperature
                                prediction.value_lower = meteosource.all_day_temperature_min
                                prediction.value_upper = meteosource.all_day_temperature_max
                                prediction.save()
                        elif prediction.data_type == 'humidity':
                            for meteosource in meteosource_data:
                                prediction.value = meteosource.all_day_humidity
                                prediction.save()
                        else:
                            for meteosource in meteosource_data:
                                prediction.value = meteosource.all_day_precipitation_total
                                prediction.save()

            print("current date ===> ", str_current_date)

        write_log_new(log_txt="Meteosource data updated at: " + formatted_ts())
        print("Meteosource data updated at: " + formatted_ts())

    except Exception as exp:
        print("Errors is ===> ", str((exp)))
        write_log_new(log_txt="Errors are : " + str(exp))
