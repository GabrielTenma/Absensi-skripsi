import App.delivery.Api as api
import App.config.variable.ApplicationConstant as appConfig
import App.util.CommonUtil as util

# TESTING CALL API
IMAGE_SAMPLE = util.checkPath(appConfig.TAKE_PICTURE_FILENAME)
print(api.matchImagePerson('20', IMAGE_SAMPLE))