package com.utec.arincon.judoclub;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.Toast;

public class InscriptionActivity extends AppCompatActivity implements AdapterView.OnItemSelectedListener {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_inscription);

        Spinner spinner = findViewById(R.id.shift_spiner);
        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this, R.array.shifts, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adapter);
        spinner.setOnItemSelectedListener(this);

        Spinner spinner2 = findViewById(R.id.teacher_spiner);
        ArrayAdapter<CharSequence> adapter2 = ArrayAdapter.createFromResource(this, R.array.teachers, android.R.layout.simple_spinner_item);
        adapter2.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner2.setAdapter(adapter2);
        spinner2.setOnItemSelectedListener(this);



    }


    @Override
    public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {

    }

    @Override
    public void onNothingSelected(AdapterView<?> parent) {

    }

    public void register(View view) {
        EditText etName = findViewById(R.id.et_name);
        EditText etLastName = findViewById(R.id.et_last_name);
        EditText etAge = findViewById(R.id.et_age);
        String name = etName.getText().toString();
        String lastName = etLastName.getText().toString();
        String age = etAge.getText().toString();
        String toast = getResources().getString(R.string.toast_error);
        if (name.equals("") || lastName.equals("") || age.equals("")) {
            Toast.makeText(getBaseContext(), toast, Toast.LENGTH_LONG).show();
        }
        else {
            Spinner shift = findViewById(R.id.shift_spiner);
            Spinner teacher = findViewById(R.id.teacher_spiner);
            Intent intent = new Intent(InscriptionActivity.this, InscriptionSumActivity.class);
            intent.putExtra("name",name);
            intent.putExtra("lastName", lastName);
            intent.putExtra("age", age);
            intent.putExtra("shift", shift.getSelectedItem().toString());
            intent.putExtra("teacher", teacher.getSelectedItem().toString());
            startActivity(intent);

        }
    }


}