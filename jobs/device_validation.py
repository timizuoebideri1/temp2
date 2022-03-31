from django.utils.text import slugify

from nautobot.dcim.models import Device, DeviceRole, DeviceType, Manufacturer, Site
from nautobot.extras.models import Status
from nautobot.extras.jobs import *

import time



class NewBranch(Job):

    class Meta:
        name = "New Branch"
        description = "Provision a new branch site"
        field_order = ['site_name']

    site_name = StringVar(
        description="Name of the new site"
    )

    def run(self, data, commit):
        STATUS_PLANNED = Status.objects.get(slug='planned')

        # Create the new site
        site = Site(
            name=data['site_name'],
            slug=slugify(data['site_name']),
            status=STATUS_PLANNED,
        )
        site.validated_save()
        self.log_success(obj=site, message="Created new site")
        self.log_info(obj=site, message="Moving to post run")

        output = ["device creation", "device okay"]

        return '\n'.join(output)

    def post_run(self):
        self.log_info(message="POST RUN REACHED INFO")

        raise Exception("Exception raised")

