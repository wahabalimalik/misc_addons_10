# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests

class OdooOverpass(models.Model):
    _name = 'odoo.overpass'

    name = fields.Many2one('osm.city',"City")
    amenity = fields.Selection([
    	('bar' , 'Bar'),
		('bbq' , 'Bbq'),
		('biergarten' , 'Biergarten'),
		('cafe' , 'Cafe'),
		('drinking_water' , 'Drinking_water'),
		('fast_food' , 'Fast_food'),
		('food_court' , 'Food_court'),
		('ice_cream' , 'Ice_cream'),
		('pub' , 'Pub'),
		('restaurant' , 'Restaurant'),
		('college' , 'College'),
		('kindergarten' , 'Kindergarten'),
		('library' , 'Library'),
		('public_bookcase' , 'Public_bookcase'),
		('school' , 'School'),
		('music_school' , 'Music_school'),
		('driving_school' , 'Driving_school'),
		('language_school' , 'Language_school'),
		('university' , 'University'),
		('bicycle_parking' , 'Bicycle_parking'),
		('bicycle_repair_station' , 'Bicycle_repair_station'),
		('bicycle_rental' , 'Bicycle_rental'),
		('boat_rental' , 'Boat_rental'),
		('boat_sharing' , 'Boat_sharing'),
		('bus_station' , 'Bus_station'),
		('car_rental' , 'Car_rental'),
		('car_sharing' , 'Car_sharing'),
		('car_wash' , 'Car_wash'),
		('charging_station' , 'Charging_station'),
		('ferry_terminal' , 'Ferry_terminal'),
		('fuel' , 'Fuel'),
		('grit_bin' , 'Grit_bin'),
		('motorcycle_parking' , 'Motorcycle_parking'),
		('parking' , 'Parking'),
		('parking_entrance' , 'Parking_entrance'),
		('parking_space' , 'Parking_space'),
		('taxi' , 'Taxi'),
		('atm' , 'Atm'),
		('bank' , 'Bank'),
		('bureau_de_change' , 'Bureau_de_change'),
		('baby_hatch' , 'Baby_hatch'),
		('clinic' , 'Clinic'),
		('dentist' , 'Dentist'),
		('doctors' , 'Doctors'),
		('hospital' , 'Hospital'),
		('nursing_home' , 'Nursing_home'),
		('pharmacy' , 'Pharmacy'),
		('social_facility' , 'Social_facility'),
		('veterinary' , 'Veterinary'),
		('blood_donation' , 'Blood_donation'),
		('arts_centre' , 'Arts_centre'),
		('brothel' , 'Brothel'),
		('casino' , 'Casino'),
		('cinema' , 'Cinema'),
		('community_centre' , 'Community_centre'),
		('fountain' , 'Fountain'),
		('gambling' , 'Gambling'),
		('nightclub' , 'Nightclub'),
		('planetarium' , 'Planetarium'),
		('social_centre' , 'Social_centre'),
		('stripclub' , 'Stripclub'),
		('studio' , 'Studio'),
		('swingerclub' , 'Swingerclub'),
		('theatre' , 'Theatre'),
		('animal_boarding' , 'Animal_boarding'),
		('animal_shelter' , 'Animal_shelter'),
		('baking_oven' , 'Baking_oven'),
		('bench' , 'Bench'),
		('clock' , 'Clock'),
		('courthouse' , 'Courthouse'),
		('coworking_space' , 'Coworking_space'),
		('crematorium' , 'Crematorium'),
		('crypt' , 'Crypt'),
		('dive_centre' , 'Dive_centre'),
		('dojo' , 'Dojo'),
		('embassy' , 'Embassy'),
		('fire_station' , 'Fire_station'),
		('game_feeding' , 'Game_feeding'),
		('grave_yard' , 'Grave_yard'),
		('hunting_stand' , 'Hunting_stand'),
		('internet_cafe' , 'Internet_cafe'),
		('kneipp_water_cure' , 'Kneipp_water_cure'),
		('marketplace' , 'Marketplace'),
		('photo_booth' , 'Photo_booth'),
		('place_of_worship' , 'Place_of_worship'),
		('police' , 'Police'),
		('post_box' , 'Post_box'),
		('post_office' , 'Post_office'),
		('prison' , 'Prison'),
		('public_bath' , 'Public_bath'),
		('ranger_station' , 'Ranger_station'),
		('recycling' , 'Recycling'),
		('rescue_station' , 'Rescue_station'),
		('sanitary_dump_station' , 'Sanitary_dump_station'),
		('shelter' , 'Shelter'),
		('shower' , 'Shower'),
		('table' , 'Table'),
		('telephone' , 'Telephone'),
		('toilets' , 'Toilets'),
		('townhall' , 'Townhall'),
		('vending_machine' , 'Vending_machine'),
		('waste_basket' , 'Waste_basket'),
		('waste_disposal' , 'Waste_disposal'),
		('waste_transfer_station' , 'Waste_transfer_station'),
		('watering_place' , 'Watering_place'),
		('water_point' , 'Water_point')
    	])
    results = fields.One2many('osm.rec','rec_id')

    @api.multi
    def action_confirm(self):
    	if self.name and self.amenity:
    		requests.get('http://localhost:8080/?w=amenity%3Dshop+in+kariakoo&R')

    		# kk.open_page('http://overpass-turbo.eu/?w=amenity%3Dshop+in+kariakoo&R')

class OsmCity(models.Model):
    _name = 'osm.city'
    name = fields.Char()

class OsmRec(models.Model):
    _name = 'osm.rec'
    name = fields.Char()
    amenity = fields.Char()
    rec_id = fields.Many2one('odoo.overpass')