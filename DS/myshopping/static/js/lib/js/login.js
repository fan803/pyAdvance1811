$(function(){
	function login(){jQuery.validator.addMethod("isMobile", function(value, element) {
	    var length = value.length;
	    var mobile = /^(13[0-9]{9})|(18[0-9]{9})|(14[0-9]{9})|(17[0-9]{9})|(15[0-9]{9})$/;
	    return this.optional(element) || (length == 11 && mobile.test(value));
	}, "请正确填写您的手机号码");
	
	$.validator.setDefaults({
		submitHandler: function() {
			window.location.href='../html/success.html';
		}
	});
	
	$('#login-form').validate({
		onfocusout: function (element) {
			$(element).valid();
		},
		rules:{
			loginname:{required:true,rangelength:[6,20]},
			loginkey:{required:true,rangelength:[6,20]},
			loginkeymore:{required:true,equalTo:'#Lgkey'},
			phonenum:{required:true,isMobile:true},
			logincode:{required:true,rangelength:[4,4]},
			loginmsg:{required:true,rangelength:[6,6],digits:true},
			loginem:{email:true}
		},
		messages:{
			loginname:{required:'请输入用户名',rangelength:'由6-20位字母数字组成'},
			loginkey:{required:'请输入密码',rangelength:'由6-20位字母数字组成'},
			loginkeymore:{required:'请确认密码',equalTo:'两次输入密码不一致'},
			phonenum:{required:'请填写手机号',isMobile:'请输入正确手机号码'},
			logincode:{required:'请填写图片证码',rangelength:'请填写4位验证码'},
			loginmsg:{required:'请填写短信验证码',rangelength:'请填写6位短信验证码',digits:'请输入数字验证码'},
			loginem:{email:'请填写正确邮箱'}
		}
	});
	};
	login();
});
