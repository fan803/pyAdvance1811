
(function($) {
	$.fn.sliders = function(options) {
		var opts = $.extend( {}, $.fn.sliders.defaults, options);
		var that = this;
		var left=false;
		var right=true;
		var scrollTimeOut=null;
		var Z_MenuList = $(that).find('.items');
		var mList = $(Z_MenuList).find('ul li');
		var isIE = navigator.userAgent.indexOf('MSIE') != -1;
		//显示
		$(that).find('a.bleft').on('click',function(){
			if(left){
				mList.find('p').removeClass('scroll');
				$(this).parent().removeClass('bleft').addClass('bright');
				left=false;
				right=true;
			}
		})
		$(that).find('a.bright').on('click',function(){
			if(right){
				mList.find('p').addClass('scroll');
				$(this).parent().removeClass('bright').addClass('bleft');
				left=true;
				right=false;
			}
		});
		//阻止冒泡
		mList.each(function(index,elem){	
			 $(this).on('mouseover',function(event){
				event.stopPropagation();
				$(that).children('.box').hide().children('.hide').hide();
				$(that).children('.box').show().css({left:170}).stop(true,false).animate({left:190}).children('.hide').eq(index).show();				  
			 })					
		})
		$(document).on('mouseover',function(){
			$(that).children('.box').hide().children('.hide').hide();								
		})
		$(that).children('.box').on('mouseover',function(event){
			event.stopPropagation();								
		})
		
	};
	// 默认配置项
	$.fn.sliders.defaults = {
		fTop: 60, // 距离顶部距离
		cTop: 100, // 滚动条滚动多少像素后开始折叠的高度
		unitHeight: 80// 每滚动多少距离折叠一个
	};
})(jQuery);