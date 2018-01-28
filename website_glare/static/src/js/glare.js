/******************************************
-   PREPARE PLACEHOLDER FOR SLIDER  -
******************************************/
var revapi;
jQuery(document).ready(function()
{
revapi = jQuery("#rev_slider").revolution(
{
sliderType: "standard",
sliderLayout: "auto",
delay: 9000,
navigation:
{
arrows:
{
enable: true
}
},
gridwidth: 1230,
gridheight: 680
});
}); /*ready*/

$(function() {
$('a[href*="#"]:not([href="#"])').click(function() {
if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
var target = $(this.hash);
target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
if (target.length) {
$('html, body').animate({
scrollTop: target.offset().top
}, 2000);
return false;
}
}
});
});