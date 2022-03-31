from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify

from nautobot.dcim.models import Device, DeviceRole, DeviceType, Manufacturer, Site
from nautobot.extras.models import Status, CustomField
from nautobot.extras.jobs import *

import time



class CustomFieldCreation(Job):

    class Meta:
        name = "Custom Field Creation"
        description = "Provision a new branch site"
        field_order = ['site_name', 'custom_field']

    site_name = StringVar(description="Name of the new site")
    cf_name = StringVar(description="Name of the new site")

    def run(self, data, commit):
        STATUS_PLANNED = Status.objects.get(slug='active')



        site_ct = ContentType.objects.get_for_model(Site)
        cf = CustomField.objects.create(name=data['cf_name'], type="text")
        cf.content_types.add(site_ct)

        site = Site.objects.create(
            name=data['site_name'],
            slug=slugify(data['site_name']),
            status=STATUS_PLANNED,
            _custom_field_data={data['cf_name']: "some-value-is-okay"},
        )
        self.log_success(obj=site, message="Created new site")
        self.log_info(obj=site, message="Creating Custom Fields")

        # site.cf["cf2"] = "some-value"
        # site.cf.validated_save()

        output = ["device creation", "device okay"]

        return '\n'.join(output)

    def post_run(self):
        self.log_info(message="POST RUN REACHED INFO")

        # raise Exception("Exception raised")


# docker cp ../custom-filed.py nautobot_celery_worker_1:/opt/nautobot/jobs/
# docker cp ../custom-filed.py nautobot_nautobot_1:/opt/nautobot/jobs/
# docker cp ../device_validation.py nautobot_celery_worker_1:/opt/nautobot/jobs/

