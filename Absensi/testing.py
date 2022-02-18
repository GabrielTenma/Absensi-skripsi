import App.delivery.Api as api
import App.config.variable.ApplicationConstant as appConfig
import App.util.CommonUtil as util

# TESTING CALL API x
IMAGE_SAMPLE = util.checkPath("App/assets/kocak.jpeg")
print(api.matchImagePerson('20', IMAGE_SAMPLE))