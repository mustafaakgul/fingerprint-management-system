package com.test;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;

public class sms {

    public static void main(String[] args){
        System.out.println("waiting");
        send();
        System.out.println("sent");
    }

    public static void send(){
        HttpURLConnection  uc = null;
        try{
            URL url = new URL("http://panel.1sms.com.tr:8080/api/smspost/v1");
            uc = (HttpURLConnection)url.openConnection();
            uc.setRequestMethod("POST");
            uc.setDoInput(true);
            uc.setDoOutput(true);
            uc.setRequestProperty("Content-Type", "text/xml; charset=UTF-8");
            uc.setRequestProperty("Content-Encoding", "UTF-8");
            uc.setReadTimeout(5*1000);
            uc.setConnectTimeout(5*1000);
            uc.connect();

            OutputStreamWriter out = new OutputStreamWriter(uc.getOutputStream(), "UTF-8");
            out.write(""
                    + "<sms>"
                    + "<username>USERNAME</username>"
                    + "<password>PASSWORD</password>"
                    + "<header>DEMO</header>"
                    + "<validity>2880</validity>"
                    + "<message>"
                    + "<gsm>"
                    + "<no>PHONE</no>"
                    + "</gsm>"
                    + "<msg><![CDATA[-test-message-deneme-]]></msg>"
                    + "</message>"
                    + "</sms>");
            out.flush();
            out.close();

            int resCode = uc.getResponseCode();
            System.out.println("HTTP "+resCode);

            int readed;
            char[] buffer = new char[4*1024];
            StringBuffer sb = new StringBuffer();
            BufferedReader in = new BufferedReader(new InputStreamReader(uc.getInputStream(), "UTF-8"));
            while( (readed = in.read(buffer)) >0 ){
                sb.append(buffer, 0, readed);
            }
            in.close();

            String ret = sb.toString();
            System.out.println("["+ret+"]");

        }catch(Exception ex){
            ex.printStackTrace();
        }finally{
            try{ uc.disconnect(); }catch(Exception ex){} uc = null;
        }
    }
}