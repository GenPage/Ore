from ore.core.regexs import EXTENDED_URL_REGEX, TRIM_URL_REGEX
from django.conf.urls import patterns, url, include
from ore.flags.views import VersionsFlagView
from ore.projects.views import FileDownloadView
from ore.versions.views import VersionsNewView, ProjectsVersionsListView, VersionsDetailView

urlpatterns = patterns(
    '',
    url(r'^(?P<namespace>' + EXTENDED_URL_REGEX + ')/(?P<project>' + EXTENDED_URL_REGEX + ')/', include(patterns('',

        url(r'^upload/$', VersionsNewView.as_view(), name='repo-versions-new'),
        url(r'^versions/$', ProjectsVersionsListView.as_view(),
            name='repo-versions-list'),

        url(r'^versions/(?P<version>' + EXTENDED_URL_REGEX + ')/', include(patterns('',
            url(r'^$', VersionsDetailView.as_view(),
                name='repo-versions-detail'),
            url(r'^manage/$', VersionsDetailView.as_view(),
                name='repo-versions-manage'),
            url(r'^flag/$', VersionsFlagView.as_view(),
                name='repo-versions-flag'),
            url(r'^delete/$', VersionsDetailView.as_view(),
                name='repo-versions-delete'),
            url(r'^(?P<file>' + TRIM_URL_REGEX + ')(?P<file_extension>\.[a-zA-Z0-9-]+)',
                FileDownloadView.as_view(),
                name='repo-files-download'),
        )))
    )))
)
