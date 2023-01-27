from typing import List


class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float,
                 ) -> None:

        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:

        message = (f'Тип тренировки: {self.training_type}; '
                   f'Длительность: {self.duration:.3f} ч.; '
                   f'Дистанция: {self.distance:.3f} км; '
                   f'Ср. скорость: {self.speed:.3f} км/ч; '
                   f'Потрачено ккал: {self.calories:.3f}.')

        return message


class Training:
    """Базовый класс тренировки."""
    LEN_STEP = 0.65
    M_IN_KM = 1000
    HOUR_TO_MIN = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:

        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        result = self.action * self.LEN_STEP / self.M_IN_KM
        return result

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        result = self.get_distance() / self.duration
        return result

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        message: InfoMessage = InfoMessage(self.__class__.__name__,
                                           self.duration,
                                           self.get_distance(),
                                           self.get_mean_speed(),
                                           self.get_spent_calories())

        return message


class Running(Training):
    training_type = 'Бег'

    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79

    def get_spent_calories(self):

        result = ((self.CALORIES_MEAN_SPEED_MULTIPLIER * self.get_mean_speed()
                  + self.CALORIES_MEAN_SPEED_SHIFT) * self.weight
                  / self.M_IN_KM * (self.duration * self.HOUR_TO_MIN))

        return result


class SportsWalking(Training):
    training_type = 'Спортивная ходьба'

    COEFFICIENT_FOR_WEIGHT = 0.035
    COEFFICIENT_FOR_WEIGHT_SEC = 0.029
    SPEED_KM_IN_M = 0.278
    SM_IN_M = 100

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float
                 ) -> None:

        super().__init__(action,
                         duration,
                         weight)

        self.height = height

    def get_spent_calories(self):

        sqrt_mean_speed_in_m = (self.get_mean_speed()
                                * self.SPEED_KM_IN_M) ** 2

        result = (
            (self.COEFFICIENT_FOR_WEIGHT * self.weight
             + ((sqrt_mean_speed_in_m / (self.height / self.SM_IN_M))
                * self.COEFFICIENT_FOR_WEIGHT_SEC * self.weight))
            * (self.duration * self.HOUR_TO_MIN))

        return result


class Swimming(Training):
    training_type = 'Плавание'

    LEN_STEP = 1.38
    AVG_SPEED_OFFSET = 1.1
    SWM_SPEED_MULT = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: int) -> None:

        super().__init__(action,
                         duration,
                         weight)

        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:

        result = (self.length_pool * self.count_pool
                  / self.M_IN_KM / self.duration)
        return result

    def get_spent_calories(self):

        result = ((self.get_mean_speed() + self.AVG_SPEED_OFFSET)
                  * self.SWM_SPEED_MULT * self.weight * self.duration)
        return result


def read_package(workout_type: str, data: List[int]) -> Training:
    """Прочитать данные полученные от датчиков."""

    WORKOUT_TYPES: dict = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }

    train_class = WORKOUT_TYPES[workout_type](*data)
    return train_class


def main(training: Training) -> None:

    info: InfoMessage = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
