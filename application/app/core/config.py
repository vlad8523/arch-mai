from app.core.app_settings import AppSettings


appSettings = AppSettings()


def get_app_settings() -> AppSettings:
    print(appSettings.database_url)
    return appSettings