import App.delivery.Api as api
import App.config.variable.ApplicationConstant as appConfig

# TESTING CALL API
print(api.matchImagePerson('20', appConfig.TAKE_PICTURE_FILENAME))