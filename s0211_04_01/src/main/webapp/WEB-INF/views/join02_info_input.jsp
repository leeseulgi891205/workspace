<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<link rel="stylesheet" type="text/css" href="css/style_header.css">
		<link rel="stylesheet" type="text/css" href="css/style_join02_info_input.css">
		<link rel="stylesheet" type="text/css" href="css/style_footer.css">
		<title>?뚯썝媛??- ?뚯썝?뺣낫?낅젰</title>
	</head>
	<body>
		<header>
			<div id="nav_up">
				<ul>
					<li><a href="#">?뚯썝媛??/a></li>
					<li><a href="#">濡쒓렇??/a></li>
					<li><a href="#">怨좉컼?됰났?쇳꽣</a></li>
					<li><a href="#">諛곗넚吏?????/a></li>
					<li><a href="#">湲고봽?몄뭅???깅줉</a></li>
				</ul>
			</div>	
			<nav>
				<a href="#"></a>
				<ul>
					<li><a href="#">COOKIT?뚭컻</a></li>
					<li><a href="#">COOKIT硫붾돱</a></li>
					<li><a href="#">由щ럭</a></li>
					<li><a href="#">?대깽??/a></li>
					<li><a href="#">MY荑≫궥</a></li>
				</ul>
				<ul>
					<li>
						<a href="#"><span>?λ컮援щ땲</span></a>
					</li>
					<li>
						<a href="#"><span>硫붾돱李얘린</span></a>
					</li>
				</ul>
			</nav>
		</header>
		
		
		
		
		
		<section>
			<form name="agree" method="get" action="join03_success.html">
				<div id="subBanner"></div>
				<div id="locationN">
					<ul>
						<li>HOME</li>
						<li>?뚯썝媛??/li>
						<li>?뚯썝?뺣낫?낅젰</li>
					</ul>
				</div>
				
				<div id="sub_top_area">
					<h3>?뚯썝媛??/h3>
				</div>
				
				<div id="join_step_div">
					<ul>
						<li>
							<span>STEP.1</span>
							<p>?쎄??숈쓽</p>
						</li>
						<li>
							<span>STEP.2</span>
							<p>?뚯썝?뺣낫</p>
						</li>
						<li>
							<span>STEP.3</span>
							<p>?뚯썝媛?낆셿猷?/p>
						</li>
					</ul>
				</div>
				
				<h4>
					?꾩닔 ?뺣낫 ?낅젰 
					<span>(* ??ぉ? ?꾩닔 ??ぉ?낅땲??)</span>
				</h4>
				<fieldset class="fieldset_class">
					<dl id="join_name_dl">
						<dt>
							<div></div>
							<label for="name">?대쫫</label>
						</dt>
						<dd>
							<input type="text" id="name" name="name" required/>
						</dd>
					</dl>
					<dl id="join_id_dl">
						<dt>
							<div></div>
							<label for="id">?꾩씠??/label>
						</dt>
						<dd>
							<input type="text" id="id" name="id" minlength="4" maxlength="16" required/>
							<input type="button" value="以묐났?뺤씤"/>
							<span>4~16?먮━???곷Ц, ?レ옄, ?뱀닔湲고샇(_)留??ъ슜?섏떎 ???덉뒿?덈떎.</span>
							<span>泥?湲?먮뒗 ?곷Ц?쇰줈 ?낅젰??二쇱꽭??</span>
						</dd>
					</dl>
					<dl id="join_pw1_dl">
						<dt>
							<div></div>
							<label for="pw1">鍮꾨?踰덊샇</label>
						</dt>
						<dd>
							<input type="password" id="pw1" name="pw1" minlength="8" required />
							<span>?곷Ц, ?レ옄, ?뱀닔臾몄옄 以?2醫낅쪟 議고빀 ??10?먮━ ?댁긽 ?낅젰</span>
							<span>?곷Ц, ?レ옄, ?뱀닔臾몄옄 紐⑤몢 議고빀 ??8?먮━ ?댁긽 ?낅젰</span>
						</dd>
					</dl>
					<dl id="join_pw2_dl">
						<dt>
							<div></div>
							<label for="pw2">鍮꾨?踰덊샇 ?뺤씤</label>
						</dt>
						<dd>
							<input type="password" id="pw2" name="pw2" minlength="8" required />
							<span>鍮꾨?踰덊샇瑜??ㅼ떆 ?쒕쾲 ?낅젰??二쇱꽭??</span>
						</dd>
					</dl>
					<dl id="join_mail_dl">
						<dt>
							<div></div>
							<label for="mail_id">?대찓??/label>
						</dt>
						<dd>
							<input type="text" id="mail_id" name="mail_id" required />
							<span>@</span>
							<input type="text" id="main_tail" name="mail_tail" required />
							<select>
								<option selected>吏곸젒?낅젰</option>
								<option>吏硫붿씪</option>
								<option>?ㅼ씠踰?/option>
								<option>?ㅼ씠??/option>
								<option>?ル찓??/option>
								<option>?뚮?</option>
								<option>?좏뙏</option>
								<option>?쇳썑</option>
								<option>?쒕┝?꾩쫰</option>
								<option>?쒕찓???ㅼ쓬)</option>
							</select>
						</dd>
					</dl>
					
					<dl id="join_address_dl">
						<dt> 
							<div></div>
							<label for="">二쇱냼</label>
						</dt>
						<dd>
							<input type="text" id="f_postal" name="f_postal" required />
							<span>-</span>
							<input type="text" id="l_postal" name="l_postal" required />
							<input type="button" value="?고렪踰덊샇"/>
							<input type="text" id="address1" name="address1" required />
							<input type="text" id="address2" name="address2" required />
						</dd>
						
					</dl>
					
					<dl id="join_tell_dl">
						<dt>
							<div></div>
							<label for="f_tell">?대??꾪솕</label>
						</dt>
						<dd>
							<input type="text" id="f_tell" name="f_tell" maxlength="3" required />
							<span> - </span>
							<input type="text" id="m_tell" name="m_tell" maxlength="4" required />
							<span> - </span>
							<input type="text" id="l_tell" name="l_tell" maxlength="4" required />
						</dd>
					</dl>
					<dl id="join_birth_dl">
						<dt>
							<div></div>
							<label for="birth_year">?앸뀈?붿씪</label>
						</dt>
						<dd>
							<select id="birth_year" name="birth_year" required>
								<option selected>?좏깮</option>
								<option value="1988">1988</option>
								<option value="1989">1989</option>
								<option value="1990">1990</option>
								<option value="1991">1991</option>
								<option value="1992">1992</option>
								<option value="1993">1993</option>
								<option value="1994">1994</option>
								<option value="1995">1995</option>
								<option value="1996">1996</option>
								<option value="1997">1997</option>
								<option value="1998">1998</option>
								<option value="1988">1999</option>
								<option value="1920">2000</option>
							</select>
							<span>??/span>
							<select id="birth_month" name="birth_month" required>
								<option selected>?좏깮</option>
								<option value="1">1</option>
								<option value="2">2</option>
								<option value="3">3</option>
								<option value="4">4</option>
								<option value="5">5</option>
								<option value="6">6</option>
								<option value="7">7</option>
								<option value="8">8</option>
								<option value="9">9</option>
								<option value="10">10</option>
								<option value="11">11</option>
								<option value="12">12</option>
							</select>
							<span>??/span>
							<select id="birth_day" name="birth_day" required>
								<option selected>?좏깮</option>
								<option value="1">1</option>
								<option value="2">2</option>
								<option value="3">3</option>
								<option value="4">4</option>
								<option value="5">5</option>
								<option value="6">6</option>
								<option value="7">7</option>
								<option value="8">8</option>
								<option value="9">9</option>
								<option value="10">10</option>
							</select>
							<span>??/span>
							<div>
								<input type="radio" name="calendar" id="lunar" value="lunar" checked="checked"/>
								<label for="lunar">?묐젰</label>
								<input type="radio" name="calendar" id="solar" value="solar" />
								<label for="solar">?뚮젰</label>
							</div>
						</dd>
					</dl>
					<dl id="join_gender_dl">
						<dt>
							<div></div>
							<label for="">?깅퀎</label>
						</dt>
						<dd>
							<div>
								<input type="radio" name="gender" id="male" value="male" checked="checked"/>
								<label for="male">?⑥꽦</label>
								<input type="radio" name="gender" id="female" value="female" />
								<label for="female">?ъ꽦</label>
							</div>
						</dd>
					</dl>
					<dl id="join_newsletter_dl">
						<dt>
							<div></div>
							<label for="">?댁뒪?덊꽣 ?섏떊?щ?</label>
						</dt>
						<dd>
							<span>?대찓?쇱쓣 ?듯븳 ?곹뭹 諛??대깽???뺣낫 ?섏떊???숈쓽?⑸땲??</span>
							<div>
								<input type="radio" name="newletter" id="newletter_y" value="yes" checked="checked"/>
								<label for="newletter_y">??/label>
								<input type="radio" name="newletter" id="newletter_n" value="no" />
								<label for="newletter_n">?꾨땲??/label>
							</div>
						</dd>
					</dl>
					<dl id="join_sms_dl">
						<dt>
							<div></div>
							<label for="">SMS ?섏떊?щ?</label>
						</dt>
						<dd>
							<span>?대찓?쇱쓣 ?듯븳 ?곹뭹 諛??대깽???뺣낫 ?섏떊???숈쓽?⑸땲??</span>
							<div>
								<input type="radio" name="sms" id="sms_y" value="yes" checked="checked"/>
								<label for="sms_y">??/label>
								<input type="radio" name="sms" id="sms_n" value="no" />
								<label for="sms_n">?꾨땲??/label>
							</div>
						</dd>
					</dl>
				</fieldset>

								
				<h4>
					遺꾩뼇 ?뚯썝 ?뺣낫 ?낅젰 
					<span>(?ㅺ뎄醫??뚯썝??寃쎌슦 媛吏怨?怨꾩떊 移대뱶踰덊샇 以??섎굹瑜??낅젰??二쇱떆硫??⑸땲??</span>
				</h4>
				<fieldset class="fieldset_class">
					<dl id="join_member_number_dl">
						<dt>
							<label for="m_number">?뚯썝踰덊샇</label>
						</dt>
						<dd>
							<input type="text" name="m_number" id="m_number" />
							<span>?섏씠??-)?대굹 ?꾩뼱?곌린 ?놁씠 ?낅젰??二쇱떆湲?諛붾엻?덈떎.</span>
						</dd>
					</dl>
					<dl id="join_verification_number_dl">
						<dt>
							<label for="v_number">?뚯썝?몄쬆踰덊샇</label>
						</dt>
						<dd>
							<input type="text" name="v_number" id="v_number" />
							<span>?レ옄 4?먮━ ?낅젰</span>
						</dd>
					</dl>
				</fieldset>
				
				<h4>
					?좏깮 ?낅젰 ?뺣낫 
				</h4>
				<fieldset class="fieldset_class">
					<dl id="join_job_dl">
						<dt>
							<label for="job">吏곸뾽</label>
						</dt>
						<dd>
							<select id="job" name="job">
								<option selected>?좏깮</option>
								<option value="worker">?뚯궗??/option>
								<option value="slef">?먯쁺?낆옄</option>
								<option value="freelancer">?꾨━?쒖꽌</option>
								<option value="housewife">?꾩뾽二쇰?</option>
								<option value="student">?숈깮</option>
								<option value="etc">湲고?</option>						
							</select>
						</dd>
					</dl>
					<dl id="join_marital_status_dl">
						<dt>
							<label for="">寃고샎?щ?</label>
						</dt>
						<dd>
							<input type="radio" name="marital_status" id="marital_status_y" value="yes" />
							<label for="marital_status_y">??/label>
							<input type="radio" name="marital_status" id="marital_status_n" value="no" />
							<label for="marital_status_n">?꾨땲??/label>
						</dd>
					</dl>
					<dl id="join_interests_dl">
						<dt>
							<label for="">愿?ъ궗</label>
						</dt>
						<dd>
							<ul>
								<li>
									<input type="checkbox" name="computer" id="computer" value="computer" />
									<label for="computer">而댄벂???명꽣??/label>
								</li>
								<li>
									<input type="checkbox" name="movie" id="movie" value="movie" />
									<label for="movie">?곹솕/鍮꾨뵒??/label>
								</li>
								<li>
									<input type="checkbox" name="music" id="music" value="music" />
									<label for="music">?뚯븙</label>
								</li>
								<li>
									<input type="checkbox" name="shopping" id="shopping" value="shopping" />
									<label for="shopping">?쇳븨</label>
								</li>
								<li>
									<input type="checkbox" name="game" id="game" value="game" />
									<label for="game">寃뚯엫</label>
								</li>
								<li>
									<input type="checkbox" name="culture" id="culture" value="culture" />
									<label for="culture">臾명솕/?덉닠</label>
								</li>
								<li>
									<input type="checkbox" name="parenting" id="parenting" value="parenting" />
									<label for="parenting">?≪븘/?꾨룞</label>
								</li>
								<li>
									<input type="checkbox" name="cooking" id="cooking" value="cooking" />
									<label for="parenting">?붾━</label>
								</li>
								<li>
									<input type="checkbox" name="interier" id="interier" value="interier" />
									<label for="interier">?명뀒由ъ뼱</label>
								</li>
								<li>
									<input type="checkbox" name="leisure" id="leisure" value="leisure" />
									<label for="leisure">?덉?/?ш?</label>
								</li>
								<li>
									<input type="checkbox" name="health" id="health" value="health" />
									<label for="health">嫄닿컯/?ㅼ씠?댄듃</label>
								</li>
								<li>
									<input type="checkbox" name="fashion" id="fashion" value="fashion" />
									<label for="fashion">?⑥뀡/誘몄슜</label>
								</li>
							</ul>
						</dd>
					</dl>
				</fieldset>
				<div id="info_input_button">
					<input type="reset" value="痍⑥냼?섍린" />
					<input type="submit" value="媛?낇븯湲? />
				</div>
				
			</form>
		</section>
		
		
		
		
		
		
		
		<footer>
			<div id="footer_wrap">
				<div id="footer_cont">
					<div id="fl_l">
						<a href="#"></a>
						<p>짤 COOKIT ALL RIGHTS RESERVED</p>
					</div>
					<div id="fl_c">
						<ul>
							<li><a href="#">?댁슜?쎄?</a></li>
							<li><a href="#">媛쒖씤?뺣낫泥섎━ 諛⑹묠</a></li>
							<li><a href="#">踰뺤쟻怨좎?</a></li>
							<li><a href="#">?ъ뾽?먯젙蹂??뺤씤</a></li>
						</ul>
						<div id="fl_c_info">
							<p>?⑥젣?댁젣?쇱젣??二?</p>
							<p>??쒖씠??: ?먭꼍??媛뺤떊???좏쁽??/p>
							<p>?ъ뾽?먮벑濡앸쾲??: 104-86-09535</p>
							<p>二쇱냼 : ?쒖슱 以묎뎄 ?숉샇濡?330 CJ?쒖씪?쒕떦 ?쇳꽣 (?? 04560</p>
							<p>?듭떊?먮ℓ?낆떊怨?以묎뎄 ??07767??/p>
							<p>媛쒖씤?뺣낫蹂댄샇梨낆엫??: 議곗쁺誘?/p>
							<p>?대찓??: cjon@cj.net</p>
							<p>?몄뒪?낆젣怨듭옄 : CJ?щ━釉뚮꽕?몄썚?ㅳ닚</p>
							<p>怨좉컼?섏? ?덉쟾嫄곕옒瑜??꾪빐 ?꾧툑?깆쑝濡?寃곗젣??LG U+ ?꾩옄 寃곗젣??留ㅻℓ蹂댄샇(?먯뒪?щ줈) ?쒕퉬?ㅻ? ?댁슜?섏떎 ???덉뒿?덈떎. <a href="#">媛???ъ떎 ?뺤씤</a></p>
						</div>
					</div>
					<div id="fl_r">
						<span>cj洹몃９怨꾩뿴??諛붾줈媛湲???/span>
						<dl>
							<dt>怨좉컼?됰났?쇳꽣</dt>
								<dd>1688-1920</dd>
						</dl>
						<a href="#">1:1臾몄쓽</a>						
					</div>
				</div>
			</div>
		
		
		
		</footer>
	</body>
</html>
