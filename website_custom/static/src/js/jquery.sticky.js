!function(a){var b={topSpacing:0,bottomSpacing:0,className:"is-sticky",wrapperClassName:"sticky-wrapper",center:!1,getWidthFrom:""},c=a(window),d=a(document),e=[],f=c.height(),g=function(){for(var b=c.scrollTop(),g=d.height(),h=g-f,i=b>h?h-b:0,j=0;j<e.length;j++){var k=e[j],l=k.stickyWrapper.offset().top,m=l-k.topSpacing-i;if(b<=m)null!==k.currentTop&&(k.stickyElement.css("position","").css("top",""),k.stickyElement.parent().removeClass(k.className),k.currentTop=null);else{var n=g-k.stickyElement.outerHeight()-k.topSpacing-k.bottomSpacing-b-i;n<0?n+=k.topSpacing:n=k.topSpacing,k.currentTop!=n&&(k.stickyElement.css("position","fixed").css("top",n),"undefined"!=typeof k.getWidthFrom&&k.stickyElement.css("width",a(k.getWidthFrom).width()),k.stickyElement.parent().addClass(k.className),k.currentTop=n)}}},h=function(){f=c.height()},i={init:function(c){var d=a.extend(b,c);return this.each(function(){var b=a(this),c=b.attr("id"),f=a("<div></div>").attr("id",c+"-sticky-wrapper").addClass(d.wrapperClassName);b.wrapAll(f),d.center&&b.parent().css({width:b.outerWidth(),marginLeft:"auto",marginRight:"auto"}),"right"==b.css("float")&&b.css({float:"none"}).parent().css({float:"right"});var g=b.parent();g.css("height",b.outerHeight()),e.push({topSpacing:d.topSpacing,bottomSpacing:d.bottomSpacing,stickyElement:b,currentTop:null,stickyWrapper:g,className:d.className,getWidthFrom:d.getWidthFrom})})},update:g,unstick:function(b){return this.each(function(){var b=a(this);removeIdx=-1;for(var c=0;c<e.length;c++)e[c].stickyElement.get(0)==b.get(0)&&(removeIdx=c);removeIdx!=-1&&(e.splice(removeIdx,1),b.unwrap(),b.removeAttr("style"))})}};window.addEventListener?(window.addEventListener("scroll",g,!1),window.addEventListener("resize",h,!1)):window.attachEvent&&(window.attachEvent("onscroll",g),window.attachEvent("onresize",h)),a.fn.sticky=function(b){return i[b]?i[b].apply(this,Array.prototype.slice.call(arguments,1)):"object"!=typeof b&&b?void a.error("Method "+b+" does not exist on jQuery.sticky"):i.init.apply(this,arguments)},a.fn.unstick=function(b){return i[b]?i[b].apply(this,Array.prototype.slice.call(arguments,1)):"object"!=typeof b&&b?void a.error("Method "+b+" does not exist on jQuery.sticky"):i.unstick.apply(this,arguments)},a(function(){setTimeout(g,0)})}(jQuery);