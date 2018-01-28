odoo.define('odoo_overpass', function (require) {
"use strict";

var core = require('web.core');
var Widget = require('web.Widget');
var Model = require('web.Model');
var session = require('web.session');
var PlannerCommon = require('web.planner.common');
var framework = require('web.framework');
var webclient = require('web.web_client');
var PlannerDialog = PlannerCommon.PlannerDialog;

var QWeb = core.qweb;
var _t = core._t;

var Dashboard = Widget.extend({
	template: 'OverpassDashboard',

    start: function() {
    	// alert("kkkkkkkkkkkkkk");
    	console.log('hello world');
    },
});
core.action_registry.add("odoo_overpass.dashboard", Dashboard);

return {
    Dashboard: Dashboard,
};

});