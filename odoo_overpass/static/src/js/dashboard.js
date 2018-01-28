odoo.define('osm.osm', function (require) {
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

var Dashboards = Widget.extend({
    template: 'DashboardsMain',

    init: function(parent, data){
        this.all_dashboards = ['apps'];
        return this._super.apply(this, arguments);
    },

    start: function(){
        return this.load(this.all_dashboards);
    },

    load: function(dashboards){
        var self = this;
        var loading_done = new $.Deferred();

        var all_dashboards_defs = [];
        _.each(dashboards, function(dashboard) {
            var dashboard_def = self['load_' + dashboard]('apps');
            if (dashboard_def) {
                all_dashboards_defs.push(dashboard_def);
            }
        });

            // Resolve loading_done when all dashboards defs are resolved
            $.when.apply($, all_dashboards_defs).then(function() {
                loading_done.resolve();
            });

        return loading_done;
    },

    load_apps: function(){
        return  new DashboardsApps(this).replace(this.$('.o_my_control_panel_apps'));
    },
});

var DashboardsApps = Widget.extend({

    template: 'DashboardsApps',

    // events: {
    //     'click .o_browse_apps': 'on_new_apps',
    //     'click .o_confirm_upgrade': 'confirm_upgrade',
    // },

    init: function(parent){
        this.parent = parent;
        return this._super.apply(this, arguments);
    },

    start: function() {
        this._super.apply(this, arguments);
        if (odoo.db_info && _.last(odoo.db_info.server_version_info) !== 'e') {
            $(QWeb.render("DashboardsEnterprise")).appendTo(this.$el);
        }
    },

    on_new_apps: function(){
        this.do_action('base.open_module_tree');
    },

    confirm_upgrade: function() {
        // framework.redirect("https://www.odoo.com/odoo-enterprise/upgrade?num_users=" + (this.data.enterprise_users || 1));
        framework.redirect("/web/underdevelop");
    },
});

core.action_registry.add('osm.main', Dashboards);

return {
    Dashboards: Dashboards,
};

});
