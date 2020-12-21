package com.utec.arincon.judoclub;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class InscriptionSumActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_inscription_sum);

        TextView nameText = findViewById(R.id.final_name);
        TextView lastNameText = findViewById(R.id.final_last_name);
        TextView ageText = findViewById(R.id.final_age);
        TextView shiftText = findViewById(R.id.final_shift);
        TextView teacherText = findViewById(R.id.final_profesor);
        TextView horaText = findViewById(R.id.final_horario);
        nameText.setText(getData("name"));
        lastNameText.setText(getData("lastName"));
        ageText.setText(getData("age"));
        shiftText.setText(getData("shift"));
        teacherText.setText(getData("teacher"));
        String m = getResources().getString(R.string.morning);
        String t = getResources().getString(R.string.afternoon);
        String n = getResources().getString(R.string.night);
        if(getData("shift").equals(m)) {
            horaText.setText("8:00 AM / 11:00 AM");
        }
        else if(getData("shift").equals(t)) {
            horaText.setText("1:00 PM / 4:00 PM");
        }
        else if(getData("shift").equals(n)) {
            horaText.setText("6:00 PM / 9:00 PM");
        }

    }

    public String  getData(String key) {
        Bundle extras = getIntent().getExtras();
        return extras.getString(key);
    }

    public void returnToMain(View view) {
        Intent intent = new Intent(InscriptionSumActivity.this, MainActivity.class);
        startActivity(intent);
    }
}