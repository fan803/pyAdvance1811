$(function () {
				
				// 创建购物车
				$(window).on("load", function () {
					loadCart();
					
					
					$('.carlists-carlists').on('click','.car-rem',function(){
					var nid = $(this).siblings('.carname').eq(0).text();
						new CartHelper().Del(nid);
						console.log(nid);
					loadCart();
					});
					
					$('.carlists-carlists').on('click','.car-add',function(){
						
					var num = parseInt($(this).siblings('.carnum').eq(0).text())+1;
					$(this).siblings('.carnum').eq(0).text(num);	
					var id = $(this).siblings('.carname').eq(0).text();
					count=Number($(this).siblings('.carnum').eq(0).text());
					new CartHelper().Change(id,count);
					loadCart();	
					//loadCart();
					});
					
					$('.carlists-carlists').on('click','.car-red',function(){
						
					var num = parseInt($(this).siblings('.carnum').eq(0).text())-1;
					if(num<=1){num=1};
					$(this).siblings('.carnum').eq(0).text(num);	
					var id = $(this).siblings('.carname').eq(0).text();
					count=Number($(this).siblings('.carnum').eq(0).text());
					new CartHelper().Change(id,count);
					loadCart();	
					//loadCart();
					});
					
	
				});
				
				
					
				// 加载购物车中的商品
				function loadCart() {
					var carts = new CartHelper().Read();// 读取购物车中的数据
					$(".nosidederty-right-car").children('.carlists').remove();
					$(".carlists-carlists").children('.carlists').remove();
					// 加载到页面上
					/******************* 加载购买商品信息 BEGIN***********************/
					$.each(carts.Items, function(index,cartItem) {
						// console.log(index + "---" + cartItem);
						// console.log(value);
						
						updateCartPage(cartItem.Id, cartItem.Name, cartItem.Count, cartItem.Price, cartItem.imgPath);
					});
					/******************* 加载购买商品信息 END***********************/
					// 加载购物结算信息
					$(".totalCount").text(carts.Count);
					$(".totalPrice").text('￥'+carts.Total);
					var Mnum=0;
					//console.log($('.carlists').length)
					for(var i=0;i<$('.carlists').length;i++){
						var nnum=$('.carlists').eq(i).children('.carnum').text();
						Mnum+=parseInt(nnum)
					};
					
					$('.cuntnum').text(Mnum);
					
				};
				//--------------------------------删除物品
			
				
				$(".buycar-join").on("click", function() {
					
					// 获取商品id
					var id = $(this).prev().prev().prev().prev().text();

					// 获取图片路径
					var imgPath = $(this).prev().prev().prev().prev().prev().attr("src");
					// 获取名称
					var goodsName = $(this).prev().prev().text();
					// 获取单价
					var price = $(this).prev().prev().prev().text();
					// 获取购买数量
					var count = 1;
					
					// 写购物车到cookie中
					new CartHelper().Add(id, goodsName, count, price, imgPath);
					
					// 加载购物车中的数据
					loadCart();
					
				});
				
				/********************** 更新页面 ************************/
				function updateCartPage(id, goodsName, count, price, imgPath) {
					var $tdId = $("<span>").addClass('carname');// 商品编号列
					var $tdImg = $("<img>").addClass('carimg');// 商品图片列
					var $tdName = $("<span>").addClass('carname');//商品名称列
					var $tdPrice = $("<span>").addClass('carprice');// 商品单价列
					var $tdCount = $("<span>").addClass('carnum');// 购买数量列
					var $tdSubtotal = $("<span>").addClass('xiaoji');// 小计价格列
					var $carreMove=$('<a>').addClass('car-rem');
					var $caradd=$('<a>').addClass('car-add');
					var $carred=$('<a>').addClass('car-red');
					var $trItem = $("<div>").addClass('carlists');
					// 更新数据
				
					$tdImg.attr("src", imgPath);
					$tdId.text(id);
					$tdName.text(goodsName);
					$tdPrice.text(price);
					$tdCount.text(count+'件');
					$tdSubtotal.text(count * price);
					$carreMove.text('删除');
					$caradd.text('+');
					$carred.text('-');
					
					$trItem.append($tdImg);
					$trItem.append($tdId);				
					$trItem.append($tdName);
					$trItem.append($tdPrice);
					$trItem.append($tdCount);
					$trItem.append($caradd);
					$trItem.append($carred);
					$trItem.append($carreMove);
					
					$trItem.append($tdSubtotal);
					
					
					$(".nosidederty-right-car").append($trItem);
					$('.carlists-carlists').append($trItem);
				}
				/********************** 更新页面 ************************/
			});