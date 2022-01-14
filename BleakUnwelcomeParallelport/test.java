import java.awt.*;
import java.awt.event.*;

public class test extends Frame implements ActionListener{
    Button submit;
    Button clear;
    Label username;
    Label text;
    Label password;
    TextField user;
    TextField pass;
    test(){
        setVisible(true);
        setSize(600, 600);
        submit=new Button("submit");
        clear=new Button("clear");
        text= new Label("result");
        username= new Label("Enter the username");   
        password= new Label("Enter the password"); 
        user = new TextField();
        pass=new TextField();
        setLayout(null);
        username.setBounds(20, 80, 120, 30);  
        user.setBounds(150, 80, 80, 30); 
        password.setBounds(20, 160, 120, 30);  
        text.setBounds(300, 160, 120, 30);  
        pass.setBounds(150, 160, 80, 30);   
        submit.setBounds(100, 260, 80, 30); 
        clear.setBounds(200, 260, 80, 30); 
        add(submit);
        add(clear);
        add(pass);
        add(password);
        add(user);
        add(username);
        add(text);
        clear.addActionListener(this);
        submit.addActionListener(this);   
    }
    public void actionPerformed(ActionEvent e) {
        if (e.getSource()== submit){
            if(user.getText().compareTo("Srivatsan")==0 && pass.getText().compareTo("sastra")==0){
            text.setText("yuup");
            }
            else{
                text.setText("nope");  
            }
        }
        else{
        user.setText("");
        pass.setText("");
        }
    }
    
    public static void main(String[] args){
        test t1= new test();
    }
}