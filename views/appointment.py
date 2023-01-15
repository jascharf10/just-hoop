import arrow

from flask.views import MethodView
from flask import render_template, request, redirect, url_for

from database import db
from models.appointment import Appointment, Location
from forms.new_appointment import NewAppointmentForm


class AppointmentResourceDelete(MethodView):
    def post(self, id):
        appt = db.session.query(Appointment).filter_by(id=id).one()
        db.session.delete(appt)
        db.session.commit()

        return redirect(url_for('appointment.index'), code=303)


class AppointmentResourceCreate(MethodView):
    def post(self):
        #available_locations=db.session.query(Location.location).distinct()
        #Now forming the list of tuples for SelectField
        #locations_list=[(i.location) for i in available_locations]
        form = NewAppointmentForm(request.form)
        form.location.choices = []
        for location in Location.query.distinct(Location.location):
            form.location.choices.append(location.location)
        #passing group_list to the form
        #form.location.choices = locations_list
        #form.location.choices = [x.location for x in db.session.query(Location.location).distinct()]
        #form.location.choices = [x.location for x in db.session.query(
        #                                              Location.location).distinct()]
        if form.validate():
            from tasks import send_sms_reminder

            for i in range(len(form.data['location'])):
        

            #for x in form.data['location']:
            #print(form.data['location'][0])

                appt = Appointment(
                    name=form.data['name'],
                    phone_number=form.data['phone_number'],
                    spots_trigger=form.data['spots_trigger'],
                    location=form.data['location'][i],
                #location=form.location.data,


                #location=form.data['location'].location,
                )
                print(form.data['location'][i])

            #appt.time = arrow.get(appt.time, appt.timezone).to('utc').naive

                db.session.add(appt)
                db.session.commit()
            # send_sms_reminder.apply_async(
            #     args=[appt.id], eta=appt.get_notification_time()
            # )

            return redirect(url_for('appointment.index'), code=303)
        else:
            return render_template('appointments/new.html', form=form), 400


class AppointmentResourceIndex(MethodView):
    def get(self):
        all_appointments = db.session.query(Appointment).all()
        return render_template('appointments/index.html', appointments=all_appointments)


class AppointmentFormResource(MethodView):
    def get(self):
        form = NewAppointmentForm()
        form.location.choices = []
        for location in Location.query.distinct(Location.location):
            form.location.choices.append(location.location)
        all_games = db.session.query(Location).all()
        return render_template('appointments/new.html', form=form, games=all_games)

# class LocationIndex(MethodView):
#     def get(self):
#         all_locations = db.session.query(Location).all()
#         # #Now forming the list of tuples for SelectField
#         # groups_list=[(i.location_id, i.location) for i in all_locations]
#         # form=NewAppointmentForm()
#         # #passing group_list to the form
#         # form.location_id.choices = all_locations
#         # if form.validate_on_submit():
#         #     name=Name(form.name.data,form.location_id.data)
#         #     db.session.add(name)
#         #     db.session.commit()
#         #     return "New name added"
#         return render_template('appointments/new.html', locations=all_locations)
