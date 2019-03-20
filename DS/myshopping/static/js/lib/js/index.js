$(function(){
	
	$('.top-left').hover(
		
		function(){$('.top-left-hide').css('display','block');$(this).css({'background':'#fff','color':'red'})},
		function(){$('.top-left-hide').css('display','none');$(this).css({'background':'#f7f7f7','color':'#666'})}
	);
	
	$('.top-left-hide span').hover(
		function(){$(this).css('background','#e2e2e2')},
		function(){$(this).css('background','#fff')}
	);
	
	$('.top-right-show').hover(
		function(){$(this).children().css({'display':'inline-block'});$(this).css({'background':'#fff','color':'red'})},
		function(){$('.top-right-show div').css('display','none');$(this).css({'background':'#f7f7f7','color':'#666'})}
	);
	$('.top-right-show div span').hover(
		function(){$(this).css('background','#e2e2e2')},
		function(){$(this).css('background','#fff')}
	);
	$('.top-right-show div dd').hover(
		function(){$(this).css('background','#e2e2e2')},
		function(){$(this).css('background','#fff')}
	);
	//nav 下的li划过的效果
	$('.nav-right li').hover(
		function(){$(this).children('a').css({'color':'red'});$(this).children('span').css({'bottom':'-3','display':'inline-block'}).animate({top:32})},
		function(){$(this).children('a').css('color','#000');$(this).children('span').css({'display':'none'})}
	);
	//banner
	$(function(){
		var Index=0;
		var oTimer=null;
		Is=true;
		function move(){
			Index++;
			if(Index>=6){Index=0}
			Is=false;
			var $Lis=$('.btn-lists li')
			$Lis.eq(Index).addClass('active').siblings().removeClass('active');
			$('.banner-cont img').attr({src:'img/banner'+(Index+1)+'.jpg'}).stop(true,false).fadeOut(10).fadeIn();
			
		};
		function auto(){
			oTimer=setInterval(function(){move()},2000)
		};
		auto();
		$('.banner-cont').hover(
			function(){clearInterval(oTimer);$('.p-btn').css({'display':'block'})},
			function(){auto();$('.p-btn').css({'display':'none'})}
		);
		$('.btn-right').click(function(){if(Is){move()};Is=true;});
		$('.btn-left').click(function(){
			if(Is){
				Is=false;
				Index--;
				if(Index<=-1){Index=5}
				var $Lis=$('.btn-lists li')
				$Lis.eq(Index).addClass('active').siblings().removeClass('active');
				$('.banner-cont img').attr({src:'img/banner'+(Index+1)+'.jpg'}).stop(true,false).fadeOut(100).fadeIn();
			}
			Is=true;
		});
	});
	//------------还有谁啊
	$('.banner-right-bottom ul li').hover(
		function(){$(this).children('img').css({'top':'50.5px'}).animate({top:'0'},100);$(this).children('span').css({'color':'red'})
			
		},
		function(){$(this).children('span').css({'color':'#666'})}
	)
	//---------------------------banner-left-lists
	
	//console.log($('.banner-left-lists  li').length)
	$('.banner-left li').hover(
		function(){$(this).children('.banner-left-cont').show().css({left:170}).animate({left:185}).fadeTo(100,.9)},
		function(){$(this).children('.banner-left-cont').fadeTo(100,1).hide()}
	);
	//--------------------------floor1
	$floorIndex=-1;
	$floorBtnIndex=-1;
	$floorTimer=null;
	console.log($('.floor-btn-lists li'));
	function floormove(){
		$floorIndex++;
		$floorBtnIndex++;
		$('.floor-pic-lists').animate({'left':-$floorIndex*306},500,function(){
			if($floorIndex===3){$floorIndex=0;$('.floor-pic-lists').css({'left':0});}
		});
		
		$('.floor-btn-lists li').eq($floorBtnIndex).children('span').animate({width:30},1000,function(){
			$(this).width('0');
			if($floorBtnIndex>=2){$floorBtnIndex=-1;}
		});
		
		
	};
	
	function floorauto(){
		setInterval(function(){
			floormove();
		
		},1000);
	};
	floorauto();
	//----------------------floor1-img
	$('.floor-right a').hover(
		function(){$(this).children('img').stop(true,false).animate({'left':-10})},
		function(){$(this).children('img').stop(true,false).animate({'left':0},100)}
	);
	$('.floor-right span').hover(
		function(){$(this).stop(true,false).fadeTo(500,0.5)},
		function(){$(this).stop(true,false).fadeTo(500,1)}
	);
	//---------------------------------------floor2
	$floor2Index=-1;
	$floor2BtnIndex=-1;
	$floor2Timer=null;
	//console.log($('.floor-btn-lists li'));
	function floor2move(){
		$floor2Index++;
		$floor2BtnIndex++;
		$('.floor2-pic-lists').animate({'left':-$floor2Index*306},500,function(){
			if($floor2Index===3){$floor2Index=0;$('.floor2-pic-lists').css({'left':0});}
		});
		
		$('.floor2-btn-lists li').eq($floor2BtnIndex).children('span').animate({width:30},1000,function(){
			$(this).width('0');
			if($floor2BtnIndex>=2){$floor2BtnIndex=-1;}
		});
		
		
	};
	
	function floor2auto(){
		setInterval(function(){
			floor2move();
		
		},1000);
	};
	floor2auto();
	//---------------------------------------floor3
	$floor3Index=-1;
	$floor3BtnIndex=-1;
	$floor3Timer=null;
	//console.log($('.floor-btn-lists li'));
	function floor3move(){
		$floor3Index++;
		$floor3BtnIndex++;
		$('.floor3-pic-lists').animate({'left':-$floor3Index*306},500,function(){
			if($floor3Index===3){$floor3Index=0;$('.floor3-pic-lists').css({'left':0});}
		});
		
		$('.floor3-btn-lists li').eq($floor3BtnIndex).children('span').animate({width:30},2000,function(){
			$(this).width('0');
			if($floor3BtnIndex>=2){$floor3BtnIndex=-1;}
		});
		
		
	};
	
	function floor3auto(){
		setInterval(function(){
			floor3move();
		
		},2000);
	};
	floor3auto();
	//---------------------------------------floor4
	$floor4Index=-1;
	$floor4BtnIndex=-1;
	$floor4Timer=null;
	//console.log($('.floor-btn-lists li'));
	function floor4move(){
		$floor4Index++;
		$floor4BtnIndex++;
		$('.floor4-pic-lists').animate({'left':-$floor4Index*306},500,function(){
			if($floor4Index===3){$floor4Index=0;$('.floor4-pic-lists').css({'left':0});}
		});
		
		$('.floor4-btn-lists li').eq($floor4BtnIndex).children('span').animate({width:30},1000,function(){
			$(this).width('0');
			if($floor4BtnIndex>=2){$floor4BtnIndex=-1;}
		});
		
		
	};
	
	function floor4auto(){
		setInterval(function(){
			floor4move();
		
		},1000);
	};
	floor4auto();
//---------------------------------------floor5
	$floor5Index=-1;
	$floor5BtnIndex=-1;
	$floor5Timer=null;
	//console.log($('.floor-btn-lists li'));
	function floor5move(){
		$floor5Index++;
		$floor5BtnIndex++;
		$('.floor5-pic-lists').animate({'left':-$floor5Index*306},500,function(){
			if($floor5Index===3){$floor5Index=0;$('.floor5-pic-lists').css({'left':0});}
		});
		
		$('.floor5-btn-lists li').eq($floor5BtnIndex).children('span').animate({width:30},1200,function(){
			$(this).width('0');
			if($floor5BtnIndex>=2){$floor5BtnIndex=-1;}
		});
		
		
	};
	
	function floor5auto(){
		setInterval(function(){
			floor5move();
		
		},1200);
	};
	floor5auto();
//---------------------------------------floor6
	$floor6Index=-1;
	$floor6BtnIndex=-1;
	$floor6Timer=null;
	//console.log($('.floor-btn-lists li'));
	function floor6move(){
		$floor6Index++;
		$floor6BtnIndex++;
		$('.floor6-pic-lists').animate({'left':-$floor6Index*306},500,function(){
			if($floor6Index===3){$floor6Index=0;$('.floor6-pic-lists').css({'left':0});}
		});
		
		$('.floor6-btn-lists li').eq($floor6BtnIndex).children('span').animate({width:30},1000,function(){
			$(this).width('0');
			if($floor6BtnIndex>=2){$floor6BtnIndex=-1;}
		});
		
		
	};
	
	function floor6auto(){
		setInterval(function(){
			floor6move();
		
		},1000);
	};
	floor6auto();	
//---------------------------------------floor7
	$floor7Index=-1;
	$floor7BtnIndex=-1;
	$floor7Timer=null;
	//console.log($('.floor-btn-lists li'));
	function floor7move(){
		$floor7Index++;
		$floor7BtnIndex++;
		$('.floor7-pic-lists').animate({'left':-$floor7Index*306},500,function(){
			if($floor7Index===3){$floor7Index=0;$('.floor7-pic-lists').css({'left':0});}
		});
		
		$('.floor7-btn-lists li').eq($floor7BtnIndex).children('span').animate({width:30},1600,function(){
			$(this).width('0');
			if($floor7BtnIndex>=2){$floor7BtnIndex=-1;}
		});
		
		
	};
	
	function floor7auto(){
		setInterval(function(){
			floor7move();
		
		},1600);
	};
	floor7auto();
//---------------------------------------floor8
	$floor8Index=-1;
	$floor8BtnIndex=-1;
	$floor8Timer=null;
	//console.log($('.floor-btn-lists li'));
	function floor8move(){
		$floor8Index++;
		$floor8BtnIndex++;
		$('.floor8-pic-lists').animate({'left':-$floor8Index*306},500,function(){
			if($floor8Index===3){$floor8Index=0;$('.floor8-pic-lists').css({'left':0});}
		});
		
		$('.floor8-btn-lists li').eq($floor8BtnIndex).children('span').animate({width:30},1000,function(){
			$(this).width('0');
			if($floor8BtnIndex>=2){$floor8BtnIndex=-1;}
		});
		
		
	};
	
	function floor8auto(){
		setInterval(function(){
			floor8move();
		
		},1000);
	};
	floor8auto();
	
	//-------------------------navigation
	$(window).on("scroll",function() {
		var $clientH=$(window).scrollTop();
		if($clientH>200){$('#navigation').css({display:'block'});$('.fliesearch').css({display:'block'})}
		else if($clientH<200){$('#navigation').css({display:'none'});$('.fliesearch').css({display:'none'})}
	});
	$('#navigation a').click(function(){
		var $navIndex=$(this).index()+1;
		/*var pTop=-$(this).index()*41
		console.log(pTop);
		$(this).css({backgroundPosition:'-45px'+pTop});*/
		var id='#floor'+$navIndex;
		if($navIndex===9){id='#top'}
		 $("html,body").stop(true,false).animate({scrollTop: $(id).offset().top-100}, 1000);
	});
	//--------------------------右侧边栏
	$('.nosidederty-left div').hover(
		function(){$(this).children('span').show().css({left:'0'}).animate({left:"-87px"})},
		function(){$(this).children('span').hide().css({left:'0'}).animate({left:"0"})}
	);
	$('.nosidederty-left1').click(function(){
		$('.nosidederty').animate({right:0});
		$('.nosidederty-right-car').hide();
		$('.nosidederty-right-login').show();
	});
	$('.nosidederty-left2').click(function(){
		$('.nosidederty').animate({right:0});
		$('.nosidederty-right-login').hide();
		$('.nosidederty-right-car').show();
	});
	
	
    $('.btn-a').click(function(){
    	$('.nosidederty').animate({right:-276})
    });
    $('.btn-a').hover(
    	function(){
    	$(this).stop(true,false).animate({left:20})},
    	function(){
    	$(this).stop(true,false).animate({left:15})}
    );
   //--------------------吸顶效果的下拉菜单
   
    
    //-------------------其他登陆方式的划过
    $('.other-login a').hover(
    	function(){$(this).css({backgroundPosition:'center top'})},
    	function(){$(this).css({backgroundPosition:'center bottom'})}
    )
   //---------------------------------------详情页放大镜效果
   $(document).ready(function(){
	// 图片上下滚动

	var count = $("#imageMenu li").length - 5; /* 显示 6 个 li标签内容 */
	var interval = $("#imageMenu li:first").width();
	var curIndex = 0;
	
	$('.scrollbutton').click(function(){
		if( $(this).hasClass('disabled') ) return false;
		
		if ($(this).hasClass('smallImgUp')) --curIndex;
		else ++curIndex;
		
		$('.scrollbutton').removeClass('disabled');
		if (curIndex == 0) $('.smallImgUp').addClass('disabled');
		if (curIndex == count-1) $('.smallImgDown').addClass('disabled');
		
		$("#imageMenu ul").stop(false, true).animate({"marginLeft" : -curIndex*interval + "px"}, 600);
	});	
	// 解决 ie6 select框 问题
	$.fn.decorateIframe = function(options) {
        
            var opts = $.extend({}, $.fn.decorateIframe.defaults, options);
            $(this).each(function() {
                var $myThis = $(this);
                //创建一个IFRAME
                var divIframe = $("<iframe />");
                divIframe.attr("id", opts.iframeId);
                divIframe.css("position", "absolute");
                divIframe.css("display", "none");
                divIframe.css("display", "block");
                divIframe.css("z-index", opts.iframeZIndex);
                divIframe.css("border");
                divIframe.css("top", "0");
                divIframe.css("left", "0");
                if (opts.width == 0) {
                    divIframe.css("width", $myThis.width() + parseInt($myThis.css("padding")) * 2 + "px");
                }
                if (opts.height == 0) {
                    divIframe.css("height", $myThis.height() + parseInt($myThis.css("padding")) * 2 + "px");
                }
                divIframe.css("filter", "mask(color=#fff)");
                $myThis.append(divIframe);
            });
        
    }
    $.fn.decorateIframe.defaults = {
        iframeId: "decorateIframe1",
        iframeZIndex: -1,
        width: 0,
        height: 0
    }
    //放大镜视窗
    $("#bigView").decorateIframe();
    //点击到中图
    var midChangeHandler = null;
	
    $("#imageMenu li img").bind("click", function(){
		if ($(this).attr("id") != "onlickImg") {
			midChange($(this).attr("src").replace("small", "mid"));
			$("#imageMenu li").removeAttr("id");
			$(this).parent().attr("id", "onlickImg");
		}
	}).bind("mouseover", function(){
		if ($(this).attr("id") != "onlickImg") {
			window.clearTimeout(midChangeHandler);
			midChange($(this).attr("src").replace("small", "mid"));
			$(this).css({ "border": "3px solid #959595" });
		}
	}).bind("mouseout", function(){
		if($(this).attr("id") != "onlickImg"){
			$(this).removeAttr("style");
			midChangeHandler = window.setTimeout(function(){
				midChange($("#onlickImg img").attr("src").replace("small", "mid"));
			}, 1000);
		}
	});
    function midChange(src) {
        $("#midimg").attr("src", src).load(function() {
            changeViewImg();
        });
    }
    //大视窗看图
    function mouseover(e) {
        if ($("#winSelector").css("display") == "none") {
            $("#winSelector,#bigView").show();
        }
        $("#winSelector").css(fixedPosition(e));
        e.stopPropagation();
    }
    function mouseOut(e) {
        if ($("#winSelector").css("display") != "none") {
            $("#winSelector,#bigView").hide();
        }
        e.stopPropagation();
    }
    $("#midimg").mouseover(mouseover); //中图事件
    $("#midimg,#winSelector").mousemove(mouseover).mouseout(mouseOut); //选择器事件

    var $divWidth = $("#winSelector").width(); //选择器宽度
    var $divHeight = $("#winSelector").height(); //选择器高度
    var $imgWidth = $("#midimg").width(); //中图宽度
    var $imgHeight = $("#midimg").height(); //中图高度
    var $viewImgWidth = $viewImgHeight = $height = null; //IE加载后才能得到 大图宽度 大图高度 大图视窗高度

    function changeViewImg() {
        $("#bigView img").attr("src", $("#midimg").attr("src").replace("mid", "big"));
    }
    changeViewImg();
    $("#bigView").scrollLeft(0).scrollTop(0);
    function fixedPosition(e) {
        if (e == null) {
            return;
        }
        var $imgLeft = $("#midimg").offset().left; //中图左边距
        var $imgTop = $("#midimg").offset().top; //中图上边距
        X = e.pageX - $imgLeft - $divWidth / 2; //selector顶点坐标 X
        Y = e.pageY - $imgTop - $divHeight / 2; //selector顶点坐标 Y
        X = X < 0 ? 0 : X;
        Y = Y < 0 ? 0 : Y;
        X = X + $divWidth > $imgWidth ? $imgWidth - $divWidth : X;
        Y = Y + $divHeight > $imgHeight ? $imgHeight - $divHeight : Y;

        if ($viewImgWidth == null) {
            $viewImgWidth = $("#bigView img").outerWidth();
            $viewImgHeight = $("#bigView img").height();
            if ($viewImgWidth < 200 || $viewImgHeight < 200) {
                $viewImgWidth = $viewImgHeight = 800;
            }
            $height = $divHeight * $viewImgHeight / $imgHeight;
            $("#bigView").width($divWidth * $viewImgWidth / $imgWidth);
            $("#bigView").height($height);
        }
        var scrollX = X * $viewImgWidth / $imgWidth;
        var scrollY = Y * $viewImgHeight / $imgHeight;
        $("#bigView img").css({ "left": scrollX * -1, "top": scrollY * -1 });
        $("#bigView").css({ "top": 50, "left": 420 });

        return { left: X, top: Y };
    }
});
//----------------------------------------------详情页物品数量加减
      
	$('.number-add').click(function(){
		var $Input=$('.change-number').children('input');
		
		var $Value=parseInt($Input.val());
		
		
		$Value++;
		//console.log($Value)
		$Input.val($Value);
	});
	$('.number-red').click(function(){
		var $Input=$('.change-number').children('input');
		var $Value=$Input.val();
		$Value--;
		console.log($Value)
		if($Value<=1){$Value=1}
		$Input.val($Value);
	});
	
//-----------------换一换
	var $changeNum=0
	$('.change-more p').click(function(){
		
		$changeNum++;
		if($changeNum>=3){$changeNum=0};
		$('.seemore-lists').css({top:-515*$changeNum})
		
	});
	
//---------------------------点击加入购物车的效果
	$('.buy-car').click(function(){
		$('.move-pic').css({left:0,bottom:-100,width:300,height:300})
		$('.move-pic').stop(true,false).animate({left:1500,bottom:500,width:0,height:0},1000)
	});
//-------------------------商品评论区的切换
	$('.dec-min-lists li').click(function(){
		$(this).addClass('active').siblings().removeClass('active');
		$('.dec-min-cont').children('div').eq($(this).index()).addClass('on').siblings().removeClass('on');
	});
//--------------------------商品详情页最下面的轮播
	
	var $Moreindex=0;
	var $MoreTime=null;
	$('.more-lists-tit span').hover(
		function(){$(this).css({backgroundColor:'black'});
		$Moreindex=$(this).index();
		$('.more-lists li').eq($(this).index()).addClass('change').animate({'opacity':1}).siblings().removeClass('change').animate({'opacity':.5});
		},
		function(){$('.more-lists-tit span').css({background:'#959595'});$(this).css({backgroundColor:'black'})}
	);
	
	function Moremove(){
		$('.more-lists-tit span').eq($Moreindex).css({backgroundColor:'black'}).siblings().css({background:'#959595'});
		$('.more-lists li').eq($Moreindex).addClass('change').animate({'opacity':1}).siblings().removeClass('change').animate({'opacity':.5});
	
	};
	
	function MoreAuto(){
		
		$MoreTime=setInterval(function(){
				$Moreindex++;
				if($Moreindex>=5){$Moreindex=0;}
				Moremove()
				
			},1000)
		};
	
	MoreAuto();//自动轮播吧
	$('.more-lists-wrap').hover(
		function(){clearInterval($MoreTime)},
		function(){MoreAuto()}
	);
	
	$('.more-lists li div').hover(
		function(){$(this).css({border:'1px solid red'})},
		function(){$(this).css({border:'1px solid #fff'})}
	);
	//--------------------------跨域获取评论
	
	function AutoView(){
	$.getJSON('http://sclub.jd.com/productpage/p-1794586-s-0-t-3-p-'+$ViewBtn+'.html?callback=?',	
			function(text){
				$('.new-view-wrap').html('');
					for(var i=0;i<text.comments.length;i++){
						var $Newbox=$('<div>');
						$Newbox.addClass('new-view');//创建一个新的评论块
						var $Newbox2=$('<div>');
						$Newbox2.addClass('new-view-left');//创建左边的部分
						var $Newimg=$('<img>')
						$Newimg.addClass('look-pic');//创建新的图片
						$Newimg.attr({src:'http://'+text.comments[i].userImageUrl});//图片的路径
						var $Newp=$('<p>');
						$Newp.addClass('buyname');//购买的Id
						$Newp.html(text.comments[i].nickname);
						var $Newp2=$('<p>');
						$Newp2.addClass('buytime');//购买的时间
						$Newp2.html(text.comments[i].days+'天前购买');
						$Newbox2.append($Newimg);
						$Newbox2.append($Newp);
						$Newbox2.append($Newp2);
						$Newbox.append($Newbox2); //左边的部分添加完毕
						var $Newimg2=$('<img>');
						$Newimg2.addClass('new-score').attr({src:'img/'+text.comments[i].score+'.png'});
						var $Newp3=$('<p>');
						$Newp3.addClass('new-cont');
						$Newp3.html(text.comments[i].content);
						var $Newp4=$('<p>');
						$Newp4.addClass('cont-time');
						$Newp4.html(text.comments[i].creationTime);
						$Newbox.append($Newimg2);
						$Newbox.append($Newp3);
						$Newbox.append($Newp4);
						$('.new-view-wrap').append($Newbox);
					};
			}
		);
	
	};
	
		
	var  $ViewBtn=0
	AutoView();//默认生成一次
	
	$('.view-btn span:lt(6)').click(
		function(){
			$("html,body").stop(true,false).animate({scrollTop: $('.view-btn').offset().top-2000}, 1000);
			$(this).addClass('btn-change').siblings().removeClass('btn-change');
			$ViewBtn=$(this).index();
			
			AutoView();
			
	});
	
	$('.view-btn span').eq(7).click(
		function(){
			$("html,body").stop(true,false).animate({scrollTop: $('.view-btn').offset().top-2000}, 1000);
			$(this).addClass('btn-change').siblings().removeClass('btn-change');
			$ViewBtn++;
			$('.view-btn span:lt(6)').eq($ViewBtn++).addClass('btn-change').siblings().removeClass('btn-change')
			AutoView();
			
	});
//------------------------------------------跨域搜索
 $('.header-search-input').on('input propertychange',function(){
 		var moremsg=$(".sinput").val();
 		
 	$.getJSON('https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?wd=' + moremsg + '&cb=?',
 		function (oData){
 			$('.header-search-ul').html('');
 			for(var i =0; i < oData.s.length; i++) {
					var $Newli=$('<li>');
					$Newli.text(oData.s[i]);
					$('.header-search-ul').append($Newli);
				}
 			}
 	
 	)
 });
	
//--------------------------------------注册页的效果
	$('.true-true').click(function(){
		$(this).toggleClass('ok');
	});
	
	$('.xieyi span').click(function(){
		$('.true-true').toggleClass('ok');
	});
	
	$('#login-form input').focus(function(){
		$(this).css({border: '2px solid #f77799',boxShadow: '0px 0px 3px #f77799'})
	});
	$('#login-form input').blur(function(){
		$(this).css({border:'1px solid #e1dfda',boxShadow: 'none'})
	});
	
	
//-------------------------------主题页的楼梯
	$(window).on("scroll",function() {
		var $clientH=$(window).scrollTop();
		if($clientH>400){$('.cakefloor-lists').css({display:'block'})}
		else if($clientH<400){$('.cakefloor-lists').css({display:'none'})}
	});
	$('.cakefloor-lists li:gt(0)').click(function(){
		//console.log($('#cfloor2').offset().top)
		var $naIndex=$(this).index()+3;
		
		var id='#cfloor'+$naIndex;
		if($naIndex===10){id='#top'};
	 	if($naIndex===4){id='#cfloor2'};
		 $("html,body").stop(true,false).animate({scrollTop: $(id).offset().top-100}, 1000);
	});
	
//-------------------------------搜索页效果
	$('.change-chu').hover(
		function(){$(this).children('.chushan-show').hide().siblings('.chuanshan-hide').show().parent().css({border:'2px solid #d5af82',backgroundColor:'#fef9ee'})},
		function(){$(this).children('.chuanshan-hide').hide().siblings('.chushan-show').show().parent().css({border:'1px solid #eee',backgroundColor:'#fff'})}
	);
	
	$('.squence-left div').hover(
		function(){$(this).css({border:'1px solid red',color:'#c01133'})},
		function(){$(this).css({border:'1px solid #f8f8f8',borderRight:'1px solid #ccc',color:'#000'})}
	);
	/*$('.squence-left div').click(function(){
		$(this).css({backgroundColor:'#c01133'}).children('i').css({backgroundPosition:'14px cnter'});
		$(this).siblings().css({backgroundColor:'#f8f8f8'}).children('i').css({backgroundPosition:'0 cnter'});
	
	});*/
	//-------------------------点击加入购物车的效果
	$('.search-pro-1').hover(
		function(){$(this).css({border:'1px solid red'})},
		function(){$(this).css({border:'1px solid #fff'})}
	);
	$('.buycar-join').hover(
		function(){$(this).css({backgroundColor:'#e6133c',color:'#fff'})},
		function(){$(this).css({backgroundColor:'#fff',color:'#e6133c'})}
	);
	$('.buycar-join').click(function(){
		$(this).siblings('.search-hide').css({left:0,top:0,width:200,height:200});
		$(this).siblings('.search-hide').stop(true,false).animate({left:1500,bottom:500,width:0,height:0},1000)
	});

	
	//-----------------------------登陆注册页面的倒计时
	$('#btn').click(function(){
		 $("#btn").attr("disabled", true);
		 var step = 59;
            $('#btn').val('重新发送59');
            var _res = setInterval(function()
            {   
               //设置disabled属性
                $('#btn').val('重新发送'+step);
                step-=1;
                if(step <= 0){
                $("#btn").removeAttr("disabled"); //移除disabled属性
                $('#btn').val('获取验证码');
                clearInterval(_res);//清除setInterval
                }
            },1000);
	});
	   
	
	

});
