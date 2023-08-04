# import logging
#
#
# def before_all(context):
#      print("Executing before all")
#
# def before_feature(context, feature):
#      print("Before feature\n")
#      # Create logger
#      context.logger = logging.getLogger('automation_tests')
#      context.logger.setLevel(logging.DEBUG)
#
# def before_scenario(context, scenario):
#     print("User data:", context.config.userdata)
#
# def after_scenario(context, scenario):
#     print("scenario status" + scenario.status)
#     context.browser.quit()
#
# def after_feature(context, feature):
#             print("\nAfter Feature")
#
# def after_all(context):
# 	print("Executing after all")