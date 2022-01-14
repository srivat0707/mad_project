import javax.swing.*;
import java.awt.*; 
import java.awt.event.*;    
public class demo{   
    String forms; 
    JFrame f;
    JButton b;
    JButton d;
    JLabel name;
    JLabel mobile;
    JLabel address;
    JLabel dob;
    JLabel gender;
    JTextArea ans;
    JTextField n;
    JTextField m;
    JTextArea a;
    JRadioButton rb1,rb2; 
    ButtonGroup bg;
    JCheckBox accept;

demo(){ 
    forms="";
String date[]={"1","2","3","4","5","6","7","8","9","10"};        
JComboBox<String> da = new JComboBox<>(date);  
String month[]={"Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"};        
JComboBox<String> mo = new JComboBox<>(month); 
String year[]={"2001","2002","2003","2004","2005","2006","2007"};        
JComboBox<String> ye = new JComboBox<>(year); 
f=new JFrame("Form");            
b=new JButton("submit");   
d=new JButton("delete"); 
name= new JLabel("name");
mobile= new JLabel("mobile");
address=new JLabel("address");
dob=new JLabel("DOB");
gender=new JLabel("gender");
ans = new JTextArea("");
n= new JTextField();
m= new JTextField();
a= new JTextArea();
rb1= new JRadioButton("male",true);
rb2= new JRadioButton("female");
bg= new ButtonGroup();
accept= new JCheckBox("Accept the terms and condition");
bg.add(rb1);
bg.add(rb2);
f.add(ans);
f.add(da);
f.add(ye);
f.add(mo);
f.add(b);f.add(n);f.add(a);f.add(m);f.add(dob);f.add(accept);
f.add(d);f.add(name);f.add(address);f.add(mobile);f.add(dob);f.add(gender); f.add(rb1);f.add(rb2);
f.setSize(1000,700);
name.setBounds(50,50,40, 20);  
mobile.setBounds(50,100,40, 20);     
gender.setBounds(50,150,70, 20);  
dob.setBounds(50,200,40, 20);  
address.setBounds(50,250,70, 80); 
n.setBounds(100,50,170, 20);
m.setBounds(100,100,170, 20);
rb1.setBounds(100,150,70, 20); 
rb2.setBounds(190,150,70, 20);  
a.setBounds(100,250,270, 80);
accept.setBounds(50,350,240, 20); 
b.setBounds(50,390,100,20);
d.setBounds(190,390,100,20);
da.setBounds(100,200,40, 20);
mo.setBounds(160,200,70, 20);
ye.setBounds(260,200,70, 20);
ans.setBounds(400,50,500, 400);
ans.setEditable(false);
f.setLayout(null);    
f.setVisible(true);    
f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);  
b.addActionListener(new ActionListener() {  
    public void actionPerformed(ActionEvent e) {       
        String ms="";
         ms= ms+n.getText()+","+m.getText()+",";
         if (rb1.isSelected()){
             ms+="male,";
         }
         else{
            ms+="female,";
         }
         ms+=da.getItemAt(da.getSelectedIndex())+"-"+mo.getItemAt(mo.getSelectedIndex())+"-"+ye.getItemAt(ye.getSelectedIndex())+",";
         StringBuilder sb = new StringBuilder(a.getText());
         for(int i=0;i<sb.length();i++){
             if (sb.charAt(i)=='\n'){
                sb.replace(i, i+1, ";");
             }
         }
         forms+=ms+sb+"\n";
         ans.setText(forms);
} 
});     
d.addActionListener(new ActionListener() {  
    public void actionPerformed(ActionEvent e) {       
        n.setText("");
        m.setText("");
        a.setText("");
} 
});         
    }       
public static void main(String[] args) {    
    new demo();    
}    
}   