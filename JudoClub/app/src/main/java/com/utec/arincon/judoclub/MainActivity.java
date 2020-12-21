package com.utec.arincon.judoclub;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void openInscription(View view) {
        Intent intent = new Intent(MainActivity.this, InscriptionActivity.class);
        startActivity(intent);
    }

    public void openTeachers(View view) {
        Intent intent = new Intent(MainActivity.this, TeachersActivity.class);
        startActivity(intent);
    }

    public void openFundTech(View view) {
        Intent intent = new Intent(MainActivity.this, TechniquesActivity.class);
        startActivity(intent);
    }

    public void openGlosari(View view) {
        Intent intent = new Intent(MainActivity.this, GlosariActivity.class);
        startActivity(intent);
    }
}