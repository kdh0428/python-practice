

















public void get_otherchat  (String parser,int i,int padding){
		try {
			byte [] eucBytes = parser.getBytes("euc-kr");
			parser = new String(eucBytes,"euc-kr");
			topLL = (LinearLayout)findViewById(R.id.Chat);
			TextView topTV11 = new TextView(chat.this);  
			topTV11.setLayoutParams(new LinearLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT));  
			topTV11.setBackgroundColor(Color.parseColor("#00FFFFFF"));  
			topTV11.setPadding(0,5,padding,0);
			topTV11.setTextColor(Color.parseColor("#FF7200"));  
			topTV11.setTextSize(i);  
			topTV11.setText(parser);  
			topLL.addView(topTV11); 
		} catch (UnsupportedEncodingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

