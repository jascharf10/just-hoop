from views.appointment import (
    AppointmentResourceIndex,
    AppointmentResourceCreate,
    AppointmentResourceDelete,
    AppointmentFormResource,
    LoginResource
    )


def init_views(app):
    app.add_url_rule('/', view_func=AppointmentResourceIndex.as_view('appointment.index'))
    app.add_url_rule(
        '/appointment', view_func=AppointmentResourceCreate.as_view('appointment.create')
    )
    app.add_url_rule(
        '/appointment/<int:id>/delete',
        view_func=AppointmentResourceDelete.as_view('appointment.delete'),
    )
    app.add_url_rule(
        '/appointment/new', view_func=AppointmentFormResource.as_view('appointment.new'),
    )
    app.add_url_rule(
        '/login', view_func=LoginResource.as_view('login'),

    )
    # app.add_url_rule(
    #     '/appointment/new', view_func=LocationIndex.as_view('appointment.new')
    # )
